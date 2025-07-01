#1
print("Ejercicio 1: Mayor de edad")

edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
    
 #2   
print("Ejercicio 2: Par o impar")

numero = int(input("Dime un número: "))

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")
    
#3
print("Ejercicio 3: Comparar dos números")

num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))

if num1 > num2:
    print("El primero es mayor")
elif num2 > num1:
    print("El segundo es mayor")
else:
    print("Son iguales")
    
    #4
print("Ejercicio 4: Año bisiesto")

año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")
    
    #5
print("Ejercicio 5: Calcular descuento")
    
precio = float(input("Precio del producto: "))
descuento = float(input("Porcentaje de descuento: "))

precio_final = precio - (precio * (descuento / 100))
print(f"Precio con descuento:", precio_final)

#6
print("Ejercicio 6: Operaciones básicas")

a = int(input("Primer número: "))
b = int(input("Segundo número: "))

suma= a+b
resta=a-b
multiplicacion=a*b
division=a/b

print(f"resultados")
print(f"suma:{suma}")
print(f"resta:{resta}")
print(f"multiplicacion:{multiplicacion}")
print(f"division:{division}")

#7
print("Ejercicio 7: Número en rango")

numero = float(input("Ingresa un número: "))

if numero >= 10 and numero <= 50:
    print("Está en el rango")
else:
    print("No está en el rango")
    
#8
print("Ejercicio 8: Información del usuario")

nombre = input("Tu nombre: ")
edad = input("Tu edad: ")
ciudad = input("Tu ciudad: ")

print(f"Nombre:{nombre}")
print(f"Edad:{edad}")
print(f"Ciudad:{ciudad}")

#9
print("Ejercicio 9: Suma de dos números")

a = int(input("Primer número: "))
b = int(input("Segundo número: "))

suma = a + b
print(f"La suma es:{suma}")

#10
print("Ejercicio 10: Comparación de dos números con operadores lógico")

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

if num1 > 10 and num2 > 10:
    print(True)
else:
    print(False)

#11
print("ejercicio 11: Comparación de tres números con operadores lógicos")

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

if a > b and b > c:
    print(True)
else:
    print(False)
    
#12
print("Ejercicio 12: Operadores lógicos (and, or, not)")

a = True
b = False

print("a AND b:", a and b)
print("a OR b:", a or b)
print("NOT a:", not a)

#13
print("Ejercicio 13: Combinación de operadores lógicos y relacionales")

num = int(input("Ingresa un número: "))

if num % 2 == 0 and num >= 20 and num <= 50:
    print(True)
else:
    print(False)
    
    
#14
print("Ejercicio 14: Calificación por nota")

nota = int(input("Ingresa tu nota (0-100): "))

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
    
#15
print("Ejercicio 15: Determinar si un número es positivo, negativo o cero")

num = int(input("Ingresa un número: "))

if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Cero")



