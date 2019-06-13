#Packages
import pandas as pd
import requests
import urllib

#Define any global vars
api_key = 'PASTE YOUR API KEY HERE'

#Set up sample df
df_list = {'col1': [40.710316, 40.716892], 'col2': [-74.004967, -73.804695], 'col3': ['presbyterian','health']}
df = pd.DataFrame(data=df_list)

#Define places search function
def search_places(lat, long, placename):
    
    location = str(lat) + "," + str(long)
    keyword = placename
    
    url_base = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    
    params = {
        'key' : api_key,
        'input' : keyword,
        'inputtype' : 'textquery',
        'locationbias' : 'point:' + location
    }
    
    url = url_base + '?' + urllib.parse.urlencode(params, safe=',:')
    
    google_request = requests.get(url)

    response = google_request.json()
    
    return str(response['candidates'])

#Apply search function to df and store json results in new col (not ideal; need to write function to parse salient parts of json results)
df['results'] = df.apply(lambda row: search_places(row['col1'], row['col2'], row['col3']), axis=1)

#Remove extra characters from result column
df['place_id'] = df['place_id'].apply(lambda x: x.replace("[{'place_id': '","").replace("'}]",""))

#Define details search function
def search_details(goog_id):
    
    url_base = 'https://maps.googleapis.com/maps/api/place/details/json'
    
    params = {
        'key' : api_key,
        'placeid' : goog_id,    
    }
    
    url = url_base + '?' + urllib.parse.urlencode(params)
    
    google_request = requests.get(url)
    
    response = google_request.json()
    
    print(response)
    
#Apply search function to df's place_id column
df['place_results'] = df['place_id'].apply(lambda x: search_details(x))
