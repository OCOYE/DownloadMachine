print("Come learn how to use this!!\n + = addition\n - = Subtraction\n * = Multiplication\n / = Division\n ** = Exponentiation\n // = Integer Division\n % = Modulus\n %- = Discount\n %+ = Increase")
print("< ------ >") # Separação

# Perguntas!!!!!!
Sinal = str(input("Enter a math expression: "))
N1 = float(input("Type your 1° number: "))
N2 = float(input("Type your 2° number: "))
N3 = float(input("Type your 3° number: "))
# Para os descontos %-
desconto = N2 / 100 * N1
descontofinal = N1 - desconto # Resultado final.
# Para os acréscimos %+
acrescimo = N2 / 100 * N1
acrescimofinal = N1 + acrescimo # Resultado final, resumidamente.

# É meio óbvio
if Sinal == "+":
    print("Result of Addition: {}".format(N1 + N2 + N3))
elif Sinal == "-":
    print("Result of Subtration: {}".format(N1 - N2 - N3))
elif Sinal == "*":
    print("Result of Multiplication: {}".format(N1 * N2 * N3))
elif Sinal == "/":
    print("Result of Division: {}".format(N1 / N2))
elif Sinal == "**":
    print("Result of Exponentiation: {}".format(N1 ** N2))
elif Sinal == "//":
    print("Result of Integer Division: {}".format(N1 // N2))
elif Sinal == "%":
    print("Result of Modulus: {}".format(N1 % N2))
elif Sinal == "%-":
    print("Result of Discount: {}".format(descontofinal))
elif Sinal == "%+":
    print("Result do Increase: {}".format(acrescimofinal))
else: # Mensagem de erro.
    print("Ops! An Error! Please, verify if you type correctly!!")

# Prescionar ENTER para fechar o programa
input("Press the 'Enter' key to close the program!!")