import urllib.request
import json
import os

getIP = input("[+] Enter IP --> ")
url = "https://ipinfo.io/" + getIP + "/json"

try:
    getInfo = urllib.request.urlopen( url )

except:
    print( "\n[!] - IP not found! - [!]\n" )

infoList = json.load(getInfo)

def whoisIPinfo(ip):

    try:

        myComand = "whois " + getIP
        whoisInfo = os.popen( myComand ).read()
        return whoisInfo

    except:

        return "\n [!] -- Error -- [!] \n"

     
print( "-" * 60 )

print( "IP: ", infoList["ip"] )
print( "City: ", infoList["city"] )
print( "Region: ", ifoList["region"] )
print( "Country: ", infoList["country"] )
print( "Hostname: ", infoList["hostname"] )

print( "-" * 60 )
print( whoisIPinfo ( getIP))