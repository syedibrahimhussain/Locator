import requests
import geocoder

def locate():
    
    g = geocoder.ip("me")

    #c_lat = g.lat
    #c_lng = g.lng

    #print(c_lng)
    #print(g)
    URL = "https://discover.search.hereapi.com/v1/discover"
    latitude = g.lat
    longitude =g.lng
    api_key = 'tu4m3GFeH7ze3oQDsOBqMpRk3-yFx7XyapfV92Yw-uo' # Acquire from developer.here.com
    query = 'hospitals'
    limit = 5

    PARAMS = {
                'apikey':api_key,
                'q':query,
                'limit': limit,
                'at':'{},{}'.format(latitude,longitude)
             } 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()


    hospitalOne = data['items'][0]['title']
    hospitalOne_address =  data['items'][0]['address']['label']

    hospitalTwo = data['items'][1]['title']
    hospitalTwo_address =  data['items'][1]['address']['label']

    hospitalThree = data['items'][2]['title']
    hospitalThree_address =  data['items'][2]['address']['label']

    hospitalFour = data['items'][3]['title']
    hospitalFour_address =  data['items'][3]['address']['label']

    hospitalFive = data['items'][4]['title']
    hospitalFive_address =  data['items'][4]['address']['label']

    result=[hospitalOne_address,hospitalTwo_address,hospitalThree_address,hospitalFour_address,hospitalFive_address]
    return result
#locate()