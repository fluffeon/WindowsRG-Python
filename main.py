#!/sbin/python
import os
from sys import argv
from sys import platform
from time import sleep

Arguments=(argv[1:])

if "--help" in Arguments:
    print("Windows RG Build 207 en Pygame / Windows RG Build 207 in Pygame")
    print("Proyecto Final")
    print()
    print("Arguments:")
    print("     --help      Mostrar ayuda / Show help")
    print("     --show-fps  Mostrar FPS / Show FPS")
    exit()

# Windows RG Build 204 recreated in Python
# Recreación en Python para un proyecto final de un curso de Python.

Fondo=(0,153,255)
BarraDeTareas=(204,204,204)
Width=800
Height=600

# Things that happen on Windows
global gameEvent
gameEvent={
    "explorerOpen": False,
    'startMenuOpen': False,
    'windowCurrentlyOpen': False,
    'shuttingDown': False,
    'startMenuSelection': 0,
    'currentExplorerPage': None,
    'currentWindow': None,
}


ProgramDirectory=os.path.dirname(__file__)
IconDirectory=os.path.join(ProgramDirectory, 'Assets', 'Icons')
VideoDirectory=os.path.join(ProgramDirectory, 'Assets', 'Video')

import pygame
from pygamevideo import Video

pygame.init()
WindowsRG = pygame.display.set_mode((Width,Height))

# Icons
Asset={}

# Load all assets in Assets folder / Cargar todos los assets en la carpeta Assets
for icon in os.listdir(IconDirectory):
    if icon.lower().endswith(('.png', '.jpeg', '.jpg')):
        AssetTemp=pygame.image.load(os.path.join(IconDirectory, icon))
        Asset[f"Icon-{icon[0: -4]}"] = pygame.transform.scale(AssetTemp, (50, 50))

for video in os.listdir(VideoDirectory):
    if video.lower().endswith(('.mp4')):
        Asset[f"Video-{icon[0: -4]}"] = Video(os.path.join(VideoDirectory, video))

Asset['StartMenu'] = pygame.image.load(os.path.join(ProgramDirectory, 'Assets', 'StartMenu.png'))
Asset['StartMenu'] = pygame.transform.scale(Asset['StartMenu'], (52, 28))

print(Asset)

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

print(MenuOptions)

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

        self.closeButtonEnabled = True
        
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
        self.closed = True
        

    def openWindow(self, title=''):
        self.closed = False
        if len(title) != 0:
            self.title = title
    
    def render(self):
        if self.closed == False:
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
                pygame.draw.rect(self.screen, self.color, self.closeButton)
            else:
                pygame.draw.rect(self.screen, self.white, self.closeButtonShade1)
                pygame.draw.rect(self.screen, self.black, self.closeButtonShade2)
                pygame.draw.rect(self.screen, self.color, self.closeButton)

            self.screen.blit(self.closeTexttoBlit, (self.x+self.w-27, self.y+1)) 
        
            GenerateText(size=bigfontsize-20, text=self.title, color=self.white, font=normalfontstyle, x=self.x+4, y=self.y+4, window=self.screen, bold=True)

    def checkPress(self, event):
        if self.closeButtonEnabled == True:
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
                self.closed = True
                self.closeButtonPressed = False
        
    def windowTitle(self):
        return self.title

    def checkIfOpen(self):
        if self.closed == True:
            return False
        else:
            return True

    def closeWindow(self):
        self.closed = True

    def disableCloseButton(self):
        self.closeButtonEnabled = False

    def enableCloseButton(self):
        self.closeButtonEnabled = True

