import pygame
from sys import platform

# Windows RG Build 204 recreated in Python
# Recreación en Python para un proyecto final de un curso de Python.

pygame.init()

Fondo=(0,153,255)
BarraDeTareas=(204,204,204)
Ancho=800
Alto=600

ventana = pygame.display.set_mode((Ancho,Alto))
pygame.display.set_caption('Windows RG Build 207')

# white color 
color_blanco = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 

color_negro = (0,0,0)
  
# stores the width of the 
# screen into a variable 
width = ventana.get_width() 
  
# stores the height of the 
# screen into a variable 
height = ventana.get_height() 
  
# defining a font 

MenuOptions=['Word', 'Windows Update', 'Crash', 'Solitaire', 'Order Food', 'Go Online', 'Paint', 'Help', 'Reboot', 'Shut Down']
  
# Function to render texts however I like
def TextObject(size,text,color,font,position,window,bold=False,italic=False,underline=False,strikethrough=False):
    fontstyle=pygame.font.SysFont(font,size)
    if bold == True:
        fontstyle.bold=True
    
    if italic == True:
        fontstyle.italic=True
    
    if underline == True:
        fontstyle.underline=True
    
    if strikethrough == True:
        fontstyle.strikethrough=True

    actualtext=fontstyle.render(text, True, color)
    window.blit(actualtext, position) 

if platform != "linux":
    normalfontsize = 20
    normalfontstyle = 'Arial'
    bigfontsize = 20
    bigfontstyle = 'Arial'
else:
    smallfontsize = 22
    smallfontstyle = 'Liberation Sans'
    normalfontsize = 22
    normalfontstyle = 'Liberation Sans'
    bigfontsize = 42
    bigfontstyle = 'Corbel'

clock = pygame.time.Clock()

MenuInicioPresionado=False
ManteniendoApretado=False
while True: 
      
    for event in pygame.event.get(): 
          
        if event.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            # Boton
            if 6 <= mouse[0] <= 6+130 and 554 <= mouse[1] <= 554+40: 
                if ManteniendoApretado == True:
                    ManteniendoApretado=False
                else:
                    ManteniendoApretado=True
        
        if event.type == pygame.MOUSEBUTTONUP:
            if 6 <= mouse[0] <= 6+130 and 554 <= mouse[1] <= 554+40 and ManteniendoApretado == True: 
                if MenuInicioPresionado == False:
                    MenuInicioPresionado=True
                else:
                    MenuInicioPresionado=False
                ManteniendoApretado=False
            else:
                MenuInicioPresionado=False
                ManteniendoApretado=False

    # fills the screen with a color 
    ventana.fill(Fondo) 

    if MenuInicioPresionado == True:
        # Geometria del Menu de Inicio
        pygame.draw.rect(ventana,color_blanco,(0, 145, 352, 402))
        pygame.draw.rect(ventana,color_negro,(2, 145, 352, 404))
        pygame.draw.rect(ventana,BarraDeTareas,(2, 145, 350, 400))

        # Botones
        pygame.draw.rect(ventana,color_blanco,(2, 145, 350, 50))

        # Opciones
        StartingPosition=145
        for i in range(len(MenuOptions)):
            if i != 0:
                StartingPosition+=40
            TextObject(size=bigfontsize-4, text=str(MenuOptions[i]), color=color_negro, font=normalfontstyle, position=(60,StartingPosition), window=ventana)
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    
    # Barra de Tareas
    pygame.draw.rect(ventana,BarraDeTareas,[0,548,800,52]) 

    # if mouse is hovered on a button it 
    # changes to lighter shade  

    # Button 
    #if 6 <= mouse[0] <= 6+130 and 554 <= mouse[1] <= 554+40:
    if MenuInicioPresionado == True or ManteniendoApretado == True:
        pygame.draw.rect(ventana,color_blanco,[4,552,134,44]) 
        pygame.draw.rect(ventana,color_negro,[4,552,132,42]) 
          
    else: 
        pygame.draw.rect(ventana,color_negro,[4,552,134,44]) 
        pygame.draw.rect(ventana,color_blanco,[4,552,132,42]) 
    
    pygame.draw.rect(ventana,BarraDeTareas,[6,554,130,40]) 
      
    # superimposing the text onto our button 

    # Start Button
    TextObject(size=bigfontsize, text="Start", color=color_negro, font=bigfontstyle, position=(60,560), window=ventana)

    # Hour
    TextObject(size=normalfontsize, text="3:00 AM", color=color_negro, font=normalfontstyle, position=(700,562), window=ventana)
      
    # updates the frames of the game 
    pygame.display.update() 