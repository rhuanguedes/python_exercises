# === EXERCÍCIO 001 === #? TIPOS PRIMITIVOS E SAÍDA DE DADOS
'''Crie um programa que escreva "Olá, mundo!" na tela.'''

# print("Olá, Mundo!")

# === EXERCÍCIO 002 ===
'''Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.'''

# nome = input("Qual é o seu nome? ")
# print(f"Olá {nome}, seja bem vindo(a).")

# === EXERCÍCIO 003 === 
'''Crie um programa que leia dois números e mostre a soma entre eles.'''

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))
# print(f"A soma destes números é {num1 + num2}.")

# === EXERCÍCIO 004 ===
'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

# var = input("Digite algo: ")
# print(f"O tipo primitivo desse valor é {type(var)}.")
# print("Só tem espaços?",var.isspace())
# print("É um número?",var.isnumeric())
# print("É alfabético?",var.isalpha())
# print("É alfanumérico?",var.isalnum())
# print("Está em maiúsculas?",var.isupper())
# print("Está em minúsculas?",var.islower())
# print("Está capitalizada?",var.istitle())

# === EXERCÍCIO 005 === #? OPERADORES ARITMÉTICOS
'''Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.'''

# num = int(input("Digite um número: "))
# print(f"O antecessor deste número é {num - 1} e o sucessor é {num + 1}.")

# === EXERCÍCIO 006 ===
'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

# num = float(input("Digite um número: "))
# print(f"O dobro deste número é {num * 2}, o triplo é {num * 3} e a raiz quadrada é {num ** 0.5:.2f}.")

# === EXERCÍCIO 007 ===
'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# print(f"A nota média foi {(nota1 + nota2) / 2:.1f}.")

# === EXERCÍCIO 008 ===
'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

# num = float(input("Digite um valor: "))
# print(f"Este valor tem {num * 100} centímetros e {num * 1000} milímetros.")

# === EXERCÍCIO 009 ===
'''Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.'''

# num = int(input("Digite um valor: "))
# print(f"1 x {num} = {num}\n2 x {num} = {num * 2}\n3 x {num} = {num * 3}\n4 x {num} = {num * 4}\n5 x {num} = {num * 5}\n6 x {num} = {num * 6}\n7 x {num} = {num * 7}\n8 x {num} = {num * 8}\n9 x {num} = {num * 9}")

# === EXERCÍCIO 010 ===
'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27.'''

# num = float(input("Digite um valor: "))
# print(f"Com este valor você pode comprar {num / 3.27:.2f} doláres.")

# === EXERCÍCIO 011 ===
'''Faça um programa que leia o comprimento e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².'''

# comprimento = float(input("Digite a comprimento: "))
# altura = float(input("Digite a altura: "))
# print(f"A sua parede tem uma área de {comprimento * altura:.2f} m², logo, você vai precisar de {(comprimento * altura) / 2:.2f} litros de tinta")

# === EXERCÍCIO 012 ===
'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

# preco = float(input("Digite um valor: "))
# print(f"Com 5% de desconto o novo preço será de R${preco - preco * 0.05:.2f}.") 

# === EXERCÍCIO 013 ===
'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

# salario = float(input("Digite um valor: "))
# print(f"Com um aumento de 15%, o novo salário será de {salario + salario * 0.15:.2f}")

# === EXERCÍCIO 014 ===
'''Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.'''

# temp = int(input("Digite a temperatura em C°: "))
# print(f"Essa temperatura equivale a {temp * 1.8 + 32}F°")

# === EXERCÍCIO 015 ===
'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
 sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

# km_percorrido = float(input("Digite a quantidade de Km percorridos: "))
# quant_dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
# print(f"Preço: R${(km_percorrido * 0.15) + (quant_dias * 60):.2f}")

# === EXERCÍCIO 016 === #? MÓDULOS
'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.'''

# from math import trunc

# num = float(input("Digite um número: "))
# print(f"A porção inteira deste número é {trunc(num)}")

# === EXERCÍCIO 017 ===
'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

# from math import hypot

# cat_oposto = float(input("Digite o valor do primeiro cateto: "))
# cat_adjacente = float(input("Digite o valor do segundo cateto: "))
# hipotenusa = hypot(cat_oposto, cat_adjacente)
# print(f"Hipotenusa: {hipotenusa:.2f}")

# === EXERCÍCIO 018 ===
'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

# from math import sin, cos, tan, radians

