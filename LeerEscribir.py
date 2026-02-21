import json

def leer_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def escribir_json(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
            json.dump(contenido, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos en {nombre_archivo}: {e}")