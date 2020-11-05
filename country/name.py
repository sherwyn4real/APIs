import requests

'''
    endpoint
    example: https://restcountries.eu/rest/v2/name/united?fullText=true
'''

def getCountryName(country_name):
    print(111)
    base_url = "https://restcountries.eu/rest/v2"
    endpoint = f'{base_url}/name/{country_name}?fullText=true'

    r = requests.get(endpoint)
    print(122)
    if r.status_code in (200,202):
        data = list(r.json())
        output = {}
        output ={
            "name": data[0]['name'],
            "alpha2Code": data[0]['alpha2Code'],
            "alpha3Code": data[0]['alpha3Code'],
            "capital": data[0]['capital'],
            "region": data[0]['region'],
            "population": data[0]['population'],
            "flag": data[0]['flag'],
            "totalLanguages": len(data[0]['languages']),
            "totalCurrencies": len(data[0]['currencies'])
        }
    else:
        output = {
            'status': r.status_code,
            'message': 'country not found'
        }
    print(133)
    return output,r.status_code