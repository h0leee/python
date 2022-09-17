from UtilidadesCursoemVideo.ex115 import *
from UtilidadesCursoemVideo.arquivoex115 import *  # daquilo importar tudo (*)
from time import sleep


arq = 'cursoemvideo.txt'
arquivo(arq)

while True:
    resposta = menu(['Ver lista de pessoas', 'Cadastrar pessoa', 'Sair do sistema'])  # aqui já está o leiaint
    if resposta == 1:
        cabecalho('Pessoas cadastradas')
        lerarquivo(arq)
        sleep(1)
    elif resposta == 2:
        cabecalho('Nova pessoa')
        nome = input('Nome: ').strip()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('Erro! Digite um número inteiro válido!')
        sleep(1)
