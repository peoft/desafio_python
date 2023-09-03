import requests

def update_user(url, user):
    response = requests.put(f"{url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False


