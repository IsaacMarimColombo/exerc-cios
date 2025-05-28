import json
import os 

data = "data.json"

def carregar_dados():
    if os.path.exists(carregar_dados):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
clientes = carregar_dados
for cliente in clientes:
    print(cliente ["nome_completo"])