from flask import Flask
from flask_restful import Api
from Resources import Carros

app = Flask(__name__)

api = Api(app)

api.add_resource(Carros,'/carros')

if __name__ == '__main__':
    app.run(debug = True)