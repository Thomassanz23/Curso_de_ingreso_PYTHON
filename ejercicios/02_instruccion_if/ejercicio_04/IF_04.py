import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Thomas
apellido: Sanchez
---
Ejercicio: instrucion_if_04
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, 
transformarlo en número y calcular si es adolescente (edad entre 13 y 17 años). Se deberá informar utilizando el Dialog alert.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        """
        Operadores Logicos
        and
        or
        not
        """
        """
        A  B  AND  OR
        v  v   v   v
        v  f   f   v
        f  v   f   v
        f  f   f   f
        """

        txt_mensaje = None
        edad =self.txt_edad.get()
        edad = int(edad)

        if 13 <= edad  <=17:
            mensaje = "Es adolescente"
        else:
            mensaje = "No es adolescente"
        
        alert ("Resultado", mensaje)




        # ESTE EJEMPLO QUE NOS DIO EL PROFESOR.
        
        """
        edad > 12 =>            12>>>>>>>>>>>>>>>>>>>>>>>>>>>Infinito
        edad < 18 => -INfinito <<<<<<<<<<<<<<<<<<<<< 18
        """
        """
        if edad > 12 and edad < 18:
            txt_mensaje = " Es adolescente"
        else: 
            txt_mensaje = "no es adolescente"
        
        if edad >12 :
            if edad <18:
                txt_mensaje = "Es adolescente"
            else :
                txt_mensaje = "No es adolescente"
        else:
            txt_mensaje = "NO es adolescente"
        alert("Edad", txt_mensaje)   
        """

        """
            if edad < 18:
                txt_mensaje = "Es adolescente"
            else: #edad mayor o igual a 18  
                if edad >65:
                    txt_mensaje = "Es jubilado"
                else: #edad menor o igual 65
                    txt_mensaje= "Es adulto"
                if edad > 100:
                   txt_mensaje = "Es centenario"
                else:
                    txt_mensaje = "Es jubilado"
        else: #edad menor  a 13
            txt_mensaje= "Es niño"
        """
            




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
