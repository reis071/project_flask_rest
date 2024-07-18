from flask import Flask
from flask_restful import Api
from resources.Carros import Carros,Carro

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:grc12grc@localhost/teste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_request
def criar_banco():
    db.create_all()

api.add_resource(Carros,'/carros')
api.add_resource(Carro,'/carros/<int:id_carro>')

if __name__ == '__main__':
    from conx import db
    db.init_app(app)
    app.run(debug = True)