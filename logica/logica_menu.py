

def listar_menu(menu_platos):
    return menu_platos


def buscar_platos(menu_platos, texto):
    texto = ''
    for [ plato for plato in menu_plato if texto in plato["nombre"] or texto in platos["categoria"]]
         
def obtener_plato_por_id(menu_platos,id_plato):
    for plato in menu_platos:
        if plato["id"] == id_plato:
            return plato
    return None

def mostrar_platos(platos):
    if not platos:
        print(p[""