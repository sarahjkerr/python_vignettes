#Packages
import pandas as pd
import requests
import urllib

#Set up sample df
df_list = {'col1': [40.1234, 40.5678], 'col2': [-73.1234, -73.5678], 'col3': ['Place1','Place2']}
df = pd.DataFrame(data=df_list)

#Define search function
def search_places(lat, long, placename):
    
    location = str(lat) + "," + str(long)
    keyword = placename
    
    api_key = 'YOUR_API_KEY'
    url_base = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    
    params = {
        'key' : api_key,
        'location' : location,
        'radius' : 3,
        'keyword' : keyword,
        'rankby' : 'distance'
    }
    
    url = url_base + '?' + urllib.parse.urlencode(params)
    
    return url

    response = requests.get(url)

#Apply search function to df and store json results in new col (not ideal; need to write function to parse salient parts of json results)
df['results'] = df.apply(lambda row: search_places(row['col1'], row['col2'], row['col3']), axis=1)
