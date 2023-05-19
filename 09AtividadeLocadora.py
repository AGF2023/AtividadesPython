''' 9) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a 
quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado'''


km = float(input('Qual a quantidade de km percorrido?  '))
dias = int(input('Quantos diarias? '))
diaria = 90
kmrodado = km * 0.20
pagamento = (kmrodado ) + (diaria * dias)
print('O valor do km foi de', kmrodado)
print('O total a pagar e de ', pagamento)