from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure
import requests

app = FastAPI()


response = requests.get('/api/get')
print(response.json())

@app.route('/api/get', methods=['GET'])
def handle_get():
    data = {'message': 'Solicitud GET recibida'}
    return jsonify(data)


data = {'title': 'ReactPy POST Request Example'}
response = requests.post('/api/post', json=data)
print(response.json())

@component
def App():
    return html.section(
        
    )

configure (app, App)