import requests
import json
import pandas as pd


if __name__=="__main__":
    json_url = 'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'
    response = requests.get(json_url)
    with open('geojson.json', mode='wb') as json_file:
        json_file.write(response.content)

    filename = 'geojson.json'
    counties = [json.loads(line) for line in open(filename)]
    
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
        dtype={"fips": str})

    import plotly.express as px

    fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
        color_continuous_scale="Viridis",
        range_color=(0, 12),
        scope="usa",
        labels={'unemp':'unemployment rate'}
        )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

