import requests
from pymongo import MongoClient

# 1 - Estabelecendo conexão com o MongoDB e Database
client = MongoClient() #Não foi passado parâmetro na classe, logo, ele se conecta à porta padrão do MongoDB (local)
db = client.nobel

# 2 - Importando os dados em documentos
for collection_name in ["prizes", "laureates"]: #Primeira iteração vai pegar os valores de "prizes" e na segunda vai pegar os valores de "laureates"
    response = requests.get(f"http://api.nobelprize.org/v1/{collection_name[:-1]}.json") #(collecton_name[:-1]) pois a chave dos valores na api é no singular (prize, laureate)
    
    documents = response.json()[collection_name] #Converte a resposta da requisição em um objeto JSON e extrai a parte que corresponde à coleção atual (collection_name)
    db[collection_name].insert_many(documents) #Insere todos os documentos extraídos acima na coleção correspondente (collection_name)
    
# 3 - Acessando coleções / Contagem de documentos na coleção
prizes = db["prizes"]
laureates = db["laureates"]

len_prizes = prizes.count_documents({})
len_laureates = laureates.count_documents({})
