from clients.weatherapi_service import ApiWeather

get_weather = ApiWeather()

input_local = input("digite uma cidade/país/estado ")

result = get_weather.get_weather_local(input_local)


print(result)
