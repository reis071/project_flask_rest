from conx import db
class CarroModel(db.Model):
    __tablename__ = 'carro'
    id_carro = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80))
    ano = db.Column(db.Integer)
    
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
        
    @classmethod
    def find(cls,id_carro):
        carro = cls.query.filter_by(id_carro = id_carro).first()
        if carro:
            return carro
        else:
            return None
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self,nome,ano):
        self.nome = nome 
        self.ano = ano
        
    def delete(self):
        
        db.session.delete(self)
        db.session.commit()