idade = int(input())
tipo = input().lower()

if idade not in range(0, 131):
    print("Idade invalida.")
else:
    idades_minima = {
    "azar" : 21,
    "mmorpg" : 14,
    "moba" : 10,
    "casual": 0
    }
    
    if tipo not in idades_minima:
        print("Jogo invalido.")
    elif idade >= idades_minima[tipo]:
        print("Pode entrar!")
    else:
        print("Volte daqui h� alguns anos.")