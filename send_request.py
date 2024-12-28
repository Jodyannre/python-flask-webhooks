import requests

url = "http://localhost:5000/webhook"

data = {
    "name": "my_name",
    "message": "my_message"
}

r = requests.post(url, json=data)

print(r.content)