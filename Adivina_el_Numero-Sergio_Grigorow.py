'''
1. Se importan Librerias
2. Se definen funciones que se utilizaran durante la ejecucion
3. Se define ciclo principal del programa
4. En necesario installar el modulo pwinput
'''

import os
from random import randint
import pandas as pd
import pwinput

def limpiar_pantalla():
    '''Limpiar la pantalla para que informacion siguiente aparezca
    con pantalla en blanco'''
    os.system('cls' if os.name == 'nt' else 'clear')

def inicio():
    '''Función de Inicio del programa. Muestra menú de bienvenida y permite seleccionar una opción para avanzar'''
    limpiar_pantalla()
    print('='*50)
    print('|'*5 + ' Bienvenido al Juego Adivina el Número ' + '|'*5)
    print('='*50)
    print('\n')

    eleccion_menu = 'x'
    # loop para asegurar que se seleccione una opcion correcta. 
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 5):
        print("Elige una opción: ")
        print('''
        [1] - Partida Modo Solitario
        [2] - Partida 2 Jugadores
        [3] - Estadística
        [4] - Salir''')
        eleccion_menu = input()

    return int(eleccion_menu)

def volver_inicio():
    '''funcion para volver al menu principal despes de finalizar un juego'''
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menú: ")

def select_nivel():
    '''Funcion que permite elegir el nivel del juego'''
    eleccion_nivel = 'x'
    while not eleccion_nivel.isnumeric() or int(eleccion_nivel) not in range(1, 4):
        print("Elige un nivel de dificultad: ")
        print('''
        [1] - Fácil (20 intentos)
        [2] - Medio (12 intentos)
        [3] - Difícil (5 intentos)''')
        eleccion_nivel = input()

    return int(eleccion_nivel)

def obtener_intentos_por_nivel(nivel):
    '''funcion para obtener la cantidad de intentos una vez elegido el nivel'''
    if nivel == 1:
        return 20
    elif nivel == 2:
        return 12
    else:
        return 5

def guardar_estadisticas(nombre, resultado, nivel, intentos_usados):
    '''Guarda el resultado del juego, el nivel y los intentos usados en un archivo Excel
    Guarda el nombre, el resultado, el nivel, y el numero de intentos'''
    archivo = 'estadisticas.xlsx'
    datos = {'Jugador': [nombre], 'Resultado': [resultado], 'Nivel': [nivel], 'Intentos Usados': [intentos_usados]}
    df = pd.DataFrame(datos)
    
    # Si el archivo ya existe, agregamos los datos; si no, lo creamos
    if os.path.exists(archivo):
        df_existente = pd.read_excel(archivo)
        df = pd.concat([df_existente, df], ignore_index=True)

    df.to_excel(archivo, index=False)
    print(f"\nSe ha guardado el resultado de {nombre} en el archivo de estadísticas.")

def mostrar_estadisticas():
    '''Lee y muestra las estadísticas guardadas en el archivo Excel filtradas por usuario'''
    archivo = 'estadisticas.xlsx'
    
    if os.path.exists(archivo):
        df = pd.read_excel(archivo)
        print("\n=== Estadísticas de Partidas ===")
        
        # Solicitar el nombre del jugador para filtrar las estadísticas
        nombre = input("Ingrese su nombre para ver sus estadísticas: ")

        # Filtrar el DataFrame por el nombre del jugador
        df_filtrado = df[df['Jugador'] == nombre]
        
        if df_filtrado.empty:
            print(f"\nNo se encontraron estadísticas para el jugador {nombre}.")
        else:
            print(df_filtrado)
    else:
        print("\nNo se encontraron estadísticas previas.")

def juego(intentos, numero_secreto, nombre, nivel):
    '''Lógica principal del juego para adivinar el número'''
    estimado = 0
    intentos_iniciales = intentos  # Guardamos la cantidad inicial de intentos
    while intentos > 0:
        estimado = int(input(f"Intentos restantes {intentos}. ¿Cuál es el número?: "))
        intentos -= 1
        if estimado < numero_secreto:
            print("Mi número es más alto")
        elif estimado > numero_secreto:
            print("Mi número es más bajo")
        else:
            intentos_usados = intentos_iniciales - intentos  # Calcular intentos usados
            print(f"¡Felicitaciones {nombre}! Adivinaste el número en {intentos_usados} intentos.")
            guardar_estadisticas(nombre, "Ganó", nivel, intentos_usados)
            return True
    intentos_usados = intentos_iniciales  # Si no adivina, se usan todos los intentos
    print(f"Lo siento, se acabaron los intentos. El número secreto era {numero_secreto}")
    guardar_estadisticas(nombre, "Perdió", nivel, intentos_usados)
    return False

def solitario():
    '''Funcion con juego para una persona'''
    eleccion_nivel = select_nivel()
    intentos = obtener_intentos_por_nivel(eleccion_nivel)
    numero_secreto = randint(1, 1001)
    nombre = input("Dime tu nombre: ")

    niveles = {1: 'Fácil', 2: 'Medio', 3: 'Difícil'}
    nivel_texto = niveles[eleccion_nivel]

    print(f"Bueno {nombre}, he pensado un número entre 1 y 1000\nTienes {intentos} intentos para adivinar")
    juego(intentos, numero_secreto, nombre, nivel_texto)

def dos_jugadores():
    '''Funcion con juego para 2 personas'''
    eleccion_nivel = select_nivel()
    intentos = obtener_intentos_por_nivel(eleccion_nivel)
    
    nombre1 = input("Dime tu nombre jugador 1: ")
    nombre2 = input("Dime tu nombre jugador 2: ")
    
    numero_secreto = 'x'
    while not numero_secreto.isnumeric() or int(numero_secreto) not in range(1, 1001):
        numero_secreto = pwinput.pwinput(prompt=f'{nombre2}, introduce el número secreto (entre 1 y 1000) que {nombre1} debe adivinar: ', mask='*')
    numero_secreto = int(numero_secreto)

    niveles = {1: 'Fácil', 2: 'Medio', 3: 'Difícil'}
    nivel_texto = niveles[eleccion_nivel]
    
    print(f"Bueno {nombre1}, {nombre2} ha pensado un número entre 1 y 1000.\nTienes {intentos} intentos para adivinar.")
    juego(intentos, numero_secreto, nombre1, nivel_texto)


# Ciclo principal del programa
finalizar_programa = False

while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        solitario()
        volver_inicio()
    elif menu == 2:
        dos_jugadores()
        volver_inicio()
    elif menu == 3:
        mostrar_estadisticas()
        volver_inicio()
    elif menu == 4:
        finalizar_programa = True
