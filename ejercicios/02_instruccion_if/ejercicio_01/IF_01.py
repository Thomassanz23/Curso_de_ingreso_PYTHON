import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Thomas
apellido: Sanchez
---
Ejercicio: instrucion_if_01
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener contenido en la caja de texto txt_edad,
transformarlo en número, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años” utilizando el Dialog Alert.
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
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        edad = self.txt_edad.get ()
    
        edad = int(edad)

        if edad == 18:
            title = "Correto"
            respuesta = "Usted tiene 18 años"
            alert(title ,f"{respuesta}")
        else:
            title = "Error"
            respuesta = "No tenes 18 años"
            alert (title , f"{respuesta}")

        #dividendo = 12
        #divisor = self.txt_edad.get()

        #divisor = int(divisor)
        
        """
        OPeradores relacionales
        >mayor
        <menor
        >=mayoe o igual
        <=menor o igual
        ==igual
        !=distinto
        """
        #if divisor != 0:
        #    resultado = dividendo / divisor
        #    
        #    alert("resultado", f"{resultado}")
        #    if divisor == 1:
        #        alert("Burro!!", "No sabes la talba del 1")
        #else:
        #    #alert("Error", "No se puede dividir por cero")
        #    resultado = "No se puede dividir por 0"
        #    title = "Error"

        #if divisor == 0 :
        #    resultado = "No se puede por 0"
        #    title= "Error" 

        
        #alert(title, f"{resultado}")



        pass

        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()