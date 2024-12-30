import pytest
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from monegros.src.ex3_histogram import TimeHistogram

@pytest.fixture
def histogram_analyzer():
    """Fixture to create a TimeHistogram instance"""
    return TimeHistogram()

@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing"""
    return pd.DataFrame({
        'dorsal': [1, 2, 3, 4, 5],
        'biker': ['Biker1', 'Biker2', 'Biker3', 'Biker4', 'Biker5'],
        'club': ['Club1', 'Club2', 'Club3', 'Club4', 'Club5'],
        'time': ['05:19:40', '05:29:40', '05:59:40', '06:05:00', '06:25:00']
    })

def test_minutes_002040_basic(histogram_analyzer):
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
        assert histogram_analyzer.minutes_002040(input_time) == expected_output

def test_minutes_002040_edge_cases(histogram_analyzer):
    """Test edge cases for minutes_002040"""
    # Test midnight
    assert histogram_analyzer.minutes_002040('00:00:00') == '00:00'
    # Test last minute of day
    assert histogram_analyzer.minutes_002040('23:59:59') == '23:40'

def test_minutes_002040_invalid_input(histogram_analyzer):
    """Test invalid input handling for minutes_002040"""
    with pytest.raises(ValueError):
        histogram_analyzer.minutes_002040('25:00:00')  # Invalid hour
    with pytest.raises(ValueError):
        histogram_analyzer.minutes_002040('invalid')   # Invalid format

def test_create_time_histogram(histogram_analyzer, sample_df, tmp_path):
    """Test histogram creation"""
    # Create temporary img directory
    img_dir = tmp_path / 'img'
    img_dir.mkdir()
    
    # Save original path and set temporary path
    original_path = histogram_analyzer.img_path
    histogram_analyzer.img_path = img_dir / 'histograma.png'
    
    plt.close('all')  # Close any existing plots
    
    try:
        # Process the data
        df_result = histogram_analyzer.create_time_histogram(sample_df)
        
        # Check that time_grouped column was added
        assert 'time_grouped' in df_result.columns
        
        # Check that all times were grouped correctly
        assert len(df_result) == len(sample_df)
        
        # Check that histogram was created
        assert histogram_analyzer.img_path.exists()
        
    finally:
        plt.close('all')  # Clean up
        histogram_analyzer.img_path = original_path

def test_time_grouping_consistency(histogram_analyzer, sample_df):
    """Test consistency of time grouping"""
    df_result = histogram_analyzer.create_time_histogram(sample_df)
    
    # Check that times are grouped consistently
    grouped_times = df_result['time_grouped'].unique()
    
    # Verify that all grouped times are in correct format
    for time in grouped_times:
        hours, minutes = map(int, time.split(':'))
        assert 0 <= hours <= 23
        assert minutes in [0, 20, 40]

if __name__ == "__main__":
    pytest.main([__file__])