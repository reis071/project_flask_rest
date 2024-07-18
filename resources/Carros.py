from flask_restful import Resource,reqparse
lista_carros = [ {
            'id_carro':1,
            'nome':'celta',
            'ano':2006},
            {'id_carro':2,
            'nome':'prisma',
            'ano':2017}]

class Carros(Resource):
    def get(self):
        return lista_carros

class Carro(Resource):
    def get(self,id_carro):
        for carro in lista_carros:
            if carro['id_carro'] == id_carro:
                return carro

    def post(self,id_carro):
        argumento = reqparse.RequestParser()
        
        argumento.add_argument('nome')
        argumento.add_argument('ano')
        
        valor = argumento.parse_args()
        
        novo_carro ={
            'id_carro':id_carro,
            'nome':valor['nome'],
            'ano':valor['ano']
        }
        
        
        lista_carros.append(novo_carro)
        return novo_carro,200
    
    def put(self,id_carro):
        argumento = reqparse.RequestParser()
        argumento.add_argument('nome')
        argumento.add_argument('ano')
        valor = argumento.parse_args()
        
        for carro in lista_carros:
            if carro['id_carro'] == id_carro:
                novo_carro = {'id_carro':id_carro,**valor}
                carro.update(novo_carro)
                return novo_carro,200
  
        argumento = reqparse.RequestParser()
        argumento.add_argument('nome')
        argumento.add_argument('ano')
        
        valor = argumento.parse_args()
        carro_novo = {'id_carro':id_carro,**valor}
        lista_carros.append(carro_novo)
        return carro_novo,201 #criado
    
    def delete(self,id_carro):
        global lista_carros
        lista_carros = [carro for carro in lista_carros if carro['id_carro'] != id_carro]
        return {"message":"carro deleted"}