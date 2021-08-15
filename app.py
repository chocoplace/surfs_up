from flask import Flask, jsonify

#Set Up the Flask APP
app = Flask(__name__)

#Welcome route 
@app.route('/')
def hello_world():
    return 'Hello world'


