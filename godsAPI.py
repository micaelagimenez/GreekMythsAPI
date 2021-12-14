from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

#get all the data
class Gods(Resource):
    def get(self):
        data = pd.read_csv('https://github.com/micaelagimenez/GreekMythsAPI/blob/main/greek_gods.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

#search for god's name
class Search(Resource):
    def __init__(self):
        # read csv file
        self.data = pd.read_csv('https://github.com/micaelagimenez/GreekMythsAPI/blob/main/greek_gods.csv')

    def get(self, name):
        name_cap = name.capitalize()
        data_gods = self.data.loc[(self.data['name-english'] == name_cap) | (self.data['name-greek'] == name_cap)].to_dict()
        # return data found in csv
        return jsonify({'message': data_gods})

#get main type
class Type(Resource):
    def __init__(self):
        # read csv file
        self.data = pd.read_csv('https://github.com/micaelagimenez/GreekMythsAPI/blob/main/greek_gods.csv')

    def get(self, type):
        data_type = self.data.loc[self.data['main-type'] == type].to_dict()
        # return data found in csv
        return jsonify({'message': data_type})


api.add_resource(Gods, '/gods')
api.add_resource(Search, '/gods/<string:name>')
api.add_resource(Type, '/<string:type>')

if __name__ == '__main__':
    app.run()  # run Flask app