class Button:
    
    def __init__(self, x, y, screen, label='', function=None, functionArguments=[], h=None, w=None, color=(204,204,204), hoverColor=(204,204,204), holdColor=(204,204,204), holdButtonifPressed=False, startButton=False, shading=True, shadingColor1=(0,0,0), shadingColor2=(255,255,255), textColor=(0,0,0)):
        self.x = x
        self.y = y
        self.color = color
        self.shadingColor1 = shadingColor1
        self.shadingColor2 = shadingColor2
        self.textColor = textColor
        self.hoverColor = hoverColor
        self.holdColor = holdColor
        self.screen = screen
        self.function = function
        self.functionArguments = functionArguments
        self.holdButtonifPressed = holdButtonifPressed
        self.startButton=startButton
        self.shading=shading
        self.buttonHover = False
        if holdButtonifPressed == True:
            self.buttonToggle = False
        else:
            self.buttonToggle = None

        self.label = label
        self.buttonHidden = False

        self.fontstyle=pygame.font.SysFont(normalfontstyle,25)
        self.actualtext=self.fontstyle.render(label, True, self.textColor)
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
    
    def render(self):
        if self.buttonHidden == False:
            if self.holdButtonifPressed == True and self.shading == True:
                if self.buttonHeld == True or self.buttonToggle == True:
                    pygame.draw.rect(self.screen, self.shadingColor2, self.buttonShade1)
                    pygame.draw.rect(self.screen, self.shadingColor1, self.buttonShade2)
                elif self.buttonPressed == False or self.buttonToggle == False:
                    pygame.draw.rect(self.screen, self.shadingColor1, self.buttonShade1)
                    pygame.draw.rect(self.screen, self.shadingColor2, self.buttonShade2)
            elif self.shading == True:
                if self.buttonHeld == False:
                    pygame.draw.rect(self.screen, self.shadingColor1, self.buttonShade1)
                    pygame.draw.rect(self.screen, self.shadingColor2, self.buttonShade2)
                else:
                    pygame.draw.rect(self.screen, self.shadingColor2, self.buttonShade1)
                    pygame.draw.rect(self.screen, self.shadingColor1, self.buttonShade2)
        
            if self.buttonHover == True and self.buttonHeld == True and gameEvent['startMenuOpen'] == False:
                pygame.draw.rect(self.screen, self.holdColor, self.button)
            elif self.buttonHover == True and gameEvent['startMenuOpen'] == False:
                pygame.draw.rect(self.screen, self.hoverColor, self.button)
            else:
                pygame.draw.rect(self.screen, self.color, self.button)
            self.screen.blit(self.actualtext, self.text_rect)

    def checkPress(self, event):
        if self.buttonHidden == False:
            if self.button.collidepoint(pygame.mouse.get_pos()):
                self.buttonHover = True
            else:
                self.buttonHover = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.collidepoint(event.pos) and gameEvent['startMenuOpen'] == False and self.startButton == False:
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
                        if gameEvent['startMenuOpen'] == False:
                            self.buttonToggle = False
                        else:
                            self.buttonToggle = True
                    elif self.holdButtonifPressed == True and self.buttonToggle == False:
                        self.buttonToggle = True
                    elif self.holdButtonifPressed == True and self.buttonToggle == True:
                        self.buttonToggle = False
                else:
                    if self.startButton == True:
                        if gameEvent['startMenuOpen'] == False:
                            self.buttonToggle = False
                        else:
                            self.buttonToggle = True
                    self.buttonPressed = False
                    self.buttonHeld = False

            if self.buttonPressed == True:
                self.buttonPressed = False
                if self.function != None and len(self.functionArguments) != 0:
                    self.function(*self.functionArguments)
                elif self.function != None:
                    self.function()
                return False
            else:
                return True

    def hideButton(self):
        self.buttonHidden = True
        self.buttonHover = False
        self.buttonHeld = False
        self.buttonPressed = False
        
    def showButton(self):
        self.buttonHidden = False

def setGameEvent(event, value):
    gameEvent[event]=value
    
DesktopIconHover=(0,153-30,255-30),
DesktopIconHold=(0,153-60,255-60),

window={
    'explorerWindow': Window(125, 10, Width-130, Height-95, WindowsRG, gameEvent['currentWindow'])
    }

