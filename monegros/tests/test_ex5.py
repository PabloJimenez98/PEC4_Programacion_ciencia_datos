import pytest
import pandas as pd
from src.ex5_ucsc import analyze_ucsc

@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing"""
    return pd.DataFrame({
        'dorsal': range(1, 7),
        'biker': [f'Biker{i}' for i in range(1, 7)],
        'club_clean': ['UCSC', 'OTHER', 'UCSC', 'OTHER', 'UCSC', 'OTHER'],
        'time': ['05:30:00', '05:15:00', '05:00:00', '05:45:00', '05:20:00', '06:00:00']
    })

def test_analyze_ucsc_basic(sample_df):
    """Test basic UCSC analysis functionality"""
    ucsc_df, best_time_df, position_info = analyze_ucsc(sample_df)
    
    # Check UCSC cyclists extraction
    assert len(ucsc_df) == 3
    assert all(ucsc_df['club_clean'] == 'UCSC')
    
    # Check best time identification
    assert best_time_df['time'] == '05:00:00'
    assert best_time_df['biker'] == 'Biker3'
    
    # Check position calculation
    assert position_info['position'] == 1
    assert position_info['total'] == 6
    assert position_info['percentage'] == pytest.approx(16.67, rel=0.01)

def test_analyze_ucsc_no_cyclists():
    """Test analysis when no UCSC cyclists are present"""
    df = pd.DataFrame({
        'dorsal': [1, 2],
        'biker': ['Biker1', 'Biker2'],
        'club_clean': ['OTHER1', 'OTHER2'],
        'time': ['05:00:00', '05:30:00']
    })
    
    ucsc_df, best_time_df, position_info = analyze_ucsc(df)
    
    assert len(ucsc_df) == 0
    assert best_time_df is None
    assert position_info is None

def test_analyze_ucsc_missing_column():
    """Test error handling when club_clean column is missing"""
    df = pd.DataFrame({
        'dorsal': [1],
        'biker': ['Biker1'],
        'time': ['05:00:00']
    })
    
    with pytest.raises(ValueError, match="DataFrame must include 'club_clean' column"):
        analyze_ucsc(df)

def test_analyze_ucsc_single_cyclist(sample_df):
    """Test analysis with only one UCSC cyclist"""
    # Keep only one UCSC cyclist
    df_single = sample_df.copy()
    df_single.loc[df_single['club_clean'] == 'UCSC', 'club_clean'] = 'OTHER'
    df_single.loc[2, 'club_clean'] = 'UCSC'  # Keep only one UCSC cyclist
    
    ucsc_df, best_time_df, position_info = analyze_ucsc(df_single)
    
    assert len(ucsc_df) == 1
    assert best_time_df['biker'] == 'Biker3'
    assert position_info['position'] == 1
    assert position_info['total'] == 6

def test_analyze_ucsc_tied_times():
    """Test analysis when there are tied times"""
    df = pd.DataFrame({
        'dorsal': range(1, 5),
        'biker': [f'Biker{i}' for i in range(1, 5)],
        'club_clean': ['UCSC', 'OTHER', 'UCSC', 'OTHER'],
        'time': ['05:00:00', '05:00:00', '05:30:00', '06:00:00']
    })
    
    ucsc_df, best_time_df, position_info = analyze_ucsc(df)
    
    assert len(ucsc_df) == 2
    assert best_time_df['time'] == '05:00:00'
    assert position_info['position'] in [1, 2]  # Could be either position due to tie

if __name__ == "__main__":
    pytest.main([__file__])