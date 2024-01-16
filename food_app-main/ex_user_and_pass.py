usuario_correto = 'feulipao'
senha_correta = 'senha'

user = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

if user == usuario_correto and senha == senha_correta:
    print('Login successful\n CHAMA FIO')
else:
    print('Errou fio!')