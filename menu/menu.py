import questionary


def mostrar_menu_principal():
    return questionary.select(
        "selecciona una opción: ",
        choices=[
            "ver menú",
            "buscar plato",
            "agregar al pedido",
            "ver pedido",
            "salir"

        ]

    ).ask()

mostrar_menu_principal()


def pedir_texto(mensaje)
    return questionary.text(mensaje).ask()

def pedir_numero(mensaje:str):
    valor = questionary.text(mensaje).ask()
    return int(valor)

pedir_numero
