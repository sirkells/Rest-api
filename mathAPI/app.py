from flask import Flask, request, jsonify
from flask_restful import Api, Resource





app = Flask(__name__)


def checkPostedData(postedData, functionName):
    if (functionName == 'add'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):
        #if Add was requested using the POST mtd it would come here
    #step1
        postedData = request.get_json()
    
     #step2
        status_code = checkPostedData(postedData, 'add')
        if (status_code != 200):
            retJson = {

                'Message': 'An error occured',
                'Status Code': status_code
            }
            return jsonify(retJson)

        x = int(postedData['x'])
        y = int(postedData['y'])
        ret = x + y
        retJson = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retJson)

@app.route('/')
def home():
    return 'Hello World'







if __name__ == '__main__':
    app.run(debug=True)