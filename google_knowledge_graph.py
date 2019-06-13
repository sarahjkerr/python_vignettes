#Libraries
import pandas as pd
import urllib
import requests

#Global vars
api_key = 'PASTE YOUR API KEY HERE'

#Define search function
def search_graph(keyword):
    base_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    
    params = {
    'query': keyword,
    'key': api_key,
    'limit': 1,
    'indent': True
    }
    
    url = base_url + '?' + urllib.parse.urlencode(params)
    
    search_the_graph = requests.get(url)
    
    response = search_the_graph.json()
    
    for element in response['itemListElement']:
        print(element['result']['name'] + ';' + str(element['result']['@type']) + ';' + element['result']['description'])
        
        
 #Apply search function
 df['response'] = df['col1'].apply(lambda x: search_graph(x))
