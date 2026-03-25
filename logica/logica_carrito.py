def agregar_a_carrito(carrito,plato,cantidad):
    carrito.append({
        "plato":plato, "cantidad":cantidad
    })


    def calcular_total_carrito(carrito):
        total = 0
        for item in carrito:
            total += item["plato"]["precio"] * item["cantidad"]

def borrar_carrito(carrito):