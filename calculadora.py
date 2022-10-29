"""
Calculadora
Autor: Pietro
cmd- python calculadora.py
"""

print("--CALCULADORA PYTHON--")

sair = False
while sair == False:
	num1 = input("Digite o primeiro número: ")
	num1 = int(num1)
	print("'+' para Soma\n'-' para Subtração\n'*' para Multiplicação\n'/' para Divisão")#\n'**' para Exponenciação")
	oprd = input("Digite o operador: ")
	num2 = input("Digite o segundo número: ")
	num2 = int(num2)

	if oprd == "+": #soma
		operacao = num1 + num2
	elif oprd == "-": #subtração
		operacao = num1 - num2
	elif oprd == "*": #multiplicação
		operacao = num1 * num2
	elif oprd == "/": #divisão
		operacao = num1 / num2
	#elif oprd == "**": #exponenciação
		#operacao = num1 ** num2

	print("Resultado: ")
	print(operacao)

	teste = input("Deseja sair? (s/n)\n")
	if teste == "s":
		sair = True