# angulo = float(input("Digite o valor do ângulo em graus: "))
# angulo_rad = radians(angulo)
# seno = sin(angulo_rad)
# cosseno = cos(angulo_rad)
# tangente = tan(angulo_rad)

# print(f"O seno desse ângulo é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}.")

# === EXERCÍCIO 019 ===
'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'''

# from random import choice

# aluno1 = input("Digite o nome do 1° aluno(a): ")
# aluno2 = input("Digite o nome do 2° aluno(a): ")
# aluno3 = input("Digite o nome do 3° aluno(a): ")
# aluno4 = input("Digite o nome do 4° aluno(a): ")
# lista_de_alunos = [aluno1, aluno2, aluno3, aluno4]
# aluno_escolhido = choices(lista_de_alunos)
# print(f"O aluno(a) escolhido(a) foi: {aluno_escolhido}")

# === EXERCÍCIO 020 ===
'''O mesmo professor do EXERCÍCIO 019 quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

# from random import sample

# aluno1 = input("Digite o nome do 1° aluno(a): ")
# aluno2 = input("Digite o nome do 2° aluno(a): ")
# aluno3 = input("Digite o nome do 3° aluno(a): ")
# aluno4 = input("Digite o nome do 4° aluno(a): ")
# lista_de_alunos = [aluno1, aluno2, aluno3, aluno4]
# aluno_escolhido = sample(lista_de_alunos, k=4) 
# print(f"A ordem de apresentação será: {aluno_escolhido}")

# === EXERCÍCIO 021 ===
'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

# import pygame

# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("D:/Programming/Python/time_machine.mp3")
# pygame.mixer.music.play()

# input("Pressione Enter para parar a música... ")
# pygame.mixer.music.stop()

# === EXERCÍCIO 022 === #? MANIPULANDO TEXTO
'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

# nome = input("Digite seu nome completo: ")
# print(f"Em maiúsculas: {nome.upper()}")
# print(f"Em minúsculas: {nome.lower()}")
# print("O nome possui {} letras".format(len(nome.replace(" ","").strip())))
# print("O primeiro nome possui {} letras".format(len(nome.split()[0])))

# === EXERCÍCIO 023 ===
'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

# num = int((input("Digite um número: ")))
# un = num // 1 % 10
# dz = num // 10 % 10
# cn = num // 100 % 10
# ml = num // 1000 % 10

# print(f"Unidade: {un}\nDezena: {dz}\nCentena: {cn}\nMilhar: {ml}")

# === EXERCÍCIO 024 ===
'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.'''

# cidade = input("Digite um nome de cidade: ").upper()
# print((cidade[:5] == "SANTO"))

# === EXERCÍCIO 025 ===
'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

# nome = input("Digite seu nome: ").upper()

# if "SILVA" in nome:
#     print("Você tem Silva no nome.")
# else:
#     print("Você não tem Silva no nome.")

# === EXERCÍCIO 026 ===
'''Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra “A”.
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.'''

# frase = input("Digite uma frase: ").upper().strip()
# print(f'Essa frase contém {frase.count("A")} letras "A".')
# print(f'A letra "A" aparece pela primeira vez na {frase.find("A") +1}ª posição.')
# print(f'E na última vez aparece na {frase.rfind("A") +1}ª posição.')

# === EXERCÍCIO 027 ===
'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

# === EXERCÍCIO 028 === #? CONDIÇÕES SIMPLES E COMPOSTAS
'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
 o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

# from random import randint

# num = int(input("Adivinhe qual número estou pensando entre 0 e 5: "))

# if num >= 0 and num <= 5:
#     num_pc = randint(0, 5)
#     print(f"Eu pensei no número {num_pc}.")
#     if num == num_pc:
#         print("Você acertou!")
#     else:
#         print("Mais sorte na próxima vez!")
# else:
#     print("Digite somente números entre 0 e 5!")
    
# === EXERCÍCIO 029 ===
'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado A multa vai custar R$7,00 por cada Km acima do limite.'''

# velocidade = int(input("Digite a velocidade do veículo: "))
# if velocidade > 80:
#     valor = (- 80 + velocidade) * 7
#     print(f"Você foi multado em R${valor}")

# === EXERCÍCIO 030 ===
'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

# num = int(input("Digite um número: "))
# if num % 2 == 0:
#     print(f"O número {num} é par.")
# else:
#     print(f"O número {num} é ímpar.")

# === EXERCÍCIO 031 ===
'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''

# dist_viagem = int(input("Qual a distância da viagem? "))

