from flask import Flask,request
from flask_restful import Api,Resource
import requests
from country import name,code,search
from twitter import user
import os

app = Flask(__name__)
myapi = Api(app)

def Country(method,param):
    if method == 'name':
        return name.getCountryName(param)
    elif method == 'code':
        return code.getCountryCode(param)
    elif method == 'search':
        return search.searchText(param)
    else:
        return {'error': 400,'message':'bad request'},400

def Covid(method,param):
    pass

def Weather(method,param):
    pass

def Twitter(method,param):
    if method == 'user':
        return user.getUser(param)
    else:
        return {"status": 400,"message": "tweets not found"},400

class RestApi(Resource):
    def get(self,res,method,param): 
        print(res,method,param)
        if(res=='country'):
           return Country(method,param)
        elif (res=='covid'):
            return Covid(method,param)
        elif (res=='weather'):
            return Weather(method,param)
        elif (res == 'twitter'):
            return Twitter(method,param)
        else:
            return {'error': 400,'message':'bad request'},400


myapi.add_resource(RestApi,'/<string:res>/<string:method>/<string:param>')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = int(os.environ['PORT']))
