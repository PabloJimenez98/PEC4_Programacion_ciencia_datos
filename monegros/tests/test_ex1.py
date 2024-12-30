import pytest
import pandas as pd
from pathlib import Path
from monegros.src.ex1_data import DataLoader

@pytest.fixture
def data_loader():
    """Fixture to create a DataLoader instance"""
    return DataLoader()

def test_load_and_analyze_data(data_loader):
    """Test the data loading and analysis function"""
    # Execute the function
    df = data_loader.load_and_analyze_data()
    
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

def test_file_not_found(data_loader):
    """Test that appropriate error is raised when file is not found"""
    # Temporarily rename the data file to simulate missing file
    original_path = data_loader.data_path
    temp_path = original_path.parent / 'dataset.csv.bak'
    
    if original_path.exists():
        original_path.rename(temp_path)
        
        with pytest.raises(FileNotFoundError):
            data_loader.load_and_analyze_data()
            
        # Restore the file
        temp_path.rename(original_path)

if __name__ == "__main__":
    pytest.main([__file__])