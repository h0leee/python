def arquivo(arq):
    try:
        with open(arq, 'rt') as file:
            file.read()
    except FileNotFoundError:
        with open(arq, 'wt') as file:   # w apaga oq tem no arquivo e escreve oq se quer ou cria um arquivo do zero
            file.write('')
            print('Arquivo criado com sucesso!')
    else:
        print('Arquivo encontrado com sucesso!')


# o with faz com que não seja necessário fazer o try e finally (linha 6)
def lerarquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0].title():<30}{dado[1]:>3} anos')


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')  # (append text)
    except:
        print('Houve um problema na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')  # mudar de linha para ao por outra pessoa ficarem em linhas diferentes
        except:
            print('Houve um erro na hora de registar os dados.')
        else:
            print(f'Novo registo de {nome} adicionado. ')
            a.close()
