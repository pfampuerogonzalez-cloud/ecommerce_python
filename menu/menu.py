import questionary


def mostrar_menu_principal():
    return questionary.select(
        "selecciona una opción: ",
        choices=[
            "Ver menú",
            "Buscar plato",
            "Agregar al carrito",
            "Vaciar carrito",
            "Salir"
         ]

    ).ask()


def pedir_texto(mensaje):
    return questionary.text(mensaje).ask()

def pedir_numero(mensaje:str):
    valor = questionary.text(mensaje).ask()
    return int(valor)

def mostrar_platos(platos):
    if not platos:
        print("No hay resultados")
        return
    
    for p in platos:
        print(f"{p['id']} - {p['nombre']} (${p['precio']}) [{p['categoria']}]")
