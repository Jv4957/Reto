# importar las librerías necesarias
import csv                           # Para leer archivos CSV
import questionary                   # Para crear una interfaz interactiva en la terminal
from questionary import Style        # Para aplicar estilo personalizado a la interfaz
from pathlib import Path             # Para verificar si la ruta del archivo existe
import sys                           # Para salir del programa en caso de error

# Estilo personalizado para los mensajes interactivos del questionary
custom_style = Style([
    ('qmark', 'fg:#ff9d00 bold'),        # Estilo del signo de pregunta
    ('answer', 'fg:#00d787 bold'),       # Estilo del texto ingresado por el usuario
    ('pointer', 'fg:#00d787 bold'),      # Estilo del cursor de selección
    ('highlighted', 'fg:#ff9d00 bold'),  # Estilo de texto resaltado
    ('selected', 'fg:#00d787 bold'),     # Estilo del texto seleccionado
])

# Función principal que procesa el archivo CSV
def procesar_csv(ruta_archivo):
    balance = 0.0  # Inicializa el balance total
    conteo = {"Crédito": 0, "Débito": 0}  # Contadores por tipo de transacción
    transaccion_max = {"id": None, "monto": float("-inf")}  # Inicializa la transacción más alta

    # Abrir el archivo CSV y leerlo línea por línea
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)  # Lee el CSV como diccionario
        for fila in lector:
            tipo = fila['tipo']
            monto = float(fila['monto'])
            trans_id = fila['id']

            # Sumar o restar del balance dependiendo del tipo de transacción
            if tipo == "Crédito":
                balance += monto
                conteo["Crédito"] += 1
            elif tipo == "Débito":
                balance -= monto
                conteo["Débito"] += 1

            # Actualizar si esta transacción tiene el monto más alto hasta ahora
            if monto > transaccion_max["monto"]:
                transaccion_max["monto"] = monto
                transaccion_max["id"] = trans_id

    # Retorna los resultados procesados
    return balance, transaccion_max, conteo

# Función que imprime el reporte final de forma clara y decorada
def mostrar_reporte(balance, trans_max, conteo):
    print("\n📊  Reporte de Transacciones")
    print("────────────────────────────")
    print(f"💰 Balance Final: ${balance:.2f}")
    print(f"🏆 Transacción de Mayor Monto: ID {trans_max['id']} - ${trans_max['monto']:.2f}")
    print("📈 Conteo de Transacciones:")
    print(f"   - Créditos: {conteo['Crédito']}")
    print(f"   - Débitos:  {conteo['Débito']}")
    print("────────────────────────────\n")

# Función principal que se ejecuta al iniciar el programa
def main():
    # Mensaje de bienvenida
    questionary.print("💼 Procesador de Transacciones Bancarias", style="bold")

    # Bucle que solicita al usuario la ruta de un archivo CSV válido
    while True:
        archivo = questionary.text("📄 Escribe la ruta del archivo CSV:", style=custom_style).ask()

        # Validar si la ruta ingresada corresponde a un archivo existente
        if archivo and Path(archivo).is_file():
            break  # Si es válido, salir del bucle
        questionary.print("❌ Archivo no válido. Intenta de nuevo.", style="bold fg:red")

    # Procesar el archivo y mostrar el reporte
    balance, trans_max, conteo = procesar_csv(archivo)
    mostrar_reporte(balance, trans_max, conteo)

# Punto de entrada del programa
if __name__ == '__main__':
    main()
