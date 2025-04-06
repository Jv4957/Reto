<h1>Sobre el código</h1>
El presente código es una solución al reto Interbank academy
Subidas hay dos versiones del código: una que funciona de forma directa y otra para el que se tiene que instalar questionary, para esta última desde el cmd se debe usar el comando pip install questionary.
Este CLI permite procesar el archivo CSV dando como resultado un reporte de las transacciones bancarias que incluye:
Balance Final:
Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".

Transacción de Mayor Monto:
Identificar el ID y el monto de la transacción con el valor más alto.

Conteo de Transacciones:
Número total de transacciones para cada tipo ("Crédito" y "Débito").

<h2>🚀 Requisitos</h2>

- Python 3.7 o superior
- Dependencias:
  - `questionary` para la interfaz interactiva
<h2> Cómo usarlo </h2>
1. Guardar el archivo python dentro de la biblioteca usada para el python
2. Iniciar el cmd
3. Ejecutar con python

<h2>Formato esperado del CSV</h2>
El archivo debe tener las siguientes columnas:
id,tipo,monto
1,Crédito,1000.00
2,Débito,250.50
3,Crédito,500.00

<h2>Ejemplo de salida</h2>
Reporte de Transacciones

────────────────────────────

Balance Final: $1249.50

Transacción de Mayor Monto: ID 1 - $1000.00

Conteo de Transacciones:
   - Créditos: 2
   - Débitos:  1

   
────────────────────────────
