import re      #Biblioteca de expressoes regulares.
import time    #Biblioteca para esperar alguns segundos.
def menu():     #Função que retorna ao usuário o menu na tela e pede ao mesmo uma opção.
    print('\n'*20)
    print('┌───────────────────────────────────────┐') 
    print('│Menu                                   │')
    print('│1. Consultar pratos.                   │')
    print('│2. Cadastrar prato.                    │')
    print('│3. Excluir prato.                      │')
    print('│4. Calcular quantidade de ingredientes.│')
    print('│5. Criar cardapio.                     │')
    print('│6. Consultar cardapio.                 │')
    print('│                                       │')
    print('│0. Sair.                               │')
    print('└───────────────────────────────────────┘')

    possibilidades = [0,1,2,3,4,5,6]                        #Lista que armazena as únidas possibilidades que o usuário tem
    opcao = int(input("Selecione a opção desejada: "))
    while opcao not in possibilidades:                  #Caso ele selecione uma posição que não está na lista, ele da Opção inválida
        print('\n')
        print("Opção Inválida! Por favor selecione uma opção do Menu.")
        opcao = int(input("Selecione a opção desejada: "))
    print('\n'*20)
    return opcao

def setup():    #Função que fará o Setup onde serão lidos os arquivos .txt e armazenados em lista. 
    arquivo_pratos = open("pratos.txt","r")             #Le o arquivo pratos.txt 
    lista_pratos = arquivo_pratos.readlines()
    lista_pratos_tratada = list()
    for prato in lista_pratos:                          #Colocando cada linha em uma posição da Lista.
        lista_pratos_tratada.append(prato.replace("\n",""))
    
    my_file = open("ingredientes.txt", "r")             #Le o arquivo ingredientes.txt
    content_list = my_file.readlines()
    ingredientes = list()
    for ingrediente in content_list:                    #Colocando cada linha em uma posição da Lista.
        ingredientes.append(ingrediente.replace("\n",""))

    my_file = open("quantidades.txt", "r")              #Le o arquivo quantidades.txt
    content_list = my_file.readlines()
    quantidades = list()
    for quantidade in content_list:                     #Colocando cada linha em uma posição da Lista.
        quantidades.append(quantidade.replace("\n",""))

    my_file = open("cardapio.txt", "r")              #Le o arquivo cardapio.txt
    content_list = my_file.readlines()
    cardapios = list()
    for cardapio in content_list:                     #Colocando cada linha em uma posição da Lista.
        cardapios.append(cardapio.replace("\n",""))   

    return lista_pratos_tratada, ingredientes, quantidades, cardapios      #Retorna as 5 listas 

def consultar_pratos(pratos, ingredientes, quantidades):    #Função que consulta os pratos.
    i = 1
    print('\n')
    print("Pratos:")                
    for prato in pratos:                                    #Printa os pratos de forma ordenada.
        print(f"{i}. {prato}")
        i += 1 
    print('\n')
    numero = int(input("Selecione o prato a ser consultado: "))
    print('\n'*20)
    print(f"Prato: {pratos[numero-1]}")
    print('\n')
    ingredientes = ingredientes[numero-1].split(',')        #Separa os ingredientes em uma lista.
    quantidades = quantidades[numero-1].split(',')          #Separa as quantidades em uma lista.
    for i in range(0,len(ingredientes)):                    #Printa os Ingredientes e quantidade de forma Ordenada.
        print(f"{i+1}. {ingredientes[i]} ({quantidades[i]})")
    print('\n')
    enter = input("Aperte <ENTER> para continuar...")
    print('\n'*20)

def cadastrar_prato(pratos, ingredientes, quantidades):     #Função que permite cadastrar os pratos.
    print("Cadastro de novos pratos: ")
    prato = input("Nome do prato: ")
    pratos.append(prato)            #Adiciona o novo prato na lista
    ingrediente = "algo"
    ingredientes_prato, quantidades_prato = list(), list()  #Cria duas listas vazias para os ingredientes e quantidades.
    print('\n')
    print("Ingredientes: ")
    print("Adicione um ingrediente por linha, um valor vazio para ambos encerrará o cadastro de ingredientes.")
    i = 1
    while ingrediente != "":
        print('\n')
        ingrediente = input(f'Digite o {i}° ingrediente: ')
        quantidade = input(f'Digite a quantidade (gramas ou un.) do {i}° ingrediente (exemplo: 20g): ')
        ingredientes_prato.append(ingrediente)      #Salva os valores na lista.
        quantidades_prato.append(quantidade)
        i += 1

    textfile = open("pratos.txt", "w")              #Salva a nova lista de pratos no arquivo .txt
    for prato in pratos:
        textfile.write(prato + "\n")
    textfile.close()

    linha_ingrediente = ""                          #Separa os Ingredientes do novo prato por , e salva na mesma célula da lista.
    for i in range(0, len(ingredientes_prato)-1):
        if i == (len(ingredientes_prato)-2):
            linha_ingrediente = linha_ingrediente + ingredientes_prato[i]
        else:
            linha_ingrediente = linha_ingrediente + ingredientes_prato[i] + ","
    ingredientes.append(linha_ingrediente)

    textfile = open("ingredientes.txt", "w")        #Salva o arquivo ingredientes novo.
    for ingrediente in ingredientes:
        textfile.write(ingrediente + "\n")
    textfile.close()

    linha_quantidade = ""
    for i in range(0, len(quantidades_prato)-1):    #Separa os Ingredientes do novo prato por , e salva na mesma célula da lista.
        if i == (len(quantidades_prato)-2):
            linha_quantidade = linha_quantidade + quantidades_prato[i]
        else:
            linha_quantidade = linha_quantidade + quantidades_prato[i] + ","
    quantidades.append(linha_quantidade)

    textfile = open("quantidades.txt", "w")         #Salva o arquivo quantidades novo.
    for quantidade in quantidades:
        textfile.write(quantidade + "\n")
    textfile.close()

    enter = input("Prato cadastrado com sucesso! Pressione <ENTER> para continuar...")

