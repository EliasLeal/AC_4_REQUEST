from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route('/v1/tipo')
def home():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    return response.json()

@app.route('/v1/tipo', methods=["POST"])
def cadastrar():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    enviar = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.post(api_url, json=enviar)
    return response.json()

@app.route('/v1/tipo', methods=["DELETE"])
def deletar():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.delete(api_url)
    return response.json()

if __name__ == '__main__':
    app.run()
