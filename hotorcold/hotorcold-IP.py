from urllib.request import urlopen
import json
import re



def getPublicIP():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)

def locateme(IP):
    # Get Location from ipinfo
    url = "http://ipinfo.io/" + IP + "/json"
    response = urlopen(url)
    data = json.load(response)
    city = data['city']
    country = data['country']
    return (city,country)

def hotorcold_IP(city_country):
    apikey = 'API key to open weather map should be inserted here'
    url = "https://api.openweathermap.org/data/2.5/weather" + "?q=" + city_country [0] + "," + city_country[1] + "&appid=" + apikey + "&units=metric"
    response = urlopen(url)
    data = json.load(response)
    city = data ['name']
    temp = data ['main']['temp']
    #temp = weather ['temp']
    print(f"at {city}")
    print(f"it's {temp} degrees outside !")


hotorcold_IP(locateme(getPublicIP()))
