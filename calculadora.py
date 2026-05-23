import tkinter as tk #Acceso al modulo de la interfaz
from tkinter import * # Importa todas las clases y funciones que tiene la libreria

#Venatana principal
ventana = tk.Tk()
ventana.title("Calculadora basica") #Nombre a la ventana
ventana.geometry("450x250") # tamaño ancho x alto

#Funciones

def sumar():
    # .get() obtiene el valor e int () lo convierte a entero para la suma
    resultado_numerico = int(numero1.get()) + int(numero2.get())
    lbl_res.config(text = resultado_numerico)
    
def restar():
    # .get() obtiene el valor e int () lo convierte a entero para la suma
    resultado_numerico = int(numero1.get()) - int(numero2.get())
    lbl_res.config(text = resultado_numerico)  

def multiplicar():
        # .get() obtiene el valor e int () lo convierte a entero para la suma
    resultado_numerico = int(numero1.get()) * int(numero2.get())
    lbl_res.config(text = resultado_numerico)

def dividir():
        # .get() obtiene el valor e int () lo convierte a entero para la suma
    resultado_numerico = int(numero1.get()) / int(numero2.get())
    lbl_res.config(text = resultado_numerico)

#Variables
numero1 = tk.IntVar()
numero2 = tk.IntVar()

# INTERFAZ:
#Titulo
tk.Label(ventana, text = "Operaciones basicas", font = ("Arial",15)).place(x=120, y=20)