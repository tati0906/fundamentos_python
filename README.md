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

## seccion2

## LAB - Literales de Python (Cadenas)

### 🎯 Objetivo

Aprender a usar:

* Cadenas
* Caracteres de escape (`\`)
* Manejo de comillas dentro de texto

---

### 📌 Enunciado

Crear una línea de código que imprima exactamente:

```text
"Estoy"""aprendiendo"""""Python"""
```

---

### ✅ Solución

Código utilizado:

```python
print("\"Estoy\"\"\"aprendiendo\"\"\"\"\"Python\"\"\"")
```

---

### 🔍 Explicación paso a paso

#### ✔ ¿Por qué usamos `\`?

El carácter `\` (barra invertida) es un **carácter de escape**.

Sirve para indicar que el siguiente carácter **no tiene su significado normal**.

---

#### ✔ Uso de `\"`

```python
\" 
```

Significa:

👉 imprimir una comilla (`"`) sin cerrar la cadena.

---

#### ✔ Construcción de la cadena

Para imprimir:

```text
"Estoy"""aprendiendo"""""Python"""
```

Se hace así:

* Cada comilla interna → `\"`
* Se repiten según la cantidad necesaria

Ejemplo:

```python
\"\"\"   →   """
```

---

### 🧪 Resultado

```text
"Estoy"""aprendiendo"""""Python"""
```

---

### ⚠️ Errores comunes

#### ❌ No usar escape

```python
print(""Estoy"")
```

Error:

```text
SyntaxError
```

📌 Porque Python confunde las comillas de apertura y cierre.

---

### 🧠 Conclusiones

* Las cadenas deben estar correctamente delimitadas
* El carácter `\` permite incluir símbolos especiales
* Python es estricto con las comillas
* Los literales de tipo cadena representan texto directamente

## seccion3

# Ejercicios de Operadores Matemáticos

---

## Ejercicio 1

Expresión:

```python
5 + 3 * 2
```

Resultado: **11**

Explicación:
Primero se multiplica (3 * 2 = 6), luego se suma (5 + 6 = 11).

---

## Ejercicio 2

Expresión:

```python
8 / 2 + 4 * 3
```

Resultado: **16.0**

Explicación:
8 / 2 = 4.0
4 * 3 = 12
4.0 + 12 = 16.0

---

## Ejercicio 3

```python
(7 + 3) * 2 - 5
```

Resultado: **15**

Explicación:
(7 + 3) = 10
10 * 2 = 20
20 - 5 = 15

---

## Ejercicio 4

```python
10 - 4 + 2 * 3
```

Resultado: **12**

Explicación:
2 * 3 = 6
10 - 4 = 6
6 + 6 = 12

---

## Ejercicio 5

```python
(10 / 2) * (3 + 2) - 4
```

Resultado: **21.0**

Explicación:
10 / 2 = 5.0
3 + 2 = 5
5.0 * 5 = 25.0
25.0 - 4 = 21.0

---

## Ejercicio 6

```python
2 + 3 * (4 - 1)
```

Resultado: **11**

Explicación:
4 - 1 = 3
3 * 3 = 9
2 + 9 = 11

---

## Ejercicio 7

```python
5 * 2 ** 3
```

Resultado: **40**

Explicación:
2 ** 3 = 8
5 * 8 = 40

---

## Ejercicio 8

```python
6 + 4 / 2 ** 2
```

Resultado: **7.0**

Explicación:
2 ** 2 = 4
4 / 4 = 1.0
6 + 1.0 = 7.0

---

## Ejercicio 9

```python
10 % 3 + 2 * 5
```

Resultado: **11**

Explicación:
10 % 3 = 1
2 * 5 = 10
1 + 10 = 11

---

## Ejercicio 10

```python
(8 + 2) * 3 ** 2
```

Resultado: **90**

Explicación:
8 + 2 = 10
3 ** 2 = 9
10 * 9 = 90

---

## Ejercicio 11

```python
7 + 2 * (3 + 5) / 4
```

Resultado: **11.0**

Explicación:
3 + 5 = 8
2 * 8 = 16
16 / 4 = 4.0
7 + 4.0 = 11.0

---

## Ejercicio 12

```python
2 ** 3 * 4 / 2
```

Resultado: **16.0**

Explicación:
2 ** 3 = 8
8 * 4 = 32
32 / 2 = 16.0

---

## Ejercicio 13

```python
9 - 6 + 3 ** 2
```

Resultado: **12**

Explicación:
3 ** 2 = 9
9 - 6 = 3
3 + 9 = 12

---

## Ejercicio 14

```python
(7 - 2) * 5 + 3 ** 2
```

Resultado: **34**

Explicación:
7 - 2 = 5
5 * 5 = 25
3 ** 2 = 9
25 + 9 = 34

---

## Ejercicio 15

```python
4 * 2 ** 3 / 8 + 1
```

Resultado: **5.0**

Explicación:
2 ** 3 = 8
4 * 8 = 32
32 / 8 = 4.0
4.0 + 1 = 5.0

---

## 🧠 Conclusiones

* La jerarquía de operadores es fundamental
* Primero paréntesis, luego potencias, multiplicación/división, y por último suma/resta
* La división (`/`) siempre devuelve flotantes
* Python respeta las reglas matemáticas
