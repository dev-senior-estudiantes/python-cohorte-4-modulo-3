# python-cohorte-4-modulo-3
Implementación de los conceptos python cohorte 4, módulo 3 Estructuras de Datos y Manipulación Inteligente con IA
---
## Cómo crear un entorno virtual y usar requirements.txt

1. **Crear el entorno virtual con venv**

   En la terminal, ejecuta:
   ```bash
   python -m venv venv
   ```
   Esto creará una carpeta llamada `venv` con el entorno virtual.

2. **Activar el entorno virtual**

   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar dependencias desde requirements.txt**

   Con el entorno virtual activado, ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

Esto instalará todos los paquetes necesarios para el proyecto, incluyendo Jupyter Notebook.

---

## Cómo actualizar requirements.txt después de instalar una nueva librería

Cuando instales una nueva librería con pip, el archivo `requirements.txt` **no se actualiza automáticamente**. Para mantenerlo actualizado con todas las dependencias de tu entorno virtual, sigue estos pasos:

1. Instala la nueva librería normalmente, por ejemplo:
   ```bash
   pip install nombre_libreria
   ```
2. Luego, actualiza el archivo `requirements.txt` ejecutando:
   ```bash
   pip freeze > requirements.txt
   ```
Esto sobrescribirá el archivo con la lista completa de paquetes y versiones instaladas en tu entorno virtual, incluyendo la nueva librería.

> **Importante:** Repite este proceso cada vez que agregues o elimines paquetes para mantener tu proyecto sincronizado.

---

## Clase 6: Composición Inteligente de Estructuras – Práctica Integral

En esta clase, exploramos cómo combinar y organizar estructuras de datos en Python de manera eficiente para manejar datos complejos, sucios o mal estructurados. El objetivo principal es aprender a refactorizar y limpiar datos para mejorar su consistencia, accesibilidad y claridad.

### Conceptos y Temas Tratados

1.  **Composición de Estructuras**:
    *   Se demostró cómo el uso combinado de `listas`, `sets` y `diccionarios` permite modelar datos de forma más efectiva. Por ejemplo, usar una lista para mantener el orden, un set para garantizar elementos únicos y un diccionario para relaciones clave-valor.

2.  **Estructuras Anidadas**:
    *   Se utilizó un diccionario principal (`biblioteca`) que contenía listas de diccionarios para representar entidades complejas como libros y préstamos, mostrando cómo anidar estructuras para crear un modelo de datos coherente.

3.  **Limpieza y Transformación de Datos**:
    *   Se abordó el problema de los datos inconsistentes (mayúsculas/minúsculas, espacios extra, duplicados).
    *   **Métodos utilizados**:
        *   `strip()`: Para eliminar espacios en blanco al inicio y al final de los strings.
        *   `title()`: Para normalizar la capitalización de los nombres (ej. "julio cortázar" -> "Julio Cortázar").
        *   `set()`: Para identificar y eliminar registros duplicados de manera eficiente.

4.  **Refactorización de Datos**:
    *   El concepto clave fue reestructurar los datos para eliminar la redundancia y mejorar la forma en que se accede a ellos.
    *   **Ejemplo práctico**: Se transformó una lista de préstamos donde se repetía el nombre del libro en cada registro a un diccionario donde el ID del libro es la clave, evitando así la duplicación de información.

### Funciones y Ejemplos Destacados

Se desarrolló una función `limpiar_datos(datos)` que encapsula las técnicas de limpieza:

```python
def limpiar_datos(datos):
    estructura_limpia = []
    vistos = set()

    for d in datos:
        # Normalización de datos
        libro = d["book"].strip()
        autor = d["author"].title().strip()
        año = int(d["date"])

        # Creación de una clave única para detectar duplicados
        clave = (libro, autor, año)
        if clave not in vistos:
            vistos.add(clave)
            estructura_limpia.append({
                "titulo": libro,
                "autor": autor,
                "año": año
            })
    return estructura_limpia
```

