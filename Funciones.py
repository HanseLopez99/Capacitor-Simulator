import math

epsilon_0 = 8.854187817e-12  # Permitividad del vacío en F/m

#Funcion para capacitor placas paralelas sin dieléctrico
def capacitor_placas_paralelas(base, altura, voltaje, distancia):
    # Constantes
    epsilon_0 = 8.854187817e-12  # Permitividad del vacío en F/m

    # Cálculos
    # Área de las placas
    A = base * altura

    # Capacitancia
    C = (epsilon_0 * A)/distancia

    # Carga del capacitor
    Q = C * voltaje

    # Energía almacenada en el capacitor
    U = 0.5 * C * voltaje**2

    return C, Q, U

#Funcion para capacitor placas paralelas con dieléctrico
def capacitor_placas_paralelas_con_dielectrico(base, altura, voltaje, distancia, half):
    # Constantes
    epsilon_0 = 8.854187817e-12  # Permitividad del vacío en F/m
    K = 3.40  # Constante dieléctrica del Plexiglas

    # Cálculos
    # Área de las placas
    A = base * altura

    # Capacitancia con aire
    C0 = (epsilon_0 * A) / distancia

    # Capacitancia con dieléctrico

    C = (epsilon_0 * K * A) / distancia
    # Carga del capacitor
    Q = C0 * voltaje
    if half:
        C = (C0 + C) / 2
        U = 0.5 * ((C0 * voltaje**2) / 2 + (C * (voltaje/K)**2) / 2)
        sigma_libre = ((Q)/((K+1)*(A)))*2
        sigma_libre_plexiglas = sigma_libre * K
        sigma_ligada = sigma_libre_plexiglas * (1-(1/K))
        return C, Q, U, sigma_libre, sigma_libre_plexiglas, sigma_ligada

    else:
        U = 0.5 * C * (voltaje/K)**2
        sigma_libre_plexiglas = (Q)/(base*altura)
        sigma_ligada = sigma_libre_plexiglas * (1-(1/K))
        return C, Q, U, sigma_libre_plexiglas, sigma_ligada

# Función para capacitor esférico sin dieléctrico
def capacitor_esferico(r1, r2, voltaje):
    C = 4 * math.pi * epsilon_0 * (r1 * r2) / (r2 - r1)
    Q = C * voltaje
    U = 0.5 * C * voltaje**2
    return C, Q, U

# Función para capacitor esférico sin dieléctrico
def capacitor_esferico_diel(r1, r2, voltaje, k, half):
    epsilon_0 = 8.854187817e-12
    C0 = 4 * math.pi * epsilon_0 * (r1 * r2) / (r2 - r1)
    Q = C0 * voltaje

    if half:
        C_dielectrico = 0.5 * C0 * k
        C_vacio = 0.5 * C0
        C = C_dielectrico + C_vacio

        Q_libre_aire_inner = (Q/(1+k))*(1/(2*math.pi*r1**2))
        Q_libre_aire_outer = (Q/(1+k))*(1/(2*math.pi*r2**2))
        Q_libre_dielectrico_inner = Q_libre_aire_inner * k
        Q_libre_dielectrico_outer = Q_libre_aire_outer * k

        Q_ligada_r1 = Q_libre_dielectrico_inner* (1-(1/k))
        Q_ligada_r2 = Q_libre_dielectrico_outer* (1-(1/k))

        U = 0.5 * ((voltaje**2)*C0/2)/2 + ((((voltaje/k)**2)*C/2))/2

        return (C, Q, U, 
                (Q_libre_aire_inner, Q_libre_aire_outer),
                (Q_libre_dielectrico_inner, Q_libre_dielectrico_outer),
                (Q_ligada_r1, Q_ligada_r2))

    else:
        C = C0 * k
        Q_libre_inner = Q/(4 * math.pi * r1**2)
        Q_libre_outer = Q/(4 * math.pi * r2**2)
        Q_ligada_inner = Q_libre_inner * (1-(1/k))
        Q_ligada_outer = Q_libre_outer * (1-(1/k))

        U = 0.5 * C * (voltaje/k)**2

        return (C, Q, U, (Q_libre_inner, Q_libre_outer), (Q_ligada_inner, Q_ligada_outer))


# Función para capacitor cilíndrico sin dieléctrico
def capacitor_cilindrico(r1, r2, L, voltaje):
    epsilon_0 = 8.854187817e-12  # Permitividad del vacío en F/m
    C = 2 * math.pi * epsilon_0 * L / math.log(r2/r1)
    Q = C * voltaje
    U = 0.5 * C * voltaje**2
    return C, Q, U

# Función para capacitor cilíndrico con dieléctrico
def capacitor_cilindrico_diel(r1, r2, L, voltaje, half):
    k = math.pi
    epsilon_0 = 8.854187817e-12

    C0 = (2*math.pi*epsilon_0*L)/(math.log(r2/r1))
    Q = C0 * voltaje

    if half:
        C_dielectrico = 0.5 * C0 * k
        C = 0.5 * C0 + C_dielectrico
        U = ((voltaje**2)*C0/2)/2 + ((((voltaje/k)**2)*C/2))/2

        rho_libre_air_inner = (Q/(1+k))*(1/(math.pi*r1*L))
        rho_libre_air_outer = (Q/(1+k))*(1/(math.pi*r2*L))
        rho_libre_dielectrico_inner =  rho_libre_air_inner * k
        rho_libre_dielectrico_outer = rho_libre_air_outer * k

        rho_ligada_inner = rho_libre_dielectrico_inner * (1-(1/k))
        rho_ligada_outer = rho_libre_dielectrico_outer * (1-(1/k))

        return (C, Q, U, 
                (rho_libre_air_inner, rho_libre_air_outer),
                ( rho_libre_dielectrico_inner, rho_libre_dielectrico_outer),
                (rho_ligada_inner, rho_ligada_outer))

    else:
        C = C0 * k
        U = 0.5 * C * (voltaje/k)**2

        rho_libre_inner = Q / (2*math.pi*r1*L)
        rho_libre_outer = Q / (2*math.pi*r2*L)
        rho_ligada_inner = rho_libre_inner * (1-(1/k))
        rho_ligada_outer = rho_libre_outer * (1-(1/k))

        return (C, Q, U, (rho_libre_inner, rho_libre_outer), (rho_ligada_inner, rho_ligada_outer))



