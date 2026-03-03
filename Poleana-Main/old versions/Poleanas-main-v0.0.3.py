{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8f9444fb-a666-4a6c-a6eb-0b25694d67b3",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "ingrese cantidad de jugadores 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "¡Destino encontrado para el jugador 1!\n",
      "¡Destino encontrado para el jugador 2!\n",
      "¡Destino encontrado para el jugador 3!\n",
      "¡Destino encontrado para el jugador 4!\n"
     ]
    },
    {
     "ename": "SyntaxError",
     "evalue": "'break' outside loop (1848557414.py, line 102)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[1], line 102\u001b[0;36m\u001b[0m\n\u001b[0;31m    break\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m 'break' outside loop\n"
     ]
    }
   ],
   "source": [
    "import matplotlib\n",
    "matplotlib.use(\"TkAgg\")  # Esencial para la ventana animada\n",
    "import matplotlib.pyplot as plt\n",
    "from collections import deque\n",
    "import time\n",
    "\n",
    "class Laberinto:\n",
    "    def __init__(self, renglones, cols, ruta_txt, ruta_png):\n",
    "        self.renglones = renglones\n",
    "        self.cols = cols\n",
    "        self.ruta_txt = ruta_txt\n",
    "        self.ruta_png = ruta_png\n",
    "        self.jugadores = input(\"ingrese cantidad de jugadores\")\n",
    "        \n",
    "        # Cargar datos\n",
    "        self.laberinto = self.leer_txt()\n",
    "        self.imagen = plt.imread(self.ruta_png)\n",
    "        \n",
    "        # Coordenadas automáticas para probar rápido (puedes volver a poner input si quieres)\n",
    "        # Orden de jugadores: [Verde, Rojo, Azul, Amarillo]\n",
    "        # Nota: Uso base 1 porque tu código resta 1 después.\n",
    "        \n",
    "        # Orden: [Verde, Rojo, Azul, Amarillo]\n",
    "        # Nota: Coordenadas de matriz (0 a 15)\n",
    "        self.Orig_x = [15, 6, 0, 9]   # x origen\n",
    "        self.Orig_y = [9, 15, 6, 0]   # y origen\n",
    "        \n",
    "        self.Destin_x = [11, 2, 2, 11]  # x destino\n",
    "        self.Destin_y = [11, 11, 2, 2] # y destino\n",
    "\n",
    "    def leer_txt(self):\n",
    "        with open(self.ruta_txt, \"r\", encoding=\"utf-8\") as archivo:\n",
    "            return [list(linea.strip()) for linea in archivo]\n",
    "\n",
    "    def bfs(self):\n",
    "        # Convertimos la cantidad de jugadores a número entero\n",
    "        num_jugadores = int(self.jugadores) \n",
    "        Orig_x, Orig_y, Destin_x, Destin_y = self.Orig_x, self.Orig_y, self.Destin_x, self.Destin_y\n",
    "        \n",
    "        plt.ion()  # Activar modo interactivo\n",
    "        fig, ax = plt.subplots(figsize=(8, 8))\n",
    "        \n",
    "        ax.imshow(self.imagen, extent=[0, self.cols, self.renglones, 0])\n",
    "        ax.set_xticks(range(self.cols + 1))\n",
    "        ax.set_yticks(range(self.renglones + 1,0))\n",
    "        ax.grid(True, color='gray', linestyle='--', alpha=0.5)\n",
    "            \n",
    "        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]\n",
    "        Colores = ['lime', 'red', 'blue', 'yellow']\n",
    "        \n",
    "        # Iteramos sobre la cantidad de jugadores\n",
    "        for i in range(num_jugadores): \n",
    "            # CORRECCIÓN 1: Agregamos las coordenadas como tupla ()\n",
    "            cola = deque([(Orig_x[i], Orig_y[i])]) \n",
    "            \n",
    "            # CORRECCIÓN 2: Marcamos el ORIGEN como visitado, no el destino\n",
    "            visitados = {(Orig_x[i], Orig_y[i])} \n",
    "            \n",
    "            # Guardamos el destino actual para validarlo más fácil\n",
    "            start_x = Orig_x[i]\n",
    "            start_y = Orig_y[i]\n",
    "            meta_x = Destin_x[i]+1\n",
    "            meta_y = Destin_y[i]+1\n",
    "            # --- MARCADORES VISUALES ---\n",
    "            # El punto de origen (Círculo de color con borde negro)\n",
    "            ax.plot(start_x + 0.5, start_y + 0.5, 'o', markerfacecolor=Colores[i], markeredgecolor='black', markersize=12, zorder=10)\n",
    "            \n",
    "            # El punto de destino (Una X del color del jugador)\n",
    "            ax.text(meta_x + 0.5, meta_y + 0.5, 'X', color=Colores[i], ha='center', va='center', fontweight='bold', fontsize=16, zorder=10)\n",
    "            while cola:\n",
    "                x, y = cola.popleft()\n",
    "                    \n",
    "                # Dibujar el paso actual\n",
    "                rect = plt.Rectangle((x,y), 1, 1, facecolor=Colores[i], alpha=0.6)\n",
    "                ax.add_patch(rect)\n",
    "                    \n",
    "                # Forzar actualización de la ventana\n",
    "                fig.canvas.draw_idle()\n",
    "                fig.canvas.flush_events()\n",
    "                plt.pause(0.001) # Velocidad de la animación\n",
    "                \n",
    "                # CORRECCIÓN 4: Verificamos que llegó a SUS coordenadas de destino\n",
    "                if x == meta_x and y == meta_y:\n",
    "                    print(f\"¡Destino encontrado para el jugador {i+1}!\")\n",
    "                    break\n",
    "                    \n",
    "                for dx, dy in direcciones:\n",
    "                    nx, ny = x + dx, y + dy\n",
    "                    if 0 <= nx < self.renglones and 0 <= ny < self.cols:\n",
    "                        if self.laberinto[nx][ny] != '#' and (nx, ny) not in visitados:\n",
    "                            cola.append((nx, ny))\n",
    "                            visitados.add((nx, ny))\n",
    "                            \n",
    "        plt.ioff()\n",
    "        plt.show()\n",
    "        \n",
    "\n",
    "# --- EJECUCIÓN ---\n",
    "plt.close('all') # Cerrar ventanas muertas\n",
    "Poleana = Laberinto(16, 16, \"TABLERO.txt\", \"Poleana-1.png\")\n",
    "Poleana.bfs()\n",
    "break"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "714a680f-01cc-4d52-b591-3d66857caca3",
   "metadata": {},
   "source": [
    "#### "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee144e03-9c47-44f1-ba3e-df0dc4b7cefb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
