import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_numero_pares = 0
        numero_pedido = prompt("Ingrese un numero", "Número")
        while numero_pedido==None or not numero_pedido.isdigit():
            numero_pedido = prompt("Ingresar un numero", "Número")
        
        numero_pedido = int(numero_pedido)

        rango_a_recorrer = range(1, numero_pedido + 1)

        for numero in rango_a_recorrer:

            if numero % 2 == 0:
                contador_numero_pares +=1
                print(numero)
        
        alert ("Numero pares", f"Se encontraton {contador_numero_pares} números pares.")

        pass
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()