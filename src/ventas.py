def calcular_total(precio, cantidad):
    return precio * cantidad


def aplicar_descuento(subtotal):
    if subtotal >= 200:
        return subtotal * 0.90
    return subtotal


precio = 50
cantidad = 4
subtotal = calcular_total(precio, cantidad)

print("Subtotal: S/", subtotal)
print("Total: S/", aplicar_descuento(subtotal))