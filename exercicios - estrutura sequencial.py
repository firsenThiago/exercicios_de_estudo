#Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print ("Alo mundo")

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input ("Digite um numero")
print ("O número informado foi {}".format(numero))

#Faça um Programa que peça dois números e imprima a soma.

numero1 = int(input ("Digite um numero"))
numero2= int(input ("Digite o segundo numero"))
soma = numero1 + numero2
print (soma)

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

etapa1 = int(input ("Digite a nota da primeira etapa"))
etapa2= int(input ("Digite a nota da segunda etapa"))
etapa3 = int(input ("Digite a nota da terceira etapa"))
etapa4= int(input ("Digite a nota da quarta etapa"))
media = (etapa1 + etapa2 + etapa3 + etapa4)/4

print (media)

#Faça um Programa que converta metros para centímetros.

metros = int(input ("Digite os metros"))
centimetros = metros * 100
print ("{} metros equivale a {} centimetros".format(metros,centimetros))

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = int(input("Qual o tamanho do raio?"))
area = 3.14 * raio
print ("A area do circulo em questao é {:.2f} ".format(area))


#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = int(input("Qual o tamanho do lado?"))
area = lado * lado 
print ("O dobro da area do quadrado em questao é {} ".format(2* area))

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhoPorHora = float(input("Quanto voce ganha por hora?"))
horasPormes = int(input("Quantas horas voce trabalha por mes?"))
salario = horasPormes * ganhoPorHora 
print ("Voce ganha R${} por mês".format(salario))

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

temperaturaF = float(input("Qual a temperatura em Fahrenheint?"))
C = 5 * ((temperaturaF-32) / 9)
print ("{} graus Fahreheint equivale a {:.1f} graus celsius".format(temperaturaF,C))

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = float(input("Qual a temperatura em celsius?"))
temperaturaF = (C* 1.8) + 32
print ("{} graus celsius equivale a {:.1f} graus Fahreheint".format(C,temperaturaF))

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    #o produto do dobro do primeiro com metade do segundo .
    #a soma do triplo do primeiro com o terceiro.
    #o terceiro elevado ao cubo.

    numero1 = int(input("Digite um numero inteiro"))
numero2 = int(input("Digite um numero inteiro"))
numero3 = float(input("Digite um numero real"))

produto = (2 * numero1) * (numero2 / 2)
soma = (3*numero1) + numero3
cubo = numero3**3

print ("O produto do dobro do primeiro com metade do segundo é {}, a soma do triplo do primeiro com o terceiro é {}, o terceiro elevado ao cubo é {}".format(produto,soma,cubo))



#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite sua altura"))
pesoIdeal = (72.7*altura) - 58
print ("Seu peso ideal é {}".format(pesoIdeal))

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    #Para homens: (72.7*h) - 58
    #Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura"))
pesoIdealHomem = (72.7*altura) - 58
pesoIDealMulher = (62.1*altura) - 44.7
print ("Seu peso ideal se voce for homem é {}, se você for mulher seu peso ideal é {}".format(pesoIdealHomem,pesoIDealMulher))


#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 
#por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.

peso = int(input("Quantos kilos você pescou hoje?"))
excesso = peso - 50
multa = 4 * excesso
print ("Voce pescou {} kg de peixe hoje, isso resultou em um excesso de {} kg, e o valor da multa é de R${} reais".format(peso,excesso,multa))

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    #salário bruto.
    #quanto pagou ao INSS.
    #quanto pagou ao sindicato.
    #o salário líquido.
    #calcule os descontos e o salário líquido, conforme a tabela abaixo:
    #+ Salário Bruto : R$
    #- IR (11%) : R$
    #- INSS (8%) : R$
    #- Sindicato ( 5%) : R$
    #= Salário Liquido : R$
    #Obs.: Salário Bruto - Descontos = Salário Líquido.

ganhoPorHora = float(input("Quanto voce ganha por hora?"))
horasPormes = int(input("Quantas horas voce trabalha por mes?"))
salarioBruto = horasPormes * ganhoPorHora 
ir = 0.11 * salarioBruto
inss = 0.08 * salarioBruto
sindicato = 0.05 * salarioBruto
salarioLiquido = salarioBruto - ir - inss - sindicato 
print ("O seu salario bruto é de R${}, o desconto do imposto de renda foi de R${}, o do inss foi de R${}, o do sindicato foi de R${}, resultando um salario liquido de R${}.".format(salarioBruto,ir,inss,sindicato,salarioLiquido ))

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

areaPintada = int(input("Qual o tamanho em metros quadrados da area a ser pintada?"))
tintaInicial = 18
custoInicial = 80 
tinta = (areaPintada / 3) /tintaInicial
custo = tinta * 80 
print ("A quantidade de lata de tinta a serem compradas é de {:.1f}, resultando num valor de R${:.1f} reais".format(tinta,custo))

#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
#ou em galões de 3,6 litros, que custam R$ 25,00.


#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    #comprar apenas latas de 18 litros;
    #comprar apenas galões de 3,6 litros;
    #misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
    #considere latas cheias.

---- FALTA UMA PARTE ----

areaPintada = int(input("Qual o tamanho em metros quadrados da area a ser pintada?"))
cobertura = areaPintada / 6

tintaInicial = 18
custoInicial = 80 

galaoInicial = 3.6
galaoCusto = 25

galao = cobertura / galaoInicial
custoGalao = galao * 25

tinta = cobertura / tintaInicial
custo = tinta * 80 

print ("A quantidade de lata de tinta de 18 litros a serem compradas é de {:.1f}, resultando num valor de R${:.1f} reais".format(tinta,custo))
print ("A quantidade de galao de tinta de 3.6 litros a serem compradas é de {:.1f}, resultando num valor de R${:.1f} reais".format(galao,custoGalao))
---- FALTA UMA PARTE ----

#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = int(input("Qual o tamanho do arquivo em MB?"))
velocidade = int(input("Qual a velocidade da interent? em Mbps"))
tempoDownload = (tamanho / velocidade) / 60 
print ("O seu arquivo de {} MB, ira demorar aproximadamente {:.1f} minutos para baixar".format(tamanho,tempoDownload))