Finalmente, se propuso un **esquema de biblioteca refactorizado** que organiza autores, libros y préstamos en diccionarios anidados para optimizar las relaciones y el acceso a los datos, sentando las bases para un sistema más robusto y escalable.

---
## Clase 7: Programación Funcional y Pipelines en Python

### Objetivos
- Aplicar listas, tuplas, diccionarios y sets en sistemas reales.
- Entender y practicar programación funcional: funciones puras, inmutabilidad, composición.
- Dominar lambda, map, filter, reduce y comprensiones.
- Diseñar pipelines de limpieza y validación de datos.
- Separar lógica de negocio de presentación/IO.
- Prepararse para trabajar con JSON y estructuras anidadas.

### Conceptos Clave

- **Programación funcional:** Paradigma que evita mutaciones y efectos colaterales, usando funciones puras y composición.
- **Funciones puras:** Mismo input → mismo output, sin modificar variables externas.
- **Inmutabilidad:** No modificar objetos tras crearlos (tuplas, cadenas). Favorece seguridad y predictibilidad.
- **Funciones lambda:** Funciones anónimas, útiles para map, filter, reduce, sorted, callbacks.
- **Composición:** Encadenar funciones simples para crear procesos complejos (pipelines).
- **Pipelines:** Secuencia de pasos de procesamiento de datos, donde la salida de un paso es la entrada del siguiente.
- **Evaluación perezosa:** Uso de generadores para procesar datos grandes sin cargar todo en memoria.
- **Separación de capas:** Core funcional (lógica pura), shell imperativo (IO, logs, errores), presentación.
- **Validación y limpieza:** Normalización, eliminación de duplicados, validación de tipos y rangos.
- **Técnicas senior:** Decoradores, memoización, inyección de dependencias, metaprogramación, procesamiento paralelo y reactivo.

### Ejemplos y Aplicaciones

- **List comprehensions:**
  ```python
  numeros_pares_cuadrados = [num ** 2 for num in numbers if num % 2 == 0]
  ```
- **Funciones de orden superior:**
  ```python
  def aplicar_operacion(op, a, b): return op(a, b)
  resultado = aplicar_operacion(lambda x, y: x + y, 5, 3)
  ```
- **Pipelines con pipe:**
  ```python
  from pipe import where, select
  resultado = numeros | where(lambda n: n % 2 == 0) | select(lambda n: n**2)
  ```
- **ETL y ML:**
  Uso de pandas y scikit-learn Pipeline para transformar y modelar datos.
- **Procesamiento de imágenes:**
  Pipeline para convertir imágenes a escala de grises y crear miniaturas.
- **Inventario funcional:**
  Separación de modelos, reglas de negocio puras, infraestructura simulada y orquestación.

### Buenas Prácticas
- Modularidad: funciones pequeñas y específicas.
- Funciones puras y sin efectos secundarios.
- Uso de herramientas declarativas (pipe, pandas, itertools).
- Evitar mutaciones, preferir estructuras inmutables.
- Legibilidad y nombres descriptivos.
- Pruebas unitarias para cada función.
- Evaluación perezosa para grandes volúmenes de datos.
- Documentación y manejo de excepciones.
- Reutilización de funciones genéricas.

### Diagrama: Arquitectura de Pipelines Funcionales y Separación de Capas

```
+-------------------+         +-------------------+         +-------------------+
|  Shell Imperativo |  --->   |  Núcleo Funcional |  --->   |  Shell Imperativo |
| (IO, logs, errores|         | (funciones puras) |         | (presentación,    |
|  lectura/escritura|         |                   |         |  reporting, etc.) |
+-------------------+         +-------------------+         +-------------------+
        |                             |                              |
        v                             v                              v
  [Leer datos]  --->  [Pipeline de funciones puras]  --->  [Guardar/mostrar]

Ejemplo de pipeline funcional:

[Datos crudos] 
    |\n    v
[Normalizar texto] 
    |\n    v
[Filtrar vacíos] 
    |\n    v
[Transformar tipos] 
    |\n    v
[Validar reglas] 
    |\n    v
[Reporte/resultado]
```

