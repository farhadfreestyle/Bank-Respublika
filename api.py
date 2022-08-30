import requests
import xmltodict
import datetime

day  = datetime.date.today().strftime("%d.%m.%Y")
url = f"https://www.cbar.az/currencies/{day}.xml"


response = requests.request("GET", url)

dict_data = xmltodict.parse(response.content)


a = dict_data['ValCurs']
for i in a['ValType'][1]['Valute']:
    if i['@Code']=='USD':
       dollar =  i['Value']
    elif i['@Code']=='EUR':
       euro =  i['Value']

    elif i['@Code']=='RUB':
       ruble =  i['Value']
    
    elif i['@Code']=='GBP':
       gbp =  i['Value']


