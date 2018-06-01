import json
import requests

api_token = 'kenon'
api_url_base = 'https://api.project/tests/v2/users'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(kenon)}

def get_account_info():

    api_url = '{0}account'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
		
account_info = get_account_info()

if account_info is not None:
    print("Here's your info: ")
    for k, v in account_info['account'].items():
        print('{0}:{1}'.format(k, v))

else:
    print('[!] Request Failed')