# if dist_viagem <= 200:
#     valor = dist_viagem * 0.50
#     print(f"O valor da viagem será de R${valor}")
# else:
#     valor = dist_viagem * 0.45
#     print(f"O valor da viagem será de R${valor}")

# === EXERCÍCIO 032 ===
'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''

# ano = int(input("Digite um ano e descubra se ele é Bissexto: "))

# if ano % 4 == 0 and not ano % 100 == 0 or ano % 4 == 0 and ano % 400 == 0:
#     print("Este ano é Bissexto!")
# else:
#     print("Esse ano não é Bissexto.")

# === EXERCÍCIO 033 ===
'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

# num1 = int(input("Digite o 1° número: "))
# num2 = int(input("Digite o 2° número: "))
# num3 = int(input("Digite o 3° número: "))
# maior = None
# menor = None

# if num1 > num2 and num1 > num3:
#     maior = num1
# if num2 > num1 and num2 > num3:
#     maior = num2
# if num3 > num1 and num3 > num2:
#     maior = num3
# if num1 < num2 and num1 < num3:
#     menor = num1
# if num2 < num1 and num2 < num3:
#     menor = num2
# if num3 < num1 and num3 < num2:
#     menor = num3

# print(f"O maior número é {maior} e o menor número é {menor}.")

# === EXERCÍCIO 034 ===
'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
- Para sálarios superiores a R$1250,00, calcule um aumento de 10%.
- Para inferiores ou iguais, o aumento é de 15%.'''

# salario = float(input("Qual o salário do funcionário? "))
# if salario > 1250:
#     aumento = salario * 0.10
#     print(f"O funcionário deve receber um aumento de R${aumento:.2f}, seu novo salário será de R${salario + aumento:.2f}.")
# else:
#     aumento = salario * 0.15
#     print(f"O funcionário deve receber um aumento de R${aumento:.2f}, seu nome salário será de R${salario + aumento:.2f}.")

# === EXERCÍCIO 035 ===
'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

# reta1 = float(input("Digite o comprimento da 1ª reta: "))
# reta2 = float(input("Digite o comprimento da 2ª reta: "))
# reta3 = float(input("Digite o comprimento da 3ª reta: "))

# if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
#     print("Essas retas podem formar um triângulo!")
# else:
#     print("Essas retas não podem formar um triângulo.")

# === EXERCÍCIO 036 === #? CONDIÇÕES ANINHADAS
'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa, perguntando o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

# valor_casa = float(input("Qual o valor do imóvel? "))
# salario = float(input("Qual o salário do comprador? "))
# quant_anos = int(input("Em quantos anos o comprador pretende pagar? "))
# prest_mensal = valor_casa / quant_anos / 12
# trinta_pct_salario = salario * 0.30

# print(f"30% do salário do comprador: R${trinta_pct_salario:.2f}")

# if prest_mensal < trinta_pct_salario:
#     print(f"As prestações mensais serão de R${prest_mensal:.2f}.\nEmpréstimo aprovado.")
# else:
#     print(f"As prestações mensais serão de R${prest_mensal:.2f}, excedendo 30% do salário total do comprador.\nEmpréstimo negado.")

# === EXERCÍCIO 037 ===
'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
[1] para binário,
[2] para octal,
[3] para hexadecimal.'''

# print("Conversor de números".center(30))
# print("=" * 30)
# num = int(input("Digite um número: "))
# print("=" * 30)
# print("[1] Binário\n[2] Octal\n[3] Hexadecimal\n")
# opcao = int(input("Selecione uma opção: "))

# if opcao == 1:
#     num = bin(num)
#     print(f"Binário: {num[2:]}")
# elif opcao == 2:
#     num = oct(num)
#     print(f"Octal: {num[2:]}")
# elif opcao == 3:
#     num = hex(num)
#     print(f"Hexadecimal: {num[2:]}")
# else:
#     print("Selecione uma opção válida!")

# === EXERCÍCIO 038 ===
'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

# num1 = int(input("Digite o 1° número: "))
# num2 = int(input("Digite o 2° número: "))

# if num1 > num2:
#     print("O primeiro número é maior.")
# elif num2 > num1:
#     print("O segundo número é maior.")
# else:
#     print("Não existe valor maior, os dois são iguais.")

# === EXERCÍCIO 039 ===
'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

# from datetime import datetime

