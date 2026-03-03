import matplotlib
matplotlib.use("TkAgg")  # Esencial para la ventana animada
import matplotlib.pyplot as plt
from collections import deque
import time

class Laberinto:
    def __init__(self, renglones, cols, ruta_txt, ruta_png):
        self.renglones = renglones
        self.cols = cols
        self.ruta_txt = ruta_txt
        self.ruta_png = ruta_png
        self.jugadores = input("ingrese cantidad de jugadores")
        
        # Cargar datos
        self.laberinto = self.leer_txt()
        self.imagen = plt.imread(self.ruta_png)
        
        # Coordenadas automáticas para probar rápido (puedes volver a poner input si quieres)
        # Orden de jugadores: [Verde, Rojo, Azul, Amarillo]
        # Nota: Uso base 1 porque tu código resta 1 después.
        
        # Orden: [Verde, Rojo, Azul, Amarillo]
        # Nota: Coordenadas de matriz (0 a 15)
        self.Orig_x = [15, 6, 0, 9]   # x origen
        self.Orig_y = [9, 15, 6, 0]   # y origen
        
        self.Destin_x = [11, 2, 2, 11]  # x destino
        self.Destin_y = [11, 11, 2, 2] # y destino

    def leer_txt(self):
        with open(self.ruta_txt, "r", encoding="utf-8") as archivo:
            return [list(linea.strip()) for linea in archivo]

    def bfs(self):
        # Convertimos la cantidad de jugadores a número entero
        num_jugadores = int(self.jugadores) 
        Orig_x, Orig_y, Destin_x, Destin_y = self.Orig_x, self.Orig_y, self.Destin_x, self.Destin_y
        
        plt.ion()  # Activar modo interactivo
        fig, ax = plt.subplots(figsize=(8, 8))
        
        ax.imshow(self.imagen, extent=[0, self.cols, self.renglones, 0])
        ax.set_xticks(range(self.cols + 1))
        ax.set_yticks(range(self.renglones + 1,0))
        ax.grid(True, color='gray', linestyle='--', alpha=0.5)
            
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        Colores = ['lime', 'red', 'blue', 'yellow']
        
        # Iteramos sobre la cantidad de jugadores
        for i in range(num_jugadores): 
            # CORRECCIÓN 1: Agregamos las coordenadas como tupla ()
            cola = deque([(Orig_x[i], Orig_y[i])]) 
            
            # CORRECCIÓN 2: Marcamos el ORIGEN como visitado, no el destino
            visitados = {(Orig_x[i], Orig_y[i])} 
            
            # Guardamos el destino actual para validarlo más fácil
            start_x = Orig_x[i]
            start_y = Orig_y[i]
            meta_x = Destin_x[i]+1
            meta_y = Destin_y[i]+1
            # --- MARCADORES VISUALES ---
            # El punto de origen (Círculo de color con borde negro)
            ax.plot(start_x + 0.5, start_y + 0.5, 'o', markerfacecolor=Colores[i], markeredgecolor='black', markersize=12, zorder=10)
            
            # El punto de destino (Una X del color del jugador)
            ax.text(meta_x + 0.5, meta_y + 0.5, 'X', color=Colores[i], ha='center', va='center', fontweight='bold', fontsize=16, zorder=10)
            while cola:
                x, y = cola.popleft()
                    
                # Dibujar el paso actual
                rect = plt.Rectangle((x,y), 1, 1, facecolor=Colores[i], alpha=0.6)
                ax.add_patch(rect)
                    
                # Forzar actualización de la ventana
                fig.canvas.draw_idle()
                fig.canvas.flush_events()
                plt.pause(0.001) # Velocidad de la animación
                
                # CORRECCIÓN 4: Verificamos que llegó a SUS coordenadas de destino
                if x == meta_x and y == meta_y:
                    print(f"¡Destino encontrado para el jugador {i+1}!")
                    break
                    
                for dx, dy in direcciones:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.renglones and 0 <= ny < self.cols:
                        if self.laberinto[nx][ny] != '#' and (nx, ny) not in visitados:
                            cola.append((nx, ny))
                            visitados.add((nx, ny))
                            
        plt.ioff()
        plt.show()
        

# --- EJECUCIÓN ---
plt.close('all') # Cerrar ventanas muertas
Poleana = Laberinto(16, 16, "TABLERO.txt", "Poleana-1.png")
Poleana.bfs()
