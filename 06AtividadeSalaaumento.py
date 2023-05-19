''' 6) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.'''

salario = float(input('Digite o valor do seu salario: '))
aumento = (salario*15)/100
salarioaumento = salario + aumento
print('O valor do seu aumento e de', aumento, ' o seu salario sera de: ', salarioaumento)