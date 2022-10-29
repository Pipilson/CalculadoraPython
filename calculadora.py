"""
Calculadora
Autor: Pietro
cmd- python calculadora.py
"""

print("\n--CALCULADORA PYTHON--\n")
soma = "+"
sub = "-"
mult = "*"
div = "/"
exp = "^"
sair = False

while sair == False:
	while True:
		try:
			num1 = int(input("Digite o primeiro número: "))
			break
		except ValueError:
			print("Você digitou algo inválido!\nPor favor, digite apenas números.\n")

	while True:
		try:
			oprd = input("Digite o operador: ")
			if oprd == soma or oprd == sub or oprd == mult or oprd == div or oprd == exp:
				break
			else:
				print("Você digitou algo inválido! Digite um operador:\n",soma, "--> Soma\n",sub, "--> Subtração\n",mult, "--> Multiplicação\n",div, "--> Divisão\n",exp, "--> Exponenciação\n")
		except ValueError:
			print("Você digitou algo inválido!\nPor favor, digite apenas números.\n")

	while True:
		try:
			num2 = int(input("Digite o segundo número: "))
			break
		except ValueError:
			print("Você digitou algo inválido!\nPor favor, digite apenas números.\n")

	if oprd == soma: #Soma
		conta = num1 + num2
		print(num1, soma, num2, "=", conta)

	elif oprd == sub: #Subtração
		conta = num1 - num2
		print(num1, sub, num2, "=", conta)

	elif oprd == mult: #Multiplicação
		conta = num1 * num2
		print(num1, mult, num2, "=", conta)

	elif oprd == div: #Divisão
		conta = num1 / num2
		print(num1, div, num2, "=", conta)

	elif oprd == exp: #Exponenciação
		conta = num1 ** num2
		print(num1, exp, num2, "=", conta)

	print("\n")
	while True:
		teste = input("Deseja sair? (s/n)\n")
		if teste == "s":
			sair = True
			break
		elif teste != "n":
			print("Digite 's' para SIM ou 'n' para NÃO\n")
		elif teste == "n":
			print("\n")
			break