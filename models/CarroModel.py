class CarroModel:
    def __init__(self,id_carro,nome,ano):
        self.id_carro = id_carro
        self.nome = nome 
        self.ano = ano
    
    def json(self):
        return {
            'id_carro': self.id_carro,
            'nome': self.nome,
            'ano': self.ano
        }
        
        
        