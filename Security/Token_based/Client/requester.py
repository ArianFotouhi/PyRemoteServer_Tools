import requests

# Replace with your server URL
server_url = 'http://127.0.0.1:8080/'

# User credentials for logging in
username = 'user1'
password = 'password1'

# Login to obtain a JWT token
login_data = {
    'username': username,
    'password': password
}

login_response = requests.post(f'{server_url}/login', json=login_data)

if login_response.status_code == 200:
    token = login_response.json()['token']
    print('Login successful. Token obtained:', token)

    # Set the Authorization header with the JWT token
    headers = {'Authorization': token}

    # Make an authenticated GET request to /route1
    route1_response = requests.get(f'{server_url}/route1', headers=headers)

    if route1_response.status_code == 200:
        print('Access to /route1 successful:')
        print(route1_response.json())
    else:
        print('Access to /route1 failed:')
        print(route1_response.status_code, route1_response.text)
else:
    print('Login failed:')
    print(login_response.status_code, login_response.text)
