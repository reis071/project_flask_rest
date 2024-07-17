from flask_restful import Resource

class Carros(Resource):
    def get(self):
        return [{
            'id_carro':1,
            'nome':'celta',
            'ano':2006},
                {
            'id_carro':2,
            'nome':'prisma',
            'ano':2017}
                ]