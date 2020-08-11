import parse_ons
import pandas as pd

def test_split_csv():
    girl_count = pd.read_csv('girl_count.csv')
    boy_count = pd.read_csv('boy_count.csv')
    first_area = 'Hartlepool'
    final_area = 'Merthyr Tydfil'
    assert girl_count.iloc[678]['AREANM'] == first_area 
    assert girl_count.iloc[1015]['AREANM'] == final_area
    assert boy_count.iloc[0]['AREANM'] == first_area
    assert boy_count.iloc[336]['AREANM'] == final_area
    for count in [boy_count, girl_count]: 
        assert len(girl_count).columns == 104
        assert len(count.index) == 337
