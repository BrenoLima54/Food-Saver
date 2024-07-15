import time     #Biblioteca para esperar alguns segundos.
import funcoes  #Bibioteca de funçoes principais

def main():     #Funçao principal, onde define o fluxo do usuário.
    opcao = 1
    while opcao != 0:
        pratos, ingredientes, quantidades, cardapios = funcoes.setup()     #Setup onde serão lidos os arquivos .txt e armazenados em lista.               
        opcao = funcoes.menu()                                  #Retorna ao usuário o menu na tela e pede ao mesmo uma opção.
        if opcao == 1:
            funcoes.consultar_pratos(pratos, ingredientes, quantidades)     #Função que consulta os pratos.
        elif opcao == 2:
            funcoes.cadastrar_prato(pratos, ingredientes, quantidades)      #Função que permite cadastrar os pratos.
        elif opcao == 3:
            funcoes.excluir_prato(pratos, ingredientes, quantidades)        #Função que permite o usuário excluir pratos.
        elif opcao == 4:
            funcoes.calcular_quantidade(pratos, ingredientes, quantidades)  #Função que calcula a quantidade exata de ingredientes para quantidade de alunos.
        elif opcao == 5:
            funcoes.cadastrar_cardapio(pratos, cardapios)                   #Função que cria o cardapio semanal.
        elif opcao == 6:
            funcoes.consultar_cardapio(pratos, cardapios, ingredientes)     #Função que consulta o cardapio semanal.
            
    print("Encerrando...")
    time.sleep(1)

if __name__ == '__main__':
    main()
