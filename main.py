#!/sbin/python
import os
from platform import system
from sys import argv
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
    'videoPlaying': False,
    'progressBarXPosition': 300,
    'wmpCrash': False
}


ProgramDirectory=os.path.dirname(__file__)
IconDirectory=os.path.join(ProgramDirectory, 'Assets', 'Icons')
VideoDirectory=os.path.join(ProgramDirectory, 'Assets', 'Video')
SoundDirectory=os.path.join(ProgramDirectory, 'Assets', 'Sound')

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
        if icon[0: -4] != "WarningIcon":
            Asset[f"Icon-{icon[0: -4]}"] = pygame.transform.scale(AssetTemp, (50, 50))
        else:
            Asset[f"Icon-{icon[0: -4]}"] = pygame.transform.scale(AssetTemp, (70, 70))
for video in os.listdir(VideoDirectory):
    if video.lower().endswith(('.mp4')):
        Asset[f"Video-{video[0: -4]}"] = Video(os.path.join(VideoDirectory, video))

print(Asset)

Asset['StartMenu'] = pygame.image.load(os.path.join(ProgramDirectory, 'Assets', 'StartMenu.png'))
Asset['StartMenu'] = pygame.transform.scale(Asset['StartMenu'], (52, 28))

Asset['ProgramIcon'] = pygame.image.load(os.path.join(ProgramDirectory, 'Assets', 'ProgramIcon.png'))
Asset['ProgramIcon'] = pygame.transform.scale(Asset['ProgramIcon'], (50, 50))


print(Asset)

pygame.display.set_caption('Windows RG Build 207')
pygame.display.set_icon(Asset['ProgramIcon'])



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

if system() == "Windows":
    normalfontsize = 22
    normalfontstyle = 'Arial'
    bigfontsize = 42
    bigfontstyle = 'Arial'
else:
    smallfontsize = 22
    smallfontstyle = 'Liberation Sans'
    normalfontsize = 22
    normalfontstyle = 'Liberation Sans'
    bigfontsize = 42
    bigfontstyle = 'dgjahkjgldakljg'

clock = pygame.time.Clock()

