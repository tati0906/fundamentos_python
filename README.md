## Seccion1

## LAB 1 - Trabajando con la función `print()`

### 🎯 Objetivo

Aprender el uso básico de la función `print()` y comprender errores comunes en Python.

---

### ✅ Paso 1: Imprimir "¡Hola, Mundo!"

Código:

```python
print("¡Hola, Mundo!")
```

Resultado esperado:

¡Hola, Mundo!

---

### ✅ Paso 2: Imprimir mi nombre

Código:

```python
print("Tatiana")
```

📌 Resultado esperado:

```
Tatiana
```

---

### ⚠️ Paso 3: Eliminar comillas

Código probado:

```python
print(¡Hola, Mundo!)
```

❌ Resultado:

Se genera un error de tipo:

```
SyntaxError
```

📌 Explicación:
Python interpreta el texto sin comillas como código, no como texto, por lo que produce un error de sintaxis.

---

### ⚠️ Paso 4: Eliminar paréntesis

Código probado:

```python
print "Hola"
```

❌ Resultado:

```
SyntaxError
```

📌 Explicación:
En Python 3, la función `print()` requiere paréntesis obligatoriamente.

---

### 🧪 Paso 5: Experimentos realizados

#### ✔ Uso de comillas simples

```python
print('Hola Mundo')
```

✔ Funciona correctamente.

---

#### ✔ Múltiples prints en una línea

```python
print("Linea 1"); print("Linea 2")
```

📌 Resultado:

```
Linea 1
Linea 2
```

---

#### ✔ Prints en diferentes líneas

```python
print("Linea 1")
print("Linea 2")
```

📌 Resultado:

```
Linea 1
Linea 2
```

---

### 🧠 Conclusiones

* La función `print()` permite mostrar información en pantalla.
* Las cadenas deben ir entre comillas.
* Los paréntesis son obligatorios en Python 3.
* Python es sensible a errores de sintaxis.
* Se pueden usar comillas simples o dobles.
* Cada `print()` genera una nueva línea por defecto.



## LAB 2 - La función `print()` y sus argumentos

### 🎯 Objetivo

Aprender a usar los argumentos `sep` y `end` para modificar la salida de la función `print()`.

---

### 📌 Enunciado

Modificar la primera línea de código usando `sep` y `end` para obtener la siguiente salida:

```
Programming***Essentials***in...Python
```

---

### ✅ Solución

Código utilizado:

```python
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")
```

---

### 🔍 Explicación paso a paso

#### ✔ Uso de `sep`

* `sep` significa **separador**
* Reemplaza el espacio por defecto entre los argumentos

Ejemplo:

```python
print("A", "B", "C", sep="-")
```

Resultado:

```
A-B-C
```

---

#### ✔ Uso de `end`

* `end` define qué se imprime al final
* Por defecto es un salto de línea (`\n`)

Ejemplo:

```python
print("Hola", end="...")
print("Mundo")
```

Resultado:

```
Hola...Mundo
```

---

### 🧪 Resultado final del laboratorio

```
Programming***Essentials***in...Python
```

---

### 🧠 Conclusiones

* `sep` permite cambiar el separador entre datos
* `end` permite controlar cómo termina la impresión
* Se pueden combinar ambos argumentos en una sola función
* `print()` es flexible y configurable


## LAB 3 - Dando formato a la salida

### 🎯 Objetivo

Aprender a dar formato a la salida usando:

* Saltos de línea (`\n`)
* Multiplicación de cadenas
* Uso eficiente de `print()`

---

### 📌 Enunciado

Modificar el código para:

* Reducir el número de `print()`
* Usar `\n`
* Duplicar la figura
* Crear una figura más grande

---

### ✅ Paso 1: Flecha original

Código:

```python
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
```

---

### ✅ Paso 2: Usar `\n` para reducir prints

Código:

```python
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")
```

📌 Explicación:
El `\n` permite hacer saltos de línea dentro de un solo `print()`.

---

### ✅ Paso 3: Duplicar la flecha (vertical)

Código:

```python
print(("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n") * 2)
```

📌 Explicación:
Multiplicar una cadena (`* 2`) repite su contenido.

---

### ✅ Paso 4: Duplicar la flecha (horizontal)

Código:

```python
print("    *    " * 2)
print("   * *   " * 2)
print("  *   *  " * 2)
print(" *     * " * 2)
print("***   ***" * 2)
print("  *   *  " * 2)
print("  *   *  " * 2)
print("  *****  " * 2)
```

📌 Explicación:
Se repite cada línea para mostrar dos figuras lado a lado.

---

### 🧪 Resultado

Se obtiene:

* Una flecha original
* Una flecha duplicada verticalmente
* Dos flechas en paralelo

---

### ⚠️ Pruebas de error realizadas

* Eliminar comillas → `SyntaxError`
* Cambiar `print` por `Print` → `NameError`
* Eliminar paréntesis → `SyntaxError`

---

### 🧠 Conclusiones

* `\n` permite optimizar el código
* Las cadenas se pueden multiplicar
* Python es sensible a mayúsculas y minúsculas
* Los errores ayudan a entender la sintaxis