button={
    # ---------
    #  BUTTONS 
    # ---------

    # Test Buttons
    'BotonPrueba': Button(x=350, y=286, screen=WindowsRG, label='Search', shading=False, hoverColor=(100, 100, 100)),
    'BotonPrueba2': Button(x=450, y=286, w=10, h=200, screen=WindowsRG, holdButtonifPressed=True, hoverColor=(100, 100, 100)),
    'BotonPrueba3': Button(x=600, y=286, screen=WindowsRG, label='Caca', hoverColor=(100, 100, 100)),

    # Start Button
    'StartButton': Button(x=5, y=564, w=125, h=31, screen=WindowsRG, holdButtonifPressed=True, startButton=True),

    # Desktop Icons
    'MyComputerButton': Button(x=0, y=0, w=120, h=90, screen=WindowsRG, shading=False, color=Fondo, hoverColor=DesktopIconHover, holdColor=DesktopIconHold, function=window['explorerWindow'].openWindow, functionArguments=['My Computer']),
    'MyDocumentsButton': Button(x=0, y=90, w=120, h=90, screen=WindowsRG, shading=False, color=Fondo, hoverColor=DesktopIconHover, holdColor=DesktopIconHold, function=window['explorerWindow'].openWindow, functionArguments=['My Documents']),
    'RecycleBinButton': Button(x=0, y=180, w=120, h=90, screen=WindowsRG, shading=False, color=Fondo, hoverColor=DesktopIconHover, holdColor=DesktopIconHold, function=window['explorerWindow'].openWindow, functionArguments=['Recycle Bin']),
    'WindowsMediaPlayerButton': Button(x=0, y=280, w=120, h=90, screen=WindowsRG, shading=False, color=Fondo, hoverColor=DesktopIconHover, holdColor=DesktopIconHold, function=window['explorerWindow'].openWindow, functionArguments=['Windows Media Player'])
}
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

Video=pygame.Surface((644, 400))

