'''7) Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada 
   e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados'''

base = float(input('Qual a medida da Base? '))
altura = float(input('Qual a medida da Altura? '))

area = base * altura
     
totaltintas = area / 2
print(' O total de litros necessario sera de ', totaltintas)