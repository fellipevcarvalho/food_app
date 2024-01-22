import os 

restaurantes = [{'nome':'Outback','categoria':'Árabe', 'ativo':False},
                {'nome':'Pizzaria Marcante','categoria':'Italiana','ativo':True},
                {'nome':'Tasty B','categoria':'Brasileira','ativo':False}
               ]




def exibir_nome_main():
    print('''
███████╗███████╗██╗░░░██╗██╗░░░░░██╗██████╗░░█████╗░░█████╗░
██╔════╝██╔════╝██║░░░██║██║░░░░░██║██╔══██╗██╔══██╗██╔══██╗
█████╗░░█████╗░░██║░░░██║██║░░░░░██║██████╔╝███████║██║░░██║
██╔══╝░░██╔══╝░░██║░░░██║██║░░░░░██║██╔═══╝░██╔══██║██║░░██║
██║░░░░░███████╗╚██████╔╝███████╗██║██║░░░░░██║░░██║╚█████╔╝
╚═╝░░░░░╚══════╝░╚═════╝░╚══════╝╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░
''')




def exibir_opcoes():
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurante')
    print ('3. Alterar status restaurante')
    print ('4. Sair\n')




def finalizar_app():
    exibir_subtitulo('Finalizar app')



def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao início')
    main()



def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()



def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha) 
    print(texto)
    print(linha)
    print()


    '''Essa função é responsavel por cadastrar um novo restaurante'''
def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria,'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} foi cadastrado\n')
    voltar_menu_principal()



    '''Essa função é responsavel por listar os restaurantes já cadastrados'''
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    
    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

        
    voltar_menu_principal()


def alterar_status_restaurante():
    exibir_subtitulo('Alterando status restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso ' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    

    voltar_menu_principal()


def escolher_opcao():
    try:    
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()    
    except:
        opcao_invalida()



def main():
    os.system('cls')
    exibir_nome_main()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()