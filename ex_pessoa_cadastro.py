pessoas = [{'nome':'Fellipe','Idade':25, 'Cidade':'Hortolândia'},
                {'nome':'Lais','Idade':21,'Cidade':'Campinas'},
                {'nome':'Roberto','Idade':56,'Cidade':'Valinhos'}
               ]


nome_att = 'Fellipe'
nova_idade = 22
profissao = 'TI'

for pessoa in pessoas:
    if pessoa['nome'] == nome_att:
        pessoa['Idade'] = nova_idade
        pessoa['profissao'] = profissao


for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}\nIdade: {pessoa['Idade']}\nCidade: {pessoa['Cidade']}\nProfissao: {profissao['profissao']}")


