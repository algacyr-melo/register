def file_exists(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createfile(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except FileExistsError:
        print('Não foi possível criar o arquivo')
    else:
        print(f'\033[32;1mArquivo {nome_arquivo} criado com sucesso\033[m')

def add_data(arquivo, nome, idade):
    try:
        lista = open(arquivo, 'at')
    except FileNotFoundError:
        print(f'\033[31;1m!Não foi possível adicionar novo registro em {arquivo}!\033[m')
    else:
        lista.write(f"{nome}|{idade}\n")

def show(arquivo):
    lista = open(arquivo, 'r')
    conteudo = lista.readlines()
    print(f'\n\033[30;1mREGISTROS em {arquivo}:')
    print('_' * 40)
    for i, v in enumerate(conteudo):
        print(f'{i + 1}. {loc_name(v):<20} {loc_age(v)} anos')
    print('_' * 40, '\033[m')

def menu(*items):
    print(f'{"[op]":<10}{"MENU PRINCIPAL"}')
    print('-' * 40)
    for i, v in enumerate(items):
        print(f'\033[34;1m[{i + 1}] -   {v}\033[m')
    print('-' * 40)

def remove_data(arquivo, codigo):
    lista = open(arquivo, 'r')
    conteudo = lista.readlines()
    conteudo.pop(codigo - 1)
    lista.close()

    lista = open(arquivo, 'w')
    lista.writelines(conteudo)

def change_data(arquivo, codigo, nome='Não-informado', idade='Não-informada'):
    lista = open(arquivo, 'r')
    conteudo = lista.readlines()
    conteudo.pop(codigo - 1)
    conteudo.insert(codigo - 1, f"{nome}|{idade}\n")
    lista.close()

    lista = open(arquivo, 'w')
    lista.writelines(conteudo)

def only_int(txt):
    while True:
        try:
            n = input(txt)
            return int(n)
        except (TypeError, ValueError):
            print('\033[31;1mERRO! Por favor, digite um número INTEIRO\033[m')

def only_name(txt):
    while True:
        nome = input(txt).title()
        if ''.join(nome.split()).isalpha():
            break
        else:
            print('\033[31;1m!ERRO! Digite apenas caracteres alfabéticos\033[m')
    return nome

def loc_name(registro):
    divisor_idx = registro.find('|')
    return registro[:divisor_idx]

def loc_age(registro):
    divisor_idx = registro.find('|')
    line_end = registro.find('\n')
    return registro[(divisor_idx + 1):line_end]