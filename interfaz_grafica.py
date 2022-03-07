import tkinter
from tkinter import messagebox
from general import validar_puzzle
from BPA import algoritmo_BPA
from BPP import algoritmo_BPP
from ascenso_colina import algoritmo_ascenso_colina
from ramificacion_acotamiento import algoritmo_ramificacion_acotamiento

class interfaz_grafica_class:

    root = tkinter.Tk()

    def __init__(self):
        self.crear_ventana()
        self.botones()
        self.crear_campos_area_texto()
        self.crear_campos_nodo_inicial()
        self.crear_campos_nodo_final()
        self.crear_campos_adicionales()
        self.root.mainloop()

    def crear_ventana(self):
        self.root.title("Algoritmos de busqueda")
        self.root.configure(width=1000, height=800)

    def crear_campos_adicionales(self):
        tkinter.Label(self.root, text='Nivel de profundidad para BPA').place(x=300, y=180)

        self.nivel_maximo = tkinter.Entry(self.root, width=4)
        self.nivel_maximo.place(x=300, y=200, height=30)

    def crear_campos_area_texto(self):
        tkinter.Label(self.root, text='Reglas aplicadas').place(x=20, y=380)
        self.text_area_reglas = tkinter.Text(self.root, height=20, width=50)
        self.text_area_reglas.place(x=20, y=400)

        tkinter.Label(self.root, text='Nodos generados').place(x=700, y=20)
        self.text_area_nodos = tkinter.Text(self.root, height=40, width=25)
        self.text_area_nodos.place(x=700, y=40)

        tkinter.Label(self.root, text='Número de nodos generados').place(x=700, y=740)
        self.text_area_nodos_num = tkinter.Text(self.root, height=1, width=25)
        self.text_area_nodos_num.place(x=700, y=760)

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

    def obtener_nivel(self):
        max = self.nivel_maximo.get()

        try:
            max = int(max)
            if max > 0:
                return max
            else:
                return False
        except:
            return False

    def ejecutar_bpa(self):
        nodo_inicial = self.obtener_nodo_inicial()
        nodo_final = self.obtener_nodo_final()

        if nodo_inicial and nodo_final:
            es_valido_inicial = validar_puzzle(nodo_inicial)
            es_valido_final = validar_puzzle(nodo_final)
            if es_valido_inicial and es_valido_final:
                clase = algoritmo_BPA(nodo_inicial, nodo_final)
                reglas_aplicadas, nodos_generados, num_nodos_gen = clase.iniciar()
                reglas = reglas_aplicadas[::-1]
                texto = ""
                primero = False
                for i in reglas:
                    if primero:
                        texto = texto + i + "\n"
                    primero = True
                self.text_area_reglas.delete('1.0', tkinter.END)
                self.text_area_reglas.insert(tkinter.END, texto)
                self.text_area_nodos.delete('1.0', tkinter.END)
                self.text_area_nodos.insert(tkinter.END, nodos_generados)
                self.text_area_nodos_num.delete('1.0', tkinter.END)
                self.text_area_nodos_num.insert(tkinter.END, str(num_nodos_gen))

            elif not es_valido_inicial:
                messagebox.showerror(title="Error", message="El nodo inicial no es valido")
            elif not es_valido_final:
                messagebox.showerror(title="Error", message="El nodo final no es valido")
        else:
            if not nodo_inicial:
                messagebox.showerror(title="Error", message="El nodo inicial no es valido")
            if not nodo_final:
                messagebox.showerror(title="Error", message="El nodo final no es valido")

    def ejecutar_bpp(self):
        nodo_inicial = self.obtener_nodo_inicial()
        nodo_final = self.obtener_nodo_final()
        nivel_maximo = self.obtener_nivel()

        if nivel_maximo:
            if nodo_inicial and nodo_final:
                es_valido_inicial = validar_puzzle(nodo_inicial)
                es_valido_final = validar_puzzle(nodo_final)
                if es_valido_inicial and es_valido_final:
                    clase = algoritmo_BPP(nodo_inicial, nodo_final, nivel_maximo)
                    reglas_aplicadas, nodos_generados, num_nodos_gen = clase.iniciar()
                    if reglas_aplicadas and nodos_generados and num_nodos_gen:

                        reglas = reglas_aplicadas[::-1]
                        texto = ""
                        primero = False
                        for i in reglas:
                            if primero:
                                texto = texto + i + "\n"
                            primero = True
                        self.text_area_reglas.delete('1.0', tkinter.END)
                        self.text_area_reglas.insert(tkinter.END, texto)
                        self.text_area_nodos.delete('1.0', tkinter.END)
                        self.text_area_nodos.insert(tkinter.END, nodos_generados)
                        self.text_area_nodos_num.delete('1.0', tkinter.END)
                        self.text_area_nodos_num.insert(tkinter.END, str(num_nodos_gen))
                    else:
                        messagebox.showerror(title="Error", message="Con el nivel maximo no fue posible encontrar una solución")

                elif not es_valido_inicial:
                    messagebox.showerror(title="Error", message="El nodo inicial no es valido")
                elif not es_valido_final:
                    messagebox.showerror(title="Error", message="El nodo final no es valido")
            else:
                if not nodo_inicial:
                    messagebox.showerror(title="Error", message="El nodo inicial no es valido")
                if not nodo_final:
                    messagebox.showerror(title="Error", message="El nodo final no es valido")
        else:
            messagebox.showerror(title="Error", message="Nivel maximo no valido")

    def ejecutar_ascenso_de_colina(self):
        nodo_inicial = self.obtener_nodo_inicial()
        nodo_final = self.obtener_nodo_final()

        if nodo_inicial and nodo_final:
            es_valido_inicial = validar_puzzle(nodo_inicial)
            es_valido_final = validar_puzzle(nodo_final)
            if es_valido_inicial and es_valido_final:
                clase = algoritmo_ascenso_colina(nodo_inicial, nodo_final)
                reglas_aplicadas, nodos_generados, num_nodos_gen = clase.iniciar()
                reglas = reglas_aplicadas[::-1]
                texto = ""
                primero = False
                for i in reglas:
                    if primero:
                        texto = texto + i + "\n"
                    primero = True
                self.text_area_reglas.delete('1.0', tkinter.END)
                self.text_area_reglas.insert(tkinter.END, texto)
                self.text_area_nodos.delete('1.0', tkinter.END)
                self.text_area_nodos.insert(tkinter.END, nodos_generados)
                self.text_area_nodos_num.delete('1.0', tkinter.END)
                self.text_area_nodos_num.insert(tkinter.END, str(num_nodos_gen))

            elif not es_valido_inicial:
                messagebox.showerror(title="Error", message="El nodo inicial no es valido")
            elif not es_valido_final:
                messagebox.showerror(title="Error", message="El nodo final no es valido")
        else:
            if not nodo_inicial:
                messagebox.showerror(title="Error", message="El nodo inicial no es valido")
            if not nodo_final:
                messagebox.showerror(title="Error", message="El nodo final no es valido")

    def ejecutar_ramificacion_acotamiento(self):
        nodo_inicial = self.obtener_nodo_inicial()
        nodo_final = self.obtener_nodo_final()

        if nodo_inicial and nodo_final:
            es_valido_inicial = validar_puzzle(nodo_inicial)
            es_valido_final = validar_puzzle(nodo_final)
            if es_valido_inicial and es_valido_final:
                clase = algoritmo_ramificacion_acotamiento(nodo_inicial, nodo_final)
                reglas_aplicadas, nodos_generados, num_nodos_gen = clase.iniciar()
                reglas = reglas_aplicadas[::-1]
                texto = ""
                primero = False
                for i in reglas:
                    if primero:
                        texto = texto + i + "\n"
                    primero = True
                self.text_area_reglas.delete('1.0', tkinter.END)
                self.text_area_reglas.insert(tkinter.END, texto)
                self.text_area_nodos.delete('1.0', tkinter.END)
                self.text_area_nodos.insert(tkinter.END, nodos_generados)
                self.text_area_nodos_num.delete('1.0', tkinter.END)
                self.text_area_nodos_num.insert(tkinter.END, str(num_nodos_gen))

            elif not es_valido_inicial:
                messagebox.showerror(title="Error", message="El nodo inicial no es valido")
            elif not es_valido_final:
                messagebox.showerror(title="Error", message="El nodo final no es valido")
        else:
            if not nodo_inicial:
                messagebox.showerror(title="Error", message="El nodo inicial no es valido")
            if not nodo_final:
                messagebox.showerror(title="Error", message="El nodo final no es valido")


    def ejecutar_a(self):
            print("A")
