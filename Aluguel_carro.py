quantidade_dias = int(input())
quilometros = int(input())

aluguel = 30*quantidade_dias
quilometro_rodado = quilometros*0.01
desconto = (aluguel + quilometro_rodado)*0.1
total = (aluguel+quilometro_rodado) - desconto
print(f"{total:.2f}")