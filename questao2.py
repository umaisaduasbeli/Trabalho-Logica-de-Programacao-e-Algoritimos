#criando a mensagem de boas-vindas através de uma função
frase = 'Seja bem-vindo a loja de sorvetes da Isabelly Pereira Neto'
tam = len(frase)
total = 0 #variavel acumuladora
def bem_vindo(nome):
 print('+', '-' * tam, '+')
 print(f'| {frase}.|')
 print('+', '-' * tam, '+')
 print(' '* 3, '+', '-' * 16,'|', ' CARDÁPIO  ','|', '-' * 16, '+')
 print(' '* 3, '|', '-' * 3,'|', 'Tamanho', '|', ' Cupuaçu (CP)', '|', ' Açaí (AC) ','|', '-' * 3, '|')
 print(' '* 3, '|', '-' * 3,'|', '   P   ', '|', '  R$ 9,00   ', '|', '  R$ 11,00  ','|', '-' * 3, '|')
 print(' '* 3, '|', '-' * 3,'|', '   M   ', '|', '  R$ 14,00  ', '|', '  R$ 16,00  ','|', '-' * 3, '|')
 print(' '* 3, '|', '-' * 3,'|', '   G   ', '|', '  R$ 18,00  ', '|', '  R$ 20,00  ','|', '-' * 3, '|')
 print(' '* 3, '+', '-' * 49, '+')
#ativando a função bem-vindo
bem_vindo('')
#solicitando dados do pedido para o cliente


while True: #loop principal do programa

  while True: #loop que verifica se o sabor é válido ou não
      sabor = input('Digite o que você deseja (CP - para cupuaçu - ou AC - para açaí): ')
      sabor = sabor.lower() #Converte a resposta para minúscula para evitar erros com letras maiúsculas
      if sabor in ('cp','ac'):
          break #encerra o loop se o sabor for válido
      print('SABOR INVÁLIDO. Digite novamente.')
      continue #pula para o início do loop

  while True: #loop que verifica se o tamanho é válido ou não
      tamanho = input('Digite o que você deseja (P/M/G): ')
      tamanho = tamanho.lower() #Converte a resposta para minúscula para evitar erros com letras maiúsculas
      if tamanho in ('p', 'm', 'g'):
          break #encerra o loop se o tamanho for válido
      print('TAMANHO INVÁLIDO. Digite novamente.')
      continue #pula para o início do loop

  #condição aninhada cupuaçu
  if (sabor == 'cp'):
      nome_sabor = 'CUPUAÇU'
      if (tamanho == 'p'):
          valor = 9.00 #valor do cupuaçu pequeno
      elif (tamanho == 'm'):
          valor = 14.00 #valor do cupuaçu medio
      else:
          valor = 18.00 #valor do cupuaçu grande
  #condição aninhada açaí
  elif (sabor == 'ac'):
      nome_sabor = 'AÇAÍ'
      if (tamanho == 'p'):
          valor = 11.00 #valor do açai pequeno
      elif (tamanho == 'm'):
          valor = 16.00 #valor do açaí medio
      else:
          valor = 20.00 #valor do açaí grande
  print(f'O valor do {nome_sabor} - {tamanho.upper()} é R${valor:.2f}.')
  total += valor #acrescentando valor do pedido ao valor acumulador total

  #loop para pedir mais itens
  while True:
      repetir = input('Você deseja mais algum item? (S/N) ')
      repetir = repetir.lower() #Converte a resposta para minúscula para evitar erros com letras maiúsculas
      if repetir in ['s', 'n']:
          break
      print('INVÁLIDO! Digite novamente.')
      continue

  if repetir == 'n':
      print(f'O valor total do seu pedido é R${total:.2f}.')
      break