class Frame:

    def __init__(self, x, y, w, h, screen, color=(255, 255, 255), shadeColor=(0, 0, 0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.color = color
        self.shadeColor = shadeColor
        
        self.mainFrameShade = pygame.Rect(x, y, w, h)
        self.mainFrame = pygame.Rect(x+2, y+2, w-2, h-2)

    def render(self):
        pygame.draw.rect(self.screen, self.shadeColor, self.mainFrameShade)
        pygame.draw.rect(self.screen, self.color, self.mainFrame)


def GenerateFrame(x, y, w, h, screen, color=(255, 255, 255), shadeColor=(0, 0, 0)):
    FrameThing=Frame(x=x, y=y, w=w, h=h, screen=screen, color=color, shadeColor=shadeColor)
    FrameThing.render()

FrameTest=Frame(x=20, y=20, w=50, h=50, screen=WindowsRG)

class Window:

    closeText=pygame.font.SysFont(normalfontstyle,bigfontsize-15)
    closeTexttoBlit=closeText.render("X", True, color_negro)

    def __init__(self, x, y, w, h, screen, title='', color=(204, 204, 204)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.black = color_negro
        self.white = color_blanco
        self.blue = "#0000FF"
        self.screen = screen

        self.closeButtonEnabled = True
        
        self.title = title

        # Main Window
        self.window = pygame.Rect(x+2, y+32, w-4, h-34)

        # Frame Decorations
        self.frame2 = pygame.Rect(x+2, y+2, w-2, h-2) # Black Shading
        self.frame1 = pygame.Rect(x, y, w, h) # White Shading

        # Title Bar
        self.bar = pygame.Rect(x+2, y+2, w-2, 28)

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
            pygame.draw.rect(self.screen, self.white, self.frame1)
            pygame.draw.rect(self.screen, self.black, self.frame2)
        
            # Main Window
            pygame.draw.rect(self.screen, self.color, self.window)

            # Title Bar
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

    def returnValue(self, value, excludeTitleBar=False):
        match value:
            case 'x':
                return self.x
            case 'y':
                if excludeTitleBar:
                    return self.y+35
                else:
                    return self.y
            case 'w':
                return self.w
            case 'h':
                if excludeTitleBar:
                    return self.h-34
                else:
                    return self.h
            case 'color':
                return self.color
            case default:
                raise ValueError('Unknown variable or parameter of this window')

    def changeValue(self, variable, value):
        match variable:
            case 'x':
                self.x = int(value)
            case 'y':
                self.y = int(value)
            case 'w':
                self.w = int(value)
            case 'h':
                self.h = int(value)
            case 'color':
                self.color = value
            case default:
                raise ValueError('Unknown variable or parameter of this window')

    def disableCloseButton(self):
        self.closeButtonEnabled = False

    def enableCloseButton(self):
        self.closeButtonEnabled = True

class Button:
    
    def __init__(self, x, y, screen, label='', function=None, functionArguments=[], h=None, w=None, color=(204,204,204), hoverColor=(204,204,204), holdColor=(204,204,204), holdButtonifPressed=False, functionOnToggleDisable=None, functionArgumentsOnToggleDisable=[], startButton=False, shading=True, shadingColor1=(0,0,0), shadingColor2=(255,255,255), textColor=(0,0,0)):
        self.x = x
        self.y = y
        self.color = color
        self.shadingColor1 = shadingColor1
        self.shadingColor2 = shadingColor2
        self.textColor = textColor
        self.hoverColor = hoverColor
        self.holdColor = holdColor
        self.screen = screen
        self.holdButtonifPressed = holdButtonifPressed
        self.toReturn = False

        # FUNCTION STUFF
        self.function = function
        self.functionArguments = functionArguments
        
        if holdButtonifPressed == False and functionOnToggleDisable != None:
            raise KeyError('This function is only available on toggle buttons.')
        
        self.functionOnToggleDisable = functionOnToggleDisable
        self.functionArgumentsOnToggleDisable = functionArgumentsOnToggleDisable

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
        self.buttonEnabled = True
    
    def render(self):
        if self.buttonHidden == False:
            if self.buttonEnabled == False:
                pygame.draw.rect(self.screen, self.shadingColor1, self.buttonShade1)
                pygame.draw.rect(self.screen, self.shadingColor2, self.buttonShade2)
            elif self.holdButtonifPressed == True and self.shading == True and self.buttonEnabled == True:
                if self.buttonHeld == True or self.buttonToggle == True:
                    pygame.draw.rect(self.screen, self.shadingColor2, self.buttonShade1)
                    pygame.draw.rect(self.screen, self.shadingColor1, self.buttonShade2)
                elif self.buttonPressed == False or self.buttonToggle == False:
                    pygame.draw.rect(self.screen, self.shadingColor1, self.buttonShade1)
                    pygame.draw.rect(self.screen, self.shadingColor2, self.buttonShade2)
            elif self.shading == True:
                if self.buttonHeld == True and self.buttonEnabled == True:
                    pygame.draw.rect(self.screen, self.shadingColor2, self.buttonShade1)
                    pygame.draw.rect(self.screen, self.shadingColor1, self.buttonShade2)
                elif self.buttonHeld == False:
                    pygame.draw.rect(self.screen, self.shadingColor1, self.buttonShade1)
                    pygame.draw.rect(self.screen, self.shadingColor2, self.buttonShade2)
        
            if self.buttonHover == True and self.buttonHeld == True and gameEvent['startMenuOpen'] == False and self.buttonEnabled == True:
                pygame.draw.rect(self.screen, self.holdColor, self.button)
            elif self.buttonHover == True and gameEvent['startMenuOpen'] == False and self.buttonEnabled == True:
                pygame.draw.rect(self.screen, self.hoverColor, self.button)
            else:
                pygame.draw.rect(self.screen, self.color, self.button)
            self.screen.blit(self.actualtext, self.text_rect)

    def checkPress(self, event):
        if self.buttonHidden == False and self.buttonEnabled == True:
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

            if self.holdButtonifPressed == True:
                if self.buttonPressed == True:
                    self.buttonPressed = False
                    if self.function != None and len(self.functionArguments) != 0 and self.buttonToggle == True:
                        self.function(*self.functionArguments)
                        self.toReturn = True
                    elif self.function != None and self.buttonToggle == True:
                        self.function()
                        self.toReturn = True

                    elif self.functionOnToggleDisable != None and len(self.functionArgumentsOnToggleDisable) != 0 and self.buttonToggle == False:
                        self.functionOnToggleDisable(*self.functionArgumentsOnToggleDisable)
                        self.toReturn = False
                    elif self.functionOnToggleDisable != None and self.buttonToggle == False:
                        self.functionOnToggleDisable()
                        self.toReturn = False
                else:
                    if self.buttonToggle == True:
                        self.toReturn = True
                    else:
                        self.toReturn = False
            else:
                if self.buttonPressed == True:
                    if self.function != None and len(self.functionArguments) != 0:
                        self.function(*self.functionArguments)
                    elif self.function != None:
                        self.function()
                    self.buttonPressed = False
                    self.toReturn = True
                else:
                    self.toReturn = False
        else:
            self.buttonPressed = False
            self.buttonHeld = False
            self.buttonHover = False

            self.toReturn = False

        return self.toReturn

    def hideButton(self):
        self.buttonHidden = True
        self.buttonHover = False
        self.buttonHeld = False
        self.buttonPressed = False
        if self.holdButtonifPressed == True:
            self.buttonToggle = False
        
    def showButton(self):
        self.buttonHidden = False

    def enableButton(self):
        self.buttonEnabled = True
    
    def disableButton(self):
        self.buttonEnabled = False
        self.buttonHover = False
        self.buttonHeld = False
        self.buttonPressed = False
        if self.holdButtonifPressed == True:
            self.buttonToggle = False

    def changeToggle(self, arg=None):
        if self.buttonToggle == True and arg == None:
            self.buttonToggle = False
        elif self.buttonToggle == False and arg == None:
            self.buttonToggle = True
        elif arg == True:
            self.buttonToggle = True
        elif arg == False:
            self.buttonToggle = False

def setGameEvent(event, value):
    gameEvent[event]=value

class ErrorMessage:

    pygame.mixer.music.load(os.path.join(SoundDirectory, 'Chord.wav'))

    def __init__(self, x, y, screen, title="", buttonLabel="OK", message="This is a warning message.", function="", functionArguments=[]):
        self.x = x
        self.y = y
        self.windowWeight=400
        self.windowHeight=200
        self.color = (0,0,0)
        self.screen = screen
        self.message = f"{str(message)} "
        print(len(message))
        print(message)
        if len(message) >= 120:
            raise TypeError('Message longer than 120 characters')
        elif len(message) >= 90:
            self.message = [self.message[0: 30], self.message[30: 60], self.message[60: 90], self.message[90: -1]]
        elif len(message) >= 60:
            self.message = [self.message[0: 30], self.message[30: 60], self.message[60: -1]]
        elif len(message) >= 30: 
            self.message = [self.message[0: 30], self.message[30: -1]]

        self.ErrorMessageWindow = Window(self.x, self.y, self.windowWeight, self.windowHeight, screen, title)
        self.ErrorMessageButton = Button(x=(self.x+self.windowWeight/2), y=(self.y+self.windowHeight), screen=self.screen, label=buttonLabel, holdButtonifPressed=True, function=function, functionArguments=[])
        self.WarningShown = False
        self.SoundPlayed = False

    def checkIfOpen(self):
        return self.ErrorMessageWindow.checkIfOpen()

    def checkPress(self, event):
        if self.WarningShown == True:
            self.ErrorMessageWindow.checkPress(event)
            self.ErrorMessageButton.checkPress(event)

            if self.ErrorMessageButton.checkPress(event) == True:
                self.WarningShown = False
                self.ErrorMessageButton.changeToggle(False)

    def render(self):
        if self.WarningShown == True:
            self.ErrorMessageWindow.render()
            self.ErrorMessageButton.render()
            TextX=self.x+90
            TextY=self.y+42
            if type(self.message) == list and len(self.message) >= 4:
                GenerateText(size=normalfontsize, text=self.message[3], color=self.color, font=normalfontstyle ,x=TextX, y=TextY+96, window=self.screen)
            if type(self.message) == list and len(self.message) >= 3:
                GenerateText(size=normalfontsize, text=self.message[2], color=self.color, font=normalfontstyle ,x=TextX, y=TextY+64, window=self.screen)
            if type(self.message) == list and len(self.message) >= 2:
                GenerateText(size=normalfontsize, text=self.message[1], color=self.color, font=normalfontstyle ,x=TextX, y=TextY+32, window=self.screen)
            if type(self.message) != list:
                GenerateText(size=normalfontsize, text=self.message, color=(0, 0, 0), font=normalfontstyle ,x=TextX, y=TextY, window=self.screen)
            else:
                GenerateText(size=normalfontsize, text=self.message[0], color=(0, 0, 0), font=normalfontstyle ,x=TextX, y=TextY, window=self.screen)
                
            self.screen.blit(Asset["Icon-WarningIcon"], (self.x+16, self.y+self.y/3))
        
            if self.SoundPlayed == False:
                pygame.mixer.music.play()
                self.SoundPlayed = True
        else:
            self.ErrorMessageWindow.closeWindow()
    
    def openWindow(self):
        self.ErrorMessageWindow.openWindow()
        self.WarningShown = True
    
    def closeWindow(self):
        self.ErrorMessageWindow.closeWindow()
        self.WarningShown = False
        self.SoundPlayed = False
    
    def isWarningOpen(self):
        return self.WarningShown
    
DesktopIconHover=(0,153-30,255-30),
DesktopIconHold=(0,153-60,255-60),

window={
    'explorerWindow': Window(125, 10, Width-130, Height-95, WindowsRG, gameEvent['currentWindow'])
    }

warnings={
    'testWarning': ErrorMessage(x=Width/4, y=Height/4, screen=WindowsRG, function=window['explorerWindow'].closeWindow, message="mediaplayer.exe has performed an illegal operation and will close...                      Isn't that a shame? Isn't it?")
}

def playVideo():
    if Asset['Video-MediaPlayer'].remaining_time == 21833.333333333332:
        Asset['Video-MediaPlayer'].play()
    else:
        Asset['Video-MediaPlayer'].resume()
    
    if Asset['Video-MediaPlayer'].is_paused:
        Asset['Video-MediaPlayer'].resume()


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
    'WindowsMediaPlayerButton': Button(x=0, y=280, w=120, h=90, screen=WindowsRG, shading=False, color=Fondo, hoverColor=DesktopIconHover, holdColor=DesktopIconHold, function=window['explorerWindow'].openWindow, functionArguments=['Windows Media Player']),

    # Windows Media Player
    'WMPPlayButton': Button(x=136, y=470, w=66, h=66, screen=WindowsRG, holdButtonifPressed=True, function=playVideo, functionOnToggleDisable=Asset['Video-MediaPlayer'].pause),
    'WMPPauseButton': Button(x=216, y=470, w=66, h=66, screen=WindowsRG, function=Asset['Video-MediaPlayer'].pause)
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

        for warningDialogObject in warnings:
            warnings[warningDialogObject].checkPress(event)

    # Render all windows that are open
    for openWindows in window:
        window[windowObject].render()

    if window['explorerWindow'].checkIfOpen():
        match window['explorerWindow'].windowTitle():
            case 'Windows Media Player':
                pygame.draw.rect(WindowsRG,color_negro,(134, 56, 648, 404))
                Asset['Video-MediaPlayer'].draw_to(Video, (0, 0))

                # Progress Bar
                pygame.draw.rect(WindowsRG,color_negro,(300, 504, 482, 4))
                pygame.draw.rect(WindowsRG,color_negro,(gameEvent['progressBarXPosition'], 490, 30, 30))

                button['WMPPlayButton'].render()
                button['WMPPauseButton'].render()
                button['WMPPlayButton'].showButton()
                button['WMPPauseButton'].showButton()

                # Play Button Triangle
                Triangle_x = 160
                Triangle_y = 482
                pygame.draw.polygon(WindowsRG, color_negro, ((0+Triangle_x, 0+Triangle_y), (20+Triangle_x, 20+Triangle_y), (0+Triangle_x, 40+Triangle_y)))

                # Square
                pygame.draw.rect(WindowsRG, color_negro, (228, 482, 40, 40))

                if Asset['Video-MediaPlayer'].is_paused == True:
                    button['WMPPlayButton'].changeToggle(False)
                elif Asset['Video-MediaPlayer'].is_playing and Asset['Video-MediaPlayer'].is_paused == False:
                    gameEvent['progressBarXPosition']+=0.3

                if Asset['Video-MediaPlayer'].is_playing and Asset['Video-MediaPlayer'].remaining_time < 21833.333333333332:
                    WindowsRG.blit(Video, (136, 58))

                if Asset['Video-MediaPlayer'].remaining_time <= 100:
                    #window['explorerWindow'].enableCloseButton()
                    gameEvent['wmpCrash'] = True
                    Asset['Video-MediaPlayer'].pause()
                    button['WMPPlayButton'].disableButton()
                    button['WMPPauseButton'].disableButton()

                if warnings['testWarning'].checkIfOpen() == False and gameEvent['wmpCrash'] == True:
                    warnings['testWarning'].openWindow()
            case 'My Computer' | 'My Documents' | 'Recycle Bin':
                pass
                #GenerateFrame(x=window['explorerWindow'].returnValue('x')+4, y=window['explorerWindow'].returnValue('y', excludeTitleBar=True), w=window['explorerWindow'].returnValue('w'), h=window['explorerWindow'].returnValue('h')-4, screen=WindowsRG)
    else:
        warnings['testWarning'].closeWindow()
        gameEvent['wmpCrash'] = False
        gameEvent['progressBarXPosition']=300
        Asset['Video-MediaPlayer'].stop()
        button['WMPPlayButton'].enableButton()
        button['WMPPauseButton'].enableButton()
        button['WMPPlayButton'].changeToggle(False)

    for openWindowDialogues in warnings:
        warnings[openWindowDialogues].render()

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
    if system() == "Windows":
        GenerateText(size=bigfontsize-18, text="Start", color=color_negro, font=bigfontstyle, x=185, y=1160, window=WindowsRG, center=True, bold=True)
    else:
        GenerateText(size=bigfontsize-6, text="Start", color=color_negro, font=bigfontstyle, x=185, y=1160, window=WindowsRG, center=True)

    # updates the frames of the game 
    clock.tick(60)
    if "--show-fps" in Arguments:
        GenerateText(size=normalfontsize-2, text=f"{int(clock.get_fps())} FPS", color=color_negro, font=normalfontstyle, x=2, y=2, window=WindowsRG)
    pygame.display.update() 