import requests
import json
import pandas as pd

class GeoChart(object):
    def __init__(self, data, geojson):
        self.data = data
        self.geojson = geojson

    def get_fig(self, column_name, palette):
        #column_name will be 'girl_count' or 'boy_count'
        fig = px.choropleth_mapbox(
            self.data, geojson=self.geojson, 
            locations='NUTS318CD', 
            color=column_name,
            featureidkey='properties.nuts318cd',
            zoom=6, center = {"lat": 52.7064, "lon": 2.7418},
            labels={column_name:'name'}, mapbox_style="carto-positron",
            color_discrete_sequence=palette
        )
        return fig

def make_color_palette(list_of_num_lists):
    rgb_list = []
    for item in list_of_num_lists:
        rgb = 'rgb({}, {}, {})'.format(item[0], item[1], item[2])
        rgb_list.append(rgb)
    return rgb_list

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
    filename = 'data/NUTS_county_boundaries.geojson'
    counties = json.load(open(filename))

    converter = pd.read_csv('data/areacd_converter.csv')
    ons_data = pd.read_csv('data/top_by_region.csv')
    ons_data = get_ons_nuts(ons_data, converter)

    import plotly.express as px

    girl_colors = [
            [250,159,181], 
            [253,224,221],
            [247,104,161], 
            [252,197,192], 
            [234,169,189],
            [220,57,119],
            [231,41,138],
            [255,247,243]
            ]
    girl_colors = make_color_palette(girl_colors)

    gc = GeoChart(ons_data, counties)
    fig = gc.get_fig('girl_count', girl_colors)
    fig.update_geos(
            fitbounds="locations", 
            visible=False, 
            showcoastlines=True)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()
