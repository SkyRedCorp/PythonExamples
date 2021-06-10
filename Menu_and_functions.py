# Ejemplo de menu de opciones y funciones en Python

#Declaracion de librerias (math para numero Pi)
from math import pi

#(time para temporizador) (sys para salir de programa)
import time, sys

#Definicion de funciones
def area_circulo(r):
    y = pi * r ** 2
    return y

def area_rect(b, a):
    y = b * a
    return y

def area_triangle(b, a):
    y = b * a / 2
    return y

def area_quad(l):
    y = l ** 2
    return y


#Funcion usada para seleccion de menu
def await_for():
    i = (input("Ingrese opcion: "))
    return i

#Funcion de Menu
def function_menu(selec):
    
    #Cuando variable "selec" coincida con la opcion, ejecutara una de
    #las funciones deseadas
    if selec == "1":
        val = float(input("Radio de circulo: "))
        print ("area de circulo: " + str(area_circulo(val)))
            
    if selec == "2":
        val = float(input("base de rectangulo: "))
        val2 = float(input("altura de rectangulo: "))
        print ("area de rectangulo: " + str(area_rect(val, val2)))
    
    if selec == "3":
        val = float(input("base de triangulo: "))
        val2 = float(input("altura de triangulo: "))
        print ("area de triangulo: " + str(area_triangle(val, val2)))
    
    if selec == "4":
        val = float(input("lado de cuadrado: "))
        print ("area de cuadrado: " + str(area_quad(val)))
    
    if selec == "0":
        sys.exit()
        
while True:
    print("seleccione la funcion a calcular: ")
    print("1 = Area de circulo")
    print("2 = Area de rectangulo")
    print("3 = Area de triangulo")
    print("4 = Area de cuadrado")
    print("0 = Salir de Script")

    iput = await_for()

    function_menu(iput)
    time.sleep(5)
    


    