---
## Clase 8: Evaluación final y optimización estructural con IA

### Objetivos y Temas Principales
- Demostrar dominio de estructuras de datos básicas y avanzadas en Python (listas, tuplas, diccionarios, sets, dataclasses).
- Aplicar abstracción y modelado con clases y objetos.
- Usar IA (ChatGPT, Copilot) para refactorizar, documentar y optimizar código.
- Integrar todo lo aprendido en un sistema de gestión de eventos escalable y listo para persistencia.
- Preparar la transición hacia manejo de archivos y bases de datos.

### Conceptos y Técnicas

- **Listas, tuplas, diccionarios, sets:** Uso para almacenar, modificar y consultar datos de eventos, sesiones, asistentes y clientes.
- **Clases y dataclasses:** Abstracción de entidades (Evento, Venue, Attendee, Registration) con tipado estático y docstrings para claridad y mantenibilidad.
- **Refactorización y documentación asistida por IA:** Uso de IA para mejorar nombres, simplificar funciones, añadir docstrings y tipado.
- **Pipelines de limpieza y validación:** Generadores y funciones puras para normalizar, limpiar y validar datos de entrada (emails, nombres, cantidades).
- **Índices y estructuras mixtas:** Diccionarios y listas anidadas para búsquedas eficientes y modelado flexible.
- **Validación de integridad:** Uso de aserciones y predicados para garantizar la consistencia de los datos.
- **Librerías estándar:**
  - `dataclasses` y `typing` para modelado y tipado.
  - `unicodedata` para normalización de texto.
  - `functools`, `collections` para pipelines y conteos.
- **Preparación para persistencia:** Estructuras listas para serialización en JSON, CSV, TXT y futura integración con bases de datos.

### Herramientas y Librerías
- **Python estándar:** dataclasses, typing, unicodedata, functools, collections.
- **IA:** ChatGPT, Copilot para revisión, refactorización y documentación.

### Documentación del Código

- **Modelado de entidades:**
  - `@dataclass` para Venue, Event, Attendee, Registration.
  - Tipado estático y docstrings en cada clase.
- **Gestor de eventos:**
  - Métodos para agregar, listar y filtrar eventos.
  - Ejemplo de uso con impresión de resultados.
- **Estructuras de datos básicas:**
  - Listas para sesiones, ponentes, entradas.
  - Tuplas para franjas horarias.
  - Diccionarios para eventos, clientes y asistentes.
  - Sets para operaciones de conjunto (unión, intersección, diferencia).
- **Normalización y validación:**
  - Funciones puras para limpiar y validar emails/nombres.
  - Pipeline perezoso con generadores para procesar datos sucios.
  - Validación de integridad con aserciones.
- **Índices auxiliares:**
  - Diccionarios para búsquedas rápidas por email, fecha, etc.

### Diagrama del Sistema de Gestión de Eventos

```
+---------+      +--------+      +-----------+
|  Venue  |<-----| Event  |<-----|Registration|
+---------+      +--------+      +-----------+
    ^                ^                ^
    |                |                |
    |                |                |
    +------------+   |                |
                 |   |                |
             +---------+          +----------+
             |Attendee |<---------+
             +---------+

[Entrada sucia] 
    |\n    v
[Pipeline de limpieza y validación]
    |\n    v
[Datos normalizados y validados]
    |\n    v
[Índices y estructuras mixtas]
    |\n    v
[Consultas, reportes y persistencia]
```

### Resumen del Flujo de Trabajo
1. **Entrada de datos:** Captura de eventos, asistentes, sesiones, clientes, etc.
2. **Limpieza y validación:** Normalización de textos, validación de emails y cantidades, eliminación de duplicados.
3. **Modelado y almacenamiento:** Uso de dataclasses y estructuras mixtas para representar entidades y relaciones.
4. **Consultas y reportes:** Listar, filtrar y analizar eventos y asistentes usando índices y operaciones de conjunto.
5. **Preparación para persistencia:** Estructuras listas para ser guardadas/cargadas en archivos o bases de datos.

