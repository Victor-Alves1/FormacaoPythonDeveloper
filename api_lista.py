from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'C#', 'JavaScript']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades