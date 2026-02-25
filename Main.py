from Menú import *
from LeerEscribir import *

def Ejecucion_menu_principal():
    while True:
        menu_principal()
        opcion = selecciona_opcion_principal()
        if opcion == 1:
            ejecucion_menu_uno()
        elif opcion == 2:
            ejecucion_menu_dos()
        elif opcion == 3:
            ejecucion_menu_tres()
        elif opcion == 4:
            ejecucion_menu_cuatro()
        elif opcion == 5:
            ejecucion_menu_cinco()
        elif opcion == 6:
            ejecucion_menu_seis()
        elif opcion == 7:
            ejecucion_menu_siete()
        elif opcion == 8:
            print("Saliendo...")
            break
        else:
            print("¡Opción no válida, intente de nuevo!")


def ejecucion_menu_uno():
   while True:
       menu_uno()
       opcion = selecciona_opcion_al4()
       try:
           if opcion == 1:
               print("\n--- Añadiendo Libro ---")
               Colección = leer_json('Libros.json')
               titulo_nuevo = input("Ingrese el Título: ").strip()
               titulos_existentes = {libro['Título'].lower() for libro in Colección}
               if titulo_nuevo.lower() in titulos_existentes:
                    print(f"Error: El libro '{titulo_nuevo}' ya existe.")
                    continue               
               Nuevo_Libro = {
                   "Título": titulo_nuevo,
                   "Autor": input("Ingrese el Autor: ").strip(),
                   "Género": input("Ingrese el Género: ").strip(),
                   "Puntuación": int(input("Ingrese la Puntuación (1-10): "))
               }
               Colección.append(Nuevo_Libro)
               escribir_json("Libros.json", Colección)
               print("¡Libro Guardado!")
           elif opcion == 2:
               print("\n--- Añadiendo Película ---")
               Colección = leer_json('Películas.json')
               titulo_nuevo = input("Ingrese el Título: ").strip()
               titulos_existentes = {pelicula['Título'].lower() for pelicula in Colección}
               if titulo_nuevo.lower() in titulos_existentes:
                    print(f"Error: La Película '{titulo_nuevo}' ya existe.")
                    continue 
               Nueva_Película = {
                   "Título": titulo_nuevo,
                   "Director": input("Ingrese el Director: ").strip(),
                   "Género": input("Ingrese el Género: ").strip(),
                   "Puntuación": int(input("Ingrese la Puntuación (1-10): "))
               }
               Colección.append(Nueva_Película)
               escribir_json("Películas.json", Colección)
               print("¡Película Guardada!")
           elif opcion == 3:
               print("\n--- Añadiendo Música ---")
               Colección = leer_json('Música.json')
               titulo_nuevo = input("Ingrese el Título: ").strip()
               titulos_existentes = {musica['Título'].lower() for musica in Colección}
               if titulo_nuevo.lower() in titulos_existentes:
                    print(f"Error: La Música '{titulo_nuevo}' ya existe.")
                    continue 
               Nueva_Música = {
                   "Título": titulo_nuevo,
                   "Artista": input("Ingrese el Artista: ").strip(),
                   "Género": input("Ingrese el Género: ").strip(),
                   "Puntuación": int(input("Ingrese la Puntuación (1-10): "))
               }
               Colección.append(Nueva_Música)
               escribir_json("Música.json", Colección)
               print("¡Música Guardada!") 
           elif opcion == 4:
             print("Regresando al menú principal")
             break
       except ValueError:
           print("Error: La puntuación debe ser un número. Intente de nuevo.")


def ejecucion_menu_dos():
    while True:
        menu_dos()
        opcion = selecciona_opcion_al4()
        if opcion == 1:
            print("\n--- LISTADO DE LIBROS ---")
            contenido = leer_json('Libros.json')
            if not contenido:
                print("La colección de libros está vacía.")
            else:
                for item in contenido:
                    print(f"Título: {item.get('Título')} | Autor: {item.get('Autor')} | Género: {item.get('Género')} | Puntuación: {item.get('Puntuación')}")
        elif opcion == 2:
            print("\n--- LISTADO DE PELÍCULAS ---")
            contenido = leer_json('Películas.json')
            if not contenido:
                print("La colección de películas está vacía.")
            else:
                for item in contenido:
                    print(f"Título: {item.get('Título')} | Director: {item.get('Director')} | Género: {item.get('Género')} | Puntuación: {item.get('Puntuación')}")
        elif opcion == 3:
            print("\n--- LISTADO DE MÚSICA ---")
            contenido = leer_json('Música.json')
            if not contenido:
                print("La colección de música está vacía.")
            else:
                for item in contenido:
                    print(f"Título: {item.get('Título')} | Artista: {item.get('Artista')} | Género: {item.get('Género')} | Puntuación: {item.get('Puntuación')}")
        elif opcion == 4:
            print("Regresando al Menú Principal")
            break
        else:
            print("¡Opción no válida, intente de nuevo!")


