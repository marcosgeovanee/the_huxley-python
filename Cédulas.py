cedula = int(input())
valor_original = cedula

cem = cedula // 100
cedula = cedula % 100

cinquenta = cedula // 50
cedula = cedula % 50

vinte = cedula // 20
cedula = cedula % 20

dez = cedula // 10
cedula = cedula % 10

cinco = cedula // 5
cedula = cedula % 5

dois = cedula // 2
cedula = cedula % 2

um = cedula

print(valor_original)
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")