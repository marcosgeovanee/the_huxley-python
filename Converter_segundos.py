segundos = int(input())
H = segundos // 3600
M = (segundos % 3600) // 60
S = segundos % 60

print(f"{H} h {M} m {S} s")