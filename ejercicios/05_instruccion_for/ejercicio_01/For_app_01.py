import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        for numero in range (1,6):
            alert("EJ1" , f"{numero}")

        """
        for numero in range (5):
            alert("EJ1" , f"{numero + 1}")
        
        """
        
        
       
            
       # numero = 0

        #while numero < 6 :
        #    alert("datos", f"{numero}")
        #    numero = numero + 1

        #listas_numeros = list (range (1,6))
        #listas_nombre = ["nombre1","nombre2","nombre3"]
        #random.shuffle(listas_nombre)

        #for nombre in listas_nombre:
            #print(nombre) 

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()