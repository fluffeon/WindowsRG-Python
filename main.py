import pygame
import os
from time import sleep
from sys import platform

# Windows RG Build 204 recreated in Python
# Recreación en Python para un proyecto final de un curso de Python.

# Things that happen on Windows
gameEvents={
    "myDocumentsOpen": False,
    'startMenuOpen': False,
    'windowCurrentlyOpen': False,
    'shuttingDown': False,
}


ProgramDirectory=os.path.dirname(__file__)
IconDirectory=os.path.join(ProgramDirectory, 'Assets', 'Icons')

pygame.init()

# Icons
Asset={}

# Load all assets in Assets folder / Cargar todos los assets en la carpeta Assets
for icon in os.listdir(IconDirectory):
    if icon.lower().endswith(('.png', '.jpeg', '.jpg')):
        AssetTemp=pygame.image.load(os.path.join(IconDirectory, icon))
        Asset[f"Icon-{icon[0: -4]}"]=pygame.transform.scale(AssetTemp, (50, 50))

Asset['StartMenu']=pygame.image.load(os.path.join(ProgramDirectory, 'Assets', 'StartMenu.png'))
Asset['StartMenu']=pygame.transform.scale(Asset['StartMenu'], (52, 28))

print(Asset)

#for icon in AssetDirectory:

Fondo=(0,153,255)
BarraDeTareas=(204,204,204)
Width=800
Height=600

WindowsRG = pygame.display.set_mode((Width,Height))
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
def GenerateText(size,text,color,font,x,y,window,bold=False,italic=False,underline=False,strikethrough=False,center=False):
    fontstyle=pygame.font.SysFont(font,size)
    position=(x,y)

    if bold == True:
        fontstyle.bold=True
    
    if italic == True:
        fontstyle.italic=True
    
    if underline == True:
        fontstyle.underline=True
    
    if strikethrough == True:
        fontstyle.strikethrough=True

    if center == True:
        actualtext=fontstyle.render(text, True, color)
        text_rect = actualtext.get_rect(center=(x/2, y/2))
        window.blit(actualtext, text_rect) 
    else:
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

