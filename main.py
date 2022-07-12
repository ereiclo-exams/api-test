from crypt import methods
from urllib import response
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

import json

app = Flask(__name__)



class Singleton:
    _instance = None
    array = []

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance
    
    def __init__(self):
        if Singleton._instance != None:
            raise Exception('This class is a singleton!')
        else:
            Singleton._instance = self


# class Usuario(db.Model):
    # def __init__(self, name):
        # self.name  = name
        # self.count = 0
@app.route('/')
def index():
    return 'hola'

@app.route('/hola')
def hola():
    response = {'vamos a ver':3}
    return jsonify(response)

@app.route('/adios',methods=['POST'])
def adios():
    response = None
    if request.get_json()['2'] == 'no':
        response = {'no vamos a ver':'si'}
    elif request.get_json()['2'] == 'si':
        response = {'no vamos a ver':'no'}

    return jsonify(response)
    

@app.route('/singleton',methods=['POST'])
def singleton():
    s = Singleton.getInstance()
    print(int(request.get_json()['data']))
    s.array.append(int(request.get_json()['data']))
    response = {'len':len(s.array)}

    return jsonify(response)
    


if __name__ == '__main__':
    app.run(host='localhost',port=5002,debug=True)

