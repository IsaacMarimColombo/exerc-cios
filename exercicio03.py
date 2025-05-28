def verificar_idade(Nome, idade):
    if idade >= 18:
        return f"{nome} é maior de idade"
    else:
        return f"{nome} é menor de idade"
    
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

resultado = verificar_idade(nome, idade)

print(resultado)
