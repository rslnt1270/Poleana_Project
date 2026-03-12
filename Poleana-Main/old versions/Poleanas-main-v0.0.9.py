import matplotlib
matplotlib.use("TkAgg")  # Esencial para la ventana animada
import matplotlib.pyplot as plt
from collections import deque
import time

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

    def dfs_estricto_poleana(self):
        num_jugadores = int(self.jugadores)
        # 8 Direcciones (Cruz + Diagonales)
        direcciones = [
            (0, 1), (1, 0), (0, -1), (-1, 0),  # Ortogonales
            (1, 1), (1, -1), (-1, 1), (-1, -1) # Diagonales (al final)
        ]
        
        Colores = ['lime', 'red', 'blue', 'yellow']
        plt.ion()
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(self.imagen, extent=[0, self.cols, self.renglones, 0])

        for i in range(num_jugadores): 
            x, y = self.Orig_x[i], self.Orig_y[i]
            
            try:
                v_actual = int(self.laberintos[i][y][x])
            except: 
                print(f"¡PETÓ! Origen inválido para jugador {i+1}")
                continue

            visitados = {(x, y)}
            camino_abierto = True

            while camino_abierto:
                # Dibujar paso actual
                rect = plt.Rectangle((x, y), 1, 1, facecolor=Colores[i], alpha=0.6)
                ax.add_patch(rect)
                plt.pause(0.01)

                if v_actual == 56:
                    print(f"¡Jugador {i+1} completó el circuito!")
                    break

                # 1. BUSCAR REPETIDOS (X) PRIMERO
                proximo_paso = None
                for dx, dy in direcciones:
                    nx, ny = x + dx, y + dy
                    if 0 <= ny < len(self.laberintos[i]) and 0 <= nx < len(self.laberintos[i][0]):
                        token = self.laberintos[i][ny][nx]
                        if token != '#' and (nx, ny) not in visitados:
                            if int(token) == v_actual:
                                proximo_paso = (nx, ny, v_actual)
                                break # Prioridad absoluta: encontró un igual, se mueve ya.

                # 2. SI NO HUBO IGUALES, BUSCAR SUCESOR (X+1)
                if not proximo_paso:
                    for dx, dy in direcciones:
                        nx, ny = x + dx, y + dy
                        if 0 <= ny < len(self.laberintos[i]) and 0 <= nx < len(self.laberintos[i][0]):
                            token = self.laberintos[i][ny][nx]
                            if token != '#' and (nx, ny) not in visitados:
                                if int(token) == v_actual + 1:
                                    proximo_paso = (nx, ny, v_actual + 1)
                                    break # Encontró el progreso.

                # 3. SI NO HAY NADA, PETAR
                if proximo_paso:
                    x, y, v_actual = proximo_paso
                    visitados.add((x, y))
                else:
                    print(f"¡PETÓ! El jugador {i+1} se quedó sin camino en el número {v_actual} ({x},{y})")
                    camino_abierto = False
                            
        plt.ioff()
        plt.show()
        

# --- EJECUCIÓN ---
plt.close('all') # Cerrar ventanas muertas
rutas = ["TABLERO1.txt", "TABLERO2.txt", "TABLERO3.txt", "TABLERO4.txt"]
Poleana1 = Laberinto(16, 16, rutas, "Poleana-1.png")
Poleana1.dfs_estricto_poleana()


