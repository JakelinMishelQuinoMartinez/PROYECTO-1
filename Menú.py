def menu_principal():
    menu = """
    =============================================
        Administrador de Colección
    =============================================
    1. Añadir un Nuevo Elemento
    2. Ver Todos los Elementos
    3. Buscar un Elemento
    4. Editar un Elemento
    5. Eliminar un Elemento
    6. Ver Elementos por Categoría
    7. Guardar y Cargar Colección
    8. Salir
    =============================================
    """
    print(menu)
  
def menu_uno():
    menu = """
    =============================================
        Añadir un Nuevo Elemento
    =============================================
    ¿Qué tipo de elemento deseas añadir?
    1. Libro
    2. Película
    3. Música
    4. Regresar al Menú Principal
    =============================================
    """
    print(menu)

def menu_dos():
    menu = """
    =============================================
        Ver Todos los Elementos
    =============================================
    ¿Qué categoría deseas ver?
    1. Ver Todos los Libros
    2. Ver Todas las Películas
    3. Ver Toda la Música
    4. Regresar al Menú Principal
    =============================================
    """
    print(menu)

def menu_tres():
    menu = """
    =============================================
        Buscar un Elemento
    =============================================
    ¿Cómo deseas buscar?
    1. Buscar por Título
    2. Buscar por Autor/Director/Artista
    3. Buscar por Género
    4. Regresar al Menú Principal
    =============================================
    """
    print(menu)

def menu_cuatro():
    menu = """
    =============================================
        Editar un Elemento
    =============================================
    ¿Qué tipo de cambio deseas realizar?
    1. Editar Título
    2. Editar Autor/Director/Artista
    3. Editar Género
    4. Editar Puntuación
    5. Regresar al Menú Principal
    =============================================
    """
    print(menu)

def menu_cinco():
    menu = """
    =============================================
        Eliminar un Elemento
    =============================================
    ¿Cómo deseas eliminar?
    1. Eliminar por Título
    2. Eliminar por Identificador Único
    3. Regresar al Menú Principal
    =============================================
    """
    print(menu)

def menu_seis():
    menu = """
    =============================================
        Ver Elementos por categoría
    =============================================
    ¿Qué categoría deseas ver?
    1. Ver Libros
    2. Ver Películas
    3. Ver Música
    4. Regresar al Menú Principal
    =============================================
    """
    print(menu)

def menu_siete():
    menu = """
    =============================================
        Guardar y cargar Colección
    =============================================
    ¿Qué deseas hacer?
    1. Guardar la Colección Actual
    2. Cargar una Colección Guardada
    3. Regresar al Menú Principal
    =============================================
    """
    print(menu)



def selecciona_opcion_principal():
    try:
        opc = int(input("Seleccione una opción (1-8): "))
        return opc
    except ValueError:
        print("El valor ingresado no es un número, intente de nuevo")
        return -1
    
def selecciona_opcion_al3():
    try:
        opc = int(input("Seleccione una opción (1-3): "))
        return opc
    except ValueError:
        print("El valor ingresado no es un número, intente de nuevo")
        return -1

def selecciona_opcion_al4():
    try:
        opc = int(input("Seleccione una opción (1-4): "))
        return opc
    except ValueError:
        print("El valor ingresado no es un número, intente de nuevo")
        return -1

def selecciona_opcion_al5():
    try:
        opc = int(input("Seleccione una opción (1-5): "))
        return opc
    except ValueError:
        print("El valor ingresado no es un número, intente de nuevo")
        return -1
