import matplotlib
matplotlib.use("TkAgg")  # Esencial para la ventana animada
import matplotlib.pyplot as plt
from collections import deque
import time
import random as random

import matplotlib.pyplot as plt

class Laberinto:
    def __init__(self, renglones, cols, Tabs, ruta_png):
        self.renglones = renglones
        self.cols = cols
        # self.ruta_txt ya no es necesario como variable única, usamos Tabs
        self.ruta_png = ruta_png
        
        # Corrección: Cerrar paréntesis del input
        self.jugadores = int(input("ingresa la cantidad de jugadores (1 a 4):") )# Forzado a 1 para la modalidad DFS 1-62
        
        self.Tabs = Tabs # Esta es tu lista externa (ej: ["T1.txt", "T2.txt"])
        
        # Cargar imagen
        self.imagen = plt.imread(self.ruta_png)
        
        # Lista para guardar las matrices de cada archivo
        self.laberintos = []
        
        # Corrección: Iterar directamente sobre la lista Tabs
        for txt in self.Tabs:
            matriz = self.leer_txt(txt)
            self.laberintos.append(matriz)
        
        # Coordenadas (Mantengo tus listas originales)
        self.Orig_x = [6, 15, 9, 0]   
        self.Orig_y = [15, 9, 0, 6]   
        
        self.Destin_x = [12, 2, 2, 11]  
        self.Destin_y = [12, 11, 2, 2] 

    def leer_txt(self, txt):
        with open(txt, "r", encoding="utf-8") as archivo:
            # split() separa correctamente números como '35' o '22' [cite: 1]
            # if linea.strip() ignora líneas vacías [cite: 3, 7]
            return [linea.split() for linea in archivo if linea.strip()]


    def dfs6(self):
        num_jugadores = int(self.jugadores)
        direcciones = [
            (0, 1), (1, 0), (0, -1), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        Colores = ['lime', 'red', 'blue', 'yellow']
        
        plt.ion()
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(self.imagen, extent=[0, self.cols, self.renglones, 0])

        # --- CREACIÓN DE LOS MARCADORES DIGITALES ---
        # 1. Indicador del jugador en turno (Arriba, centrado)
        txt_turno = ax.text(8, 6, '', fontsize=20, fontweight='bold', 
                            color='black', ha='center', va='center',
                            bbox=dict(facecolor='black', alpha=0.8, boxstyle='round,pad=0.3'))

        # 2. Los dos dados (Abajo, separados)
        txt_marcador1 = ax.text(6.5, 8, '', fontsize=45, fontweight='bold', 
                               color='white', ha='center', va='center',
                               bbox=dict(facecolor='black', alpha=0.5, edgecolor='cyan', boxstyle='round,pad=0.08'))
        
        txt_marcador2 = ax.text(9.5, 8, '', fontsize=45, fontweight='bold', 
                               color='white', ha='center', va='center',
                               bbox=dict(facecolor='black', alpha=0.5, edgecolor='magenta', boxstyle='round,pad=0.08'))

        pos_x = [x for x in self.Orig_x]
        pos_y = [y for y in self.Orig_y]
        valores_actuales = []
        visitados_por_jugador = []
        activos = [True] * num_jugadores

        for i in range(num_jugadores):
            visitados_por_jugador.append({(pos_x[i], pos_y[i])})
            try:
                valores_actuales.append(int(self.laberintos[i][pos_y[i]][pos_x[i]]))
            except:
                activos[i] = False

        partida_en_curso = True
        while partida_en_curso:
            for i in range(num_jugadores):
                if not activos[i]: continue

                # --- ACTUALIZAR INDICADOR DE TURNO ---
                txt_turno.set_text(f"JUGADOR {i+1}")
                txt_turno.set_color(Colores[i]) # El texto toma el color del jugador
                txt_turno.set_bbox(dict(facecolor='black', alpha=0.5, edgecolor='white', boxstyle='round, pad=0.2'))
                plt.pause(0.1) # Pequeña pausa para que se note el cambio de turno

                # --- ANIMACIÓN DE LOS DOS DADOS ---
                for _ in range(15): 
                    num1 = random.randint(1, 6)
                    num2 = random.randint(1, 6)
                    
                    txt_marcador1.set_text(f"{num1}")
                    txt_marcador2.set_text(f"{num2}")
                    
                    txt_marcador1.set_color('black')
                    txt_marcador2.set_color('black')
                    plt.pause(0.05)
                
                # Resultado final de los dados
                dado1 = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                pasos_dados = (dado1 + dado2)-1 
                
                txt_marcador1.set_text(f"{dado1}")
                txt_marcador2.set_text(f"{dado2}")
                txt_marcador1.set_color('white')
                txt_marcador2.set_color('white')
                plt.pause(0.5) 

                v_inicio_turno = valores_actuales[i]
                meta_turno = v_inicio_turno + pasos_dados
                if meta_turno > 56: meta_turno = 56

                camino_abierto = True
                while camino_abierto:
                    x, y = pos_x[i], pos_y[i]
                    v_actual = valores_actuales[i]
                    
                    rect = plt.Rectangle((x, y), 1, 1, facecolor=Colores[i], alpha=0.6)
                    ax.add_patch(rect)
                    plt.pause(0.05)

                    if v_actual >= meta_turno:
                        if v_actual >= 56:
                            txt_turno.set_text("¡GANADOR!")
                            txt_marcador1.set_text("WI")
                            txt_marcador2.set_text("N!")
                            print(f"¡EL JUGADOR {i+1} HA GANADO!")
                            partida_en_curso = False
                        break

                    proximo_paso = None
                    # Prioridad 1: Mismo número
                    for dx, dy in direcciones:
                        nx, ny = x + dx, y + dy
                        if 0 <= ny < len(self.laberintos[i]) and 0 <= nx < len(self.laberintos[i][0]):
                            token = self.laberintos[i][ny][nx]
                            if token != '#' and (nx, ny) not in visitados_por_jugador[i]:
                                try:
                                    if int(token) == v_actual:
                                        proximo_paso = (nx, ny, int(token))
                                        break
                                except: pass
                    
                    # Prioridad 2: Siguiente número
                    if not proximo_paso:
                        for dx, dy in direcciones:
                            nx, ny = x + dx, y + dy
                            if 0 <= ny < len(self.laberintos[i]) and 0 <= nx < len(self.laberintos[i][0]):
                                token = self.laberintos[i][ny][nx]
                                if token != '#' and (nx, ny) not in visitados_por_jugador[i]:
                                    try:
                                        if int(token) == v_actual + 1:
                                            proximo_paso = (nx, ny, int(token))
                                            break
                                    except: pass

                    if proximo_paso:
                        pos_x[i], pos_y[i], valores_actuales[i] = proximo_paso
                        visitados_por_jugador[i].add((pos_x[i], pos_y[i]))
                    else:
                        print(f"Jugador {i+1} bloqueado.")
                        camino_abierto = False
                
                if not partida_en_curso: break

        plt.ioff()
        plt.show()
        

# --- EJECUCIÓN ---
plt.close('all') # Cerrar ventanas muertas
rutas = ["TABLERO1.txt", "TABLERO2.txt", "TABLERO3.txt", "TABLERO4.txt"]
Poleana1 = Laberinto(16, 16, rutas, "Poleana-1.png")
Poleana1.dfs6()


