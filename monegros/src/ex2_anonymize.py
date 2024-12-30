import pandas as pd
from faker import Faker
from monegros.utils.logger import Logger

class DataAnonymizer:
    def __init__(self):
        self.fake = Faker()
        Faker.seed(42)
        self.logger = Logger("DataAnonymizer")

    def name_surname(self, df):
        """
        Anonymizes the biker names in the dataframe using Faker.
        
        Args:
            df (pd.DataFrame): Original dataframe with biker names
            
        Returns:
            pd.DataFrame: New dataframe with anonymized names
        """
        df_anon = df.copy()
        df_anon['biker'] = [self.fake.name() for _ in range(len(df))]
        return df_anon

    def clean_dataset(self, df):
        """
        Removes entries where time is '00:00:00' (did not participate).
        
        Args:
            df (pd.DataFrame): DataFrame to clean
            
        Returns:
            pd.DataFrame: Cleaned DataFrame
        """
        return df[df['time'] != '00:00:00'].copy()

    def anonymize_and_clean_data(self, df):
        """
        Main function to anonymize and clean the dataset.
        
        Args:
            df (pd.DataFrame): Original dataframe
            
        Returns:
            pd.DataFrame: Processed dataframe
        """
        # Anonymize names
        self.logger.info("Starting data anonymization...")
        df_processed = self.name_surname(df)
        self.logger.info("First 5 rows after anonymization:")
        print(df_processed.head())
        
        # Clean dataset
        self.logger.info("Cleaning dataset...")
        df_processed = self.clean_dataset(df_processed)
        self.logger.info(f"Number of participants after cleaning: {len(df_processed)}")
        self.logger.info("First 5 rows after cleaning:")
        print(df_processed.head())
        
        # Get data for biker with dorsal 1000
        biker_1000 = df_processed[df_processed['dorsal'] == 1000]
        if not biker_1000.empty:
            self.logger.info("Data for biker with dorsal 1000:")
            print(biker_1000)
        else:
            self.logger.warning("No biker found with dorsal 1000")
        
        return df_processed

if __name__ == "__main__":
    from ex1_data import DataLoader
    loader = DataLoader()
    df_original = loader.load_and_analyze_data()
    anonymizer = DataAnonymizer()
    anonymizer.anonymize_and_clean_data(df_original)