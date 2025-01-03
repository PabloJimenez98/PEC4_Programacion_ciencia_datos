import pytest
import pandas as pd
from monegros.src.ex2_anonymize import DataAnonymizer

@pytest.fixture
def anonymizer():
    """Fixture to create a DataAnonymizer instance"""
    return DataAnonymizer()

@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing"""
    return pd.DataFrame({
        'dorsal': [1, 2, 3, 4],
        'biker': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown'],
        'club': ['Club A', 'Club B', 'Club C', 'Club D'],
        'time': ['05:30:00', '00:00:00', '06:15:00', '00:00:00']
    })

def test_name_surname(anonymizer, sample_df):
    """Test the name anonymization function"""
    df_anon = anonymizer.name_surname(sample_df)
    
    # Check that the structure remains the same
    assert len(df_anon) == len(sample_df)
    assert all(df_anon.columns == sample_df.columns)
    
    # Check that names have been changed
    assert not any(df_anon['biker'].isin(sample_df['biker']))
    
    # Check that names are unique
    assert len(df_anon['biker'].unique()) == len(df_anon)
    
    # Check that other columns remain unchanged
    assert all(df_anon['dorsal'] == sample_df['dorsal'])
    assert all(df_anon['club'] == sample_df['club'])
    assert all(df_anon['time'] == sample_df['time'])

def test_clean_dataset(anonymizer, sample_df):
    """Test the dataset cleaning function"""
    df_clean = anonymizer.clean_dataset(sample_df)
    
    # Check that only non-zero times remain
    assert len(df_clean) == 2
    assert not any(df_clean['time'] == '00:00:00')
    
    # Check that the correct rows remain
    expected_times = ['05:30:00', '06:15:00']
    assert all(time in expected_times for time in df_clean['time'])

def test_anonymize_and_clean_data(anonymizer, sample_df):
    """Test the complete anonymization and cleaning process"""
    df_processed = anonymizer.anonymize_and_clean_data(sample_df)
    
    # Check final structure
    assert len(df_processed) == 2  # Only non-zero times
    assert all(col in df_processed.columns for col in ['dorsal', 'biker', 'club', 'time'])
    
    # Check that names have been anonymized
    assert not any(df_processed['biker'].isin(sample_df['biker']))
    
    # Check that zero times have been removed
    assert not any(df_processed['time'] == '00:00:00')


if __name__ == "__main__":
    pytest.main([__file__])