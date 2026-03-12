import matplotlib
matplotlib.use("TkAgg")  # Esencial para la ventana animada
import matplotlib.pyplot as plt
from collections import deque
import time
import random

class Laberinto:
    def __init__(self, renglones, cols, Tabs, ruta_png):
        self.renglones = renglones
        self.cols = cols
        self.ruta_png = ruta_png
        
        self.jugadores = int(input("Ingresa la cantidad de jugadores (1 a 4): "))
        
        self.Tabs = Tabs
        
        # Cargar imagen
        self.imagen = plt.imread(self.ruta_png)
        
        # Lista para guardar las matrices de cada archivo
        self.laberintos = []
        
        for txt in self.Tabs:
            matriz = self.leer_txt(txt)
            self.laberintos.append(matriz)
        
        # Coordenadas
        self.Orig_x = [6, 15, 9, 0]   
        self.Orig_y = [15, 9, 0, 6]   
        
        self.Destin_x = [12, 2, 2, 11]  
        self.Destin_y = [12, 11, 2, 2] 

    def leer_txt(self, txt):
        with open(txt, "r", encoding="utf-8") as archivo:
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
        txt_turno = ax.text(8, 6, '', fontsize=20, fontweight='bold', 
                            color='black', ha='center', va='center',
                            bbox=dict(facecolor='black', alpha=0.8, boxstyle='round,pad=0.3'))

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
                txt_turno.set_color(Colores[i])
                txt_turno.set_bbox(dict(facecolor='black', alpha=0.5, edgecolor='white', boxstyle='round, pad=0.2'))
                plt.pause(0.1)

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
                pasos_restantes = dado1 + dado2 # Total de movimientos permitidos
                
                txt_marcador1.set_text(f"{dado1}")
                txt_marcador2.set_text(f"{dado2}")
                txt_marcador1.set_color('white')
                txt_marcador2.set_color('white')
                plt.pause(0.5) 

                # --- LÓGICA DE MOVIMIENTO PASO A PASO ---
                while pasos_restantes > 0:
                    x, y = pos_x[i], pos_y[i]
                    v_actual = valores_actuales[i]
                    
                    # Dibujar rastro
                    rect = plt.Rectangle((x, y), 1, 1, facecolor=Colores[i], alpha=0.6)
                    ax.add_patch(rect)
                    plt.pause(0.05)

                    # Verificar si ya llegó a la meta
                    if v_actual >= 56:
                        txt_turno.set_text("¡GANADOR!")
                        txt_marcador1.set_text("WI")
                        txt_marcador2.set_text("N!")
                        print(f"¡EL JUGADOR {i+1} HA GANADO!")
                        partida_en_curso = False
                        break

                    proximo_paso = None
                    
                    # Prioridad 1: Siguiente número (avanzar a la siguiente casilla de la ruta)
                    for dx, dy in direcciones:
                        nx, ny = x + dx, y + dy
                        if 0 <= ny < len(self.laberintos[i]) and 0 <= nx < len(self.laberintos[i][0]):
                            token = self.laberintos[i][ny][nx]
                            if token != '#' and (nx, ny) not in visitados_por_jugador[i]:
                                try:
                                    if int(token) == v_actual + 1:
                                        proximo_paso = (nx, ny, int(token))
                                        break
                                except ValueError: pass
                    
                    # Prioridad 2: Mismo número (moverse dentro de la misma casilla si ocupa varios espacios)
                    if not proximo_paso:
                        for dx, dy in direcciones:
                            nx, ny = x + dx, y + dy
                            if 0 <= ny < len(self.laberintos[i]) and 0 <= nx < len(self.laberintos[i][0]):
                                token = self.laberintos[i][ny][nx]
                                if token != '#' and (nx, ny) not in visitados_por_jugador[i]:
                                    try:
                                        if int(token) == v_actual:
                                            proximo_paso = (nx, ny, int(token))
                                            break
                                    except ValueError: pass

                    if proximo_paso:
                        pos_x[i], pos_y[i], valores_actuales[i] = proximo_paso
                        visitados_por_jugador[i].add((pos_x[i], pos_y[i]))
                        pasos_restantes -= 1 # Resta un movimiento exitoso
                    else:
                        print(f"Jugador {i+1} bloqueado o sin ruta válida.")
                        break # Rompe el ciclo de pasos si se queda atorado
                
                if not partida_en_curso: break

        plt.ioff()
        plt.show()

# --- EJECUCIÓN ---
if __name__ == "__main__":
    plt.close('all') # Cerrar ventanas muertas
    rutas = ["TABLERO1.txt", "TABLERO2.txt", "TABLERO3.txt", "TABLERO4.txt"]
    # Asegúrate de que estos archivos existan en el mismo directorio donde ejecutas el script
    Poleana1 = Laberinto(16, 16, rutas, "Poleana-1.png")
    Poleana1.dfs6()
