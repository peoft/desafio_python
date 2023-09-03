import requests

def get_user(url, id):
    response = requests.get(f'{url}/users/{id}');
    return response.json() if response.status_code == 200 else None;
