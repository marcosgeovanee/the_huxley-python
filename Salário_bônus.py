nome = input()
salario = float(input())
valor_vendas = float(input())

montante = (valor_vendas * 0.15) + salario

print(f"TOTAL = R$ {montante:.2f}")