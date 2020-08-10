import requests
import json
import pandas as pd


if __name__=="__main__":
    json_url = 'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'
    uk_json_url = 'https://raw.githubusercontent.com/deldersveld/topojson/master/countries/united-kingdom/uk-counties.json' 
    response = requests.get(json_url)
    with open('geojson.json', mode='wb') as json_file:
        json_file.write(response.content)

    #filename = 'geojson.json'
    #counties = [json.loads(line) for line in open(filename)]
    filename = '/Users/ccb/Desktop/NUTS_Level_3__January_2018__Boundaries.geojson'
    counties = json.load(open(filename))

    df = pd.DataFrame({
        'NUTS': ['UKC11', 'UK0'],
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

