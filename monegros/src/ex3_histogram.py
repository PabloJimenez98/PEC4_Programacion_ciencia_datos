import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from monegros.utils.logger import Logger

class TimeHistogram:
    def __init__(self):
        self.img_path = Path(__file__).parent.parent / 'img' / 'histograma.png'
        self.logger = Logger("TimeHistogram")

    def minutes_002040(self, time_str):
        """
        Groups time into 20-minute intervals.
        
        Args:
            time_str (str): Time in format 'HH:MM:SS'
            
        Returns:
            str: Time grouped in 20-minute intervals in format 'HH:MM'
            
        Example:
            '06:19:40' -> '06:00'
            '06:29:40' -> '06:20'
            '06:59:40' -> '06:40'
        """
        try:
            time = pd.to_datetime(time_str, format='%H:%M:%S')
            hours = time.hour
            minutes = time.minute
            
            if minutes < 20:
                grouped_minutes = 0
            elif minutes < 40:
                grouped_minutes = 20
            else:
                grouped_minutes = 40
                
            return f"{hours:02d}:{grouped_minutes:02d}"
        
        except ValueError as e:
            self.logger.error(f"Invalid time format: {time_str}. Expected HH:MM:SS")
            raise ValueError(f"Invalid time format: {time_str}. Expected HH:MM:SS") from e

    def create_time_histogram(self, df):
        """
        Creates a histogram of completion times grouped in 20-minute intervals.
        
        Args:
            df (pd.DataFrame): DataFrame with race data
            
        Returns:
            pd.DataFrame: DataFrame with added time_grouped column
        """
        self.logger.info("Creating time histogram...")
        df_hist = df.copy()
        df_hist['time_grouped'] = df_hist['time'].apply(self.minutes_002040)
        
        self.logger.info("First 15 rows with grouped times:")
        print(df_hist[['time', 'time_grouped']].head(15))
        
        time_freq = df_hist.groupby('time_grouped').size().reset_index(name='count')
        time_freq = time_freq.sort_values('time_grouped')
        
        self.logger.info("Frequency table of grouped times:")
        print(time_freq)
        
        self.logger.info("Generating histogram plot...")
        plt.figure(figsize=(15, 6))
        plt.bar(range(len(time_freq)), time_freq['count'])
        plt.xticks(range(len(time_freq)), time_freq['time_grouped'], rotation=45)
        plt.title('Distribution of Race Completion Times')
        plt.xlabel('Time (HH:MM)')
        plt.ylabel('Number of Cyclists')
        plt.grid(True, alpha=0.3)
        
        self.img_path.parent.mkdir(exist_ok=True)
        plt.savefig(self.img_path, bbox_inches='tight')
        plt.close()
        
        self.logger.info(f"Histogram saved to {self.img_path}")
        
        return df_hist

if __name__ == "__main__":
    from ex1_data import DataLoader
    from ex2_anonymize import DataAnonymizer
    
    loader = DataLoader()
    df_original = loader.load_and_analyze_data()
    anonymizer = DataAnonymizer()
    df_clean = anonymizer.anonymize_and_clean_data(df_original)
    
    histogram = TimeHistogram()
    histogram.create_time_histogram(df_clean)