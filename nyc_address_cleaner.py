##Working toward creating a class that cleans address, with methods that work on specific parts of the address string
##Will be included in a larger data cleaning package
##Also include USPS address validation

cities = ['BRONX','BROOKLYN','MANHATTAN','QUEENS','STATEN ISLAND','BX','BK','BKLYN','BKLN','QNS','SI','MN','NYC','Arverne','Astoria','Bayside','Bayswater','Beechhurst','Bellaire',
          'Belle Harbor','Blissville','Breezy Point','Broad Channel','Brooklyn Manor','Bushwick Junction','Cambria Heights','Cedar Manor','Cedar Manor Houses','College Point',
          'Corona','Douglaston','East Elmhurst','Edgemere','Edgemere Houses','Elmhurst','Far Rockaway','Flushing','Forest Hills','Forest Hills Gardens','Fresh Meadows','Fresh Pond',
          'Fresh Pond Junction','Garden Bay Manor','Glen Oaks','Glendale','Haberman','Hamilton Beach','Hammel','Hammel','Hammels Houses','Hillside','Holland','Hollis','Hollis Hills',
          'Howard Beach','Jackson Heights','Jamaica','Kew Gardens','Kew Gardens Hills','Laurelton','Lefrak City','Linden Hill','Little Neck','Locust Manor','Long Island City','Malba',
          'Maspeth','Middle Village','Morris Park','Murray Hill','Neponsit','North Beach','Oakland Gardens', 'Old Germania Heights','Ozone Park','Parkside','Parsons Beach','Queens',
          'Queens Village','Queensbridge Houses','Ravenswood Houses','Rego Park','Richmond Hill','Ridgewood','Rochdale Village','Rockaway Park','Rockaway Point','Rosedale','Roxbury',
          'Roy Reuther Houses','Saint Albans','Seaside','Somerville','South Ozone Park','Springfield Gardens','Steinway','Sunnyside','Sunnyside Gardens','Surrey Estates','Terrace Heights',
          'Utopia','Walden Terrace','Wave Crest','Whitestone','Woodhaven','Woodside','Woodside Houses','NEW YORK CITY','NEW YORK']
          
cities = [i.upper() for i in cities]

def get_city(x, city_list):

    for item in city_list:
        if item in x.upper():
            return item
        else:
            pass           
