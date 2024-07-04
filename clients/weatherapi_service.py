import requests

class ApiWeather():
    
    def __init__(self):
        self.__base_url = 'http://api.weatherapi.com/v1/current.json'
        self.__api_key = 'sua_api_key'

    def get_weather_local(self, local):
        response = requests.get(
            url= f'{self.__base_url}?key={self.__api_key}&q={local}'
            )
        response.raise_for_status()
        data = response.json()
        return {
            'Local': data.get('location', {}).get('name', {}),
            'País': data.get('location',{}).get('country',{}),
            'Temperatura': data.get('current', {}).get('temp_c',{}),
            'Horario': data.get('location', {}).get('localtime',{}),
        }


    
   

    