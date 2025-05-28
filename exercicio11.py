import json
import os

veiculos = "veiculos.json"

def carregar_dados():
    if os.path.exists(veiculos):
        with open(veiculos, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
def obter_dados():
    marca = input("Informe a marca do carro: ")
    modelo = input("Informe o modelo do carro: ")
    ano = int(input("Informe o ano do carro: "))
    cor = input("Informe a cor do carro: ")

    carros ={
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "cor": cor
    }
    
    return carros

def cadastrar_veiculo(dados_veiculo):
    carros = carregar_dados()
    carros.append(dados_veiculo)

    with open(veiculos, "w", encoding="utf-8" ) as arq_json:
        json.dump(carros, arq_json, ensure_ascii=False, indent=4)

def mostrar_veiculos(dados_veiculo):
    if dados_veiculo:
        for carro in dados_veiculo:
            print("="*80)
            print(f"""
                Marca: {carro["marca"]}
                Modelo: {carro["modelo"]}  
                Ano: {carro["ano"]}        
                Cor: {carro["cor"]}
""")
    else:
        print("Nenhum veiculo cadastrado no momento")

def iniciar_sistema():
    carros = carregar_dados()
    while True:
        print(" ")
        print("="*80)
        print("Opção 1 - Mostrar lista de veiculos.")
        print("Opção 2 - Cadastrar novo veiculo.")
        print("Opção 3 - Sair do sistema.")
        print("="*80)

        escolha = input("Escolha uma das opções para iniciar: ")

        if escolha == "1":
            mostrar_veiculos(carros)
        elif escolha == "2":
            cadastrar_veiculo(obter_dados())
        elif escolha == "3":
            print("Seu sistema foi finalizado!")
            break
        else:
            print("Essa escolha é invalida, por favor tente novamente.")

iniciar_sistema()


