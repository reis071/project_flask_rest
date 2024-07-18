from flask_restful import Resource,reqparse
from models.CarroModel import CarroModel



class Carros(Resource):
    def get(self):
        return {"carros":[carro.json() for carro in CarroModel.query.all()]}

class Carro(Resource):
    def get(self,id_carro):
        carro = CarroModel.find(id_carro)
        if carro:
            return carro.json()
        
        return {"message":"car is not found"}

    def post(self,id_carro):
        if CarroModel.find(id_carro):
            return {"message": "car exists"}
        argumento = reqparse.RequestParser()
        
        argumento.add_argument('nome')
        argumento.add_argument('ano')
        
        valor = argumento.parse_args()
        
        objeto_carro = CarroModel(id_carro, **valor)
        objeto_carro.save()
        return objeto_carro.json()
    
    def put(self,id_carro):
        argumento = reqparse.RequestParser()
        argumento.add_argument('nome')
        argumento.add_argument('ano')
        valor = argumento.parse_args()
        
        carro = CarroModel.find(id_carro)
        if carro:
            carro.update(**valor)
            carro.save()
            return carro.json(),200
        
        carro = CarroModel(id_carro,**valor)
        
        carro.save()
        
        return carro.json(),201
    
    def delete(self,id_carro):
        carro = CarroModel.find(id_carro)
        
        if carro:
            carro.delete()
            return {"message":"carro delete"}