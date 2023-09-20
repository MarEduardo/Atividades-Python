#atividade 1
print('Hello world')
#atividade 2
nome = input('Digite seu nome')
print('Olá, ' + nome)
#atividade 3
coisa = input('Digite alguma coisa')
print(type(coisa))
#atividade 4
num1 = 9
num2 = 8
num3 = num1 + num2
num4 = num1 - num2
num5 = num1 * num2
num6 = num1 / num2
print('A soma do numero é {}, a subtração dos numeros é {}, a multiplicação dos numeros é {} e a divisão dos numeros é {}' .format(num3,num4,num5,num6))
#atividade 5
num = 40
quadrada = num ** (1/2)
cubica = num ** (1/2)
print('A raiz quadrada de 40 é {:3} e a raiz cubida é {:3}' .format(quadrada,cubica))
#atividade 6
nota1 = int(input('Digite sua primeira nota'))
nota2 = int(input('Digite sua segunda nota'))
nota3 = int(input('Digite sua terceira nota'))
nota4 = int(input('Digite sua quarta nota'))
nota5 = (nota1 + nota2 + nota3 + nota4) / 4
print('A media da sua nota é ', nota5)
#atividade 7
tabuada = int(input("Digite um número inteiro: "))
print(f"Tabuada do {tabuada}:")

for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")
