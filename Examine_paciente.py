temperatura = float(input())
resposta = input().upper()

if resposta != "S" and resposta != "N":
    print("Erro")
    
elif temperatura < 35 or temperatura > 41:
    print("Erro")

else:
    if temperatura >= 37 and resposta == "S":
        print("Exames Especiais")
    elif temperatura >= 37 and resposta == "N":
        print("Exames Basicos")
    elif temperatura < 37 and resposta == "N":
        print("Liberado")
    elif temperatura < 37 and resposta == "S":

        print("Exames Basicos")
