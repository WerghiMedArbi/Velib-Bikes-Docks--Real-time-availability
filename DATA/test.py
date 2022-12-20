import requests
baseurl="https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-emplacement-des-stations&q="
requests.get(baseurl).json()
list(requests.get(baseurl).json()   )
