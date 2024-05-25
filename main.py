import pygame

# Windows RG Build 204 recreated in Python
# Recreación en Python para un proyecto final de un curso de Python.

Fondo=(0,153,255)
BarraDeTareas=(204,204,204)
Ancho=550
Alto=400

ventana = pygame.display.set_mode((Ancho,Alto))

clock = pygame.time.Clock()

while True:
    ventana.fill(Fondo)