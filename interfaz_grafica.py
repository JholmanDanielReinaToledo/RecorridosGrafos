import tkinter
from tkinter import messagebox
from general import validar_puzzle

class interfaz_grafica_class:

    root = tkinter.Tk()

    def __init__(self):
        self.crear_ventana()
        self.botones()
        self.crear_campos_nodo_inicial()
        self.crear_campos_nodo_final()
        self.root.mainloop()

    def crear_ventana(self):
        self.root.title("Algoritmos de busqueda")
        self.root.configure(width=1000, height=800)

    def botones(self):
        self.iniciar_boton = tkinter.Button(self.root, command=self.ejecutar_bpp, text="BPP", width=30, height=3)
        self.iniciar_boton.place(x=20, y=20)

        self.iniciar_boton = tkinter.Button(self.root, command=self.ejecutar_bpa, text="BPA", width=30, height=3)
        self.iniciar_boton.place(x=20, y=80)

        self.iniciar_boton = tkinter.Button(self.root, command=self.ejecutar_ascenso_de_colina, text="Ascenso de colina", width=30, height=3)
        self.iniciar_boton.place(x=20, y=140)

        self.iniciar_boton = tkinter.Button(self.root, command=self.ejecutar_ramificacion_acotamiento, text="Ramificación y acotamiento", width=30, height=3)
        self.iniciar_boton.place(x=20, y=200)

        self.iniciar_boton = tkinter.Button(self.root, command=self.ejecutar_a, text="A*", width=30, height=3)
        self.iniciar_boton.place(x=20, y=260)

    def crear_campos_nodo_inicial(self):
        tkinter.Label(self.root, text='Nodo inicial').place(x=310, y=0)
        self.primera_posicion_inicial = tkinter.Entry(self.root, width=4)
        self.primera_posicion_inicial.place(x=300, y=20, height=30)

        self.cuarta_posicion_inicial = tkinter.Entry(self.root, width=4)
        self.cuarta_posicion_inicial.place(x=300, y=60, height=30)

        self.septima_posicion_inicial = tkinter.Entry(self.root, width=4)
        self.septima_posicion_inicial.place(x=300, y=100, height=30)

        self.segunda_posicion_inicial = tkinter.Entry(self.root, width=4)
        self.segunda_posicion_inicial.place(x=330, y=20, height=30)

        self.quinta_posicion_inicial = tkinter.Entry(self.root, width=4)
        self.quinta_posicion_inicial.place(x=330, y=60, height=30)

        self.octava_posicion_inicial = tkinter.Entry(self.root, width=4)
        self.octava_posicion_inicial.place(x=330, y=100, height=30)

        self.tercera_posicion_inicial = tkinter.Entry(self.root, width=4)
        self.tercera_posicion_inicial.place(x=360, y=20, height=30)

        self.sexta_posicion_inicial = tkinter.Entry(self.root, width=4)
        self.sexta_posicion_inicial.place(x=360, y=60, height=30)

        self.novena_posicion_inicial = tkinter.Entry(self.root, width=4)
        self.novena_posicion_inicial.place(x=360, y=100, height=30)

    def crear_campos_nodo_final(self):
        tkinter.Label(self.root, text='Nodo final').place(x=460, y=0)

        self.primera_posicion_final = tkinter.Entry(self.root, width=4)
        self.primera_posicion_final.place(x=450, y=20, height=30)

        self.cuarta_posicion_final = tkinter.Entry(self.root, width=4)
        self.cuarta_posicion_final.place(x=450, y=60, height=30)

        self.septima_posicion_final = tkinter.Entry(self.root, width=4)
        self.septima_posicion_final.place(x=450, y=100, height=30)

        self.segunda_posicion_final = tkinter.Entry(self.root, width=4)
        self.segunda_posicion_final.place(x=480, y=20, height=30)

        self.quinta_posicion_final = tkinter.Entry(self.root, width=4)
        self.quinta_posicion_final.place(x=480, y=60, height=30)

        self.octava_posicion_final = tkinter.Entry(self.root, width=4)
        self.octava_posicion_final.place(x=480, y=100, height=30)

        self.tercera_posicion_final = tkinter.Entry(self.root, width=4)
        self.tercera_posicion_final.place(x=510, y=20, height=30)

        self.sexta_posicion_final = tkinter.Entry(self.root, width=4)
        self.sexta_posicion_final.place(x=510, y=60, height=30)

        self.novena_posicion_final = tkinter.Entry(self.root, width=4)
        self.novena_posicion_final.place(x=510, y=100, height=30)


    def obtener_nodo_inicial(self):
        primero_inicial = self.primera_posicion_inicial.get()
        segundo_inicial = self.segunda_posicion_inicial.get()
        tercero_inicial = self.tercera_posicion_inicial.get()
        cuarto_inicial = self.cuarta_posicion_inicial.get()
        quinta_inicial = self.quinta_posicion_inicial.get()
        sexta_inicial = self.sexta_posicion_inicial.get()
        septima_inicial = self.septima_posicion_inicial.get()
        octava_inicial = self.octava_posicion_inicial.get()
        novena_inicial = self.novena_posicion_inicial.get()

        try:
            primero_inicial = int(primero_inicial)
            segundo_inicial = int(segundo_inicial)
            tercero_inicial = int(tercero_inicial)
            cuarto_inicial = int(cuarto_inicial)
            quinta_inicial = int(quinta_inicial)
            sexta_inicial = int(sexta_inicial)
            septima_inicial = int(septima_inicial)
            octava_inicial = int(octava_inicial)
            novena_inicial = int(novena_inicial)

            return [primero_inicial, segundo_inicial, tercero_inicial, cuarto_inicial, quinta_inicial, sexta_inicial, septima_inicial, octava_inicial, novena_inicial]
        except:
            return False

    def obtener_nodo_final(self):
        primero_final = self.primera_posicion_final.get()
        segundo_final = self.segunda_posicion_final.get()
        tercero_final = self.tercera_posicion_final.get()
        cuarto_final = self.cuarta_posicion_final.get()
        quinta_final = self.quinta_posicion_final.get()
        sexta_final = self.sexta_posicion_final.get()
        septima_final = self.septima_posicion_final.get()
        octava_final = self.octava_posicion_final.get()
        novena_final = self.novena_posicion_final.get()

        try:
            primero_final = int(primero_final)
            segundo_final = int(segundo_final)
            tercero_final = int(tercero_final)
            cuarto_final = int(cuarto_final)
            quinta_final = int(quinta_final)
            sexta_final = int(sexta_final)
            septima_final = int(septima_final)
            octava_final = int(octava_final)
            novena_final = int(novena_final)

            return [primero_final,segundo_final,tercero_final,cuarto_final,quinta_final,sexta_final,septima_final,octava_final,novena_final]
        except:
            return False

    def ejecutar_bpp(self):
        nodo_inicial = self.obtener_nodo_inicial()
        nodo_final = self.obtener_nodo_final()

        if nodo_inicial and nodo_final:
            es_valido_inicial = validar_puzzle(nodo_inicial)
            es_valido_final = validar_puzzle(nodo_final)
            if es_valido_inicial and es_valido_final:
                pass
                #mandar a ejecutar el algoritmo
            elif not es_valido_inicial:
                messagebox.showerror(title="Error", message="El nodo inicial no es valido")
            elif not es_valido_final:
                messagebox.showerror(title="Error", message="El nodo final no es valido")
        else:
            if not nodo_inicial:
                messagebox.showerror(title="Error", message="El nodo inicial no es valido")
            if not nodo_final:
                messagebox.showerror(title="Error", message="El nodo final no es valido")

    def ejecutar_bpa(self):
        print("BPA")

    def ejecutar_ascenso_de_colina(self):
        print("Ascenso de colina")

    def ejecutar_ramificacion_acotamiento(self):
        print("Ramificación y acotamiento")

    def ejecutar_a(self):
        print("A")