# ano_atual = datetime.now().year
# ano_nasc = int(input("Ano de nascimento: "))
# idade = ano_atual - ano_nasc
# print(f"Esse ano você completa {idade} anos.")

# if idade < 18:
#     saldo = (idade - 18) * -1
#     if saldo == 1:
#         print(f"Falta {saldo} ano para você se alistar.")
#     else:
#         print(f"Faltam {saldo} anos para você se alistar.")       
# elif idade == 18:
#     print("Você está no prazo de alistamento! Busque uma junta militar com urgência!")
# else:
#     saldo = idade - 18
#     if saldo == 1:
#         print(f"Você já passou do prazo de alistamento. Você deveria ter se alistado a {saldo} ano.")
#     else:
#         print(f"Você já passou do prazo de alistamento. Você deveria ter se alistado a {saldo} anos.")

# === EXERCÍCIO 040 ===
'''Crie um programa que leia duas notas de um aluno, calcule sua média e mostre uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

# nota1 = float(input("Digite a 1ª nota: "))
# nota2 = float(input("Digite a 2ª nota: "))
# media = (nota1 + nota2) / 2

# print(f"Nota média: {media}")

# if media < 5:
#     print("REPROVADO")
# elif media >= 5 and media <= 6.9:
#     print("RECUPERAÇÃO")
# else:
#     print("APROVADO")

# === EXERCÍCIO 041 ===
'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER'''

# from datetime import datetime

# ano_atual = datetime.now().year
# ano_nasc = int(input("Ano de nascimento: "))
# idade = ano_atual - ano_nasc

# if idade > 0 and idade <= 120:
#     print(f"Você tem {idade} anos") 
#     if idade < 10:
#         print("Você pertence a categoria MIRIM.")
#     elif idade < 15:
#         print("Você pertence a categoria INFANTIL.")
#     elif idade < 20:
#         print("Você pertence a categoria JÚNIOR.")
#     elif idade == 20:
#         print("Você pertence a categoria SÊNIOR.")
#     else:
#         print("Você pertence a categoria MASTER.")
# else:
#     print("Digite um ano de nascimento válido!")

# === EXERCÍCIO 042 ===
'''Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais
- ESCALENO: todos os lados diferentes'''

# reta1 = float(input("Digite o comprimento da 1ª reta: "))
# reta2 = float(input("Digite o comprimento da 2ª reta: "))
# reta3 = float(input("Digite o comprimento da 3ª reta: "))

# if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
#     print("Essas retas podem formar um triângulo!")
#     if reta1 == reta2 == reta3:
#         print("Triângulo equilátero.")
#     elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
#         print("Triângulo isósceles.")
#     else:
#         print("Triângulo escaleno")
# else:
#     print("Essas retas não podem formar um triângulo.")

# === EXERCÍCIO 043 ===
'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

# peso = float(input("Peso: "))
# altura = float(input("Altura: "))
# imc = peso / altura ** 2

# print(f"IMC: {imc:.1f}")

# if imc < 18.5:
#     print("Abaixo do peso.")
# elif imc < 25:
#     print("Peso ideal.")
# elif imc < 30:
#     print("Sobrepeso.")
# elif imc < 40:
#     print("Obesidade.")
# elif imc > 40:
#     print("Obesidade mórbida.")
# else:
#     print("IMC inválido, analise os valores informados!")

# === EXERCÍCIO 044 ===
'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

# valor = float(input("Valor: "))
# print("Formas de pagamento:\n[1] À vista dinheiro/cheque(10% de desconto)\n[2] À vista no cartão(5% de desconto)\n[3] Em até 2x no cartão(preço normal)\n[4] 3x ou mais no cartão: 20% de juros")
# forma_pag = int(input("Forma de pagamento: "))

# if forma_pag == 1:
#     print(f"Valor final: R${valor - valor * 0.10:.2f}")
# elif forma_pag == 2:
#     print(f"Valor final: R${valor - valor * 0.05:.2f}")
# elif forma_pag == 3:
#     print(f"Valor final: R${valor:.2f}")
# elif forma_pag == 4:
#     print(f"Valor final: R${valor + valor * 0.20:.2f}")
# else:
#     print("Selecione uma opção válida!")

# === EXERCÍCIO 045 ===
'''Crie um programa que faça o computador jogar Jokenpô com você.'''

# from random import choice

# opcoes = ["Pedra", "Papel", "Tesoura"]
# user = input("Pedra, papel ou tesoura? ").capitalize().strip()
# pc = choice(opcoes)

