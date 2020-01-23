from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def online():
    return 'on-line!'

artists = ['Bruno Mars','Jack Johnson','Adele'];

@app.route('/artists', methods=['GET'])
def get_all():
    return json.dumps(artists)

@app.route('/artists/<int:index>', methods=['GET'])
def get_by_index(index):
    return json.dumps(artists[index])

@app.route('/artists/<int:index>', methods=['DELETE'])
def delete(index):
    artists.pop(index)
    return json.dumps(artists)

@app.route('/artists', methods=['POST'])
def post():
    name = request.json['name']
    artists.append(name)
    return json.dumps(artists)

@app.route('/artists/<int:index>', methods=['PUT'])
def put(index):
    name = request.json['name']
    artists.insert(index, name)
    return json.dumps(artists)
