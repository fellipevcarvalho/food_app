import os 

restaurantes = ['Pizza','Churrasco']

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
    print ('3. Ativar restaurante')
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
    print(texto)
    print()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'Restaurante {nome_restaurante} foi cadastrado\n')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes:
        print(f'.{restaurante}')

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
            print('Ativar Restaurantes')
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