# 1. Puntaje total
nivel1 = int(input("Nivel 1: "))
nivel2 = int(input("Nivel 2: "))
nivel3 = int(input("Nivel 3: "))
total = nivel1 + nivel2 + nivel3
print("Puntaje total:", total)

# 2. Tiempo total en segundos
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
total_segundos = horas * 3600 + minutos * 60 + segundos
print("Tiempo total en segundos:", total_segundos)

# 3. Daño total
ataque1 = int(input("Ataque 1: "))
ataque2 = int(input("Ataque 2: "))
ataque3 = int(input("Ataque 3: "))
danio_total = ataque1 + ataque2 + ataque3
print("Daño total:", danio_total)