# Importamos pandas para poder leer los datos que tenemos en Excel
import pandas as pd

# Usamos pathlib para trabajar con las rutas de los archivos
from pathlib import Path


# Obtenemos la carpeta donde se encuentra nuestro archivo main.py
Carpeta = Path(__file__).resolve().parent

# Indicamos la ruta del Excel que guardamos en la carpeta datos
RutaExcel = Carpeta / "datos" / "tienda.xlsx"


# Esta función nos permite abrir el Excel y mostrar la información de sus hojas
def MostrarDatosExcel():

    # Primero revisamos si el archivo existe en la ruta que indicamos
    if not RutaExcel.is_file():
        print("Error: no se encontró el archivo tienda.xlsx")

        # Si no existe, salimos de esta función
        return

    # Intentamos abrir el archivo para evitar que el programa falle si hay algún problema
    try:

        # Abrimos el Excel para poder revisar las hojas que contiene
        with pd.ExcelFile(RutaExcel) as Excel:

            # Recorremos cada una de las hojas del archivo
            for NombreHoja in Excel.sheet_names:

                # Leemos la hoja actual y guardamos sus datos en un DataFrame
                Datos = pd.read_excel(Excel, sheet_name=NombreHoja)

                # Mostramos el nombre de la hoja que estamos leyendo
                print(f"\n--- {NombreHoja} ---")

                # Mostramos los nombres de las columnas
                print("Columnas:", list(Datos.columns))

                # Contamos cuántos registros tiene la hoja
                print("Cantidad de registros:", len(Datos))

                # Mostramos los primeros 5 registros sin los índices de pandas
                print(Datos.head().to_string(index=False))

    # Si ocurre alguno de estos errores al leer el Excel, mostramos el problema
    except (OSError, ValueError, ImportError) as Error:
        print("No se pudo leer el archivo Excel:", Error)


# Esta función transforma las ventas del Excel en una matriz de listas
def ConstruirMatrizVentas(DatosVentas):

    # Creamos una lista vacía donde guardaremos las filas de la matriz
    MatrizVentas = []

    # Aquí guardaremos los códigos para saber a qué producto pertenece cada fila
    CodigosProductos = []

    # Indicamos las columnas del Excel que contienen las ventas semanales
    Semanas = ["SEMANA_1", "SEMANA_2", "SEMANA_3", "SEMANA_4"]

    # Recorremos los productos según la cantidad de registros del Excel
    for i in range(len(DatosVentas)):

        # Creamos una lista nueva para guardar las ventas del producto actual
        FilaVentas = []

        # Obtenemos el código del producto que estamos recorriendo
        Codigo = DatosVentas["Codigo"].iloc[i]

        # Guardamos su código en la lista de productos
        CodigosProductos.append(Codigo)

        # Recorremos las 4 semanas para obtener las cantidades vendidas
        for Semana in Semanas:

            # Obtenemos las ventas de esa semana y las convertimos a entero
            Cantidad = int(DatosVentas[Semana].iloc[i])

            # Agregamos la cantidad a la fila del producto
            FilaVentas.append(Cantidad)

        # Cuando tenemos las 4 semanas, agregamos la fila completa a la matriz
        MatrizVentas.append(FilaVentas)

    # Devolvemos la matriz y los códigos para utilizarlos fuera de la función
    return MatrizVentas, CodigosProductos


# Ejecutamos la función para mostrar la información del archivo Excel
MostrarDatosExcel()


# Mostramos un título para separar la matriz de los datos anteriores
print("\n--- MATRIZ DE VENTAS ---")


# Leemos solamente la hoja Ventas, que contiene las cantidades semanales
DatosVentas = pd.read_excel(RutaExcel, sheet_name="Ventas")


# Llamamos a la función y guardamos los dos resultados que nos devuelve
MatrizVentas, CodigosProductos = ConstruirMatrizVentas(DatosVentas)


# Recorremos las filas de la matriz para mostrar las ventas de cada producto
for i in range(len(MatrizVentas)):

    # Mostramos el código del producto junto con sus 4 semanas de ventas
    print(CodigosProductos[i], MatrizVentas[i])


# Mostramos cuántos productos tenemos contando las filas de la matriz
print("\nCantidad de productos:", len(MatrizVentas))

# Contamos las semanas utilizando la cantidad de elementos de la primera fila
print("Cantidad de semanas:", len(MatrizVentas[0]))
