# python-cohorte-4-modulo-3
Implementación de los conceptos python cohorte 4, módulo 3 Estructuras de Datos y Manipulación Inteligente con IA

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
