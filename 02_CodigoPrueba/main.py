import pandas as pd #para leer los archivos
from pathlib import Path

Carpeta = Path(__file__).resolve().parent
#__file__ identifica el archivo Python que se está ejecutando.
#.resolve() obtiene su ruta absoluta.
#.parent obtiene la carpeta que contiene ese archivo.


#/ "paquetes.csv" construye la ruta del CSV dentro de esa carpeta.
Datos = pd.read_csv(Carpeta / "paquetes.csv")
#al usar el pandas y buscar la ruta del archivo que leera, hay un error que pandas busca el mismo paquete en el mismo directorio en donde se encuentre este archivo, asi que se usa pathlib



print(Datos)