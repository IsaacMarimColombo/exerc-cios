db_clientes = "db_clientes.json"
# clientes = []
import json
import os
def carregar_dados():
    if os.path.exists(db_clientes):
        with open(db_clientes, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return [] 

 
def obter_dados_cliente():
    nome_cliente = input("Informe o Nome Completo do Cliente")
    cpf_cliente = int(input("Informe o CPF Completo do Cliente"))
    rg_cliente = int(input("Informe o  Numero de RG Completo do Cliente"))
    data_de_nascimento_cliente = input("Informe a Data de Nascimento do Cliente")
    endereco_cliente = input("Informe o Endereço do Cliente")
    cidade_cliente = input("Informe a Cidade do Cliente")
    estado_cliente = input("Informe o Estado do Cliente")
    telefone_cliente = int(input("Informe o Numero de Telefone do Cliente"))
    celular_cliente = int(input("Informe o Numero de Celular do Cliente"))
    email_cliente = input("Informe o E-mail Completo do Cliente")

    cliente = {
        "nome_cliente": nome_cliente,
        "cpf_cliente": cpf_cliente,
        "rg_cliente": rg_cliente,
        "data_de_nascimento_cliente": data_de_nascimento_cliente,
        "endereco_cliente": endereco_cliente,
        "cidade_cliente": cidade_cliente,
        "estado_cliente": estado_cliente,
        "telefone_cliente": telefone_cliente,
        "celular_cliente": celular_cliente,
        "email_cliente": email_cliente

    }

    return cliente

def cadastrar_cliente(dados_cliente):
    clientes = carregar_dados()
    clientes.append(dados_cliente)

    with open(db_clientes, "w" , encoding="utf-8") as arq_json:
        json.dump(clientes, arq_json, indent=4, ensure_ascii=False)



def mostrar_dados_clientes():
    for cliente in obter_dados_cliente:
        print(f"""
              Nome do Cliente: {cliente["nome do cliente"]}
              CPF do Cliente: {cliente["cpf do cliente"]}
              RG do Cliente: {cliente["RG do cliente"]}
              Data de Nascimento do Cliente{cliente["data de nascimento do cliente"]}
              Endereco do Cliente{cliente["endereço do cliente"]}
              Cidade do Cliente{cliente["cidade do cliente"]}
              Estado do Cliente{cliente["estado do cliente"]}
              Telefone do Cliente{cliente["telefone do cliente"]}
              Celular do Cliente{cliente["celular do cliente"]}
              """)
        
def iniciar_sistema():
    clientes = carregar_dados()
    while True:
        
        print("")
        print("="*80)
        print("Opcao 1 - Mostrar Lista de Clientes")
        print("Opcao 2 - Cadastrar Clientes")
        print("Opcao 3 - Sair do Sistema.")
        print("="*80)

        opcao = input("Escolha uma das opções do Menu: ")

        if opcao == "1":
            mostrar_dados_clientes(clientes)
        elif opcao == "2":
            cadastrar_cliente(obter_dados_cliente())
        elif opcao == "3":
            print("Sistema Finalizado")
            break
        else:
            print("Opcao invalida, escolha uma das opções no menu.")
iniciar_sistema()