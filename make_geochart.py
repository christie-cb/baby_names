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
    filename = 'NUTS_county_boundaries.geojson'
    counties = json.load(open(filename))

    converter = pd.read_csv('csv_data/areacd_converter.csv')
    ons_data = pd.read_csv('csv_data/top_by_region.csv')
    ons_data = get_ons_nuts(ons_data, converter)

    import plotly.express as px

    girl_colours = [
            'rgb(250,159,181)', 
            'rgb(253,224,221)',
            'rgb(247,104,161)', 
            'rgb(252,197,192)', 
            'rgb(234,169,189)']

    fig = px.choropleth_mapbox(ons_data, geojson=counties, 
        locations='NUTS318CD', color='girl_count',
        featureidkey='properties.nuts318cd',
        zoom=6, center = {"lat": 52.7064, "lon": 2.7418},
        labels={'girl_count':'name'}, mapbox_style="carto-positron",
        color_discrete_sequence=girl_colours
        )
    fig.update_geos(
            fitbounds="locations", 
            visible=False, 
            showcoastlines=True)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()
    fig.write_html('geochart.html')
