# Calcular el total de una compra (cantidad x precio)
nombre_producto = input("nombre del producto: ")
cantidad = int(input("Cantidad: "))
precio_unitario = float(input("Precio unitario: "))
total = cantidad * precio_unitario
print("Total de la compra:", round(total, 2))
print("Producto:", nombre_producto)