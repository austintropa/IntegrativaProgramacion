import pandas as pd
from pathlib import Path

# Ubicación del proyecto y del archivo Excel
Carpeta = Path(__file__).resolve().parent
RutaExcel = Carpeta / "datos" / "tienda.xlsx"


def MostrarDatosExcel():
    # Comprobamos que el archivo exista
    if not RutaExcel.is_file():
        print("Error: no se encontró el archivo tienda.xlsx")
        return

    try:
        # Abrimos el archivo y revisamos sus hojas
        with pd.ExcelFile(RutaExcel) as Excel:
            for NombreHoja in Excel.sheet_names:
                Datos = pd.read_excel(Excel, sheet_name=NombreHoja)

                print(f"\n--- {NombreHoja} ---")
                print("Columnas:", list(Datos.columns))
                print("Cantidad de registros:", len(Datos))
                print(Datos.head().to_string(index=False))

    except (OSError, ValueError, ImportError) as Error:
        print("No se pudo leer el archivo Excel:", Error)


MostrarDatosExcel()