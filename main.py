import pandas as pd
from pathlib import Path

Carpeta = Path(__file__).resolve().parent
RutaExcel = Carpeta / "datos" / "tienda.xlsx"


def ConstruirMatriz(Datos, Columnas, NombreHoja):
    for Columna in Columnas:
        if Columna not in Datos.columns:
            print(f"Error: falta la columna {Columna} en {NombreHoja}.")
            return None

    if len(Datos) == 0:
        print(f"Error: la hoja {NombreHoja} está vacía.")
        return None

    # Pasamos las columnas necesarias de pandas a una lista de listas.
    Matriz = Datos[Columnas].values.tolist()
    Codigos = []

    for i in range(len(Matriz)):
        Fila = Matriz[i]
        for j in range(len(Fila)):
            Valor = Fila[j]
            Lugar = f"{NombreHoja}, fila {i + 2}, {Columnas[j]}"

            if pd.isna(Valor) or str(Valor).strip() == "":
                print(f"Error: celda vacía en {Lugar}.")
                return None

            if Columnas[j] in ["Codigo", "Nombre", "Categoria"]:
                if type(Valor) != str:
                    print(f"Error: texto inválido en {Lugar}.")
                    return None
                Fila[j] = Valor.strip()
            else:
                try:
                    Cantidad = float(Valor)
                except (ValueError, TypeError, OverflowError):
                    print(f"Error: cantidad no numérica en {Lugar}.")
                    return None

                # Si el resto de dividir por 1 no es cero, no es un entero.
                if type(Valor) == bool or Cantidad < 0 or Cantidad % 1 != 0:
                    print(f"Error: cantidad inválida en {Lugar}.")
                    return None
                Fila[j] = int(Cantidad)

        Fila[0] = Fila[0].upper()
        if Fila[0] in Codigos:
            print(f"Error: código repetido {Fila[0]} en {NombreHoja}.")
            return None
        Codigos.append(Fila[0])

    return Matriz


def BuscarIndice(Matriz, Codigo):
    for i in range(len(Matriz)):
        if Matriz[i][0] == Codigo:
            return i
    return -1


def CargarDatos(Ruta):
    if not Ruta.is_file():
        print("Error: no se encontró el archivo tienda.xlsx.")
        return None, None

    try:
        DatosVentas = pd.read_excel(Ruta, sheet_name="Ventas", engine="openpyxl", dtype=object)
        DatosInventario = pd.read_excel(Ruta, sheet_name="Inventario", engine="openpyxl", dtype=object)
    except Exception as Error:
        print("Error al leer el Excel:", Error)
        return None, None

    ColumnasVentas = ["Codigo", "SEMANA_1", "SEMANA_2", "SEMANA_3", "SEMANA_4"]
    ColumnasInventario = ["Codigo", "Nombre", "Categoria", "Stock_Actual", "Stock_Minimo"]

    Ventas = ConstruirMatriz(DatosVentas, ColumnasVentas, "Ventas")
    Inventario = ConstruirMatriz(DatosInventario, ColumnasInventario, "Inventario")
    if Ventas is None or Inventario is None:
        return None, None

    # Comprobamos que cada producto tenga ventas e inventario.
    for Fila in Ventas:
        if BuscarIndice(Inventario, Fila[0]) == -1:
            print(f"Error: {Fila[0]} no aparece en Inventario.")
            return None, None
    for Fila in Inventario:
        if BuscarIndice(Ventas, Fila[0]) == -1:
            print(f"Error: {Fila[0]} no aparece en Ventas.")
            return None, None

    return Ventas, Inventario


def MostrarProductos(Ventas, Inventario):
    print("\nCódigo  Producto          S1   S2   S3   S4  Stock  Mínimo")
    for Fila in Ventas:
        i = BuscarIndice(Inventario, Fila[0])
        Producto = Inventario[i]
        print(f"{Fila[0]:<7} {Producto[1]:<16} {Fila[1]:>4} {Fila[2]:>4} {Fila[3]:>4} {Fila[4]:>4} {Producto[3]:>6} {Producto[4]:>7}")


