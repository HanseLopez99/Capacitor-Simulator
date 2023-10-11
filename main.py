import tkinter as tk
from tkinter import ttk
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Funciones import *

class CapacitorSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simulador de Capacitores")
        self.geometry("800x600")

        # Sección para mostrar la figura del capacitor
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Sección para elegir el tipo de capacitor
        self.capacitor_type = tk.StringVar()
        self.capacitor_options = ttk.Combobox(self, textvariable=self.capacitor_type)
        self.capacitor_options['values'] = ('Placas paralelas', 'Cilindrico', 'Esferico')
        self.capacitor_options.pack(pady=20)
        self.capacitor_options.bind("<<ComboboxSelected>>", self.update_input_fields)

        # Sección para ingresar parámetros
        self.inputs_frame = ttk.LabelFrame(self, text="Parámetros")
        self.inputs_frame.pack(pady=20, fill=tk.X)
        self.input_vars = {}

        # Sección para resultados
        self.results_frame = ttk.LabelFrame(self, text="Resultados")
        self.results_frame.pack(pady=20, fill=tk.X)
        self.results_vars = {}

        # Botón para calcular
        self.calculate_btn = ttk.Button(self, text="Calcular", command=self.calculate)
        self.calculate_btn.pack(pady=20)

    def update_input_fields(self, event=None):
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

        capacitor = self.capacitor_type.get()
        if capacitor == 'Placas paralelas':
            self.create_input("base", "Base")
            self.create_input("altura", "Altura")
            self.create_input("voltaje", "Voltaje")
            self.create_input("distancia", "Distancia")
            self.create_checkbox("dielectrico", "Con dieléctrico")
            self.create_checkbox("half_dielectrico", "Dieléctrico a la mitad")

        elif capacitor == 'Cilindrico':
            self.create_input("r1", "Radio interior")
            self.create_input("r2", "Radio exterior")
            self.create_input("largo", "Largo")
            self.create_input("voltaje", "Voltaje")
            self.create_checkbox("dielectrico", "Con dieléctrico")
            self.create_checkbox("half_dielectrico", "Dieléctrico a la mitad")

        elif capacitor == 'Esferico':
            self.create_input("r1", "Radio interior")
            self.create_input("r2", "Radio exterior")
            self.create_input("voltaje", "Voltaje")
            self.create_checkbox("dielectrico", "Con dieléctrico")
            self.create_checkbox("half_dielectrico", "Dieléctrico a la mitad")

    def create_input(self, var_name, label):
        frame = ttk.Frame(self.inputs_frame)
        frame.pack(fill=tk.X, pady=5)

        lbl = ttk.Label(frame, text=label)
        lbl.pack(side=tk.LEFT, padx=5)

        var = tk.DoubleVar()
        entry = ttk.Entry(frame, textvariable=var)
        entry.pack(side=tk.RIGHT, padx=5)

        self.input_vars[var_name] = var

    def create_checkbox(self, var_name, label):
        var = tk.BooleanVar()
        chk = ttk.Checkbutton(self.inputs_frame, text=label, variable=var)
        chk.pack(pady=5)
        self.input_vars[var_name] = var

    def calculate(self):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        capacitor = self.capacitor_type.get()

        if capacitor == 'Placas paralelas':
            base = self.input_vars["base"].get()
            altura = self.input_vars["altura"].get()
            voltaje = self.input_vars["voltaje"].get()
            distancia = self.input_vars["distancia"].get()
            dielectrico = self.input_vars["dielectrico"].get()
            half_dielectrico = self.input_vars["half_dielectrico"].get() if dielectrico else False

            if dielectrico:
                results = capacitor_placas_paralelas_con_dielectrico(base, altura, voltaje, distancia, half_dielectrico)
                labels = ["Capacitancia", "Carga del capacitor", "Energía almacenada", "Densidad de carga libre", "Densidad de carga libre (Plexiglas)", "Densidad de carga ligada"]
            else:
                results = capacitor_placas_paralelas(base, altura, voltaje, distancia)
                labels = ["Capacitancia", "Carga del capacitor", "Energía almacenada"]
            print(results)

        elif capacitor == 'Cilindrico':
            r1 = self.input_vars["r1"].get()
            r2 = self.input_vars["r2"].get()
            largo = self.input_vars["largo"].get()
            voltaje = self.input_vars["voltaje"].get()
            dielectrico = self.input_vars["dielectrico"].get()
            half_dielectrico = self.input_vars["half_dielectrico"].get() if dielectrico else False

            if dielectrico:
                results = capacitor_cilindrico_diel(r1, r2, largo, voltaje, half_dielectrico)
                labels = ["Capacitancia", "Carga del capacitor", "Energía almacenada", "Densidad de carga libre (Aire - Interior)", "Densidad de carga libre (Aire - Exterior)", "Densidad de carga ligada (Interior)", "Densidad de carga ligada (Exterior)"]
            else:
                results = capacitor_cilindrico(r1, r2, largo, voltaje)
                labels = ["Capacitancia", "Carga del capacitor", "Energía almacenada"]
            print(results)

        elif capacitor == 'Esferico':
            r1 = self.input_vars["r1"].get()
            r2 = self.input_vars["r2"].get()
            voltaje = self.input_vars["voltaje"].get()
            dielectrico = self.input_vars["dielectrico"].get()
            half_dielectrico = self.input_vars["half_dielectrico"].get() if dielectrico else False

            if dielectrico:
                results = capacitor_esferico_diel(r1, r2, voltaje, half_dielectrico)
                labels = ["Capacitancia", "Carga del capacitor", "Energía almacenada", "Densidad de carga libre (Aire - Interior)", "Densidad de carga libre (Aire - Exterior)", "Densidad de carga ligada (Interior)", "Densidad de carga ligada (Exterior)"]
            else:
                results = capacitor_esferico(r1, r2, voltaje)
                labels = ["Capacitancia", "Carga del capacitor", "Energía almacenada"]
            print(results)

        for label, value in zip(labels, results):
            self.show_result(label, value)

        # Actualizar la figura del capacitor
        self.update_figure()

    def show_result(self, label, value):
        frame = ttk.Frame(self.results_frame)
        frame.pack(fill=tk.X, pady=5)

        lbl = ttk.Label(frame, text=f"{label}:")
        lbl.pack(side=tk.LEFT, padx=5)

        result = ttk.Label(frame, text=f"{value:.4f}")
        result.pack(side=tk.RIGHT, padx=5)


    def update_figure(self):
        self.ax.clear()
        # Aquí iría la lógica para dibujar el corte transversal del capacitor
        # usando matplotlib.
        self.canvas.draw()

if __name__ == "__main__":
    app = CapacitorSimulator()
    app.mainloop()
