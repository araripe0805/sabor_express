import os, time

lista_restaurantes = []

def exibir_titulo():
    '''Função que vai exibir o titulo inicial'''

    print('''
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    \n''')

def exibir_opcoes():
    '''Função para exibir as opções que são possiveis utilizar no programa'''

    print('1. Cadastrar novo restaurantes.\n'
    '2. Listar restaurantes cadastrados.\n'
    '3. Ativar restaurante cadastrado.\n'
    '4. Sair.\n')
    
    try:
        escolha = int(input('Escolha uma das opções a seguir: '))
        verificar_opcao(escolha)
    
    except:
        mensagem_opcao('Opção invalida!')
        main()

def cadastrando_novo_restaurante():
    '''Função que vai cadastrar novos restaurantes'''

    nome_restaurante = input('Digite o nome do novo restaurante: ').upper()
    print('')
    categoria_restaurante = input('Digite a categoria do novo restaurante: ').upper()
    print('')
    status_restaurante = 'desativado'

    dados_novo_restaurante = {'nome' : nome_restaurante , 'categoria' : categoria_restaurante , 'status' : status_restaurante}
    lista_restaurantes.append(dados_novo_restaurante)
    
    retorno()

def listando_restaurantes():
    '''Função que vai exibir os restaurantes cadastrados e algumas informações adicionais'''

    print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria do Restaurante'.ljust(20)} | {'Status do Restaurante'.ljust(20)}\n')

    for i in lista_restaurantes:
        nome_restaurante = i['nome']
        categoria_restaurante = i['categoria']
        if i['status'] == 'ativo':
            status_restaurante = 'ativo'
        
        else:
            status_restaurante = 'desativado'

        print(f'{nome_restaurante.title().ljust(20)} | {categoria_restaurante.title().ljust(24)} | {status_restaurante.title().ljust(20)}\n')

    retorno()

def ativando_restaurante():
    '''Função usada para ativar restaurantes'''

    nome_restaurante = input('Digite o restaurante que deseja ativas: ').upper()
    encontrado = 'nao'
    
    for i in lista_restaurantes:
        if i['nome'] == nome_restaurante:
            if i['status'] == 'desativado':
                i['status'] = 'ativo'
                print(f'\nO restaurante {nome_restaurante.title()} está ativo agora\n')
                encontrado = 'sim'
                break

            else:
                print(f'\nO restaurante {nome_restaurante.title()} já está ativo!\n')
                encontrado = 'sim'
                break

    if encontrado == 'sim':
        retorno()
    
    else:
        print(f'\nO restaurante {nome_restaurante.title()} não foi encontrado na lista de cadastros!\n')
        retorno()

def limpar_terminal():
    '''Função que vai limpar o terminal'''

    os.system('cls')

def retorno():
    '''Função que vai servir para exibir uma mensagem repetitiva'''

    input('Aperte qualquer tecla para retornar ao menu: ')
    limpar_terminal()
    print('Voltando ao menu...')
    time.sleep(2)
    main()

def verificar_opcao(escolha):
    '''Função que vai verificar qual opção você escolheu e direcionar para a função correspodente'''
    
    if escolha == 1:
        mensagem_opcao('Cadastrando novo restaurante...')
        cadastrando_novo_restaurante()

    elif escolha == 2:
        mensagem_opcao('Verificando restaurantes no sistema...')
        listando_restaurantes()

    elif escolha == 3:
        mensagem_opcao('Ativando restaurante no sistema...')
        ativando_restaurante()

    elif escolha == 4:
        mensagem_opcao('Encerrando programa...')
        retorno()

    else:
        mensagem_opcao('Opção invalida!')
        main()

def mensagem_opcao(texto):
    limpar_terminal()
    print(texto)
    time.sleep(2)
    limpar_terminal()

def main():
    '''Função que vai rodar códigos iniciais e principais'''
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    

if __name__ == '__main__':
    main()
