from Functions import *
opcao = perguntar()
while opcao == 'I' or opcao == 'S' or opcao == 'U' or opcao == 'D':
    if opcao == 'I':
        insert()
    if opcao == 'S':
        select()
    if opcao == 'U':
        update()
    if opcao == 'D':
        delete()
    if opcao == 'SAIR':
        break
    opcao = perguntar()