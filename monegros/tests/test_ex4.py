import pytest
import pandas as pd
from monegros.src.ex4_clubs import ClubAnalyzer

@pytest.fixture
def club_analyzer():
    """Fixture to create a ClubAnalyzer instance"""
    return ClubAnalyzer()

@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing"""
    return pd.DataFrame({
        'dorsal': range(1, 8),
        'biker': [f'Biker{i}' for i in range(1, 8)],
        'club': [
            'C.C. Huesca',
            'Club Ciclista Oscense',
            'PEÑA CICLISTA EXAMPLE',
            'A.C. Testing Club',
            'Club Testing C.C.',
            None,
            ''
        ],
        'time': ['05:00:00' for _ in range(7)]
    })

def test_clean_club_basic(club_analyzer):
    """Test basic club name cleaning"""
    test_cases = [
        ('C.C. Huesca', 'HUESCA'),
        ('Club Ciclista Oscense', 'OSCENSE'),
        ('PEÑA CICLISTA EXAMPLE', 'EXAMPLE'),
        ('A.C. Testing', 'TESTING'),
        ('Testing C.C.', 'TESTING'),
    ]
    
    for input_name, expected_output in test_cases:
        assert club_analyzer.clean_club(input_name) == expected_output

def test_clean_club_edge_cases(club_analyzer):
    """Test edge cases for club cleaning"""
    test_cases = [
        (None, 'INDEPENDIENTE'),
        ('', 'INDEPENDIENTE'),
        (' ', 'INDEPENDIENTE'),
        ('INDEPENDIENTE', 'INDEPENDIENTE'),
    ]
    
    for input_name, expected_output in test_cases:
        assert club_analyzer.clean_club(input_name) == expected_output

def test_clean_club_complex_cases(club_analyzer):
    """Test more complex club name cleaning scenarios"""
    test_cases = [
        ('C.C. Test C.C.', 'TEST'),
        ('A.D. Test A.C.', 'TEST'),
        ('Club Ciclista Test CC', 'TEST'),
        ('PEÑA CICLISTA Test C.D.', 'TEST'),
    ]
    
    for input_name, expected_output in test_cases:
        assert club_analyzer.clean_club(input_name) == expected_output

def test_analyze_clubs(club_analyzer, sample_df):
    """Test club analysis functionality"""
    df_result = club_analyzer.analyze_clubs(sample_df)
    
    # Check that club_clean column was added
    assert 'club_clean' in df_result.columns
    
    # Check that all rows have a club_clean value
    assert not df_result['club_clean'].isna().any()
    
    # Check that empty/null clubs are marked as INDEPENDIENTE
    empty_clubs = df_result[df_result['club'].isna() | (df_result['club'] == '')]
    assert all(empty_clubs['club_clean'] == 'INDEPENDIENTE')
    
    # Check that original data wasn't modified
    assert 'club_clean' not in sample_df.columns

def test_club_summary_structure(club_analyzer, sample_df):
    """Test the structure of the club summary"""
    df_result = club_analyzer.analyze_clubs(sample_df)
    
    # Get unique clubs
    unique_clubs = df_result['club_clean'].value_counts()
    
    # Check that all clubs are represented
    assert len(unique_clubs) > 0
    
    # Check that counts are positive
    assert all(unique_clubs > 0)
    
    # Check that INDEPENDIENTE exists (due to None/empty values in sample)
    assert 'INDEPENDIENTE' in unique_clubs.index

if __name__ == "__main__":
    pytest.main([__file__])