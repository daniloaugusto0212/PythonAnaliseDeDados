#calculadora em Python

print('Selecione a operação desejada: ')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
operacao = int(input('Digite sua opção (1/2/3/4):\n'))
if operacao > 4:
    print('Opção inválida, reinicie o programa!')
    exit()
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número'))

if operacao == 4 and y == 0:
    print('Não é possível dividir um número por 0.')
    exit()

soma = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y



if operacao == 1:
    resultado = soma
    sinal = '+'
elif operacao == 2:
    resultado = subtracao
    sinal = '-'
elif operacao == 3:
    resultado = multiplicacao
    sinal = 'x'
elif operacao == 4:
    resultado = divisao
    sinal = '/'


print(f'{x} {sinal} {y} = {resultado}')
