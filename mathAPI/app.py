from flask import Flask, request, jsonify
from flask_restful import Api, Resource





app = Flask(__name__)
api = Api(app)

#check if the data poted is correct
def checkPostedData(postedData, functionName):
    if (functionName == 'Add'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200
    if (functionName == 'Subtract'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200
    if (functionName == 'Multiply'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200
    if (functionName == 'Divide'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200
 #if Add was requested using the POST mtd it would come here
class Add(Resource):
    def post(self):
       
    #step1: get posted data
        postedData = request.get_json()
    
     #step2 check if data posted is correct
        status_code = checkPostedData(postedData, 'Add')
        if (status_code != 200):
            retJson = {
                'Message': 'An error occured: one or more value not given',
                'Status Code': status_code
            }
            return jsonify(retJson)
    #step3: if posted data is correct perform this
        x = int(postedData['x'])
        y = int(postedData['y'])
        ret = x + y
        retJson = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retJson)

#if Add was requested using the POST mtd it would come here
class Subtract(Resource):
    def post(self):
        #step1: get posted data
        postedData = request.get_json()
    
     #step2 check if data posted is correct
        status_code = checkPostedData(postedData, 'Subtract')
        if (status_code != 200):
            retJson = {
                'Message': 'An error occured: one or more value not given',
                'Status Code': status_code
            }
            return jsonify(retJson)
    #step3: if posted data is correct perform this
        x = int(postedData['x'])
        y = int(postedData['y'])
        ret = x - y
        retJson = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retJson)
class Multipy(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, 'Multiply')
        if (status_code != 200):
            retJson = {
                'Message': 'An error occured: one or more value not given',
                'Status Code': status_code
            }
            return jsonify(retJson)
    #step3: if posted data is correct perform this
        x = int(postedData['x'])
        y = int(postedData['y'])
        ret = x * y
        retJson = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retJson)

class Divide(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, 'Divide')
        if (status_code != 200):
            retJson = {
                'Message': 'An error occured: one or more value not given',
                'Status Code': status_code
            }
            return jsonify(retJson)
    #step3: if posted data is correct perform this
        x = int(postedData['x'])
        y = int(postedData['y'])
        res = x / y
        #round() rounds up to 2d.p
        ret = round(res, 2)
        retJson = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retJson)



api.add_resource(Add, '/add')
api.add_resource(Subtract, '/sub')
api.add_resource(Multipy, '/mult')
api.add_resource(Divide, '/div')


@app.route('/')
def home():
    return 'Hello World'







if __name__ == '__main__':
    app.run(debug=True)