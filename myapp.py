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



post_data()