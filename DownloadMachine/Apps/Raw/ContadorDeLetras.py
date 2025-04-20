# CONTADOR DE LETRAS #
import time
##

print("Seja bem-vindo(a) ao contador de letras! Isso é útil para estudantes que queiramm contar a quantidade de letras que há no texto.")
print("< --- >\n")

##
perg = input("Deseja que o programa conte os espaços como letras? (S para sim e N para não):\n")
Coisa = input("Digite o texto aqui:\n") # O usuário irá digitar o texto :fire:

CoisaCon = len(Coisa) # Isso irá contar a quantidade de palavras. ISSO É ABSOLUTE CINEMA! NÃO TOQUE NISTO!!!!!!!!
CoisaConEs = len(Coisa.replace(" ", ""))

if perg.upper() == "S":
    print("Carregando...\n") # Carregamento, isso irá ficar inacreditável e tecnológico!
    time.sleep(1.25)

    print("O texto têm: {} palavras".format(CoisaCon))
elif perg.upper() == "N":
    print("Carregando...\n") # Carregamento, isso irá ficar inacreditável e tecnológico!
    time.sleep(1.25)

    print("O texto têm: {} palavras".format(CoisaConEs))

else: # Mensagem de erro.
    print("Ops! Algo deu errado! Verifique a sua resposta.")

# Clique em 'Enter' para sair do programa! Uau!!!!!
input("Clique na tecla 'Enter' para sair do programa.")