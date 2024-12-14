# EJERCICIO 1
# Crea una clase Staff con los atributos role, depty
# salary. Crea una clase Profesor que herede de la
# clase anterior y que además tenga como
# atributos nombre y edad. Haz que sea posible
# instanciar un profesor dándole valor a todos los atributos.

class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

class Profesor(Staff):
    def __init__(self, role, dept, salary, nombre, edad):
        super().__init__(role, dept, salary)
        self.nombre = nombre
        self.edad = edad

    def __repr__(self) -> str:
        return f"Nombre: {self.nombre}, edad: {self.edad}, rol: {self.role}, departamento: {self.dept}, salario: {self.salary}"
    

teacher = Profesor("profesor", "programación", 30000, "Tomás", 65)

print(teacher)       


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 2
# Representa el siguiente diagrama con sus clases
# atributos y métodos correspondientes.
# Cada método display debe imprimr el nombre de
# la clase, atributos y valores de la instancia en ese
# momento. Ejemplo: ln
# displaymethodofParent1x=10

class Parent1:
    def __init__(self, x):
        self.x = x
    
    def display(self):
        print(f"Clase: Parent1, atributo: x --> valor: {self.x}")


class Parent2:
    def __init__(self, y):
        self.y = y
    
    def display(self):
        print(f"Clase: Parent2, atributo: y --> valor: {self.y}")

class Child(Parent1, Parent2):
    def __init__(self, x, y, z):
        Parent1.__init__(self, x)
        Parent2.__init__(self, y)
        self.z = z
    def display(self):
        print(f"Clase: Child, atributo: x --> valor: {self.x}, atributo: y --> valor: {self.y}, atributo: z --> valor: {self.z}")   


child = Child(10, 20, 30)

child.display()


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 3
# Crea una clase llamada Car que herede de la clase Vehicle y que
# sobreescriba los métodos mas_speed() y
# change_gear(). Instancia dos objetos de cada 
# clase y comprueba que la salida de cada método
# es distinta.

class  Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print(f"Details: {self.name}, {self.color}, {self.price}")

    def max_speed(self):
        print('Vehicle max speed is 150')
    
    def change_gear(self):
        print('Vehicle change 6 gear')


class Car(Vehicle):
    def __init__(self, name, color, price):
        super().__init__(name, color, price)
    
    def max_speed(self):
        print("Car max speed is 220")

    def change_gear(self):
        print("Car change 5 gear")


vehicle1 = Vehicle("Opel", "red", 17000)
vehicle2 = Vehicle("Peugot", "white", 22000)

car1 = Car("Honda", "red", 25000)
car2 = Car("Tesla", "black", 70000)

print("--> VEHICLE 1:")
vehicle1.show()
vehicle1.max_speed()
vehicle1.change_gear()

print("--> VEHICLE 2:")
vehicle2.show()
vehicle2.max_speed()
vehicle2.change_gear()

print("--> CAR 1:")
car1.show()
car1.max_speed()
car1.change_gear()

print("--> CAR 2:")
car2.show()
car2.max_speed()
car2.change_gear()


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 1
# Dadas las siguientes clases con el output de sus
# respectivos métodos, crea una interfaz formal
# que las implemente.

from abc import ABC, abstractmethod

class Model (ABC):
    @abstractmethod
    def preprocess_data(self):
        pass

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass


class SMV(Model):
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at SVM")

    def fit(self):
        print("Training at SVM")

    def predict(self):
        print("Evaluating at SVM")


class DecisionTree(Model):
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at DecisionTree")
    
    def fit(self):
        print("Training at DecisionTree")

    def predict(self):
        print("Evaluating at DecisionTree")


smv = SMV()
smv.preprocess_data(data=None, y=None)
smv.fit()
smv.predict()

dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 2
# Repite el ejercicio anterior esta vez creando una
# interfaz informal.

class Model:
    def preprocess_data(self):
        pass

    def fit(self):
        pass

    def predict(self):
        pass


class SMV(Model):
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at SVM")

    def fit(self):
        print("Training at SVM")

    def predict(self):
        print("Evaluating at SVM")


class DecisionTree(Model):
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at DecisionTree")
    
    def fit(self):
        print("Training at DecisionTree")

    def predict(self):
        print("Evaluating at DecisionTree")


smv = SMV()
smv.preprocess_data(data=None, y=None)
smv.fit()
smv.predict()

dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 3
# Crea una clase virtual llamada Algoritmo con los
# atributos nombre, tarea y aprendizaje que sea 
# superclase de la clase BaseClassifier del
# problema anterior. Comprueba con el método
# issubclass que Algoritmo es padre de
# BaseClassifier.

# from abc import ABCMeta

# class Algoritmo(metaclass=ABCMeta):
#     def __init__(self, nombre, tarea, aprendizaje):
#         self.nombre = nombre
#         self.tarea = tarea
#         self.aprendizaje = aprendizaje


# class BaseClassifier:


# print("\nFIN DEL PROGRAMA")

# print("-----------------------\n")


# EJERCICIO 1
# Escribe un script en Python para mostrar los
# distintos formatos de fecha y hora.

from datetime import datetime

    # Fecha y hora actuales

fecha = datetime.now()
print(f"Fecha y hora actuales: {fecha}")
    
    # Año actual

print(f"Año actual: {fecha.year}")

    # Mes del año

print(f"Mes del año: {fecha.month}")

    # Número de la semana del año

print(f"Número de la semana del año: {fecha.strftime('%W')}")

    # Día de la semana

print(f"Día de la semana: {fecha.strftime('%w')}")

    # Día del año

print(f"Día del año: {fecha.strftime('%j')}")

    # Día del mes

