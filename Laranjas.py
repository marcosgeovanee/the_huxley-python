quantidade = int(input(""))
duzia = quantidade // 12
valor_unidade = 8.35 / 12
valor_duzia = 8.35
unidade = quantidade % 12 * valor_unidade
print(duzia)
print(f"{unidade+(valor_duzia*duzia):.2f}")