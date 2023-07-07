import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Thomas
apellido: Sanchez
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
<<<<<<< HEAD:ejercicios/01_entrada_salida/ejercicio_01/app.py
        alert(title="EJ 01" , message="Esto no anda, fuciona")    
        
=======
        pass

>>>>>>> 1f442cc264dd3330454d5b18f58c36600d1c9652:ejercicios/01_entrada_salida/ejercicio_01/app_ES_01.py

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