def excluir_prato(pratos, ingredientes, quantidades):       #Função que permite o usuário excluir pratos.
    i = 1
    print('\n')
    print("Pratos:")
    for prato in pratos:
        print(f"{i}. {prato}")
        i += 1 
    print('\n')
    n = int(input("Selecione o prato a ser removido: "))

    confirmacao = input(f"Você deseja remover '{pratos[n-1]}'? [s/n]: ")    #Confirma com o usuário se o mesmo tem certeza da operação

    if confirmacao == 's' or confirmacao == 'S':                            #Caso selecione 's' irá excluir as listas e reescrever o arquivo
        pratos.pop(n-1)                     #Excluindo o prato da lista.
        ingredientes.pop(n-1)               #Excluindo os ingredientes da lista.
        quantidades.pop(n-1)                #Excluindo as quantidades da lista.
        textfile = open("pratos.txt", "w")  #Salvando o arquivo novamente com a nova lista pratos.
        for prato in pratos:
            textfile.write(prato + "\n")
        textfile.close()

        textfile = open("ingredientes.txt", "w")    #Salvando o arquivo novamente com a nova lista ingredientes.
        for ingrediente in ingredientes:
            textfile.write(ingrediente + "\n")
        textfile.close()

        textfile = open("quantidades.txt", "w")     #Salvando o arquivo novamente com a nova lista quantidades.
        for quantidade in quantidades:
            textfile.write(quantidade + "\n")
        textfile.close()
    elif confirmacao == 'n' or confirmacao == 'N':  #Caso selecione 'n' irá retornar ao menu em 2 segundos.
        print("Retornando ao Menu...")
        time.sleep(2)
    else:
        print("Erro, tente novamente...")           #Caso selecione qualquer outra coisa apresenta erro e retorna ao menu.
        time.sleep(2)

def calcular_quantidade(pratos, ingredientes, quantidades): #Função que calcula a quantidade exata de ingredientes para quantidade de alunos.
    i = 1
    print('\n')
    print("Pratos:")
    for prato in pratos:
        print(f"{i}. {prato}")
        i += 1 
    print('\n')
    n = int(input("Selecione o prato a ser calculado a quantidade de ingredientes: "))
    alunos = int(input("Para quantos alunos serão produzidos o prato: "))
    print('\n'*20)
    print(f"Prato '{pratos[n-1]}' para {alunos} alunos.")
    print("Serão necessários: ")
    ingredientes = ingredientes[n-1].split(',')         #Separa os ingredientes da linha por ',' do prato em uma lista 
    quantidades = quantidades[n-1].split(',')           #Separa as quantidades da linha por ',' do prato em uma lista 
    for i in range(0,len(ingredientes)):
        quantidade = int(''.join(filter(str.isdigit, quantidades[i])))      #Pega apenas os valores numéricos da string.
        unidade = "".join(re.split("[^a-zA-Z.]*", quantidades[i]))          #Pega apenas os caracteres da string.
        print(f"{i+1}. {ingredientes[i]}: {quantidade*alunos}{unidade}")    #Retorna de forma ordenada na tela para o usuário
    print('\n')
    enter = input("Pressione <ENTER> para continuar...")

def cadastrar_cardapio(pratos, cardapios):              #Função de cadastrar o cardapio da semana
    semana=['segunda', 'terça', 'quarta', 'quinta', 'sexta']
    almoco=[]
    cardapios=[]
    for i in semana:
        print(f'Informe o almoço da {i}-feira')
        print('Opções: \n')
        for x in range(len(pratos)):
            print(x,' - ',pratos[x])
        while True:
            opcao=int(input('Digite o numero referente a refeição escolhida: '))  #Apenas adiciona ao cardapio as refeiçoes cadastradas
            if opcao <0 or opcao >=len(pratos):
                print('Opcão invalida! Por favor tente novamente ')
            else:
                print('Refeição adicionada no cardapio')
                print('\n'*20)
                cardapios.append(pratos[opcao])
                almoco.append(pratos[opcao])
                break
    textfile = open("cardapio.txt", "r+")              #Abre o arquivo cardapio.txt
    textfile.truncate(0)
    for cardapio in cardapios:
        textfile.write(cardapio + "\n")
    textfile.close() 
    print('\n')
    enter = input("Pressione <ENTER> para continuar...")

def consultar_cardapio(pratos, cardapios, ingredientes):   #Função de consulta do cardapio
    semana=['segunda', 'terça', 'quarta', 'quinta', 'sexta']
    for c in range(len(cardapios)):
        print(semana[c]+"-feira: \t", cardapios[c])

        for i in range(len(pratos)):                       #Exibe os ingredientes separando por virgula
            if pratos[i] == cardapios[c]:
                print("\t\t Ingredientes: ",ingredientes[i].replace(",",", "),"\n") 
                break
    print('\n')
    enter = input("Pressione <ENTER> para continuar...")

