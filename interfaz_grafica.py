import tkinter


class interfaz_grafica_class:

    root = tkinter.Tk()

    def __init__(self):
        self.crear_ventana()
        self.botones()
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

    def ejecutar_bpp(self):
        print("No son iguales")

    def ejecutar_bpa(self):
        print("BPA")

    def ejecutar_ascenso_de_colina(self):
        print("Ascenso de colina")

    def ejecutar_ramificacion_acotamiento(self):
        print("Ramificación y acotamiento")

    def ejecutar_a(self):
        print("A")