print(f"Día del mes: {fecha.day}")



print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 2
# Escribe un programa en Python para convertir
# una cadena a datetime.

from datetime import datetime

cadena = "13/12/2024 20:30:00"

fecha = datetime.strptime(cadena, "%d/%m/%Y %H:%M:%S")

print(fecha)


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 3
# Escribe un programa en Python para obtener la
# hora actual.

from datetime import datetime

print(datetime.now().time())


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 4
# Escribe un programa en Python para restar cinco
# días a la fecha actual.

from datetime import datetime, timedelta

dt = datetime.now() - timedelta(5)

print(dt)


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 5
# Escribe un programa en Python para convertir
# una cadena de marcas de tiempo unix en una
# fecha legible.

from datetime import datetime

unix = 1284105682

print(datetime.fromtimestamp(unix))


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 6
# Escribe un programa en Python para sumar 5
# segundos con la hora actual.

from datetime import datetime, timedelta

dt = datetime.now() + timedelta(0,5)

print(datetime.now())
print(dt)


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 7
# Escribe un programa en Python para obtenr el
# número de la semana.

from datetime import datetime

print(datetime.now().strftime("%W"))


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 8
# Escribe un programa en Python para seleccionar
# todos los domingos de un año derterminado.

from datetime import datetime, timedelta

def domingos(year):
    dt = datetime(year, 1, 1)
    while dt.year == year:
        if dt.weekday() == 6:
            yield dt
        dt += timedelta(1)

for domingo in domingos(2024):
    print(domingo)


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 9
# Escribe un programa en Python para contar el
# número de lunes del primer día del mes desde 
# 2015 hasta 2016.

from datetime import datetime

lunes = 0

for year in range(2015, 2017):
    for month in range(1, 13):
        if datetime(year, month, 1).weekday() == 0:
            lunes += 1

print(lunes)


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 10
# Escribe un programa en Python para crear 12
# fechas fijas a partir de una fecha especificada en 
# un periodo determinado. La diferencia entre dos
# fechas será de 20.

from datetime import datetime, timedelta

dt = datetime(2024, 1, 1)

print(f"Fecha inicial: {dt}")

for day in range(1, 13):
    print(dt + timedelta(day * 20))
  

print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 1
# Implementa una función generadora que dadas
# dos listas del mismo tamaño, devuelva la
# multiplicación entre los elementos de cada una,
# el primer elemento de la lista 1 por el primero de
# la lista 2, el segundo con el segundo y así
# sucesivamente. Sigue la siguiente estructura:

def prod(l1, l2):
    try:
        for i in range(len(l1)):
            yield l1[i] * l2[i]
    except StopIteration:
        pass
    return "solution"

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

print(list(prod(list1, list2)))


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 2
# Implements un generador, que dado un entorno n,
# genere n números aleatorios. Puedes usar el
# método random de la libreria random para
# generar números aleatorios.

from random import random

def random_numbers(n):
    for i in range(n):
        yield int(random() *100)

for number in random_numbers(10):
    print(number)


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 3
# Implementa un generador de Fibonacci que
# genere n números de la secuencia de Fibonacci,
# que tiene la forma:
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# Cuyos dos primeros valores son 0 y 1 por
# definición y el resto se calculan sumando los dos
# últimos valores de la suceción.

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for number in fibonacci(15):
    print(number)


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 4
# Implementa un generador, que dado un entero n,
# imprima todos los números inferiores a n
# multiplicados por dos.

def multiplicador(n):
    for i in range(n):
        yield i * 2

for i, number in enumerate(multiplicador(7)): 
    print(f"{i} * 2 = {number}")


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 5
# Implementa un generador, que dado un entero n,
# genere n números impares

def impares(n):
    numero = 1
    for i in range(n):
        yield numero
        numero += 2

for impar in impares(15):
    print(impar)


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 1
# Crea una función que genere una excepción e
# imprima su tipo, los argumentos de la excepción
# y su mensaje de error.

def exception():
    try:
        operacion = 10 / 0
    except Exception as e:
        print(type(e))
        print(e.args)
        print(e)

exception()


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")

#DESDE AQUI
# EJERCICIO 2
# Crea una función que compute la diferencia
# entre dos enteros. En caso de que la diferencia
# sea negativa genera una excepción inventada
# por ti que informe sobre ello. Por ejemplo: la
# excepción podría llamarse NegativeDifferenceException.

class NegativeDifferenceException(Exception):
    def __init__(self, message="La diferencia es negativa"):
        self.message = message
        super().__init__(self.message)

def diferencia(a, b):
    if a - b < 0:
        raise NegativeDifferenceException("Diferencia negativa")
    return a - b

try:
    print(diferencia(10, 20))
except NegativeDifferenceException as e:
    print(e)


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 3
# Crea una funcicón que calcule la división entre
# dos números. Debe imprimir el mensaje 'Los
# parámetros deben ser números enteros' cuando
# se genera una excepción de tipo y 'El divisor no
# puede ser 0' cuando se genera un
# zerodivisionerror.

def division(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Los parámetros deben ser números enteros")
    if b == 0:
        raise ZeroDivisionError("El divisor no puede ser 0")
    return a / b

try:
    print(division(10, 0.1))
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")


# EJERCICIO 4
# Añade a la función anterior un mensaje que se
# imprima al final de la ejecución de la función
# indepentientemente de si se ha generado
# excepción o no.

def division(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Los parámetros deben ser números enteros")
    if b == 0:
        raise ZeroDivisionError("El divisor no puede ser 0")
    return a / b

try:
    print(division(10, 0))
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

finally:
    print("Fin de la ejecución")


print("\nFIN DEL PROGRAMA")

print("-----------------------\n")