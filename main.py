import pygame
from time import sleep
from sys import platform

# Windows RG Build 204 recreated in Python
# Recreación en Python para un proyecto final de un curso de Python.

pygame.init()

Fondo=(0,153,255)
BarraDeTareas=(204,204,204)
Width=800
Height=600

ventana = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('Windows RG Build 207')

# white color 
color_blanco = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 

color_negro = (0,0,0)

StartingPosition2=145

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

class Window:
    def __init__(self, x, y, w, h, title=''):
        self.x = x
        self.y = y
        self.color = BarraDeTareas
        self.black = color_negro
        self.white = color_blanco
        self.blue = "#0000FF"
        
        self.title = title

        # Main Window
        self.window = pygame.Rect(x, y+32, w, h)

        # Frame Decorations
        self.frame2 = pygame.Rect(x-2, y-2, w+4, h+36)
        self.frame1 = pygame.Rect(x-2, y-2, w+2, h+34)

        # Title Bar
        self.barShade = pygame.Rect(x, y+3, w, 32)
        self.bar = pygame.Rect(x, y, w, 32)
        

    def open(self, screen):
        # Frame Decorations
        pygame.draw.rect(screen, self.black, self.frame2)
        pygame.draw.rect(screen, self.white, self.frame1)
        
        # Main Window
        pygame.draw.rect(screen, self.color, self.window)

        # Title Bar
        pygame.draw.rect(screen, self.black , self.barShade)
        pygame.draw.rect(screen, self.blue, self.bar)
        

        TextObject(size=bigfontsize-20, text=self.title, color=self.white, font=normalfontstyle, position=(self.x+3,self.y+3), window=ventana, bold=True)
        return True

VentanaPrueba=Window(Width/4, Height/4, 200, 200, "Caca")

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        # Main
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

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
            
            if 6 <= mouse[0] <= 6+130 and 554 <= mouse[1] <= 554+40 and ManteniendoApretado == True and MenuInicioPresionado == False: 
                MenuInicioPresionado=True
                ManteniendoApretado=False
            else:
                MenuInicioPresionado=False
                ManteniendoApretado=False

    # fills the screen with a color 
    ventana.fill(Fondo) 

    if MenuInicioPresionado == True:
        # Geometria del Menu de Inicio
        pygame.draw.rect(ventana,color_blanco,(0, 145, 354, 437))
        pygame.draw.rect(ventana,color_negro,(4, 145, 352, 437))
        pygame.draw.rect(ventana,BarraDeTareas,(2, 145, 352, 400))

        for a in range(145,545,40):
            if 2 <= mouse[0] <= 352 and 140 <= mouse[1] <= a+40: 
                pygame.draw.rect(ventana,color_blanco,(2, a, 352, 40))
                break

        # Botones
        #pygame.draw.rect(ventana,color_blanco,(2, StartingPosition2, 352, 40))
        StartingPosition2+=40
        if StartingPosition2 == 545:
            StartingPosition2=145
        

        # Opciones
        StartingPosition=145
        for i in range(len(MenuOptions)):
            if i != 0:
                StartingPosition+=40
            TextObject(size=bigfontsize-8, text=str(MenuOptions[i]), color=color_negro, font=normalfontstyle, position=(60,StartingPosition), window=ventana)
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    
    # Barra de Tareas
    pygame.draw.rect(ventana,BarraDeTareas,[0,548,800,52]) 

    # if mouse is hovered on a button it 
    # changes to lighter shade  

    VentanaPrueba.open(ventana)

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
    clock.tick(60)
    pygame.display.update() 