def TotalProducto(Fila):
    # El primer elemento es el código, por eso sumamos desde la posición 1.
    return sum(Fila[1:5])


def MostrarTotales(Ventas):
    for Fila in Ventas:
        print(f"{Fila[0]}: {TotalProducto(Fila)} unidades")


def MayorVenta(Ventas):
    Totales = []
    for Fila in Ventas:
        Totales.append(TotalProducto(Fila))

    Mayor = max(Totales)
    for i in range(len(Totales)):
        if Totales[i] == Mayor:
            print(f"{Ventas[i][0]}: {Mayor} unidades (mayor venta)")


def StockBajo(Inventario):
    Contador = 0
    for Fila in Inventario:
        if Fila[3] < Fila[4]:
            print(f"{Fila[0]} - {Fila[1]}: faltan {Fila[4] - Fila[3]} unidades para el mínimo")
            Contador += 1
    print(f"Productos bajo el mínimo: {Contador}")


def BuscarProducto(Ventas, Inventario):
    Codigo = input("Código del producto: ").strip().upper()
    i = BuscarIndice(Ventas, Codigo)
    if i == -1:
        print("Producto no encontrado.")
        return

    j = BuscarIndice(Inventario, Codigo)
    print(f"{Codigo} - {Inventario[j][1]} ({Inventario[j][2]})")
    print("Ventas por semana:", Ventas[i][1:5])
    print("Total de ventas:", TotalProducto(Ventas[i]))
    print(f"Stock actual: {Inventario[j][3]} | Mínimo: {Inventario[j][4]}")


def TotalesSemanales(Ventas):
    for j in range(1, 5):
        Total = 0
        for Fila in Ventas:
            Total += Fila[j]
        print(f"Semana {j}: {Total} unidades")


def ActualizarVenta(Ventas):
    Codigo = input("Código del producto: ").strip().upper()
    i = BuscarIndice(Ventas, Codigo)
    if i == -1:
        print("Producto no encontrado.")
        return

    try:
        Semana = int(input("Semana (1 a 4): "))
        Cantidad = int(input("Nueva cantidad vendida: "))
    except ValueError:
        print("Error: ingrese números enteros.")
        return

    if Semana < 1 or Semana > 4 or Cantidad < 0:
        print("Error: semana fuera de rango o cantidad negativa.")
        return

    Ventas[i][Semana] = Cantidad
    print(f"Venta actualizada en memoria: {Codigo}, semana {Semana}, {Cantidad} unidades.")
    print("Nuevo total:", TotalProducto(Ventas[i]))
    print("El archivo Excel original no se modifica.")


def Principal():
    Ventas, Inventario = CargarDatos(RutaExcel)
    if Ventas is None:
        return

    print(f"Excel cargado: {len(Ventas)} productos y {len(Ventas[0]) - 1} semanas.")
    while True:
        print("\n===== VENTAS E INVENTARIO =====\n1. Mostrar productos y ventas\n2. Total de ventas por producto\n3. Producto con mayores ventas\n4. Productos bajo el stock mínimo\n5. Buscar producto por código\n6. Totales por semana\n7. Actualizar una venta en memoria\n8. Salir")
        try:
            Opcion = int(input("Ingrese opción: "))
        except ValueError:
            print("Error: ingrese una opción numérica.")
            continue

        if Opcion == 1:
            MostrarProductos(Ventas, Inventario)
        elif Opcion == 2:
            MostrarTotales(Ventas)
        elif Opcion == 3:
            MayorVenta(Ventas)
        elif Opcion == 4:
            StockBajo(Inventario)
        elif Opcion == 5:
            BuscarProducto(Ventas, Inventario)
        elif Opcion == 6:
            TotalesSemanales(Ventas)
        elif Opcion == 7:
            ActualizarVenta(Ventas)
        elif Opcion == 8:
            print("Saliendo del programa.")
            break
        else:
            print("Error: opción fuera de rango.")


if __name__ == "__main__":
    Principal()