class Window:

    closeText=pygame.font.SysFont(normalfontstyle,bigfontsize-15)
    closeTexttoBlit=closeText.render("X", True, color_negro)

    def __init__(self, x, y, w, h, screen, title=''):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = BarraDeTareas
        self.black = color_negro
        self.white = color_blanco
        self.blue = "#0000FF"
        self.screen = screen
        
        self.title = title

        # Main Window
        self.window = pygame.Rect(x, y+32, w, h)

        # Frame Decorations
        self.frame2 = pygame.Rect(x-2, y-2, w+4, h+36)
        self.frame1 = pygame.Rect(x-2, y-2, w+2, h+34)

        # Title Bar
        self.barShade = pygame.Rect(x, y+3, w, 32)
        self.bar = pygame.Rect(x, y, w, 32)

        # Close Button
        self.closeButtonShade1 = pygame.Rect(x+w-32, y+4, 30, 28)
        self.closeButtonShade2 = pygame.Rect(x+w-32, y+2, 28, 28)

        self.closeButton = pygame.Rect(x+w-30, y+4, 26, 26)

        self.closeButtonHeld = False
        self.closeButtonPressed = False
        

    def open(self):
        # Frame Decorations
        pygame.draw.rect(self.screen, self.black, self.frame2)
        pygame.draw.rect(self.screen, self.white, self.frame1)
        
        # Main Window
        pygame.draw.rect(self.screen, self.color, self.window)

        # Title Bar
        pygame.draw.rect(self.screen, self.black , self.barShade)
        pygame.draw.rect(self.screen, self.blue, self.bar)

        # Close Button
        if self.closeButtonHeld == False:
            pygame.draw.rect(self.screen, self.black, self.closeButtonShade1)
            pygame.draw.rect(self.screen, self.white, self.closeButtonShade2)
        else:
            pygame.draw.rect(self.screen, self.white, self.closeButtonShade1)
            pygame.draw.rect(self.screen, self.black, self.closeButtonShade2)
        pygame.draw.rect(self.screen, self.color, self.closeButton)

        self.screen.blit(self.closeTexttoBlit, (self.x+self.w-27, self.y+1)) 
        
        GenerateText(size=bigfontsize-20, text=self.title, color=self.white, font=normalfontstyle, x=self.x+4, y=self.y+4, window=self.screen, bold=True)
        return True

    def checkIfOpen(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.closeButton.collidepoint(event.pos):
                self.closeButtonHeld = True
            else:
                self.closeButtonHeld = False

        if event.type == pygame.MOUSEBUTTONUP:
            if self.closeButtonHeld == True and self.closeButton.collidepoint(event.pos):
                self.closeButtonPressed = True
                self.closeButtonHeld = False
            else:
                self.closeButtonPressed = False
                self.closeButtonHeld = False

        if self.closeButtonPressed == True:
            self.closeButtonPressed = False
            return False
        else:
            return True

    def close(self):
        self.closeButtonPressed = True

class Button:
    
    def __init__(self, x, y, screen, label='', function="", h=None, w=None, holdButtonifPressed=False, startButton=False):
        self.x = x
        self.y = y
        self.color = BarraDeTareas
        self.black = color_negro
        self.white = color_blanco
        self.blue = "#0000FF"
        self.screen = screen
        self.holdButtonifPressed = holdButtonifPressed
        self.startButton=startButton
        if holdButtonifPressed == True:
            self.buttonToggle = False
        else:
            self.buttonToggle = None

        self.label = label

        self.fontstyle=pygame.font.SysFont(normalfontstyle,25)
        self.actualtext=self.fontstyle.render(label, True, self.black)
        self.text_rect = self.actualtext.get_rect(center=(self.x, self.y)) 

        self.textx=self.text_rect[0]
        self.texty=self.text_rect[1]
        self.textweight=self.text_rect[2]
        self.textheight=self.text_rect[3]

        # Button
        if h == None and w == None:
            self.buttonShade1 = pygame.Rect(self.textx-8, self.texty-2, self.textweight+18, self.textheight+4)
            self.buttonShade2 = pygame.Rect(self.textx-8, self.texty-2, self.textweight+16, self.textheight+2)

            self.button = pygame.Rect(self.textx-6, self.texty, self.textweight+14, self.textheight)
        else:
            self.h = h
            self.w = w
            self.buttonShade2 = pygame.Rect(self.x-2, self.y-2, self.w+2, self.h+2)
            self.buttonShade1 = pygame.Rect(self.x-2, self.y-2, self.w+4, self.h+4)
            
            self.button = pygame.Rect(self.x, self.y, self.w, self.h)

        self.buttonHeld = False
        self.buttonPressed = False
    
    def show(self):
        if self.holdButtonifPressed == True:
            if self.buttonHeld == True or self.buttonToggle == True:
                pygame.draw.rect(self.screen, self.white, self.buttonShade1)
                pygame.draw.rect(self.screen, self.black, self.buttonShade2)
            elif self.buttonPressed == False or self.buttonToggle == False:
                pygame.draw.rect(self.screen, self.black, self.buttonShade1)
                pygame.draw.rect(self.screen, self.white, self.buttonShade2)
        else:
            if self.buttonHeld == False:
                pygame.draw.rect(self.screen, self.black, self.buttonShade1)
                pygame.draw.rect(self.screen, self.white, self.buttonShade2)
            else:
                pygame.draw.rect(self.screen, self.white, self.buttonShade1)
                pygame.draw.rect(self.screen, self.black, self.buttonShade2)

        pygame.draw.rect(self.screen, self.color, self.button)
        self.screen.blit(self.actualtext, self.text_rect)

    def checkPress(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.button.collidepoint(event.pos) and gameEvents['startMenuOpen'] == False and self.startButton == False:
                self.buttonHeld = True
            elif self.button.collidepoint(event.pos) and self.startButton == True:
                self.buttonHeld = True
            else:
                self.buttonHeld = False

        if event.type == pygame.MOUSEBUTTONUP:
            if self.buttonHeld == True and self.button.collidepoint(event.pos):
                self.buttonPressed = True
                self.buttonHeld = False
                if self.startButton == True:
                    if gameEvents['startMenuOpen'] == False:
                        self.buttonToggle = False
                    else:
                        self.buttonToggle = True
                elif self.holdButtonifPressed == True and self.buttonToggle == False:
                    self.buttonToggle = True
                elif self.holdButtonifPressed == True and self.buttonToggle == True:
                    self.buttonToggle = False
            else:
                if self.startButton == True:
                    if gameEvents['startMenuOpen'] == False:
                        self.buttonToggle = False
                    else:
                        self.buttonToggle = True
                self.buttonPressed = False
                self.buttonHeld = False

        if self.buttonPressed == True:
            self.buttonPressed = False
            return False
        else:
            return True

BotonPrueba=Button(x=350, y=286, screen=WindowsRG, label='Search')
BotonPrueba3=Button(x=600, y=286, screen=WindowsRG, label='Caca')

BotonPrueba2=Button(x=450, y=286, w=10, h=200, screen=WindowsRG, holdButtonifPressed=True)

StartButton=Button(x=5, y=564, w=125, h=31, screen=WindowsRG, holdButtonifPressed=True, startButton=True)

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

# 
bigWindow=Window(10, 10, Width-20, Height-105, WindowsRG, "My Documents")

while True: 
      
    for event in pygame.event.get(): 
          
        if event.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if event.type == pygame.MOUSEBUTTONUP:
            
            if 6 <= mouse[0] <= 6+130 and 554 <= mouse[1] <= 554+40 and gameEvents['startMenuOpen'] == False: 
                gameEvents['startMenuOpen'] = True
            else:
                gameEvents['startMenuOpen'] = False

        if bigWindow.checkIfOpen(event) == False:
            gameEvents['myDocumentsOpen'] = False

        BotonPrueba.checkPress(event)
        BotonPrueba2.checkPress(event)
        BotonPrueba3.checkPress(event)
        StartButton.checkPress(event)

    # fills the screen with a color 
    WindowsRG.fill(Fondo) 

    if gameEvents['myDocumentsOpen'] == True:
        bigWindow.open()
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    
    # Barra de Tareas
    pygame.draw.rect(WindowsRG,BarraDeTareas,[0,558,800,42]) 

    # if mouse is hovered on a button it 
    # changes to lighter shade  
    StartButton.show()
    BotonPrueba.show()
    BotonPrueba2.show()
    BotonPrueba3.show()

    if gameEvents['startMenuOpen'] == True:
        # Geometria del Menu de Inicio
        pygame.draw.rect(WindowsRG,color_blanco,(0, 145, 356, 402))
        pygame.draw.rect(WindowsRG,color_negro,(2, 145, 354, 402))
        pygame.draw.rect(WindowsRG,BarraDeTareas,(2, 145, 352, 400))

        for a in range(145,545,40):
            if 2 <= mouse[0] <= 352 and 140 <= mouse[1] <= a+40: 
                pygame.draw.rect(WindowsRG,color_blanco,(2, a, 352, 40))
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
            GenerateText(size=bigfontsize-8, text=str(MenuOptions[i]), color=color_negro, font=normalfontstyle, x=60, y=StartingPosition, window=WindowsRG)
      
    # superimposing the text onto our button 

    # Start Button
    WindowsRG.blit(Asset["StartMenu"], (8, 564))
    GenerateText(size=bigfontsize-6, text="Start", color=color_negro, font=bigfontstyle, x=185, y=1160, window=WindowsRG, center=True)

    # Hour
    GenerateText(size=normalfontsize, text="3:00 AM", color=color_negro, font=normalfontstyle, x=700, y=562, window=WindowsRG)

    WindowsRG.blit(Asset["Icon-Computer"], (33, 10))
    GenerateText(size=normalfontsize-6, text="My Computer", color=color_negro, font=normalfontstyle, x=120, y=150, window=WindowsRG, center=True)

    WindowsRG.blit(Asset["Icon-MyDocuments"], (33, 100))
    GenerateText(size=normalfontsize-6, text="My Documents", color=color_negro, font=normalfontstyle, x=120, y=330, window=WindowsRG, center=True)

    WindowsRG.blit(Asset["Icon-RecycleBin"], (33, 190))
    GenerateText(size=normalfontsize-6, text="Recycle Bin", color=color_negro, font=normalfontstyle, x=120, y=510, window=WindowsRG, center=True)

    WindowsRG.blit(Asset["Icon-MediaPlayer"], (33, 280))
    GenerateText(size=normalfontsize-6, text="Windows Media", color=color_negro, font=normalfontstyle, x=120, y=685, window=WindowsRG, center=True)
    GenerateText(size=normalfontsize-6, text="Player", color=color_negro, font=normalfontstyle, x=120, y=720, window=WindowsRG, center=True)
    
      
    # updates the frames of the game 
    clock.tick(60)
    pygame.display.update() 