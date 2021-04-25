import requests, base64
import json

auth_url = "https://accounts.spotify.com/api/token"
client_id = 'b74cf8069d564daaa6bcc7eb21e80c52'
client_secret = '217c6d35964545128c1efc70908ebfbc'

authHeader = {}
authData = {}

def getAccessToken(client_id, client):
    message = f"{client_id}:{client_secret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    authHeader['Authorization'] = "Basic " + base64_message
    authData['grant_type'] = "client_credentials"
    res = requests.post(auth_url, headers=authHeader, data=authData)

    responseObject = res.json()
    #print(json.dumps(responseObject, indent=2))
    accessToken = responseObject['access_token']
    return accessToken

display_token = getAccessToken(client_id, client_secret)
print(display_token)
