import requests
import datetime

class SensorParser():
    def __init__(self,id):
        url = "https://airapi.airly.eu/v1/sensor/measurements?sensorId=" + str(id) + "&historyHours=24&historyResolutionHours=1&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        idJson = requests.get(url).json()
        self.name = "Sensor ID: " + str(id)
        self.DateTime = datetime.datetime.now().strftime("%y-%m-%d  %H:%M")
        self.error = ""
        if idJson['currentMeasurements']  == {}:
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
            if idJson['currentMeasurements']['airQualityIndex'] == '':
                self.AirQualityIndex = "?"
            else: self.AirQualityIndex = "{0:.2f}".format(idJson['currentMeasurements']['airQualityIndex'])
            if idJson['currentMeasurements']['pm1'] == '':
                self.PM1 = "?"
            else: self.PM1 = "{0:.2f}".format(idJson['currentMeasurements']['pm1'])
            if idJson['currentMeasurements']['pm25'] == '':
                self.PM25 = "?"
            else: self.PM25 = "{0:.2f}".format(idJson['currentMeasurements']['pm25'])
            if idJson['currentMeasurements']['pm10'] == '':
                self.PM10 = "?"
            else: self.PM10 = "{0:.2f}".format(idJson['currentMeasurements']['pm10'])
            if idJson['currentMeasurements']['pressure'] == '':
                self.Pressure = "?"
            else: self.Pressure = "{0:.2f}".format(float(idJson['currentMeasurements']['pressure'])/100)
            if idJson['currentMeasurements']['humidity'] == '':
                self.Humidity = "?"
            else: self.Humidity = "{0:.2f}".format(idJson['currentMeasurements']['humidity'])
            if idJson['currentMeasurements']['temperature'] == '':
                self.Temperature = "?"
            else: self.Temperature = "{0:.2f}".format(idJson['currentMeasurements']['temperature'])
            if idJson['currentMeasurements']['pollutionLevel'] == '':
                self.PollutionLevel = "?"
            else: self.PollutionLevel = idJson['currentMeasurements']['pollutionLevel']
