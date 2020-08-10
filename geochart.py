import requests
import json

if __name__=="__main__":
    json_url = 'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'
    response = requests.get(json_url)
    with open('geojson.json', mode='wb') as json_file:
        json_file.write(response.content)

    filename = 'geojson.json'
    counties = [json.loads(line) for line in open(filename)]
    counties[0]['features']
