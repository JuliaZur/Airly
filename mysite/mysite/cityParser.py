import requests
import datetime

class CityParser():
    def __init__(self,city):
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + str(city) + "&key=AIzaSyCtsPG6-Nc-I7NgzPqo9LvZF7pOXX_as1E"
        cityJson = requests.get(url).json()
        self.name = cityJson['results'][0]['formatted_address']
        latitude = cityJson['results'][0]['geometry']['location']['lat']
        longitude = cityJson['results'][0]['geometry']['location']['lng']
        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=" + str(latitude) + "&longitude=" + str(longitude) + "&historyResolutionHours=24&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        geoJson = requests.get(url).json()
        self.DateTime = datetime.datetime.now().strftime("%y-%m-%d  %H:%M")
        self.error = ""
        if geoJson['currentMeasurements']  == {}:
            self.error = "Brak aktualnych danych"
            self.AirQualityIndex = "?"
            self.Humidity = "?"
            self.PollutionLevel = "?"
            self.Temperature = "?"
            self.Pressure = "?"
            self.PM10 = "?"
            self.PM1 = "?"
            self.PM25 = "?"
        else:
            if geoJson['currentMeasurements']['airQualityIndex'] == '':
                self.AirQualityIndex = "?"
            else: self.AirQualityIndex = "{0:.2f}".format(geoJson['currentMeasurements']['airQualityIndex'])
            if geoJson['currentMeasurements']['pm1'] == '':
                self.PM1 = "?"
            else: self.PM1 = "{0:.2f}".format(geoJson['currentMeasurements']['pm1'])
            if geoJson['currentMeasurements']['pm25'] == '':
                self.PM25 = "?"
            else: self.PM25 = "{0:.2f}".format(geoJson['currentMeasurements']['pm25'])
            if geoJson['currentMeasurements']['pm10'] == '':
                self.PM10 = "?"
            else: self.PM10 = "{0:.2f}".format(geoJson['currentMeasurements']['pm10'])
            if geoJson['currentMeasurements']['pressure'] == '':
                self.Pressure = "?"
            else: self.Pressure = "{0:.2f}".format(float(geoJson['currentMeasurements']['pressure'])/100)
            if geoJson['currentMeasurements']['humidity'] == '':
                self.Humidity = "?"
            else: self.Humidity = "{0:.2f}".format(geoJson['currentMeasurements']['humidity'])
            if geoJson['currentMeasurements']['temperature'] == '':
                self.Temperature = "?"
            else: self.Temperature = "{0:.2f}".format(geoJson['currentMeasurements']['temperature'])
            if geoJson['currentMeasurements']['pollutionLevel'] == '':
                self.PollutionLevel = "?"
            else: self.PollutionLevel = geoJson['currentMeasurements']['pollutionLevel']
