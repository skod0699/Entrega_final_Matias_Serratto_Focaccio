import os

def mostrar_estructura_y_css(ruta, nivel=0, max_nivel=3):
    if nivel > max_nivel:
        return
    for entry in sorted(os.listdir(ruta)):
        path = os.path.join(ruta, entry)
        indent = "  " * nivel
        if os.path.isdir(path):
            print(f"{indent}{entry}/")
            mostrar_estructura_y_css(path, nivel + 1, max_nivel)
        else:
            print(f"{indent}{entry}")
            if entry.endswith('.css'):
                print(f"{indent}  <-- Archivo CSS encontrado aquí")

def buscar_archivos_css(ruta_static):
    print(f"\nBuscando archivos CSS en: {ruta_static}\n")
    for root, dirs, files in os.walk(ruta_static):
        for file in files:
            if file.endswith('.css'):
                full_path = os.path.join(root, file)
                print(f"Archivo CSS encontrado: {full_path}")

if __name__ == "__main__":
    ruta_proyecto = input("Ingresa la ruta raíz de tu proyecto: ")
    ruta_static = os.path.join(ruta_proyecto, 'static')
    print("\n--- Estructura hasta nivel 3 ---\n")
    mostrar_estructura_y_css(ruta_proyecto, max_nivel=3)
    if os.path.exists(ruta_static):
        buscar_archivos_css(ruta_static)
    else:
        print(f"No se encontró la carpeta static en {ruta_static}")
