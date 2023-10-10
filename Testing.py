from Funciones import *

""""

---CAPACITOR DE PLACAS PARALELAS CON DIELECTRICO---


# Definimos los parámetros
base = 2  # 10 cm en metros
altura = 1  # 10 cm en metros
voltaje = 10  # 5 V
distancia = 1  # 0.01 m

# Llamamos a la función para el caso con la mitad de dieléctrico
C_half, Q_half, U_half, sigma_libre_half, sigma_libre_plexiglas_half, sigma_ligada_half = capacitor_placas_paralelas_con_dielectrico(base, altura, voltaje, distancia, True)

print("Resultados con la mitad de dieléctrico:")
print(f"Capacitancia: {C_half} F")
print(f"Carga: {Q_half} C")
print(f"Energía: {U_half} J")
print(f"Densidad de carga libre: {sigma_libre_half} C/m^2")
print(f"Densidad de carga libre en Plexiglas: {sigma_libre_plexiglas_half} C/m^2")
print(f"Densidad de carga ligada: {sigma_ligada_half} C/m^2")
print("\n")

# Llamamos a la función para el caso con todo el espacio lleno de dieléctrico
C_full, Q_full, U_full, sigma_libre_full, sigma_ligada_full = capacitor_placas_paralelas_con_dielectrico(base, altura, voltaje, distancia, False)

print("Resultados con todo el espacio lleno de dieléctrico:")
print(f"Capacitancia: {C_full} F")
print(f"Carga: {Q_full} C")
print(f"Energía: {U_full} J")
print(f"Densidad de carga libre: {sigma_libre_full} C/m^2")
print(f"Densidad de carga ligada: {sigma_ligada_full} C/m^2")




---CAPACITOR ESFERICO CON PLACAS PARALELAS--




# Definimos los parámetros
r1 = 3  # Radio interior en cm
r2 = 6  # Radio exterior en cm
voltaje = 10  # 10 V
k = 3.4  # Constante dieléctrica del Plexiglas

# Llamamos a la función para el caso con la mitad de dieléctrico
r1 = 3
r2 = 6
voltaje = 10
k = 3.4


# Llamada a la función
C, Q, U, Q_libre_aire, Q_libre_dielectrico, Q_ligada = capacitor_esferico_diel(r1, r2, voltaje, k, True)

# Impresión de resultados
print(f"Capacitancia con dieléctrico en la mitad: {C} F")
print(f"Carga del capacitor: {Q} C")
print(f"Energía almacenada en el capacitor: {U} J")
print(f"\nDensidades de carga libre en aire:")
print(f"Interior: {Q_libre_aire[0]} C/m^2")
print(f"Exterior: {Q_libre_aire[1]} C/m^2")
print(f"\nDensidades de carga libre en dieléctrico:")
print(f"Interior: {Q_libre_dielectrico[0]} C/m^2")
print(f"Exterior: {Q_libre_dielectrico[1]} C/m^2")
print(f"\nDensidades de carga ligada:")
print(f"Interior: {Q_ligada[0]} C/m^2")
print(f"Exterior: {Q_ligada[1]} C/m^2")



# Llamamos a la función para el caso con todo el espacio lleno de dieléctrico
C_full, Q_full, U_full, Q_libre_full, Q_ligada_full = capacitor_esferico_diel(r1, r2, voltaje, k, False)

print("\nResultados con todo el espacio lleno de dieléctrico:\n")
print(f"Capacitancia: {C_full} F")
print(f"Carga: {Q_full} C")
print(f"Energía: {U_full} J")
print("Densidades de carga libre:")
print(f"Interior: {Q_libre_full[0]} C/m^2")
print(f"Exterior: {Q_libre_full[1]} C/m^2")
print("Densidades de carga ligada:")
print(f"Interior: {Q_ligada_full[0]} C/m^2")
print(f"Exterior: {Q_ligada_full[1]} C/m^2")






---CAPACITOR ESFERICO CON PLACAS PARALELAS---


# Definimos los parámetros
r1 = 3  # Radio interior en cm
r2 = 6  # Radio exterior en cm
L = 5   # Longitud del cilindro en cm
voltaje = 10  # 10 V
k = 3.4  # Constante dieléctrica del Plexiglas

# Llamada a la función
C, Q, U, rho_libre_air, rho_libre_dielectrico, rho_ligada = capacitor_cilindrico_diel(r1, r2, L, voltaje, k, True)

# Impresión de resultados
print(f"Capacitancia con dieléctrico en la mitad: {C} F")
print(f"Carga del capacitor: {Q} C")
print(f"Energía almacenada en el capacitor: {U} J")
print(f"\nDensidades de carga libre en aire:")
print(f"Interior: {rho_libre_air[0]} C/m^2")
print(f"Exterior: {rho_libre_air[1]} C/m^2")
print(f"\nDensidades de carga libre en dieléctrico:")
print(f"Interior: {rho_libre_dielectrico[0]} C/m^2")
print(f"Exterior: {rho_libre_dielectrico[1]} C/m^2")
print(f"\nDensidades de carga ligada:")
print(f"Interior: {rho_ligada[0]} C/m^2")
print(f"Exterior: {rho_ligada[1]} C/m^2")



# Llamamos a la función para el caso con todo el espacio lleno de dieléctrico
C_full, Q_full, U_full, rho_libre_full, rho_ligada_full = capacitor_cilindrico_diel(r1, r2, L, voltaje, k, False)

print("Resultados con todo el espacio lleno de dieléctrico:")
print(f"Capacitancia: {C_full} F")
print(f"Carga: {Q_full} C")
print(f"Energía: {U_full} J")
print("Densidades de carga libre:")
print(f"Interior: {rho_libre_full[0]} C/m^2")
print(f"Exterior: {rho_libre_full[1]} C/m^2")
print("Densidades de carga ligada:")
print(f"Interior: {rho_ligada_full[0]} C/m^2")
print(f"Exterior: {rho_ligada_full[1]} C/m^2")

"""

