# CONTADOR DE LETRAS #
import time
##

print("Welcome to Letter Count! This program is perfect for count the quantity of letters that your text has!")
print("< --- >\n")

##
perg = input("Do you want the program count 'espace' like letter? (Y for yes and N for not):\n")
Coisa = input("Enter the text here:\n") # O usuário irá digitar o texto :fire:

CoisaCon = len(Coisa) # Isso irá contar a quantidade de palavras. ISSO É ABSOLUTE CINEMA! NÃO TOQUE NISTO!!!!!!!!
CoisaConEs = len(Coisa.replace(" ", ""))

if perg.upper() == "Y":
    print("Loading...\n") # Carregamento, isso irá ficar inacreditável e tecnológico!
    time.sleep(1.25)

    print("The text have: {} letters".format(CoisaCon))
elif perg.upper() == "N":
    print("Loading...\n") # Carregamento, isso irá ficar inacreditável e tecnológico!
    time.sleep(1.25)

    print("The text have: {} letters".format(CoisaConEs))

else: # Mensagem de erro.
    print("Ops! An Error!! Verify if you insered the text correctly!")

# Clique em 'Enter' para sair do programa! Uau!!!!!
input("Press the 'Enter' key to close the program!")