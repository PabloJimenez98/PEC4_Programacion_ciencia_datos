import pandas as pd
from monegros.utils.logger import Logger

class UCSCAnalyzer:
    def __init__(self):
        self.logger = Logger("UCSCAnalyzer")

    def analyze_ucsc(self, df):
        """
        Analyzes the performance of UCSC (Unió Ciclista Sant Cugat) cyclists.
        
        Args:
            df (pd.DataFrame): DataFrame with race data including club_clean column
            
        Returns:
            tuple: (ucsc_df, best_time_df, position_info)
                - ucsc_df: DataFrame with UCSC cyclists
                - best_time_df: DataFrame with best UCSC cyclist
                - position_info: Dict with position and percentage info
        """
        if 'club_clean' not in df.columns:
            error_msg = "DataFrame must include 'club_clean' column. Run analyze_clubs first."
            self.logger.error(error_msg)
            raise ValueError(error_msg)
        
        self.logger.info("Analyzing UCSC cyclists...")
        ucsc_df = df[df['club_clean'] == 'UCSC'].copy()
        
        self.logger.info("UCSC cyclists:")
        print(ucsc_df[['dorsal', 'biker', 'time']])
        
        best_time_df = ucsc_df.loc[ucsc_df['time'].idxmin()] if not ucsc_df.empty else None
        
        if best_time_df is not None:
            self.logger.info("Best time for UCSC:")
            print(f"Biker: {best_time_df['biker']}")
            print(f"Time: {best_time_df['time']}")
            
            total_participants = len(df)
            df_sorted = df.sort_values('time')
            position = df_sorted.index.get_loc(best_time_df.name) + 1
            percentage = (position / total_participants) * 100
            
            position_info = {
                'position': position,
                'total': total_participants,
                'percentage': percentage
            }
            
            self.logger.info(f"Position: {position} out of {total_participants}")
            self.logger.info(f"Top {percentage:.2f}%")
        else:
            self.logger.warning("No UCSC cyclists found in the dataset")
            position_info = None
            
        return ucsc_df, best_time_df, position_info

if __name__ == "__main__":
    from ex1_data import DataLoader
    from ex2_anonymize import DataAnonymizer
    from ex4_clubs import ClubAnalyzer
    
    loader = DataLoader()
    df_original = loader.load_and_analyze_data()
    anonymizer = DataAnonymizer()
    df_clean = anonymizer.anonymize_and_clean_data(df_original)
    club_analyzer = ClubAnalyzer()
    df_clubs = club_analyzer.analyze_clubs(df_clean)
    
    ucsc_analyzer = UCSCAnalyzer()
    ucsc_analyzer.analyze_ucsc(df_clubs)