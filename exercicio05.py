from exercicio04 import somar_numeros  
alunos = []

def obter_dados_aluno():
    nome_aluno = input("informe seu nome completo: ")
    email = input("informe o seu email completo: ")
    serie = input("informe sua serie: ")
    nota01 = int(input("informe sua primeira nota: "))
    nota02 = int(input("informe sua segunda nota: "))
    nota03 = int(input("informe sua terceira nota: "))

    return cadastrar(nome_aluno, email, serie, nota01, nota02, nota03)
    
def cadastrar(nome, email, Serie, nota01=0, nota02=0, nota03=0):


    notas = [nota01, nota02, nota03]   
    
    aluno = {
        "nome" : nome, 
        "email" : email,
        "serie" : Serie, 
        "notas" : notas,
        "media" : somar_numeros(notas)
        }

    alunos.append(aluno)

    return alunos

def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f"Nome do aluno: {aluno["nome"]} | email do aluno: {aluno["email"]} | serie do aluno: {aluno["serie"]} | Nota 01: {aluno["Nota01"]} | Nota 02: {aluno["Nota02"]} | Nota 03: {aluno["Nota03"]} | Media do Aluno: {aluno["media"]}")
  
    return

def iniciar_sistema():
    while True:
        print("="*80)
        print("opcao 1 => mostrar lista de alunos cadrastrados")
        print("opcao 2 => cadastar alunos")
        print("opcao 3 => sair do sistema")
        print("="*80)


        opcao = input("Escolha uma das opções acima: ")

        if opcao == "1":
            mostrar_dados_alunos(alunos)
        elif opcao == "2":
            obter_dados_aluno()
        else:
            print("Sistema finalizado")

iniciar_sistema()
