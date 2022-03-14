from modules.index import *
from time import sleep

"""
--> meu_primeiro_sistema
---------------------------------------------------------
Challenge 115 | 2.0 - Python course by CursoEmVideo
Author: Algacyr Melo
 --------------------------------------------------------
"""

arquivo = "registrants.txt"

# Criação de arquivo de texto caso não exista
if not file_exists(arquivo):
    createfile(arquivo)

while True:

    # Atribuição do conteúdo do arquivo de texto à variável conteúdo
    lista = open(arquivo, 'r')
    conteudo = lista.readline()
    lista.close()

    show(arquivo)

    # Menu principal
    menu('Cadastrar novo registro', 'Apagar registro', 'Editar registro', 'Sair do sistema')

    # Validação da operação selecionada
    while True:
        try:
            op = only_int("Digite a operação desejada [op]: ")
            break
        except ValueError:
            print('\033[31;1mCódigo inválido! Digite um número inteiro\033[m')

    # Cadastro de novo registro
    if op == 1:
        nome = only_name('Nome: ')      # Validação do NOME
        idade = only_int('Idade: ')     # Validação da IDADE
        add_data(arquivo, nome, idade)  # Adição de dados no arquivo
        print('\033[32;1m\nRegistro adicionado com sucesso!\033[m')

    # Remoção de registro
    elif op == 2 and len(conteudo) > 0:
        while True:
            if len(conteudo) == 1:
                codigo = 1
            else:
                codigo = only_int('Digite o código do registro que deseja apagar: ')
            try:
                remove_data(arquivo, codigo)
            except IndexError:
                print(f'\033[31;1mO código solicitado não existe em {arquivo}\033[m')
            else:
                print('\033[32;1m\nRegistro removido com sucesso!\033[m')
                break

    # Edição de registro
    elif op == 3 and len(conteudo) > 0:
        while True:
            if len(conteudo) == 1:
                codigo = 1
                break
            else:
                try:
                    codigo = only_int('Digite o código do registro que deseja editar: ')
                    change_data(arquivo, codigo)
                except IndexError:
                    print(f'\033[31;1mO código solicitado não existe em {arquivo}\033[m')
                else:
                    break

        nome = only_name('Novo nome: ')
        idade = only_int('Nova idade: ')
        change_data(arquivo, codigo, nome, idade)
        print('\033[32;1m\nRegistro alterado com sucesso!\033[m')

    # Finalizando programa
    elif op == 4:
        print("\nEncerrando...")
        sleep(1)
        break

    else:
        print('\033[31;1mOperação indisponível\033[m')
