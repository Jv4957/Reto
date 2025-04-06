import csv
import argparse

# Función principal que procesa el archivo CSV
def procesar_csv(ruta_archivo):
    balance = 0.0
    conteo = {"Crédito": 0, "Débito": 0}
    transaccion_max = {"id": None, "monto": float("-inf")}

    with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            tipo = fila['tipo']
            monto = float(fila['monto'])
            trans_id = fila['id']

            if tipo == "Crédito":
                balance += monto
                conteo["Crédito"] += 1
            elif tipo == "Débito":
                balance -= monto
                conteo["Débito"] += 1

            if monto > transaccion_max["monto"]:
                transaccion_max["monto"] = monto
                transaccion_max["id"] = trans_id

    return balance, transaccion_max, conteo

# Función para mostrar el reporte
def mostrar_reporte(balance, trans_max, conteo):
    print("\n--- Reporte de Transacciones ---")
    print(f"Balance Final: ${balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {trans_max['id']} - ${trans_max['monto']:.2f}")
    print("Conteo de Transacciones:")
    print(f"  Créditos: {conteo['Crédito']}")
    print(f"  Débitos: {conteo['Débito']}")

# Entrada principal del script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesador de archivo CSV de transacciones")
    parser.add_argument("archivo", help="Ruta del archivo CSV")

    args = parser.parse_args()
    balance, trans_max, conteo = procesar_csv(args.archivo)
    mostrar_reporte(balance, trans_max, conteo)
