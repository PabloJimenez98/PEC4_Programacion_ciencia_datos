import pandas as pd
import re
from monegros.utils.logger import Logger

class ClubAnalyzer:
    def __init__(self):
        self.logger = Logger("ClubAnalyzer")
        self.prefixes = [
            'PEÑA CICLISTA ', 'PENYA CICLISTA ',
            'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ',
            'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ',
            'CLUB CICLISTA ', 'CLUB '
        ]
        self.start_patterns = [
            r'^C\.C\. ', r'^C\.C ', r'^CC ',
            r'^C\.D\. ', r'^C\.D ', r'^CD ',
            r'^A\.C\. ', r'^A\.C ', r'^AC ',
            r'^A\.D\. ', r'^A\.D ', r'^AD ',
            r'^A\.E\. ', r'^A\.E ', r'^AE ',
            r'^E\.C\. ', r'^E\.C ', r'^EC ',
            r'^S\.C\. ', r'^S\.C ', r'^SC ',
            r'^S\.D\. ', r'^S\.D ', r'^SD '
        ]
        self.end_patterns = [
            r' T\.T\.$', r' T\.T$', r' TT$',
            r' T\.E\.$', r' T\.E$', r' TE$',
            r' C\.C\.$', r' C\.C$', r' CC$',
            r' C\.D\.$', r' C\.D$', r' CD$',
            r' A\.D\.$', r' A\.D$', r' AD$',
            r' A\.C\.$', r' A\.C$', r' AC$'
        ]

    def clean_club(self, club_name):
        """
        Cleans and standardizes cycling club names.
        
        Args:
            club_name (str): Original club name
            
        Returns:
            str: Cleaned club name
            
        Example:
            'C.C. Huesca' -> 'HUESCA'
            'Club Ciclista Oscense' -> 'OSCENSE'
        """
        if not isinstance(club_name, str):
            return 'INDEPENDIENTE'
        
        cleaned = club_name.upper()
        
        for prefix in self.prefixes:
            cleaned = cleaned.replace(prefix, '')
        
        for pattern in self.start_patterns:
            cleaned = re.sub(pattern, '', cleaned)
        
        for pattern in self.end_patterns:
            cleaned = re.sub(pattern, '', cleaned)
        
        cleaned = cleaned.strip()
        return cleaned if cleaned else 'INDEPENDIENTE'

    def analyze_clubs(self, df):
        """
        Analyzes cycling clubs participation.
        
        Args:
            df (pd.DataFrame): DataFrame with race data
            
        Returns:
            pd.DataFrame: DataFrame with added club_clean column
        """
        self.logger.info("Starting club analysis...")
        df_clubs = df.copy()
        df_clubs['club_clean'] = df_clubs['club'].apply(self.clean_club)
        
        self.logger.info("First 15 rows with cleaned club names:")
        print(df_clubs[['club', 'club_clean']].head(15))
        
        club_summary = df_clubs['club_clean'].value_counts().reset_index()
        club_summary.columns = ['club', 'participants']
        
        self.logger.info("Club participation summary (top 10):")
        print(club_summary.head(10))
        
        return df_clubs

if __name__ == "__main__":
    from ex1_data import DataLoader
    from ex2_anonymize import DataAnonymizer
    
    loader = DataLoader()
    df_original = loader.load_and_analyze_data()
    anonymizer = DataAnonymizer()
    df_clean = anonymizer.anonymize_and_clean_data(df_original)
    
    club_analyzer = ClubAnalyzer()
    club_analyzer.analyze_clubs(df_clean)