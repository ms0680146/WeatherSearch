import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
	# Get the Open Weather Map data! 
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e838d1d6af30ba43c999889e016cd428'

	if request.method == 'POST':
		# print(request.POST)
		form = CityForm(request.POST)
		form.save()

	form = CityForm() # Instantiate the CityForm

	cities = City.objects.all() # Get the cities name from database(City Modle)!
	weather_data = []  # Store all cities weather data!
	iskeyerror = False
	for city in cities:
		try:
			r = requests.get(url.format(city)).json()   # request to get the url info and convert to json!
			# Create a dict to store the city weather information!
			city_weather = {  
				'city' :  city.name,
				'lat' : r['coord']['lat'],
				'lon' : r['coord']['lon'],
				'temperature' :  r['main']['temp'],
				'description' : r['weather'][0]['description'],
				'icon' : r['weather'][0]['icon'],
			}
			print(city_weather)		
			weather_data.append(city_weather)
		except KeyError:
			iskeyerror = True
	#print(weather_data)
		iskeyerror = False
		# Create a dict to store the information and send to templates(weathersearch.html)!
		context = {'weather_data' : weather_data, 'form' : form, 'iskeyerror' : iskeyerror} 
    # Render on the templates(weathersearch.html)
	return render(request,'weather/weathersearch.html', context)