def buscar_en_todos_los_archivos(criterio, valor_buscado):
    archivos = {"Libros": "Libros.json", "Películas": "Películas.json", "Música": "Música.json"}
    resultados = []
    for categoria, nombre_archivo in archivos.items():
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                for elemento in datos:
                    if criterio == "Autor/Director/Artista":
                        valor_llave = str(elemento.get("Autor", "") or elemento.get("Director", "") or elemento.get("Artista", ""))
                    else:
                        valor_llave = str(elemento.get(criterio, "")) 
                    if valor_buscado.lower() in valor_llave.lower():
                        item = elemento.copy()
                        item["Origen"] = categoria
                        resultados.append(item)
        except: continue       
    return resultados

def ejecucion_menu_tres():
    while True:
        menu_tres()
        opcion = selecciona_opcion_al4()
        if opcion == 4: break  
        criterios = {1: "Título", 2: "Autor/Director/Artista", 3: "Género"}
        criterio_elegido = criterios.get(opcion) 
        if criterio_elegido:
            valor = input(f"Ingrese el {criterio_elegido} a buscar: ").strip()
            resultados = buscar_en_todos_los_archivos(criterio_elegido, valor)
            if resultados:
                for res in resultados:
                    print(f"[{res['Origen']}] {res['Título']} - Puntuación: {res['Puntuación']}")
            else:
                print("No se encontraron resultados.")

def ejecucion_menu_cuatro():
    while True:
        menu_cuatro()
        opcion = selecciona_opcion_al5()
        if opcion == 5: break 
        titulo_buscar = input("Título a editar: ").strip()
        resultados = buscar_en_todos_los_archivos("Título", titulo_buscar)
        if resultados:
            res = resultados[0]
            archivo = f"{res['Origen']}.json"
            datos = leer_json(archivo)
            for item in datos:
                if item['Título'].lower() == titulo_buscar.lower():
                    if opcion == 1: item['Título'] = input("Nuevo Título: ")
                    elif opcion == 3: item['Género'] = input("Nuevo Género: ")
                    elif opcion == 4: item['Puntuación'] = int(input("Nueva Puntuación: "))
                    escribir_json(archivo, datos)
                    print("¡Editado!")
                    break
        else: print("No encontrado.")

def ejecucion_menu_cinco():
    while True:
        menu_cinco()
        opcion = selecciona_opcion_al3()
        if opcion == 3: break
        if opcion == 1:
            titulo = input("Título a eliminar: ").strip()
            encontrados = buscar_en_todos_los_archivos("Título", titulo)
            if encontrados:
                res = encontrados[0]
                confirmar = input(f"¿Eliminar {res['Título']}? (s/n): ")
                if confirmar.lower() == 's':
                    archivo = f"{res['Origen']}.json"
                    datos = leer_json(archivo)
                    datos = [i for i in datos if i['Título'].lower() != titulo.lower()]
                    escribir_json(archivo, datos)
                    print("Eliminado.")
            else: print("No encontrado.")

def ejecucion_menu_seis():
    listar_todos_los_elementos()
    input("Presione Enter para volver...")

def listar_todos_los_elementos():
    fuentes = {"Libro": "Libros.json", "Película": "Películas.json", "Música": "Música.json"}
    print("\n" + "="*95)
    print(f"{'TIPO':<10} | {'TÍTULO':<25} | {'GÉNERO':<15} | {'AUTOR/DIR/ART':<20} | {'PUNT'}")
    print("="*95)
    for etiqueta, archivo in fuentes.items():
        datos = leer_json(archivo)
        for item in datos:
            creador = item.get("Autor") or item.get("Director") or item.get("Artista") or "N/A"
            print(f"{etiqueta:<10} | {item.get('Título', 'N/A'):<25} | {item.get('Género', 'N/A'):<15} | {creador:<20} | {item.get('Puntuación', '-')}")

def ejecucion_menu_siete():
    print("¡Archivos cargados y guardados!")

if __name__ == "__main__":
    Ejecucion_menu_principal()