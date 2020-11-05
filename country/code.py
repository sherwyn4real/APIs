import requests

'''example = https://restcountries.eu/rest/v2/alpha/{code}'''

def getCountryCode(code):
    base_url = "https://restcountries.eu/rest/v2"
    method = 'alpha'
    endpoint = f'{base_url}/{method}/{code}'
    r = requests.get(endpoint)

    if(r.status_code in (200,202)):
        data = dict(r.json())
        output = {
            "name": data['name'],
            "alpha2Code": data['alpha2Code'],
            "alpha3Code": data['alpha3Code'],
            "capital": data['capital'],
            "region": data['region'],
            "population": data['population'],
            "flag": data['flag'],
            "totalLanguages": len(data['languages']),
            "totalCurrencies": len(data['currencies']),
            "totalTimezones":len(data['timezones'])
        }
    else:
        output = {
            'status': r.status_code,
            'message': 'country not found'
        }
    return output,r.status_code
