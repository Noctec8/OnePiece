import pymongo
from bson.objectid import ObjectId

class Model:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client["OnePiece"]
        self.usuario_collection = self.db["AreaLogin"]
        self.piratas_collection = self.db["Piratas"]
        
        if not self.usuario_collection.find_one({"Usuario": "admin"}):
            self.usuario_collection.insert_one({"Usuario": "admin", "Senha": "123456", "Nivel": 2})

    def verificar_usuario(self, usuario, senha):
        return self.usuario_collection.find_one({"Usuario": usuario, "Senha": senha})

    def cadastrar_usuario(self, usuario, senha):
        verificarCadastro = self.usuario_collection.find_one({"Usuario": usuario})
        if verificarCadastro:
            return False 
        else:
            self.usuario_collection.insert_one({"Usuario": usuario, "Senha": senha, "Nivel": 1})
            return True  

    def inserir_pirata(self, nomePirata, akuma, haki, nomeTripulacao, possuiArma, recompensa):
        
        if self.piratas_collection.find_one({"Nome do Pirata": nomePirata}):
            return False

        return self.piratas_collection.insert_one({
            "Nome do Pirata": nomePirata, 
            "Akuma no Mi": akuma, 
            "Haki": haki, 
            "Nome da Tripulação": nomeTripulacao, 
            "Possui Arma": possuiArma, 
            "Recompensa": recompensa
            })
    
    def editar_pirata(self, _id, nomePirata, akuma, haki, nomeTripulacao, possuiArma, recompensa):
        query = { "_id": ObjectId(_id) }
        values = { "$set": { "Nome do Pirata": nomePirata, "Akuma no Mi": akuma, "Haki": haki, "Nome da Tripulação": nomeTripulacao, "Possui Arma": possuiArma, "Recompensa": recompensa } }
        
        return self.piratas_collection.update_one(query, values)

    def buscar_piratas(self, pirata):
        if pirata == "":
            return self.piratas_collection.find({})
        else:
            return self.piratas_collection.find_one({"Nome do Pirata": pirata})
            
    
    def deletar_pirata(self, pirata):
        return self.piratas_collection.delete_one({"Nome do Pirata": pirata})



            
        