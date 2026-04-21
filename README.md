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
