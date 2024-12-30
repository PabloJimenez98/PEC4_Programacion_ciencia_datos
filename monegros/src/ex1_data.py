import pandas as pd
from pathlib import Path
from monegros.utils.logger import Logger

class DataLoader:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent
        self.data_path = self.root_dir / 'data' / 'dataset.csv'
        self.df = None
        self.logger = Logger("DataLoader")

    def load_and_analyze_data(self):
        """
        Loads and performs initial analysis of the Orbea Monegros dataset.
                
        Returns:
            pd.DataFrame: The loaded dataset
        
        Raises:
            FileNotFoundError: If the data file is not found
        """
        self.logger.info("Loading dataset...")
        self.df = pd.read_csv(self.data_path, sep=";")
        
        self.logger.info(f"Dataset loaded with {len(self.df)} rows")
        self.logger.info("First 5 rows of the dataset:")
        print(self.df.head())
        
        self.logger.info(f"Number of participants: {len(self.df)}")
        
        self.logger.info("Dataframe columns:")
        print(self.df.columns.tolist())
        
        return self.df

if __name__ == "__main__":
    loader = DataLoader()
    loader.load_and_analyze_data()