import pytest
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from src.ex3_histogram import minutes_002040, create_time_histogram

@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing"""
    return pd.DataFrame({
        'dorsal': [1, 2, 3, 4, 5],
        'biker': ['Biker1', 'Biker2', 'Biker3', 'Biker4', 'Biker5'],
        'club': ['Club1', 'Club2', 'Club3', 'Club4', 'Club5'],
        'time': ['05:19:40', '05:29:40', '05:59:40', '06:05:00', '06:25:00']
    })

def test_minutes_002040_basic():
    """Test basic functionality of minutes_002040"""
    test_cases = [
        ('06:19:40', '06:00'),
        ('06:29:40', '06:20'),
        ('06:59:40', '06:40'),
        ('06:00:00', '06:00'),
        ('06:20:00', '06:20'),
        ('06:40:00', '06:40')
    ]
    
    for input_time, expected_output in test_cases:
        assert minutes_002040(input_time) == expected_output

def test_minutes_002040_edge_cases():
    """Test edge cases for minutes_002040"""
    # Test midnight
    assert minutes_002040('00:00:00') == '00:00'
    # Test last minute of day
    assert minutes_002040('23:59:59') == '23:40'

def test_minutes_002040_invalid_input():
    """Test invalid input handling for minutes_002040"""
    with pytest.raises(ValueError):
        minutes_002040('25:00:00')  # Invalid hour
    with pytest.raises(ValueError):
        minutes_002040('invalid')   # Invalid format

def test_create_time_histogram(sample_df, tmp_path):
    """Test histogram creation"""
    # Create temporary img directory
    img_dir = tmp_path / 'img'
    img_dir.mkdir()
    
    # Temporarily redirect image output
    original_path = Path(__file__).parent.parent / 'img'
    plt.close('all')  # Close any existing plots
    
    try:
        # Process the data
        df_result = create_time_histogram(sample_df)
        
        # Check that time_grouped column was added
        assert 'time_grouped' in df_result.columns
        
        # Check that all times were grouped correctly
        assert len(df_result) == len(sample_df)
        
        # Check that histogram was created
        histogram_path = original_path / 'histograma.png'
        assert histogram_path.exists()
        
    finally:
        plt.close('all')  # Clean up

def test_time_grouping_consistency(sample_df):
    """Test consistency of time grouping"""
    df_result = create_time_histogram(sample_df)
    
    # Check that times are grouped consistently
    grouped_times = df_result['time_grouped'].unique()
    
    # Verify that all grouped times are in correct format
    for time in grouped_times:
        hours, minutes = map(int, time.split(':'))
        assert 0 <= hours <= 23
        assert minutes in [0, 20, 40]

if __name__ == "__main__":
    pytest.main([__file__])