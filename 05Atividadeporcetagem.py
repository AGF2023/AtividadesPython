'''5) Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto. '''


produto = float(input('Digite o valor do produto: '))

desconto = (produto*5)/100
pcdesconto = produto - desconto
print('O valor de desconto e de ', desconto, ' com isso o valor do produto e de ', pcdesconto)
