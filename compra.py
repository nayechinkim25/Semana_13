# Definición de la función
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

# Bloque principal (se ejecuta al correr el programa)
if __name__ == "__main__":
    # Valores de ejemplo
    precio_producto = 10
    cantidad_productos = 3
    
    # Llamada a la función
    resultado = calcular_total(precio_producto, cantidad_productos)
    
    # Mostrar resultado en consola
    print(f"El total de la compra es: {resultado}")