import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón  'Mostrar', se deberán mostrar los números 
almacenados en el vector lista_datos utilizando Dialog Alert para informar cada elemento.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]


    def btn_mostrar_on_click(self):
        """
        lista =  [1, 2.2, "3", [4], range(5), None , True]

        cantidad_de_elementos =len(lista)
        print(f"Cantidad de elementos: {cantidad_de_elementos}")
        print (type(lista))

        lista_de_enteros = list(range(10))

        for item in lista:
            print("=================")
            print(item, type(item))
        
        for i in lista_de_enteros:
            print(i)
        """
        lista = self.lista_datos
        for i in lista:
            print(i)
            
            alert ("EJ1",f"Lista de numero:{i}")

        
        
        pass
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()