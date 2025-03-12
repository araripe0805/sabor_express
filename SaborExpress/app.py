import os

restaurantes = [{'nome':'Inácio Burguers', 'Categoria':'Hamgueres', 'Atividade':False},
                {'nome':'Yasmim Sushis', 'Categoria':'Comida Japonesa', 'Atividade':True},
                {'nome':'Leo Churrascos', 'Categoria':'Carnes', 'Atividade':False}]

def exibir_titulo():
    '''Função para exibir titulo'''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
\n''')

def exibir_opcoes():
    '''Função para exibir as opções disponiveis no programa'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def encerrando_programa():
    '''Função para encerrar o programa quando escolher a opção sair'''
    limpar_terminal('Encerrando programa')

def opcao_invalida():
    '''Função para quando inserir uma opção invalida'''
    print('Opção invalida!\n')
    reiniciar()

def cadastrar_novo_restaurante():
    '''Essa Função é responsavel por cadastrar novos restaurantes'''
    limpar_terminal('Cadastro de novos Restaurantes')
    nome_restaurante = input('Digite o nome restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'Categoria': categoria_restaurante, 'Atividade': False}
    restaurantes.append(dados_restaurante)
    print('')
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso\n')
    reiniciar()

def listar_restaurantes():
    '''Função para listar todos os restaurantes cadastrados'''
    limpar_terminal('Listando todos os restaurantes')
    print(f'{'Nome do Restaurante:'.ljust(20)} | {'Categoria do Restaurante:'.ljust(20)} | {'Status do Restaurante:'.ljust(20)} \n')
    for i in restaurantes:
        nome_restaurante = i['nome']
        cadeira_restaurante = i['Categoria']
        atividade_restaurante = 'ativo' if i['Atividade'] else 'desativado'
        print(f'-> {nome_restaurante.ljust(20)} | {cadeira_restaurante.ljust(20)} | {atividade_restaurante.ljust(20)}\n')
    reiniciar()

def ativando_restaurante():
    '''Função para ativar um restaurante recem inserido'''
    limpar_terminal('Alterando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for i in restaurantes:
        if i['nome'] == nome_restaurante:
            restaurante_encontrado = True
            i['Atividade'] = not i['Atividade']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if i['Atividade'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O Restaurante não foi encontrado')
    reiniciar()

def reiniciar():
    '''Função para reiniciar as opções para selecionar uma nova'''
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def limpar_terminal(texto):
    '''Função para limpar textos anteriores'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcoes(): 
    '''Função para escolher a opção desejada'''
    try:  
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            print('Listar restaurantes')
            listar_restaurantes()

        elif opcao_escolhida == 3:
            ativando_restaurante()

        elif opcao_escolhida == 4:
            encerrando_programa()

        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()