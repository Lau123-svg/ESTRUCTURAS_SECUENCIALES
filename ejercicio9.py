# Calcular el IVA de un producto
print("Calcular el IVA de un producto")
print("-" * 40)
precio = float(input("Precio del producto: "))
iva = precio * 0.19
print("IVA:", round(iva, 2))
print("Precio con IVA:", round(precio + iva, 2))
