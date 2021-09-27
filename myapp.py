import requests
import json

URL="http://127.0.0.1:8000/api/v1/users/"



def post_data():
    python_data = {
        "name":"vijay",
        "email":"a@gmail.com",
        "password":"blore",
    }

    json_data = json.dumps(python_data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

def get_data(id=None):
    data={}
    if id is not None:
        data['id'] = id
    json_data = json.dumps(data)
    headers = { 'content-type' : 'application/json' }
    r = requests.get(url=URL, headers = headers, data=json_data)
    data = r.json()
    print(data)



get_data(21)