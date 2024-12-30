import pytest
import pandas as pd
from pathlib import Path
from src.ex1_data import load_and_analyze_data

def test_load_and_analyze_data():
    """Test the data loading and analysis function"""
    # Execute the function
    df = load_and_analyze_data()
    
    # Test that we get a DataFrame back
    assert isinstance(df, pd.DataFrame)
    
    # Test that the DataFrame is not empty
    assert not df.empty
    
    # Test that we have the expected columns
    expected_columns = ['dorsal', 'biker', 'club', 'time']
    assert all(col in df.columns for col in expected_columns)
    
    # Test that dorsal is numeric
    assert pd.api.types.is_numeric_dtype(df['dorsal'])
    
    # Test that time is in the correct format (HH:MM:SS)
    def is_time_format(time_str):
        try:
            pd.to_datetime(time_str, format='%H:%M:%S')
            return True
        except ValueError:
            return False
    
    assert all(df['time'].apply(is_time_format))

def test_file_not_found():
    """Test that appropriate error is raised when file is not found"""
    # Temporarily rename the data file to simulate missing file
    root_dir = Path(__file__).parent.parent
    data_path = root_dir / 'data' / 'dataset.csv'
    temp_path = root_dir / 'data' / 'dataset.csv.bak'
    
    if data_path.exists():
        data_path.rename(temp_path)
        
        with pytest.raises(FileNotFoundError):
            load_and_analyze_data()
            
        # Restore the file
        temp_path.rename(data_path)

if __name__ == "__main__":
    pytest.main([__file__])