salario = float(input())
comprometido = float(input())

limite_comprometido = salario * 0.30

limite_disponivel = limite_comprometido - comprometido

if limite_disponivel < 0:
    limite_disponivel = 0

print(f"{limite_disponivel:.2f}")