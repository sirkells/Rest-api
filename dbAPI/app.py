from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt







app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb://db:27017")
db = client.SentenceDB
users = db['Users']

class Register(Resource):
    def post(self):
        #step1 get posted data from user
        postedData = request.get_json()

        #get the data
        username = postedData['username']
        password = postedData['password']

        hashedpw = bcrypt.hashpw(password, bcrypt.gensalt())

        #store username and pwd into db
        users.insert({
            "Username": username,
            "Password": hashedpw,
            "Sentence": ""
        })

        retJson = {
            "status": 200,
            "message": "You succesfully signed up"

        }
        return jsonify(retJson)

class Store(Resource):
    

    









if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")