import requests

class Map():
    def __init__(self):
        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=50.06&longitude=19.94&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.malopolskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.malopolskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=50.26&longitude=19.02&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.slaskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.slaskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=50.67&longitude=17.92&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.opolskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.opolskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=51.10&longitude=17.03&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.dolnoslaskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.dolnoslaskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=51.93&longitude=15.50&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.lubuskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.lubuskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=53.42&longitude=14.44&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.zachodniopomorskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.zachodniopomorskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=54.35&longitude=18.64&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.pomorskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.pomorskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=53.77&longitude=20.48&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.warminskomazurskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.warminskomazurskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=53.13&longitude=23.16&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.podlaskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.podlaskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=51.24&longitude=22.45&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.lubelskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.lubelskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=50.04&longitude=21.99&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.podkarpackie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.podkarpackie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=50.86&longitude=21.99&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.swietokrzyskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.swietokrzyskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=51.75&longitude=19.45&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.lodzkie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.lodzkie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=52.40&longitude=16.92&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.wielkopolskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.wielkopolskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=53.12&longitude=18.00&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.kujawskopomorskie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.kujawskopomorskie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])

        url = "https://airapi.airly.eu/v1/mapPoint/measurements?latitude=52.22&longitude=21.01&apikey=MfISs2LAcsqLAIKBkuMLrYyqrNXvXdLe&Accept:%20application/json"
        json = requests.get(url).json()
        self.mazowieckie = "?"
        if json['currentMeasurements'] != {}:
            if json['currentMeasurements']['airQualityIndex'] != '':
                self.mazowieckie = "{0:.2f}".format(json['currentMeasurements']['airQualityIndex'])
