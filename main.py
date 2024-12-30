import argparse
from monegros.src.ex1_data import DataLoader
from monegros.src.ex2_anonymize import DataAnonymizer
from monegros.src.ex3_histogram import TimeHistogram
from monegros.src.ex4_clubs import ClubAnalyzer
from monegros.src.ex5_ucsc import UCSCAnalyzer

def main(exercise=None):
    """
    Main function to run the Orbea Monegros 2024 data analysis
    """
    # Initialize classes
    loader = DataLoader()
    anonymizer = DataAnonymizer()
    histogram = TimeHistogram()
    club_analyzer = ClubAnalyzer()
    ucsc_analyzer = UCSCAnalyzer()
    
    # Load initial data
    if exercise is None or exercise == '1':
        print("\n=== Exercise 1: Data Loading and EDA ===")
        df = loader.load_and_analyze_data()
        
    if exercise is None or exercise == '2':
        print("\n=== Exercise 2: Data Anonymization and Cleaning ===")
        df = anonymizer.anonymize_and_clean_data(df)
        
    if exercise is None or exercise == '3':
        print("\n=== Exercise 3: Time Histogram ===")
        df = histogram.create_time_histogram(df)
        
    if exercise is None or exercise == '4':
        print("\n=== Exercise 4: Cycling Clubs Analysis ===")
        df = club_analyzer.analyze_clubs(df)
        
    if exercise is None or exercise == '5':
        print("\n=== Exercise 5: UCSC Analysis ===")
        ucsc_analyzer.analyze_ucsc(df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Orbea Monegros 2024 Data Analysis')
    parser.add_argument('--exercise', type=str, choices=['1', '2', '3', '4', '5'],
                      help='Specific exercise to run (1-5)')
    args = parser.parse_args()
    
    main(args.exercise)