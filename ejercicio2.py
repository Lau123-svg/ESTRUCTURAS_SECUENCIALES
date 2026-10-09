# Calcular promedio de 3 notas
estudiante=input("nombre del estudiante: ")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1 + n2 + n3) / 3
print("Estudiante:", estudiante)
print("Promedio:",round(promedio, 2))