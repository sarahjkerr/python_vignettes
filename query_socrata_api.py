#Import libraries

from sodapy import Socrata
import pandas as pd
import time

#Set your credentials; this example queries the NYSDOS Open Data Active Corporations Since 1800 dataset

app_token = 'YOUR APP TOKEN'
username = 'YOUR USERNAME'
password = 'YOUR PASSWORD'
dataset_id = 'n9v6-gdp6'

client = Socrata('data.ny.gov',
                app_token,
                username=username,
                password=password)

#Create an empty dataframe where query results will be stored

nysdos = pd.DataFrame()

#Figure out the total length of the dataset. If you're planning on pulling a subset, define that here as well.
#For this example, I am pulling only businesses whose corporate registrations are in the Bronx (county = Bronx), since the full
#dataset is 2.7 million rows.

no_records = client.get(dataset_id, county = 'BRONX', select="COUNT(*)")
total_results = int(no_records[0]['COUNT'])
#88979

#Figure out how you want to chunk the dataset down. The latest version of the API allows for unlimited size; however, it's a bit
#uncouth to make a huge API call for a free open data service. The old max was 50,000, so that's a good rule of thumb.
#I use 30,000 in this example to test the printing and loop functions

loop_size = 30000
num_loops = round(total_results/loop_size)
#will run 3 loops

#Finally, make the request

for i in range(num_loops):
    socrata_results = client.get(dataset_id, 
                                 county="BRONX", 
                                 limit=loop_size, 
                                 offset=loop_size*i, 
                                 order="current_entity_name ASC")
    
    #Appends the results to the dataframe
    nysdos = nysdos.append(socrata_results, ignore_index=True)
    
    #Puts some time between the API calls to be gentle to Socrata's infrastructure. I'd make the wait longer for bigger
    #requests with a sizeable number of loops
    wait = np.random.randint(low=15, high=45, size=1)
    time.sleep(wait)
    
    #Gives you a heads up about status
    print('It\'s ' + str(time.asctime()) + ' and I fetched ' + str(len(nysdos)) + ' records! Now I\'m taking a ' + str(wait) + ' second nap before asking for more records so I don\'t blow up the API :) ')
    
