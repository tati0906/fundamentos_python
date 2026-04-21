## LABORATORIOS DE PYTHON

# Sección 1 – Función print()

## LAB 1: Trabajando con print()

Se utilizó la función print() para mostrar mensajes en pantalla.

Qué hace el código:
Imprime "¡Hola, Mundo!"
Imprime el nombre del usuario
Se probaron errores comunes

Conclusiones:
Sin comillas → error de sintaxis (SyntaxError)
Sin paréntesis → error porque print es una función
Se pueden usar comillas simples o dobles
Se pueden usar varios print() en una misma línea

## LAB 2: Argumentos de print()

Uso de argumentos sep y end para modificar la salida.

Qué hace el código:
sep="***" separa palabras con ***
end="..." evita salto de línea y agrega ...

Resultado:
Programming***Essentials***in...Python

## LAB 3: Formato de salida

Se trabajó con saltos de línea (\n) y repetición de cadenas.

Qué hace el código:
Dibuja una figura (flecha) con print()
Usa \n para evitar múltiples prints
Duplica figuras vertical y horizontalmente

Conclusiones:
\n permite controlar saltos de línea
Se pueden multiplicar cadenas (* 2)
Python es sensible a mayúsculas (print ≠ Print)

# Sección 2 – Cadenas

## LAB: Literales de Python

Uso de caracteres de escape en cadenas.

Qué hace el código:
Usa \" para imprimir comillas dentro del texto

Resultado:
"Estoy"""aprendiendo"""""Python"""

Conclusión:
Los caracteres de escape permiten mostrar símbolos especiales

# Sección 3 – Operadores

## Ejercicios de operadores

Se resolvieron expresiones matemáticas aplicando prioridad de operadores.

Regla clave:

Paréntesis
Potencias
Multiplicación y división
Suma y resta

Ejercicios resueltos

Regla general:
Python sigue la jerarquía de operaciones:

Paréntesis
Potencias **
Multiplicación, división, módulo * / %
Suma y resta + -

Ejercicio 1:
Expresión: 5 + 3 * 2
Resultado: 11
Explicación: Primero 3*2=6, luego 5+6=11.

Ejercicio 2:
Expresión: 8 / 2 + 4 * 3
Resultado: 16.0
Explicación: 8/2=4 y 4*3=12, luego 4+12=16.

Ejercicio 3:
Expresión: (7 + 3) * 2 - 5
Resultado: 15
Explicación: (7+3)=10, 10*2=20, 20-5=15.

Ejercicio 4:
Expresión: 10 - 4 + 2 * 3
Resultado: 12
Explicación: 2*3=6, luego 10-4+6=12.

Ejercicio 5:
Expresión: (10 / 2) * (3 + 2) - 4
Resultado: 21.0
Explicación: 10/2=5, (3+2)=5, 5*5=25, 25-4=21.

Ejercicio 6:
Expresión: 2 + 3 * (4 - 1)
Resultado: 11
Explicación: (4-1)=3, 3*3=9, 2+9=11.

Ejercicio 7:
Expresión: 5 * 2 ** 3
Resultado: 40
Explicación: 2³=8, 5*8=40.

Ejercicio 8:
Expresión: 6 + 4 / 2 ** 2
Resultado: 7.0
Explicación: 2²=4, 4/4=1, 6+1=7.

Ejercicio 9:
Expresión: 10 % 3 + 2 * 5
Resultado: 11
Explicación: 10%3=1, 2*5=10, 1+10=11.

Ejercicio 10:
Expresión: (8 + 2) * 3 ** 2
Resultado: 90
Explicación: (8+2)=10, 3²=9, 10*9=90.

Ejercicio 11:
Expresión: 7 + 2 * (3 + 5) / 4
Resultado: 11.0
Explicación: (3+5)=8, 2*8=16, 16/4=4, 7+4=11.

Ejercicio 12:
Expresión: 2 ** 3 * 4 / 2
Resultado: 16.0
Explicación: 2³=8, 8*4=32, 32/2=16.

Ejercicio 13:
Expresión: 9 - 6 + 3 ** 2
Resultado: 12
Explicación: 3²=9, 9-6+9=12.

Ejercicio 14:
Expresión: (7 - 2) * 5 + 3 ** 2
Resultado: 34
Explicación: (7-2)=5, 5*5=25, 3²=9, 25+9=34.

Ejercicio 15:
Expresión: 4 * 2 ** 3 / 8 + 1
Resultado: 5.0
Explicación: 2³=8, 4*8=32, 32/8=4, 4+1=5.

# Sección 4 – Variables

## LAB: Convertidor de unidades

Conversión entre millas y kilómetros.

Qué hace el código:
Usa variables para almacenar valores
Realiza conversiones matemáticas
Usa round() para redondear

Fórmulas:
Millas → km: millas * 1.61
Km → millas: km / 1.61

Conclusión:
round() permite controlar decimales
print() puede combinar texto y variables

## LAB: Expresiones algebraicas

Evaluación de una expresión matemática.

Expresión:
3x³ - 2x² + 3x - 1

Qué hace el código:
Convierte x a tipo float
Calcula el resultado usando operadores

Conclusión:
En Python se debe escribir la multiplicación explícitamente (*)
Se usan potencias con **

## LAB: Algoritmos básicos

Se desarrollaron algoritmos usando entradas del usuario (input()).

Qué hace el código:
Calcula valores como:
Puntaje total
Tiempo en segundos
Daño total

Ejemplo:
total = nivel1 + nivel2 + nivel3

Conclusión:
input() permite interacción con el usuario
Se deben convertir datos (int) para operar
Los algoritmos siguen estructura: entrada → proceso → salida