# if user in opcoes:
#     print(f"O computador escolheu {pc}.")
#     if user == pc:
#         print("Empate!")
#     elif user == "Pedra" and pc == "Papel" or user == "Papel" and pc == "Tesoura" or user == "Tesoura" and pc == "Pedra":
#         print("Computador venceu!")
#     else:
#         print("Você venceu!")
# else:
#     print('Digite apenas "Pedra", "Papel" ou "Tesoura"')

# === EXERCÍCIO 046 === #? ESTRUTURA FOR
'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de um segundo entre eles.'''

# from time import sleep

# for i in range(10, -1, -1):
#     print(i)
#     sleep(1)
# print("Boom!!!")

# === EXERCÍCIO 047 ===
'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i,end= " ")

# === EXERCÍCIO 048 ===
'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

# soma = 0
# for i in range(1, 501):
#     if i % 2 != 0 and i % 3 == 0:
#         soma += i
# print(f"A soma dos números ímpares que são múltiplos de três é {soma}.")

# === EXERCÍCIO 049 ===
'''Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

# num = int(input("Digite um número: "))
# for i in range(1, 10):
#     print(f"{i} x {num} = {num * i}")

# === EXERCÍCIO 050 ===
'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

# soma = 0
# for i in range(1, 7):
#     nums = int(input(f"Digite o {i}º número: "))
#     if nums % 2 == 0:
#         soma += nums
# print(f"A soma dos números pares digitados é {soma}.")

# === EXERCÍCIO 051 ===
'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

#! Exercício pendente

# === EXERCÍCIO 052 ===
'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

#! Exercício pendente

# === EXERCÍCIO 053 ===
'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

#! Exercício pendente

# === EXERCÍCIO 054 ===
'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

# from datetime import datetime

# ano_atual = datetime.now().year
# maiores = 0
# menores = 0

# for i in range(1, 8):
#     ano_nasc = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
#     idade = ano_atual - ano_nasc
#     if idade < 18:
#         menores = menores + 1
#     else:
#         maiores = maiores + 1
# print(f"{menores} pessoas ainda não atingiram a maioridade e {maiores} pessoas já são maiores de idade.")


# === EXERCÍCIO 055 ===
'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

# maior = 0
# menor = 0

# for i in range(1, 6):
#     peso = float(input(f"Digite o peso da {i}ª pessoa: "))
#     if peso > maior:
#         maior = peso
#     if menor == 0 or peso < menor:
#         menor = peso
# print(f"O menor peso lido foi {menor} Kg e o maior foi {maior} Kg.")
 

# === EXERCÍCIO 056 ===
'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
 qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

# from datetime import datetime

# ano_atual = datetime.now().year
# soma_idade = 0

# idade_homem_mais_velho = 0
# nome_homem_mais_velho = ""
# mulheres_menores_20_anos = 0

# for i in range(1, 5):
#     nome = input(f"Nome da {i}ª pessoa: ")

#     ano_nasc = int(input(f"Ano de nascimento da {i}ª pessoa: "))
#     idade = ano_atual - ano_nasc
#     soma_idade += idade
    
#     sexo = input(f"Sexo da {i}ª pessoa [M/F]: ").upper().strip()
#     if sexo not in ("M", "F"):
#         print("Sexo inválido, use M ou F.")
#         continue
#     else:
#         if sexo in "Ff" and idade < 20:
#             mulheres_menores_20_anos += 1
#         if sexo in "Mm" and idade > idade_homem_mais_velho:
#             idade_homem_mais_velho = idade
#             nome_homem_mais_velho = nome

# idade_media = soma_idade / 4

# if nome_homem_mais_velho == "":
#     print(f"Idade média do grupo: {idade_media} anos.\nNome do homem mais velho: Não há homem cadastrado.\nQuantidade de mulheres menores de 20 anos: {mulheres_menores_20_anos}.")
# else:
#     print(f"Idade média do grupo: {idade_media} anos.\nNome do homem mais velho: {nome_homem_mais_velho}.\nQuantidade de mulheres menores de 20 anos: {mulheres_menores_20_anos}.")

# === EXERCÍCIO 057 === #? ESTRUTURA WHILE
'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

# while(True):
#     sexo = input("Digite o sexo [M/F]: ").upper().strip()
#     if sexo in ("M", "F"):
#         break
#     else:
#          print("Digite apenas M para masculino ou F para femenino.")
# print("Sexo registrado com sucesso!")  

# === EXERCÍCIO 058 ===
'''Melhore o EXERCÍCIO 028 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
 mostrando no final quantos palpites foram necessários para vencer.'''

# from random import randint

# pc = randint(1, 10)
# palpites = 1 
# while(True):
#     num = int(input("Descubra que número estou pensando: "))
#     if num == pc:
#         print(f"Eu pensei no número {pc}. Você acertou!")
#         break
#     else:
#         print("Não foi esse. Tente outro!")
#         palpites = palpites + 1
       
# if palpites == 1:
#     print(f"Foi necessário {palpites} palpite.")
# else:
#     print(f"Foram necessários {palpites} palpites.")

# === EXERCÍCIO 059 ===
'''Crie um programa que leia dois valores e mostre um menu na tela: [1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair do programa.
 Seu programa deverá realizar a operação solicitada em cada caso.'''

# num1 = float(input("Digite um valor: "))
# num2 = float(input("Digite outro valor: "))

# while(True):
#     print("=" * 30)
#     print("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa.")
#     print("=" * 30)
#     opcao = int(input("Selecione uma opção: "))

#     if opcao == 1:
#         print(f"A soma dos valores é {num1 + num2}.")
#     elif opcao == 2:
#         print(f"O produto dos valores é {num1 * num2}.")
#     elif opcao == 3:
#         maior = num1
#         if num1 > num2:
#             maior = num1
#         else:
#             maior = num2
#         print(f"O maior número {maior}.")
#     elif opcao == 4:
#         novo_num1 = float(input("Digite o primeiro valor: "))
#         num1 = novo_num1
#         novo_num2 = float(input("Digite o segundo valor: "))
#         num2 = novo_num2
#     elif opcao == 5:
#         print("Encerramento programa...")
#         break
#     else:
#         print("Digite uma opção válida.")


# === EXERCÍCIO 060 ===
'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120''' 

#! Exercício pendente

# === EXERCÍCIO 061 ===
'''Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

#! Exercício pendente

# === EXERCÍCIO 062 ===
'''Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser
 que quer mostrar 0 termos'''

#! Exercício pendente

# === EXERCÍCIO 063 ===
'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
 Ex.: 0 --> 1 --> 1 --> 2 --> 3 --> 5 --> 8'''

#! Exercício pendente

# === EXERCÍCIO 064 ===
'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
 que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

#! Exercício pendente

# === EXERCÍCIO 065 ===
'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
 e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

#! Exercício pendente

# === EXERCÍCIO 066 ===
'''()'''



# === EXERCÍCIO 067 ===
'''()'''



# === EXERCÍCIO 068 ===
'''()'''



# === EXERCÍCIO 069 ===
'''()'''



# === EXERCÍCIO 070 ===
'''()'''



# === EXERCÍCIO 071 ===
'''()'''



# === EXERCÍCIO 072 ===
'''()'''



# === EXERCÍCIO 073 ===
'''()'''



# === EXERCÍCIO 074 ===
'''()'''



# === EXERCÍCIO 075 ===
'''()'''



# === EXERCÍCIO 076 ===
'''()'''



# === EXERCÍCIO 077 ===
'''()'''



# === EXERCÍCIO 078 ===
'''()'''



# === EXERCÍCIO 079 ===
'''()'''



# === EXERCÍCIO 080 ===
'''()'''



# === EXERCÍCIO 081 ===
'''()'''



# === EXERCÍCIO 082 ===
'''()'''



# === EXERCÍCIO 083 ===
'''()'''



# === EXERCÍCIO 084 ===
'''()'''



# === EXERCÍCIO 085 ===
'''()'''



# === EXERCÍCIO 086 ===
'''()'''



# === EXERCÍCIO 087 ===
'''()'''



# === EXERCÍCIO 088 ===
'''()'''



# === EXERCÍCIO 089 ===
'''()'''



# === EXERCÍCIO 090 ===
'''()'''



# === EXERCÍCIO 091 ===
'''()'''



# === EXERCÍCIO 092 ===
'''()'''



# === EXERCÍCIO 093 ===
'''()'''



# === EXERCÍCIO 094 ===
'''()'''



# === EXERCÍCIO 095 ===
'''()'''



# === EXERCÍCIO 096 ===
'''()'''



# === EXERCÍCIO 097 ===
'''()'''



# === EXERCÍCIO 098 ===
'''()'''



# === EXERCÍCIO 099 ===
'''()'''



# === EXERCÍCIO 100 ===
'''()'''



