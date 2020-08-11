import requests
import json
import pandas as pd

def get_ons_nuts(ons_data, converter):
    merged = ons_data.merge(converter, on="LAU118CD", how="left")
    merged = merged.drop_duplicates('NUTS318CD')
    return merged

def get_geojson_areanames(json_data):
    geojson_names = []
    for item in json_data['features']:
        county_name = item['properties']['nuts318cd']
        geojson_names.append(county_name)
    return geojson_names

if __name__=="__main__":
    filename = 'NUTS_Level_3__January_2018__Boundaries.geojson'
    counties = json.load(open(filename))

    converter = pd.read_csv('areacd_converter.csv')
    ons_data = pd.read_csv('top_by_region.csv')
    ons_data = get_ons_nuts(ons_data, converter)

    import plotly.express as px

    fig = px.choropleth(ons_data, geojson=counties, locations='NUTS318CD', color='girl_count',
        featureidkey='properties.nuts318cd',
        labels={'girl_count':'name'}
        )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

