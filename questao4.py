#Frase de boas vindas
frase = 'Seja bem-vindo a livraria da Isabelly Pereira Neto.'
tam = len(frase)
print('+', '-' * tam, '+')
print(f'| {frase} |')
print('+', '-' * tam, '+')

id_global = 0 #variavel global dos id's dos livros
lista_livro = [] #Lista vazia

#criando a funçao de cadastro de um novo livro
def cadastrar_livro(id):
    print('+', '-' * tam, '+')
    print('+', '-' * 15, 'CADASTRAR LIVRO', '-' * 15, '+')
    #solicitando informações do livro a ser cadastrado para o usuário
    print(f'ID do livro {id}')
    nome = input('Digite o nome do livro para cadastro: ').strip()
    autor = input('Digite o nome do autor/autora para cadastro: ').strip()
    editora = input('Digite o nome da editora para cadastro: ').strip()
    #cria um dicionário com os dados do livro
    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }
    #adicionando um novo livro ao dicionário
    lista_livro.append(livro)
    print('Livro cadastrado!')

#criando a funçao de consulta de um livro
def consultar_livro():
    print('+', '-' * tam, '+')
    print('+', '-' * 15, 'CONSULTAR LIVROS', '-' * 15, '+')
    #verifica se a lista está vazia ou nao
    if lista_livro:
        while True:
            #exibe opções de consulta
            print('1 - Consultar TODOS os livros.')
            print('2 - Consultar o livro por ID.')
            print('3 - Consultar o livro por AUTOR.')
            print('4 - RETORNAR')
            try:
                consulta = int(input('Digite a opção desejada: '))
                #mostra TODOS os livros cadastrados
                if (consulta == 1):
                    for livro in lista_livro:
                        print('-' * 40)
                        print(f"ID: {livro['id']}\n"
                              f"NOME: {livro['nome']}\n"
                              f"AUTOR: {livro['autor']}\n"
                              f"EDITORA: {livro['editora']}")
                #mostra o livro selecionado pelo ID
                elif (consulta == 2):
                    id_livro = int(input('Digite o ID do livro: '))
                    id_encontrado = False
                    for livro in lista_livro:
                        if livro['id'] == id_livro:
                            print('-' * 40)
                            print(f"ID: {livro['id']}\n"
                                  f"NOME: {livro['nome']}\n"
                                  f"AUTOR: {livro['autor']}\n"
                                  f"EDITORA: {livro['editora']}")
                            id_encontrado = True
                            break
                    if not id_encontrado:
                        print('Não existe nenhum livro com esse ID. Tente outra vez.')
                #mostra o livro selecionado pelo AUTOR
                elif (consulta == 3):
                    autor_livro = input('Digite o AUTOR do livro: ')
                    autor_encontrado = False
                    for livro in lista_livro:
                        if livro['autor'].lower() == autor_livro.lower():
                            print('-' * 40)
                            print(f"ID: {livro['id']}\n"
                                  f"NOME: {livro['nome']}\n"
                                  f"AUTOR: {livro['autor']}\n"
                                  f"EDITORA: {livro['editora']}")
                            autor_encontrado = True
                    if not autor_encontrado:
                        print('Não existe nenhum livro com esse AUTOR. Tente outra vez.')
                #encerra a função e retorna ao menu anterior
                elif (consulta == 4):
                    break
                #qualquer outro valor é considerado inválido
                else:
                    print('OPÇÃO INVÁLIDA!')
            #erro caso o usuário digite um valor inválido (letras onde se espera número)
            except ValueError:
                print('Por favor, digite uma opção válida!')
                continue
    else:
        print('Não existem livros cadastrados.')

#criando a funçao de exclusão de um livro por ID
def remover_livro():
    print('+', '-' * tam, '+')
    print('+', '-' * 15, 'REMOVER LIVROS', '-' * 15, '+')
    #verifica se a lista está vazia ou nao
    if lista_livro:
        try:
            id_remover = int(input('Digite o ID do livro a ser removido: '))
            id_encontrado = False

            for livro in lista_livro:
                if livro['id'] == id_remover:
                    lista_livro.remove(livro)
                    print('Livro REMOVIDO!')
                    id_encontrado = True
                    break
            if not id_encontrado:
                print('O livro não foi encontrado.')
        except ValueError:
            print('Valor informado inválido, informe novamente!')
    else:
        print('Não existem livros cadastrados.')

#loop principal (MENU)
while True:
    print('+', '-' * tam, '+')
    print('+', '-' * 15, 'MENU PRINCIPAL', '-' * 15, '+')
    print('1 - CADASTRAR novo livro.')
    print('2 - CONSULTAR livro(s).')
    print('3 - REMOVER livro.')
    print('4 - ENCERRAR PROGRAMA')
    try:
        #usuário informa a opção desejada
        menu = int(input('\nDigite a opção desejada: '))
        if (menu == 1):
            id_global += 1 #
            cadastrar_livro(id_global)
        elif (menu == 2):
            consultar_livro()
        elif (menu == 3):
            remover_livro()
        elif (menu == 4):
            print('Gratidão por escolher a nossa livraria! Até mais!')
            break
        else:
            print('Opção inválida!')
            continue
    except ValueError:
        print('Número INVÁLIDO! Tente novamente.')
        continue



