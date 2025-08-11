peso = float(input())

if peso <= 20:
    taxa = 0.0
    print(f'{taxa:.2f}')

elif peso <=25.0:
    taxa = (peso-20) * 12.50
    print(f"{taxa:.2f}")

elif peso <= 30.0:
    taxa = (peso-20) * 32.75
    print(f"{taxa:.2f}")

elif peso > 30:
    print("PESO LIMITE EXCEDIDO")