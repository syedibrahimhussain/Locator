

from flask import Flask, render_template,request,jsonify
import requests
import geocoder
import urllib.parse
app = Flask(__name__)
'''

'''

@app.route("/")
def index():
	#Import Libraries
	return render_template('index.html')

@app.route("/thankyous", methods=['POST'])
def thank_you():
	# Then get the data from the form
	address = str(request.form['loc'])
	print(address)
	url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
	response = requests.get(url).json()
	URL = "https://discover.search.hereapi.com/v1/discover"
	latitude =  str(response[0]["lat"])
	longitude = str(response[0]["lon"])
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
	#print(result)
	return render_template('thankyou.html',result=result)



if __name__ == '__main__':
    app.run(debug=True)


