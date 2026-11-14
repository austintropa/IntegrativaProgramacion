# Proyecto Integrativo ICC202 — Equipo A

## 1. Identificación del proyecto

**Asignatura:** Fundamentos de la Programación (ICC202)  
**Equipo:** A  
**Problemática seleccionada:** Comercio electrónico — Análisis de ventas e inventario  
**Estado:** Propuesta preliminar  
**Lenguaje de programación:** Python  
**Fuente de datos prevista:** Microsoft Excel (.xlsx)

---

## 2. Nombre provisional

**Sistema de análisis de ventas e inventario para una tienda en línea**

## 3. Contexto de la problemática

En el comercio electrónico, las tiendas reciben pedidos de distintos productos a lo largo del tiempo. Para administrar adecuadamente sus operaciones, necesitan conocer qué productos se venden con mayor frecuencia, cómo varían las ventas y cuáles podrían requerir reposición.

Una tienda pequeña puede registrar sus ventas en planillas Excel. Sin embargo, revisar manualmente estos registros puede dificultar la identificación de tendencias, la comparación de resultados y el control de las existencias disponibles.

Para este proyecto se utilizará como caso de estudio una tienda ficticia que comercializa productos por internet y mantiene registros de sus ventas e inventario.

## 4. Descripción de la problemática

La problemática consiste en la dificultad para organizar, procesar e interpretar los registros de ventas de una tienda en línea cuando la información se encuentra almacenada en planillas y se analiza manualmente.

Esta situación puede ocasionar:

- Dificultades para identificar los productos más y menos vendidos.
- Demoras en la obtención de totales de ventas por periodo.
- Falta de información resumida para comparar el comportamiento de distintos productos.
- Dificultades para detectar productos cuyas existencias están por debajo de un nivel mínimo establecido.
- Mayor riesgo de errores durante los cálculos manuales.

La ausencia de un procesamiento sistemático limita la posibilidad de utilizar los registros disponibles para apoyar decisiones relacionadas con el inventario y la reposición de productos.

El proyecto buscará abordar esta necesidad mediante el procesamiento automatizado de datos, sin pretender reemplazar una plataforma completa de comercio electrónico.

## 5. Beneficiarios preliminares

### Beneficiarios directos

- **Propietario o administrador de la tienda:** podrá consultar información resumida sobre las ventas y las existencias.
- **Encargado de inventario:** podrá identificar productos con niveles bajos de stock y revisar su comportamiento de ventas.

### Beneficiarios indirectos

- **Personal responsable de compras:** podrá utilizar los resultados para apoyar decisiones de reposición.
- **Clientes de la tienda:** podrían beneficiarse indirectamente de una mejor planificación de las existencias, aunque el programa no garantizará la disponibilidad de productos.

## 6. Propuesta preliminar de solución

Se propone desarrollar un programa en Python capaz de leer registros almacenados en un archivo Excel, organizarlos en estructuras de datos y procesarlos mediante una matriz bidimensional.

La matriz principal representará las cantidades vendidas de distintos productos durante periodos semanales.

El programa permitirá consultar información, realizar cálculos, comparar resultados y mostrar indicadores útiles mediante un menú ejecutado en la consola.

La información de inventario se mantendrá diferenciada de los registros de ventas, ya que la cantidad vendida de un producto no representa necesariamente su stock actual.

## 7. Datos preliminares necesarios

Se considera utilizar datos ficticios y coherentes con el funcionamiento de una tienda pequeña.

Entre las variables propuestas se encuentran:

- Código identificador del producto.
- Nombre del producto.
- Categoría del producto.
- Cantidad de unidades vendidas por semana.
- Existencias actuales del producto.
- Nivel mínimo de existencias definido para cada producto.

### Representación matricial

La matriz principal podría organizarse de la siguiente manera:

- **Filas:** productos comercializados.
- **Columnas:** semanas del periodo analizado.
- **Valores:** unidades vendidas de cada producto durante cada semana.

Esta estructura permitiría utilizar recorridos por filas y columnas para calcular totales, comparar cantidades e identificar resultados relevantes.

La estructura definitiva de los archivos Excel y las matrices será determinada en una etapa posterior.

## 8. Posibles funcionalidades

Se consideran inicialmente las siguientes operaciones:

