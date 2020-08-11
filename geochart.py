import requests
import json
import pandas as pd

def get_ons_areanames(ons_data):
    return ons_data["LAU118CD"]

def get_geojson_areanames(json_data):
    geojson_names = []
    for item in json_data['features']:
        county_name = item['properties']['nuts318cd']
        geojson_names.append(county_name)
    return geojson_names

if __name__=="__main__":
    filename = 'NUTS_Level_3__January_2018__Boundaries.geojson'
    counties = json.load(open(filename))

    df = pd.DataFrame({
        'NUTS': ['"Bristol, City of"', "Somerset"],
        'name': ['Jolene', 'Dolly']
        })

    import plotly.express as px

    fig = px.choropleth(df, geojson=counties, locations='NUTS', color='name',
        featureidkey='properties.nuts318cd',
        labels={'name':'name'}
        )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