print(button)
while True: 

    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 

    for windowInParticular in window:
        if window[windowInParticular].checkIfOpen():
            gameEvent['windowCurrentlyOpen'] = True
            break
        gameEvent['windowCurrentlyOpen'] = False

    WindowsRG.fill(Fondo) 
    
    if gameEvent['windowCurrentlyOpen'] == False:
        button['MyComputerButton'].showButton()
        button['MyDocumentsButton'].showButton()
        button['RecycleBinButton'].showButton()
        button['WindowsMediaPlayerButton'].showButton()

        button['MyComputerButton'].render()
        button['MyDocumentsButton'].render()
        button['RecycleBinButton'].render()
        button['WindowsMediaPlayerButton'].render()
    else:
        button['MyComputerButton'].hideButton()
        button['MyDocumentsButton'].hideButton()
        button['RecycleBinButton'].hideButton()
        button['WindowsMediaPlayerButton'].hideButton()


    WindowsRG.blit(Asset["Icon-Computer"], (33, 10))
    WindowsRG.blit(Asset["Icon-MyDocuments"], (33, 100))
    WindowsRG.blit(Asset["Icon-RecycleBin"], (33, 190))
    WindowsRG.blit(Asset["Icon-MediaPlayer"], (33, 280))
    
    GenerateText(size=normalfontsize-6, text="My Computer", color=color_negro, font=normalfontstyle, x=120, y=150, window=WindowsRG, center=True)
    GenerateText(size=normalfontsize-6, text="My Documents", color=color_negro, font=normalfontstyle, x=120, y=330, window=WindowsRG, center=True)
    GenerateText(size=normalfontsize-6, text="Recycle Bin", color=color_negro, font=normalfontstyle, x=120, y=510, window=WindowsRG, center=True)
    GenerateText(size=normalfontsize-6, text="Windows Media", color=color_negro, font=normalfontstyle, x=120, y=685, window=WindowsRG, center=True)
    GenerateText(size=normalfontsize-6, text="Player", color=color_negro, font=normalfontstyle, x=120, y=720, window=WindowsRG, center=True)
    
    for event in pygame.event.get(): 
          
        if event.type == pygame.QUIT: 
            pygame.quit() 
              
        # Checks if mouse is clicked
        if event.type == pygame.MOUSEBUTTONUP and gameEvent['startMenuOpen'] == True and gameEvent['startMenuSelection'] in range(0,10):
            print(f"Seleccionaste: {MenuOptions[gameEvent['startMenuSelection']]}")
            match MenuOptions[gameEvent['startMenuSelection']]:
                case 'Word':
                    pass
                case 'Windows Update':
                    pass
                case 'Crash':
                    pass
                case 'Solitaire':
                    pass
                case 'Order Food':
                    pass
                case 'Go Online':
                    pass
                case 'Paint':
                    pass
                case 'Help':
                    pass
                case 'Reboot':
                    pass
                case 'Shut Down':
                    pass

        if event.type == pygame.MOUSEBUTTONUP:
            
            if 6 <= mouse[0] <= 6+130 and 554 <= mouse[1] <= 554+40 and gameEvent['startMenuOpen'] == False: 
                gameEvent['startMenuOpen'] = True
            else:
                gameEvent['startMenuOpen'] = False
        
        for buttonObject in button:
            button[buttonObject].checkPress(event)

        for windowObject in window:
            window[windowObject].checkPress(event)

    # Render all windows that are open
    for openWindows in window:
        window[windowObject].render()

    if window['explorerWindow'].checkIfOpen() and window['explorerWindow'].windowTitle() == 'Windows Media Player':
        WindowsRG.blit(Video, (136, 58))
        Asset['Video-MediaPlayer'].draw_to(Video, (0, 0))
        if Asset['Video-MediaPlayer'].remaining_time <= 100:
            window['explorerWindow'].enableCloseButton()
            Asset['Video-MediaPlayer'].pause()
        else:
            window['explorerWindow'].disableCloseButton()
            Asset['Video-MediaPlayer'].play(loop=False)
    else:
        Asset['Video-MediaPlayer'].stop() 

    if gameEvent['startMenuOpen'] == True:
        # Geometria del Menu de Inicio
        pygame.draw.rect(WindowsRG,color_blanco,(0, 157, 356, 402))
        pygame.draw.rect(WindowsRG,color_negro,(2, 157, 354, 402))
        pygame.draw.rect(WindowsRG,BarraDeTareas,(2, 157, 352, 400))

        gameEvent['startMenuSelection']=0
        for a in range(157,557,40):
            if 2 <= mouse[0] <= 352 and 140 <= mouse[1] <= a+40: 
                pygame.draw.rect(WindowsRG,(BarraDeTareas[0]-50, BarraDeTareas[1]-50, BarraDeTareas[2]-50),(2, a, 352, 40))
                break        
            gameEvent['startMenuSelection']+=1

        # Opciones
        StartingPosition=157
        for i in range(len(MenuOptions)):
            if i != 0:
                StartingPosition+=40
            GenerateText(size=bigfontsize-8, text=str(MenuOptions[i]), color=color_negro, font=normalfontstyle, x=60, y=StartingPosition, window=WindowsRG)

    # Barra de Tareas
    pygame.draw.rect(WindowsRG,BarraDeTareas,[0,558,800,42]) 

    # Hour
    GenerateText(size=normalfontsize-2, text="3:00 AM", color=color_negro, font=normalfontstyle, x=1480, y=1155, window=WindowsRG, center=True)

    # Start Button
    button['StartButton'].render()
    WindowsRG.blit(Asset["StartMenu"], (8, 564))
    GenerateText(size=bigfontsize-6, text="Start", color=color_negro, font=bigfontstyle, x=185, y=1160, window=WindowsRG, center=True)

    # updates the frames of the game 
    clock.tick(60)
    if "--show-fps" in Arguments:
        GenerateText(size=normalfontsize-2, text=f"{int(clock.get_fps())} FPS", color=color_negro, font=normalfontstyle, x=2, y=2, window=WindowsRG)
    pygame.display.update() 