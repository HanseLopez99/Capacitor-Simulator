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
        self.geometry("1200x1200")

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
        self.parameters_frame = ttk.LabelFrame(self, text="Parámetros")
        self.parameters_frame.pack(pady=20, fill=tk.X)
        self.inputs = {}

        # Sección para mostrar resultados
        self.results_frame = ttk.LabelFrame(self, text="Resultados")
        self.results_frame.pack(pady=20, fill=tk.X)
        self.results = {}

        # Botón para calcular
        self.calculate_btn = ttk.Button(self, text="Calcular", command=self.calculate)
        self.calculate_btn.pack(pady=20)

    def update_input_fields(self, event):
        for widget in self.parameters_frame.winfo_children():
            widget.destroy()

        capacitor = self.capacitor_type.get()
        if capacitor == 'Placas paralelas':
            self.create_input('base', 'Base (m)')
            self.create_input('altura', 'Altura (m)')
            self.create_input('voltaje', 'Voltaje (V)')
            self.create_input('distancia', 'Distancia (m)')
            self.create_checkbox('dieléctrico', 'Con Dieléctrico')
            self.create_checkbox('half', 'Dieléctrico a la mitad', state=tk.DISABLED)
        elif capacitor == 'Cilindrico':
            self.create_input('r1', 'Radio Interior (m)')
            self.create_input('r2', 'Radio Exterior (m)')
            self.create_input('largo', 'Largo (m)')
            self.create_input('voltaje', 'Voltaje (V)')
            self.create_checkbox('dieléctrico', 'Con Dieléctrico')
            self.create_checkbox('half', 'Dieléctrico a la mitad', state=tk.DISABLED)
        elif capacitor == 'Esferico':
            self.create_input('r1', 'Radio Interior (m)')
            self.create_input('r2', 'Radio Exterior (m)')
            self.create_input('voltaje', 'Voltaje (V)')
            self.create_input('k', 'Constante Dieléctrica')
            self.create_checkbox('dieléctrico', 'Con Dieléctrico')
            self.create_checkbox('half', 'Dieléctrico a la mitad', state=tk.DISABLED)

    def create_input(self, name, label):
        frame = ttk.Frame(self.parameters_frame)
        frame.pack(fill=tk.X, pady=5)
        ttk.Label(frame, text=label).pack(side=tk.LEFT, padx=5)
        self.inputs[name] = ttk.Entry(frame)
        self.inputs[name].pack(side=tk.RIGHT, padx=5)

    def create_checkbox(self, name, label, state=tk.NORMAL):
        self.inputs[name] = ttk.Checkbutton(self.parameters_frame, text=label, state=state, command=self.toggle_half)
        self.inputs[name].pack(pady=5)

    def toggle_half(self):
        if self.inputs['dieléctrico'].instate(['selected']):
            self.inputs['half']['state'] = tk.NORMAL
        else:
            self.inputs['half']['state'] = tk.DISABLED
            self.inputs['half'].state(['!selected'])

    def calculate(self):
        capacitor = self.capacitor_type.get()
        if capacitor == 'Placas paralelas':
            base = float(self.inputs['base'].get())
            altura = float(self.inputs['altura'].get())
            voltaje = float(self.inputs['voltaje'].get())
            distancia = float(self.inputs['distancia'].get())
            if self.inputs['dieléctrico'].instate(['selected']):
                half = self.inputs['half'].instate(['selected'])
                results = capacitor_placas_paralelas_con_dielectrico(base, altura, voltaje, distancia, half)
            else:
                results = capacitor_placas_paralelas(base, altura, voltaje, distancia)
        elif capacitor == 'Cilindrico':
            r1 = float(self.inputs['r1'].get())
            r2 = float(self.inputs['r2'].get())
            largo = float(self.inputs['largo'].get())
            voltaje = float(self.inputs['voltaje'].get())
            if self.inputs['dieléctrico'].instate(['selected']):
                half = self.inputs['half'].instate(['selected'])
                results = capacitor_cilindrico_diel(r1, r2, largo, voltaje, half)
            else:
                results = capacitor_cilindrico(r1, r2, largo, voltaje)
        elif capacitor == 'Esferico':
            r1 = float(self.inputs['r1'].get())
            r2 = float(self.inputs['r2'].get())
            voltaje = float(self.inputs['voltaje'].get())
            k = float(self.inputs['k'].get())
            if self.inputs['dieléctrico'].instate(['selected']):
                half = self.inputs['half'].instate(['selected'])
                results = capacitor_esferico_diel(r1, r2, voltaje, k, half)
            else:
                results = capacitor_esferico(r1, r2, voltaje)

        self.show_results(results)
        self.draw_capacitor()

    def show_results(self, results):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        labels = ['Capacitancia (F)', 'Carga del Capacitor (C)', 'Energía Almacenada (J)']
        for i, result in enumerate(results[:3]):
            frame = ttk.Frame(self.results_frame)
            frame.pack(fill=tk.X, pady=5)
            ttk.Label(frame, text=labels[i]).pack(side=tk.LEFT, padx=5)
            ttk.Label(frame, text=f'{result:.2e}').pack(side=tk.RIGHT, padx=5)

        if len(results) > 3:
            additional_labels = [
                'Densidad de Carga Libre (C/m^2)',
                'Densidad de Carga Libre (Dieléctrico) (C/m^2)',
                'Densidad de Carga Ligada (C/m^2)'
            ]
            for i, result in enumerate(results[3:], start=3):
                if isinstance(result, tuple):
                    for sub_result in result:
                        frame = ttk.Frame(self.results_frame)
                        frame.pack(fill=tk.X, pady=5)
                        ttk.Label(frame, text=additional_labels[i-3]).pack(side=tk.LEFT, padx=5)
                        ttk.Label(frame, text=f'{sub_result:.2e}').pack(side=tk.RIGHT, padx=5)
                else:
                    frame = ttk.Frame(self.results_frame)
                    frame.pack(fill=tk.X, pady=5)
                    ttk.Label(frame, text=additional_labels[i-3]).pack(side=tk.LEFT, padx=5)
                    ttk.Label(frame, text=f'{result:.2e}').pack(side=tk.RIGHT, padx=5)


    def draw_capacitor(self):
        self.ax.clear()
        capacitor = self.capacitor_type.get()

        if capacitor == 'Placas paralelas':
            base = float(self.inputs['base'].get())
            altura = float(self.inputs['altura'].get())
            distancia = float(self.inputs['distancia'].get())

            # Dibuja la placa inferior
            self.ax.add_patch(plt.Rectangle((0.5 - base/2, 0.5 - altura/2 - distancia), base, altura, color='blue'))
            self.ax.text(0.5, 0.5 - altura/2 - distancia/2, 'Placa inferior', ha='center', va='center', color='white')
            
            # Dibuja la placa superior
            self.ax.add_patch(plt.Rectangle((0.5 - base/2, 0.5 + distancia/2), base, altura, color='red'))
            self.ax.text(0.5, 0.5 + distancia/2 + altura/2, 'Placa superior', ha='center', va='center', color='white')
            
            # Dibuja el dieléctrico si está seleccionado
            if self.inputs['dieléctrico'].instate(['selected']):
                if self.inputs['half'].instate(['selected']):
                    self.ax.add_patch(plt.Rectangle((0.5 - base/2, 0.5 - altura/2), base/2, altura, color='yellow'))
                    self.ax.text(0.5 - base/4, 0.5, 'Dieléctrico', ha='center', va='center', color='black')
                else:
                    self.ax.add_patch(plt.Rectangle((0.5 - base/2, 0.5 - altura/2), base, altura, color='yellow'))
                    self.ax.text(0.5, 0.5, 'Dieléctrico', ha='center', va='center', color='black')

        elif capacitor == 'Cilindrico':
            r1 = float(self.inputs['r1'].get()) / 10
            r2 = float(self.inputs['r2'].get()) / 10
            circle1 = plt.Circle((0.5, 0.5), r1, color='blue')
            circle2 = plt.Circle((0.5, 0.5), r2, color='red', fill=False)
            self.ax.add_artist(circle1)
            self.ax.add_artist(circle2)
            self.ax.text(0.5, 0.5, 'Interior', ha='center', va='center', color='white')
            if self.inputs['dieléctrico'].instate(['selected']):
                if self.inputs['half'].instate(['selected']):
                    wedge = plt.Wedge(center=(0.5, 0.5), r=r2, theta1=0, theta2=180, width=r2-r1, color='yellow')
                    self.ax.add_artist(wedge)
                else:
                    circle3 = plt.Circle((0.5, 0.5), r2, color='yellow', fill=False, linewidth=2*(r2-r1))
                    self.ax.add_artist(circle3)
        elif capacitor == 'Esferico':
            r1 = float(self.inputs['r1'].get()) / 10
            r2 = float(self.inputs['r2'].get()) / 10
            circle1 = plt.Circle((0.5, 0.5), r1, color='blue')
            circle2 = plt.Circle((0.5, 0.5), r2, color='red', fill=False)
            self.ax.add_artist(circle1)
            self.ax.add_artist(circle2)
            self.ax.text(0.5, 0.5, 'Interior', ha='center', va='center', color='white')
            if self.inputs['dieléctrico'].instate(['selected']):
                if self.inputs['half'].instate(['selected']):
                    wedge = plt.Wedge(center=(0.5, 0.5), r=r2, theta1=0, theta2=180, width=r2-r1, color='yellow')
                    self.ax.add_artist(wedge)
                else:
                    circle3 = plt.Circle((0.5, 0.5), r2, color='yellow', fill=False, linewidth=2*(r2-r1))
                    self.ax.add_artist(circle3)

        if capacitor == 'Placas paralelas':
            max_dimension = max(base + 2 * distancia, altura + 2 * distancia)
            self.ax.set_xlim(0.5 - max_dimension, 0.5 + max_dimension)
            self.ax.set_ylim(0.5 - max_dimension, 0.5 + max_dimension)
            self.canvas.draw()
        elif capacitor == 'Cilindrico':
            max_dimension = max(r1 + 1, r2 + 1)
            self.ax.set_xlim(0.5 - max_dimension, 0.5 + max_dimension)
            self.ax.set_ylim(0.5 - max_dimension, 0.5 + max_dimension)
            self.canvas.draw()
        elif capacitor == 'Esferico':
            max_dimension = max(r1 + 1, r2 + 1)
            self.ax.set_xlim(0.5 - max_dimension, 0.5 + max_dimension)
            self.ax.set_ylim(0.5 - max_dimension, 0.5 + max_dimension)
            self.canvas.draw()


if __name__ == "__main__":
    app = CapacitorSimulator()
    app.mainloop()

