print('Bem-vindo(a) a Loja da Isabelly Pereira Neto')

#Solicita o valor unitário do produto
valor_unitario = float(input('Digite o valor da sua compra: '))
#Solicita a quantidade de produtos
quantidade = int(input('Digite a quantidade de produto: '))

#Calcula valor total dos produtos SEM o desconto
total_sem_desconto = valor_unitario * quantidade
#variavel para inserir desconto
desconto = 0

print(f'O valor da sua compra SEM desconto é de: {total_sem_desconto}')

if (total_sem_desconto >= 2500 and total_sem_desconto < 6000):
    desconto = 0.04
    #Calcula valor total dos produtos COM o desconto
    valor_com_desconto = total_sem_desconto - (total_sem_desconto * desconto)
    print(f'O valor da sua compra COM desconto é de: R$ {valor_com_desconto:.2f}')
elif (total_sem_desconto >= 6000 and total_sem_desconto < 10000):
    desconto = 0.07
    #Calcula valor total dos produtos COM o desconto
    valor_com_desconto = total_sem_desconto - (total_sem_desconto * desconto)
    print(f'O valor da sua compra COM desconto é de: {valor_com_desconto}')
elif (total_sem_desconto >= 10000):
    desconto = 0.11
    #Calcula valor total dos produtos COM o desconto
    valor_com_desconto = total_sem_desconto - (total_sem_desconto * desconto)
    print(f'O valor da sua compra COM desconto é de: {valor_com_desconto}')
else:
    print('Infelizmente sua compra não possui desconto!')