1. Consultar las ventas registradas de un producto.
2. Calcular el total de unidades vendidas por producto.
3. Calcular el total de unidades vendidas durante una semana.
4. Identificar el producto con mayor cantidad de unidades vendidas.
5. Detectar productos cuyas existencias estén por debajo del mínimo establecido.
6. Actualizar registros de ventas, incorporando validaciones.
7. Salir del programa.

Las operaciones de totales por producto, totales semanales e identificación del producto más vendido requerirán recorrer y procesar efectivamente la matriz principal.

Estas funcionalidades son propuestas iniciales y podrán modificarse después de revisar la pauta oficial.

## 9. Justificación preliminar

El desarrollo de esta solución resulta pertinente porque permite transformar registros de ventas en información resumida que facilite el análisis de la actividad comercial.

Desde el punto de vista académico, la problemática ofrece la oportunidad de aplicar fundamentos de programación a una situación concreta mediante:

- Lectura y procesamiento de archivos Excel.
- Utilización de listas y matrices bidimensionales.
- Estructuras condicionales e iterativas.
- Funciones para organizar las operaciones.
- Cálculos, búsquedas y comparaciones.
- Validación de entradas y comprobación de resultados.

La propuesta también permite trabajar con datos simulados sin utilizar información comercial confidencial ni datos personales de clientes.

## 10. Alcance y limitaciones preliminares

### Dentro del alcance

- Procesamiento de registros ficticios de ventas.
- Lectura de información desde Excel.
- Análisis cuantitativo de productos y periodos.
- Consulta de existencias actuales.
- Visualización de resultados en consola.
- Validación de registros y operaciones.

### Fuera del alcance

- Desarrollo de un sitio web de comercio electrónico.
- Procesamiento de pagos en línea.
- Autenticación de usuarios.
- Gestión de pedidos reales.
- Conexiones con servicios externos.
- Predicción avanzada de demanda.
- Administración de bases de datos complejas.

## 11. Viabilidad técnica preliminar

La propuesta se considera técnicamente viable para estudiantes de primer año porque puede desarrollarse utilizando conceptos fundamentales de Python y una biblioteca para trabajar con archivos Excel.

El procesamiento se basará principalmente en recorridos de matrices, acumuladores, condiciones, búsquedas y funciones.

Las principales dificultades de aprendizaje previstas serán la lectura de archivos Excel, la construcción correcta de matrices y la validación de los datos.

No será necesario implementar interfaces gráficas, servidores ni sistemas comerciales avanzados.

## 12. Consideraciones éticas y calidad de datos

Se utilizarán registros simulados, evitando nombres de clientes, direcciones, medios de pago y otros datos personales.

Las cantidades vendidas deberán ser valores numéricos no negativos y las existencias deberán mantener un significado claramente definido.

Las conclusiones estarán limitadas a los datos utilizados. Los resultados de una simulación no podrán presentarse como información real de una empresa.

## 13. Correspondencia preliminar con ICC202

De acuerdo con las condiciones de trabajo comunicadas para el proyecto, esta propuesta contempla:

- Una problemática concreta y delimitada.
- Beneficiarios identificables.
- Un propósito de análisis y apoyo a decisiones.
- Datos estructurados y procesables.
- Utilización de Python y Excel.
- Una matriz bidimensional pertinente.
- Al menos cinco acciones funcionales, además de salir.
- Al menos tres operaciones de procesamiento efectivo de la matriz.
- Posibilidades de validación, pruebas e interpretación de resultados.

**Importante:** esta correspondencia es preliminar. Todavía debe comprobarse contra el documento oficial del proyecto y sus criterios de evaluación.

## 14. Aspectos pendientes de definición

- Revisar el documento oficial y verificar los requisitos aplicables.
- Formular y revisar el objetivo general y los objetivos específicos.
- Determinar las categorías y cantidades de productos que tendrá la tienda ficticia.
- Definir el periodo que abarcarán los registros.
- Precisar cómo se representarán las ventas y las existencias.
- Diseñar posteriormente el archivo Excel y las estructuras de datos.
- Validar el alcance y la dificultad académica antes de iniciar la implementación.

---

**Estado del documento:** Borrador inicial del Equipo A. Su contenido podrá corregirse y ampliarse durante las próximas etapas del Proyecto Integrativo ICC202.