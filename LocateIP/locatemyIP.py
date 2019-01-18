from urllib.request import urlopen
import json
import re

def get_IP():
    IP = str(input("please enter the IP address you want to locate "))
    return IP

def locateme(IP):
    # Get Location from ipinfo
    url = "http://ipinfo.io/" + IP + "/json"
    response = urlopen(url)
    data = json.load(response)
    city = data['city']
    country = data['country']
    location = data['loc']
    org = data['org']

    # Print Extracted Details
    print("\n")
    print (f"IP-info details for {IP}")
    print (f"City {city}")
    print (f"country {country}")
    print (f"location {location}")
    print("\n")


    #Get location from IP-API
    url = "http://ip-api.com/json/" + IP
    response = urlopen(url)
    data = json.load(response)
    city = data['city']
    country = data['country']
    location = data['lat']
    asnb = data['as']
    print (f"IP-API details for {IP}")
    print (f"City {city}")
    print (f"country {country}")
    print (f"location {location}")
    print (f"AS {asnb}")
    print("\n")

    #Get location from extreme-IP
    url = "http://ip-api.com/json/" + IP
    response = urlopen(url)
    data = json.load(response)
    city = data['city']
    country = data['country']
    location = data['lat']
    ispinfo = data['isp']
    print (f"extreme-IP details for {IP}")
    print (f"City {city}")
    print (f"country {country}")
    print (f"location {location}")
    print (f"ispinfo {ispinfo}")
    print("\n")

    #Get location from IP-stack
    url = "http://api.ipstack.com/" + IP + "?access_key=<accesskey to IP-stack inserted here>"
    response = urlopen(url)
    data = json.load(response)
    city = data['city']
    country = data['country_name']
    location = data['latitude']
    print (f"IP-stack details for {IP}")
    print (f"City {city}")
    print (f"country {country}")
    print (f"location {location}")
    print("\n")



IP = get_IP()
locateme(IP)