### Reflexión y Conexión
- La IA potencia la calidad y mantenibilidad del código.
- El sistema está listo para escalar y persistir datos en el siguiente módulo.
- Se aplican buenas prácticas de documentación, validación y modelado profesional.
---



## Proyecto Final: Sistema de Gestión de Eventos

### Descripción General

El proyecto final integra todos los conceptos del módulo en un sistema profesional de gestión de eventos. Permite administrar sedes (venues), eventos, asistentes y registros de participación, aplicando buenas prácticas de modelado, validación y limpieza de datos.

### Conceptos y Temas Principales

- **Listas y tuplas**: Para almacenar secuencias y datos inmutables.
- **Diccionarios y sets**: Para modelar relaciones clave-valor y eliminar duplicados.
- **Estructuras anidadas y mixtas**: Modelado de entidades complejas (eventos, asistentes, registros).
- **Composición inteligente**: Uso de IDs y relaciones normalizadas para eficiencia y claridad.
- **Programación funcional**: Uso de funciones puras, generadores, map/filter/reduce para pipelines de limpieza y validación.
- **Validación y limpieza**: Normalización de textos, eliminación de duplicados, validación de emails y capacidades.

### Funciones y Métodos Clave

- `add_venue(ciudad, nombre, capacidad)`: Agrega una sede.
- `add_event(nombre, fecha, venue_id)`: Crea un evento asociado a una sede.
- `upsert_attendee(email, nombre)`: Registra o actualiza un asistente por email.
- `register(event_id, attendee_id)`: Registra la participación de un asistente en un evento, validando capacidad.
- `eventos_por_fecha(fecha)`: Lista eventos en una fecha dada.
- `asistentes_de_evento(event_id)`: Lista asistentes de un evento.
- `eventos_por_ciudad(ciudad)`: Lista eventos en una ciudad.
- `duplicados_por_email()`: Detecta emails duplicados.
- `top_ciudades_por_eventos(k)`: Top ciudades por cantidad de eventos.
- `ocupacion_por_evento()`: Porcentaje de ocupación por evento.

### Ejemplo de Uso

```python
em = EventManager()
v1 = em.add_venue("Bogotá", "Centro Convenciones", 3)
v2 = em.add_venue("Medellín", "Plaza Mayor", 2)
e1 = em.add_event("Conferencia Python", "2025-09-20", v1)

sucios = [
    {"email": " ANA@mail.com ", "nombre": "Ana"},
    {"email": "luis@mail.COM", "nombre": "Luis"},
    {"email": "maria@mail.com", "nombre": "María"},
]

for fila in pipeline_personas(sucios):
    aid = em.upsert_attendee(fila["email"], fila["nombre"])
    em.register(e1, aid)

print("Eventos 2025-09-20:", em.eventos_por_fecha("2025-09-20"))
print("Asistentes de e1:", em.asistentes_de_evento(e1))
```

### Diagrama del Modelo de Datos

```
+---------+      +--------+      +-----------+
|  Venue  |<-----| Event  |<-----|Registration|
+---------+      +--------+      +-----------+
    ^                ^                ^
    |                |                |
    |                |                |
    +------------+   |                |
                 |   |                |
             +---------+          +----------+
             |Attendee |<---------+
             +---------+
```
- **Venue**: Sede del evento.
- **Event**: Evento con referencia a Venue.
- **Attendee**: Asistente identificado por email.
- **Registration**: Relación entre Event y Attendee.

### Notas
- El sistema utiliza índices para búsquedas eficientes (por fecha, email).
- Incluye validaciones de capacidad y limpieza de datos de entrada.
- El código está preparado para ser ejecutado tanto en scripts como en notebooks.

---
