from django.shortcuts import render
from django.shortcuts import redirect
from .forms import inputform
import requests

# Create your views here.
def Get_Weather(request):
 city_name= None
 weather_data=None
 if request.method == 'POST':
  city_name= request.POST.get("city")
  weather_data=Get_APIData(city_name)
  print(weather_data)
 return render(request, 'forms.html', {"city":city_name, "weather": weather_data})

def Get_APIData(city_name):
  API_key = 'cf89e2ee26d64335b79135336253108'
  print("city name is ", city_name)
  #city_name = "Karachi"
  #if city_name:
  Weather_API_EndPoint = f"https://api.weatherapi.com/v1/current.json?key=cf89e2ee26d64335b79135336253108&q={city_name}&aqi=2"
  Get_Long_Lat = "http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={l}&appid={API key}"

 
  
  response = requests.get(Weather_API_EndPoint)  
  data=response.json()
  
  weather_dict = {
    "city": data["location"]["name"],
    "country" : data["location"]["country"],
    "temperature": data["current"]["temp_c"],
    "condition": data["current"]["condition"]["text"]
  
}
  return weather_dict
  
    

