{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8f9444fb-a666-4a6c-a6eb-0b25694d67b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1 1\n",
      " 13 13\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "¡Destino encontrado!\n"
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
    "        \n",
    "        # Cargar datos\n",
    "        self.laberinto = self.leer_txt()\n",
    "        self.imagen = plt.imread(self.ruta_png)\n",
    "        \n",
    "        # Ajustar puertas manualmente\n",
    "        self.ajustar_puertas()\n",
    "\n",
    "        # Coordenadas automáticas para probar rápido (puedes volver a poner input si quieres)\n",
    "        self.x1, self.y1 = [int(x) for x in input().split()]\n",
    "        self.x2, self.y2 = [int(x) for x in input().split()]\n",
    "        self.laberinto[self.x1-1][self.y1-1] = 'O'\n",
    "        self.laberinto[self.x2-1][self.y2-1] = 'D'\n",
    "\n",
    "    def leer_txt(self):\n",
    "        with open(self.ruta_txt, \"r\", encoding=\"utf-8\") as archivo:\n",
    "            return [list(linea.strip()) for linea in archivo]\n",
    "\n",
    "    def ajustar_puertas(self):\n",
    "        for col in range(5, 10):\n",
    "            self.laberinto[1][col] = '.'\n",
    "            self.laberinto[14][col] = '.'\n",
    "\n",
    "    def bfs(self):\n",
    "        plt.ion()  # Activar modo interactivo\n",
    "        fig, ax = plt.subplots(figsize=(8, 8))\n",
    "        \n",
    "        ax.imshow(self.imagen, extent=[0, self.cols, self.renglones, 0])\n",
    "        ax.set_xticks(range(self.cols + 1))\n",
    "        ax.set_yticks(range(self.renglones + 1))\n",
    "        ax.grid(True, color='gray', linestyle='--', alpha=0.5)\n",
    "        \n",
    "        cola = deque([(self.x1 - 1, self.y1 - 1)])\n",
    "        visitados = {(self.x1 - 1, self.y1 - 1)}\n",
    "        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]\n",
    "\n",
    "        while cola:\n",
    "            x, y = cola.popleft()\n",
    "            \n",
    "            # Dibujar el paso actual\n",
    "            rect = plt.Rectangle((y, x), 1, 1, facecolor='lime', alpha=0.5)\n",
    "            ax.add_patch(rect)\n",
    "            \n",
    "            # Forzar actualización de la ventana\n",
    "            fig.canvas.draw_idle()\n",
    "            fig.canvas.flush_events()\n",
    "            plt.pause(0.01) # Velocidad de la animación\n",
    "            \n",
    "            if self.laberinto[x][y] == 'D':\n",
    "                print(\"¡Destino encontrado!\")\n",
    "                break\n",
    "            \n",
    "            for dx, dy in direcciones:\n",
    "                nx, ny = x + dx, y + dy\n",
    "                if 0 <= nx < self.renglones and 0 <= ny < self.cols:\n",
    "                    if self.laberinto[nx][ny] != '#' and (nx, ny) not in visitados:\n",
    "                        cola.append((nx, ny))\n",
    "                        visitados.add((nx, ny))\n",
    "        \n",
    "        plt.ioff()\n",
    "        plt.show()\n",
    "\n",
    "# --- EJECUCIÓN ---\n",
    "plt.close('all') # Cerrar ventanas muertas\n",
    "Poleana = Laberinto(16, 16, \"TABLERO.txt\", \"Poleana-1.png\")\n",
    "Poleana.bfs()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "714a680f-01cc-4d52-b591-3d66857caca3",
   "metadata": {},
   "outputs": [],
   "source": []
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
