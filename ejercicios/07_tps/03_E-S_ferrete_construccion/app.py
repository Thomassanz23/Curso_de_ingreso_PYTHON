import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (F)Poste Quebracho Fino de 2.2 mts
    (V)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        largo = self.txt_largo.get()
        ancho = self.txt_ancho.get ()

        largo = float(largo)
        ancho = float(ancho)

        metros_cuadrados = ancho * largo
        metros_lineales = 2 * largo + 2 * ancho



        #A
        resultado =f"Metros cuadrados del terreno : {metros_cuadrados}\n"
        resultado +=f"Metros lineales del perimetro: {metros_lineales}\n"

        #B
        cantidad_postes_grueso = metros_lineales // 250 + 4
        resultado += f"Cantidad de postes de quebracho Gueso de 2.4 mts : {cantidad_postes_grueso}\n"

        #C
        cantidad_postes_fino=metros_lineales // 12 - cantidad_postes_grueso
        resultado += f"Cantidad de postes de quebracho Fino de 2.2 mts: {cantidad_postes_fino}\n"

        #D
        cantidad_varillas = metros_lineales // 2
        resultado += f"Cantidad de varillas : {cantidad_varillas}\n"

        #E
        cantidad_alambre = metros_lineales * 7
        resultado += f"Cantidad de alambre alta resistencia 17/15 : {cantidad_alambre}\n"

        alert(title="Resultado", message=resultado)


        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
