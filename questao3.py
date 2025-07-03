valor_dig = 1.10
valor_ico = 1.00
valor_ipb = 0.40
valor_fot = 0.20

frase = 'Seja bem-vindo a loja de cópias da Isabelly Pereira Neto.'
tam = len(frase)
print('+', '-' * tam, '+')
print(f'| {frase} |')
print('+', '-' * tam, '+')

#função para o usuário escolher o serviço
def escolha_servico():
    while True:
        print('|', 'SELECIONE O CÓDIGO DO SERVIÇO DESEJADO.', '|')
        print('|', 'DIG', '|', 'Digitalização', '|')
        print('|', 'ICO', '|', 'Impressão Colorida', '|')
        print('|', 'IPB', '|', 'Impressão Preto e Branco', '|')
        print('|', 'FOT', '|', 'Fotocópia', '|')
        servico = input('» ')
        servico = servico.strip().lower() #remove espaços indesejados e converte a resposta para minúscula, evita erros

        if servico in ('dig', 'ico', 'ipb', 'fot'):
            break  # finaliza caso o serviço seja selecionado corretamente
        else:
            print('SERVIÇO INVÁLIDO. Digite novamente.')
            continue  # pula para o início do loop se o serviço for incorreto

    #dando valores para ops serviços
    if (servico == 'dig'):
        valor = valor_dig
    elif (servico == 'ico'):
        valor = valor_ico
    elif (servico == 'ipb'):
        valor = valor_ipb
    else:
        valor = valor_fot

    return valor

#função para o usuário informar a quantidade de páginas e o desconto
def num_pagina():
    while True:
        try: #validando a quantidade de páginas
            pagina = int(input('Digite a quantidade de páginas: '))

            #aplica descontos progressivos conforme o enunciado
            if (pagina > 0 and pagina < 20000):
                if (pagina < 20):
                    pagina = pagina
                elif (pagina >= 20 and pagina < 200):
                    pagina = pagina - (pagina * 0.15) #15% de desconto
                elif (pagina >= 200 and pagina < 2000):
                    pagina = pagina - (pagina * 0.2) #20% de desconto
                elif (pagina >= 2000 and pagina < 20000):
                    pagina = pagina - (pagina * 0.25) #20% de desconto
            elif (pagina > 20000):
                print('Ops, você excedeu o limite de 20.000 páginas. Digite novamente.')
                continue
            else:
                print('Digite um número de páginas válido, por favor!')
                continue
            return pagina #retorna quantidade com desconto

        except ValueError:
            print('Ops, quantidade inválida. Digite novamente.')

#função para escolher um serviço extra de encadernação
def servico_extra():
    while True:
        try:
            print("1 - Encadernação Simples - R$20.00")
            print("2 - Encadernação Capa Dura - R$40.00")
            print("0 - Não desejo serviço extra.")
            opcao_extra = int(input('» '))
            #valida a opção escolhida
            if opcao_extra in (1, 2, 0):
                if (opcao_extra == 1):
                    valor_extra = 20
                elif (opcao_extra == 2):
                    valor_extra = 40
                else:
                    valor_extra = 0

                return valor_extra #retorna valor do serviço selecionado
            else:
                print('OPÇÃO INVÁLIDA. Digite novamente.')
                continue

        except ValueError:
            print('OPÇÃO INVÁLIDA. Por favor, digite 1, 2 ou 0.')

#CÓDIGO PRINCIPAL
#chamando as funções no codigo
servico = escolha_servico()
qtd_pagina = num_pagina()
extra = servico_extra()

#fórmula do valor total dos serviços escolhidos
total = (servico * qtd_pagina) + extra

print(f'O valor total é {total:.2f}.\nValor serviço:{servico:.2f}.\nNúmero de páginas (com desconto):{int(qtd_pagina)}.\nServiço extra:{extra:.2f}.')


