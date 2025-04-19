print("Aprenda a usar esta calculadora!\n + = Adição\n - = Subtração\n * = Multiplicação\n / = Divisão\n ** = Potência\n // = Divisão sem decimal\n % = Divisão Inteira\n %- = Desconto\n %+ = acréscimo")
print("< ------ >") # Separação

# Perguntas!!!!!!
Sinal = str(input("Digite a operação:"))
N1 = float(input("Digite o primeiro número:"))
N2 = float(input("Digite o segundo número:"))
N3 = float(input("Digite o terceiro número:"))
# Para os descontos %-
desconto = N2 / 100 * N1
descontofinal = N1 - desconto # Resultado final.
# Para os acréscimos %+
acrescimo = N2 / 100 * N1
acrescimofinal = N1 + acrescimo # Resultado final, resumidamente.

# É meio óbvio
if Sinal == "+":
    print("Resultado da adição: {}".format(N1 + N2 + N3))
elif Sinal == "-":
    print("Resultado da subtração: {}".format(N1 - N2 - N3))
elif Sinal == "*":
    print("Resultado da multiplicação: {}".format(N1 * N2 * N3))
elif Sinal == "/":
    print("Resultado da divisão: {}".format(N1 / N2))
elif Sinal == "**":
    print("Resultado da potenciação: {}".format(N1 ** N2))
elif Sinal == "//":
    print("Resultado da divisão sem decimal: {}".format(N1 // N2))
elif Sinal == "%":
    print("Resultado da divisão inteira: {}".format(N1 % N2))
elif Sinal == "%-":
    print("Resultado do desconto: {}".format(descontofinal))
elif Sinal == "%+":
    print("Resultado do acrescimo: {}".format(acrescimofinal))
else: # Mensagem de erro.
    print("Ops! Algo deu erro! Por favor, verifique o sinal digitado ou os números digitados!")

# Prescionar ENTER para fechar o programa
input("Prescione a tecla 'Enter' para fechar o programa.")