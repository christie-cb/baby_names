import requests
import json
import pandas as pd


if __name__=="__main__":
    filename = 'NUTS_Level_3__January_2018__Boundaries.geojson'
    counties = json.load(open(filename))

    df = pd.DataFrame({
        'NUTS': ['"Bristol, City of"', "Somerset"],
        'name': ['Jolene', 'Dolly']
        })

    import plotly.express as px

    fig = px.choropleth(df, geojson=counties, locations='NUTS', color='name',
        featureidkey='properties.nuts318nm',
        labels={'name':'name'}
        )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

