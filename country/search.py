import requests

'''
http://localhost:3000/country/search?searchText=Bhutan

by full name: https://restcountries.eu/rest/v2/name/{name}?fullText=true
by alpha code: https://restcountries.eu/rest/v2/alpha/{code}
by calling code: https://restcountries.eu/rest/v2/callingcode/{callingcode}
by capital: https://restcountries.eu/rest/v2/capital/{capital}
'''

def searchText(text):
    base_url = "https://restcountries.eu/rest/v2"
    endpoint = f'{base_url}/name/{text}?fullText=true' ## searching name first
    r = requests.get(endpoint)
    data_found = True

    if(r.status_code in (200,202)):
        data = list(r.json())[0]
    else:
        endpoint = f'{base_url}/alpha/{text}' ## search by code
        r = requests.get(endpoint)
        if(r.status_code in (200,202)):
            data = dict(r.json())
        else:
            endpoint = f'{base_url}/callingcode/{text}'   ## search by callcode
            r = requests.get(endpoint)
            if(r.status_code in (200,202)):
                data = list(r.json())[0]
            else:
                endpoint = f'{base_url}/capital/{text}'   ## search by capital
                r = requests.get(endpoint)
                if(r.status_code in (200,202)):
                    data = list(r.json())[0]
                else:
                    data_found = False

    if(data_found):
        output = {
                "name": data['name'],
                "capital": data['capital'],
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