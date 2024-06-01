#!/sbin/python
import os
from platform import system
from sys import argv
from time import sleep

import json

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


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
    'wmpCrash': False,
    'documentsCrash': False,
    'timer': -2,
    'openingPaint': False,
    'customVideoLoaded': False,
    'orderFoodPage': 0,
    'windowsUpdatePage': 0
}


ProgramDirectory=os.path.dirname(__file__)
IconDirectory=os.path.join(ProgramDirectory, 'Assets', 'Icons')
VideoDirectory=os.path.join(ProgramDirectory, 'Assets', 'Video')
LanguageDirectory=os.path.join(ProgramDirectory, 'Languages')


import pygame
from pygamevideo import Video

def setTimeBomb(time, millis=1000):
    if gameEvent['timer'] == -2:
        gameEvent['timer'] = time
        pygame.time.set_timer(pygame.USEREVENT, millis)

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
    if video.lower().endswith(('.mp4')) and video.lower() == "mediaplayer.mp4":
        Asset[f"Video-{video[0: -4]}"] = Video(os.path.join(VideoDirectory, video))

Asset['Video-Custom'] = None

def LoadCustomVideo():
    try:
        Filedir = os.path.join(filedialog.askopenfilename())
        return Filedir
    except FileNotFoundError:
        pass
    except ZeroDivisionError:
        pass
    except TypeError:
        pass

Asset['StartMenu'] = pygame.image.load(os.path.join(ProgramDirectory, 'Assets', 'StartMenu.png'))
Asset['StartMenu'] = pygame.transform.scale(Asset['StartMenu'], (52, 28))

Asset['ProgramIcon'] = pygame.image.load(os.path.join(ProgramDirectory, 'Assets', 'ProgramIcon.png'))
Asset['ProgramIcon'] = pygame.transform.scale(Asset['ProgramIcon'], (50, 50))

Asset['WindowsRGLogo'] = pygame.image.load(os.path.join(ProgramDirectory, 'Assets', 'WindowsRGLogo.png'))
Asset['WindowsRGLogo-Small'] = pygame.transform.scale(Asset['WindowsRGLogo'], (344, 80))
Asset['WindowsRGLogo'] = pygame.transform.scale(Asset['WindowsRGLogo'], (688, 160))

Asset['WindowsRGStartFlag'] = pygame.image.load(os.path.join(ProgramDirectory, 'Assets', 'WindowsRGStartFlag.png'))
Asset['WindowsRGStartFlag'] = pygame.transform.scale(Asset['WindowsRGStartFlag'], (46, 400))

Asset['PaintSplash'] = pygame.image.load(os.path.join(ProgramDirectory, 'Assets', 'PaintSplashScreen.png'))

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

from UIElements.Frame import Frame
from UIElements.Frame import GenerateFrame

FrameTest=Frame(x=20, y=20, w=50, h=50, screen=WindowsRG)

def setGameEvent(event, value, action="equals"):
    match action:
        case "equals":
            gameEvent[event]=value
        case "subst":
            gameEvent[event]-=value
        case "sum":
            gameEvent[event]+=value

from UIElements.Window import Window
from UIElements.Window import ErrorMessage

from UIElements.Buttons import Button
from UIElements.Buttons import IconButton


languageSelection = [
    Button(
        x=Width/2, 
        y=Height/2 - 32, 
        label="Español", screen=WindowsRG, 
        holdButtonifPressed = True),
    
    Button(
        x=Width/2, 
        y=Height/2 + 32, 
        label="English", screen=WindowsRG,
        holdButtonifPressed = True)
]

languagenotselected = True
while languagenotselected:

    WindowsRG.fill(Fondo) 

    for event in pygame.event.get(): 
          
        if event.type == pygame.QUIT: 
            pygame.quit() 

        if languageSelection[0].checkPress(event) == True:
            languageSelected = "es-AR"
            languagenotselected = False
        
        if languageSelection[1].checkPress(event) == True:
            languageSelected = "en-GB"
            languagenotselected = False
                        
    for buttonObject in languageSelection:
        buttonObject.render()
        buttonObject.showButton()

    clock.tick(120)
    if "--show-fps" in Arguments:
        GenerateText(size=normalfontsize-2, text=f"{int(clock.get_fps())} FPS", color=color_negro, font=normalfontstyle, x=2, y=2, window=WindowsRG)
    pygame.display.update() 
            

for language in os.listdir(LanguageDirectory):
    if language.startswith(languageSelected) and language.endswith(('.json')):
        translation = json.load(open(os.path.join(LanguageDirectory, language)))

DesktopIconHover=(0,153-30,255-30),
DesktopIconHold=(0,153-60,255-60),

MenuOptions=[
    translation['StartMenu-Word'], 
    translation['StartMenu-WindowsUpdate'], 
    translation['StartMenu-Crash'], 
    translation['StartMenu-Solitaire'], 
    translation['StartMenu-OrderFood'], 
    translation['StartMenu-GoOnline'], 
    translation['StartMenu-Paint'], 
    translation['StartMenu-Help'], 
    translation['StartMenu-Reboot'], 
    translation['StartMenu-Shutdown']
]

window={
    'explorerWindow': Window(125, 10, Width-130, Height-65, WindowsRG, gameEvent['currentWindow']),
    'bigWindow': Window(4, 4, Width-8, Height-50, WindowsRG, gameEvent['currentWindow'])
    }

warnings={
    'testWarning': ErrorMessage(
        x=Width/4, y=Height/4, 
        screen=WindowsRG, 
        function=window['explorerWindow'].closeWindow, 
        message=translation['Warning-WMPCrash'],
        wordWrap=True),
        
    'documentsCrash': ErrorMessage(
        x=window['explorerWindow'].returnValue('middleX') - 400 / 2, 
        y=window['explorerWindow'].returnValue('middleY', excludeTitleBar=True) - 240 / 4, 
        screen=WindowsRG, 
        function=window['explorerWindow'].closeWindow, 
        message=translation['Warning-MyDocumentsCrash'],
        wordWrap=True)
}

def playVideo(status='play'):
    if gameEvent['customVideoLoaded'] == False:
        match status:
            case 'play':
                if Asset['Video-MediaPlayer'].remaining_time == 21833.333333333332:
                    Asset['Video-MediaPlayer'].play()
                else:
                    Asset['Video-MediaPlayer'].resume()
    
                if Asset['Video-MediaPlayer'].is_paused:
                    Asset['Video-MediaPlayer'].resume()
            case 'pause':
                Asset['Video-MediaPlayer'].pause()
    else:
        match status:
            case 'play':  
                if Asset['Video-Custom'].remaining_time == Asset['Video-Custom'].duration:
                    Asset['Video-Custom'].play()
                else:
                    Asset['Video-Custom'].resume()

                if Asset['Video-Custom'].is_paused:
                    Asset['Video-Custom'].resume()
            case 'pause':
                Asset['Video-Custom'].pause()


StartButton = Button(x=5, y=564, w=125, h=31, screen=WindowsRG, holdButtonifPressed=True)

button={
    # ---------
    #  BUTTONS 
    # ---------

    # Start Button
    

    # Windows Media Player
    'WMPPlayButton': Button(x=136, y=470, w=66, h=66, screen=WindowsRG, holdButtonifPressed=True, function=playVideo, functionOnToggleDisable=playVideo, functionArgumentsOnToggleDisable=['pause']),
    'WMPPauseButton': Button(x=216, y=470, w=66, h=66, screen=WindowsRG, function=playVideo, functionArguments=['pause']),
    'WMPLoadCustomVideo': Button(x=64, y=Height-64, screen=WindowsRG, label=translation['Button-WMPLoadCustomVideo'], holdButtonifPressed=True),

    # Recycle Bin
    'EmptyRecycleBin': Button(x=216, y=400, label=translation['Button-EmptyBin'], screen=WindowsRG),

    # Order Food
    'OrderFoodOKButton': Button(
        x=window['bigWindow'].returnValue('middleX'), 
        y=window['bigWindow'].returnValue('y') + window['bigWindow'].returnValue('h') - 32, 
        label=translation['Button-OrderFoodOKButton'], screen=WindowsRG, 
        function=setGameEvent, functionArguments=('orderFoodPage', 1, 'sum')),

    # Food Selection menu
    'OrderFoodQuitButton': Button(
        x=window['bigWindow'].returnValue('middleX'), 
        y=window['bigWindow'].returnValue('y') + window['bigWindow'].returnValue('h') - 32, 
        label=translation['Button-OrderFoodQuitButton'], screen=WindowsRG, 
        function=setGameEvent, functionArguments=('orderFoodPage', 6)),

    'OrderFoodTryAgainButton': Button(
        x=window['bigWindow'].returnValue('middleX'), 
        y=window['bigWindow'].returnValue('y') + window['bigWindow'].returnValue('h') - 32, 
        label=translation['Button-OrderFoodTryAgainButton'], screen=WindowsRG, 
        function=setGameEvent, functionArguments=('orderFoodPage', 4)), 

    'FoodSelection1': Button(
        x=window['bigWindow'].returnValue('middleX') + window['bigWindow'].returnValue('h') / 2, 
        y=window['bigWindow'].returnValue('middleY', excludeTitleBar = True) - 40, 
        label=translation['Button-OrderFoodOrder'], screen=WindowsRG, 
        function=setGameEvent, functionArguments=('orderFoodPage', 5)),
    
    'FoodSelection2': Button(
        x=window['bigWindow'].returnValue('middleX') + window['bigWindow'].returnValue('h') / 2, 
        y=window['bigWindow'].returnValue('middleY', excludeTitleBar = True), 
        label=translation['Button-OrderFoodOrder'], screen=WindowsRG, 
        function=setGameEvent, functionArguments=('orderFoodPage', 5)),

    'FoodSelection3': Button(
        x=window['bigWindow'].returnValue('middleX') + window['bigWindow'].returnValue('h') / 2, 
        y=window['bigWindow'].returnValue('middleY', excludeTitleBar = True) + 40, 
        label=translation['Button-OrderFoodOrder'], screen=WindowsRG, 
        function=setGameEvent, functionArguments=('orderFoodPage', 5))    
}

desktopIcons={
    'MyComputerButton': Button(
        x=0, y=0, w=120, h=90, 
        screen=WindowsRG, 
        shading=False, 
        color=Fondo, 
        hoverColor=DesktopIconHover, 
        holdColor=DesktopIconHold, 
        function=window['explorerWindow'].openWindow, 
        functionArguments=[translation['WindowTitle-MyComputer']]),

    'MyDocumentsButton': Button(
        x=0, y=90, w=120, h=90, 
        screen=WindowsRG, 
        shading=False, 
        color=Fondo, 
        hoverColor=DesktopIconHover, 
        holdColor=DesktopIconHold, 
        function=window['explorerWindow'].openWindow, 
        functionArguments=[translation['WindowTitle-MyDocuments']]),

    'RecycleBinButton': Button(
        x=0, y=180, w=120, h=90, 
        screen=WindowsRG, 
        shading=False, 
        color=Fondo, 
        hoverColor=DesktopIconHover, 
        holdColor=DesktopIconHold, 
        function=window['explorerWindow'].openWindow, 
        functionArguments=[translation['WindowTitle-RecycleBin']]),

    'WindowsMediaPlayerButton': Button(
        x=0, y=280, w=120, h=90, 
        screen=WindowsRG, 
        shading=False, 
        color=Fondo, 
        hoverColor=DesktopIconHover, 
        holdColor=DesktopIconHold, 
        function=window['explorerWindow'].openWindow, 
        functionArguments=[translation['WindowTitle-MediaPlayer']])
}

myComputerIcons={
    # Test Button
    'myComputerIcon1': IconButton(
        x=window['explorerWindow'].returnValue('x') + 178, y=window['explorerWindow'].returnValue('y', excludeTitleBar=True) + 14, w=100, h=100, 
        screen=WindowsRG, 
        label=translation['Label-ADrive'],
        icon=Asset['Icon-FloppyDisk'],
        function=window['explorerWindow'].openWindow, 
        functionArguments=[f"{translation['WindowTitle-ADrive']}"]),

    'myComputerIcon2': IconButton(
        x=window['explorerWindow'].returnValue('x') + 278, y=window['explorerWindow'].returnValue('y', excludeTitleBar=True) + 14, w=100, h=100, 
        screen=WindowsRG, 
        label=translation['Label-CDrive'],
        icon=Asset['Icon-HardDisk'],
        function=window['explorerWindow'].openWindow, 
        functionArguments=[f"{translation['WindowTitle-CDrive']}"]),

    'myComputerIcon3': IconButton(
        x=window['explorerWindow'].returnValue('x') + 378, y=window['explorerWindow'].returnValue('y', excludeTitleBar=True) + 14, w=100, h=100, 
        screen=WindowsRG, 
        label=translation['Label-DDrive'],
        icon=Asset['Icon-CDDrive'],
        function=window['explorerWindow'].openWindow, 
        functionArguments=[f"{translation['WindowTitle-DDrive']}"]),
}

CDriveIcons={
    # Test Button
    'CDriveIcon1': IconButton(
        x=window['explorerWindow'].returnValue('x') + 178, y=window['explorerWindow'].returnValue('y', excludeTitleBar=True) + 14, w=104, h=100, 
        screen=WindowsRG, 
        label=translation['Label-MyDocuments'],
        icon=Asset['Icon-MyDocuments'],
        function=window['explorerWindow'].openWindow, 
        functionArguments=[translation['WindowTitle-MyDocuments']]),

    'CDriveIcon2': IconButton(
        x=window['explorerWindow'].returnValue('x') + 282, y=window['explorerWindow'].returnValue('y', excludeTitleBar=True) + 14, w=100, h=100, 
        screen=WindowsRG, 
        label=translation['Label-RecycleBin'],
        icon=Asset['Icon-RecycleBin'],
        function=window['explorerWindow'].openWindow, 
        functionArguments=[translation['WindowTitle-RecycleBin']]),

    'CDriveIcon3': IconButton(
        x=window['explorerWindow'].returnValue('x') + 382, y=window['explorerWindow'].returnValue('y', excludeTitleBar=True) + 14, w=100, h=100, 
        screen=WindowsRG, 
        label=translation['Label-WindowsFolder'],
        icon=Asset['Icon-Folder'],
        function=window['explorerWindow'].openWindow, 
        functionArguments=[f"This is not implemented yet."]),
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

VideoFrame=pygame.Surface((644, 400))

BigWindowSummaryX=window['bigWindow'].returnValue('x') + window['bigWindow'].returnValue('w') / 64
BigWindowSummaryY=window['bigWindow'].returnValue('y', excludeTitleBar=True) + 116

from UIElements.Canvas import Canvas

PaintCanvas=Canvas(
    x=window['bigWindow'].returnValue('x') + 12, 
    y=window['bigWindow'].returnValue('y', excludeTitleBar=True) + 12, 
    w=window['bigWindow'].returnValue('w') - 24, 
    h=window['bigWindow'].returnValue('h', excludeTitleBar=True) - 24, 
    color=(0, 0, 0),
    screen=WindowsRG
)

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
    
    if gameEvent['windowCurrentlyOpen'] == False and gameEvent['openingPaint'] == False and gameEvent['startMenuOpen'] == False:
        for buttonObject in desktopIcons:
            desktopIcons[buttonObject].showButton()
            desktopIcons[buttonObject].render()
        gameEvent['timer'] = -2
    else:
        for buttonObject in desktopIcons:
            desktopIcons[buttonObject].hideButton()

    if gameEvent['openingPaint'] == False:
        StartButton.enableButton()
        WindowsRG.blit(Asset["Icon-Computer"], (33, 10))
        WindowsRG.blit(Asset["Icon-MyDocuments"], (33, 100))
        WindowsRG.blit(Asset["Icon-RecycleBin"], (33, 190))
        WindowsRG.blit(Asset["Icon-MediaPlayer"], (33, 280))
    
        GenerateText(size=normalfontsize-6, text=translation['Label-MyComputer'], color=color_negro, font=normalfontstyle, x=120, y=150, window=WindowsRG, center=True)
        GenerateText(size=normalfontsize-6, text=translation['Label-MyDocuments'], color=color_negro, font=normalfontstyle, x=120, y=330, window=WindowsRG, center=True)
        GenerateText(size=normalfontsize-6, text=translation['Label-RecycleBin'], color=color_negro, font=normalfontstyle, x=120, y=510, window=WindowsRG, center=True)
        GenerateText(size=normalfontsize-6, text="Windows Media", color=color_negro, font=normalfontstyle, x=120, y=685, window=WindowsRG, center=True)
        GenerateText(size=normalfontsize-6, text="Player", color=color_negro, font=normalfontstyle, x=120, y=720, window=WindowsRG, center=True)
    else:
        StartButton.disableButton()
    
    for event in pygame.event.get(): 
          
        if event.type == pygame.QUIT: 
            pygame.quit() 
              
        # Checks if mouse is clicked
        if event.type == pygame.MOUSEBUTTONUP and gameEvent['startMenuOpen'] == True and gameEvent['startMenuSelection'] in range(0,10):
            
            if MenuOptions[gameEvent['startMenuSelection']] == translation['StartMenu-Word']:
                window['bigWindow'].openWindow(translation['WindowTitle-Word'])
            elif MenuOptions[gameEvent['startMenuSelection']] == translation['StartMenu-WindowsUpdate']:
                window['bigWindow'].openWindow(translation['WindowTitle-WindowsUpdate'])
            elif MenuOptions[gameEvent['startMenuSelection']] == translation['StartMenu-Crash']:
                pass
            elif MenuOptions[gameEvent['startMenuSelection']] == translation['StartMenu-Solitaire']:
                window['bigWindow'].openWindow(translation['WindowTitle-Solitaire'])
            elif MenuOptions[gameEvent['startMenuSelection']] == translation['StartMenu-OrderFood']:
                window['bigWindow'].openWindow(translation['WindowTitle-OrderFood'])
            elif MenuOptions[gameEvent['startMenuSelection']] == translation['StartMenu-GoOnline']:
                window['bigWindow'].openWindow(translation['WindowTitle-Browser'])
            elif MenuOptions[gameEvent['startMenuSelection']] == translation['StartMenu-Paint']:
                if window['bigWindow'].windowTitle() != translation['WindowTitle-Paint']:
                    window['bigWindow'].closeWindow()
                    window['explorerWindow'].closeWindow()
                    gameEvent['openingPaint'] = True
            elif MenuOptions[gameEvent['startMenuSelection']] == translation['StartMenu-Help']:
                window['bigWindow'].openWindow(translation['WindowTitle-Help'])
            elif MenuOptions[gameEvent['startMenuSelection']] == translation['StartMenu-Reboot']:
                pass
            elif MenuOptions[gameEvent['startMenuSelection']] == translation['StartMenu-Shutdown']:
                pass

        if event.type == pygame.MOUSEBUTTONUP:
            
            if 6 <= mouse[0] <= 6+130 and 554 <= mouse[1] <= 554+40 and gameEvent['startMenuOpen'] == False: 
                gameEvent['startMenuOpen'] = True
            else:
                gameEvent['startMenuOpen'] = False

        if event.type == pygame.USEREVENT and gameEvent['timer'] != -2:
            if gameEvent['timer'] > 0:
                gameEvent['timer'] -= 1
            else:
                gameEvent['timer'] = 0

            
        StartButton.checkPress(event)

        PaintCanvas.checkPress(event)

        for buttonObject in button:
            button[buttonObject].checkPress(event)

        for buttonObject in desktopIcons:
            desktopIcons[buttonObject].checkPress(event)

        if window['explorerWindow'].checkIfOpen() and window['explorerWindow'].windowTitle() == translation['WindowTitle-MyComputer']:
            for buttonObject in myComputerIcons:
                myComputerIcons[buttonObject].checkPress(event)
        elif window['explorerWindow'].checkIfOpen() and window['explorerWindow'].windowTitle() == translation['WindowTitle-CDrive']:
            for buttonObject in CDriveIcons:
                CDriveIcons[buttonObject].checkPress(event)

        for windowObject in window:
            window[windowObject].checkPress(event)

        for warningDialogObject in warnings:
            warnings[warningDialogObject].checkPress(event)

        if button['WMPLoadCustomVideo'].checkPress(event) == True:
            try:
        
                FileDirectoryofCustomVideo = LoadCustomVideo()
                
                if len(FileDirectoryofCustomVideo) == 0:
                    FileDirectoryofCustomVideo = None
                    button['WMPLoadCustomVideo'].changeToggle(False)
                elif FileDirectoryofCustomVideo.lower().endswith(('.mp4')):
                    if Asset['Video-Custom'] == None:
                        Asset['Video-Custom'] = Video(FileDirectoryofCustomVideo)
                        button['WMPPlayButton'].changeToggle(False)
                        gameEvent['progressBarXPosition']=300
                    elif Asset['Video-Custom'] != None:
                        Asset['Video-Custom'].stop()
                        Asset['Video-Custom'] = Video(FileDirectoryofCustomVideo)
                        button['WMPPlayButton'].changeToggle(False)
                        gameEvent['progressBarXPosition']=300
                    button['WMPLoadCustomVideo'].changeToggle(False)
                    gameEvent['customVideoLoaded'] = True
                else:
                    FileDirectoryofCustomVideo = None
                    button['WMPLoadCustomVideo'].changeToggle(False)
            except FileNotFoundError:
                FileDirectoryofCustomVideo = None
                button['WMPLoadCustomVideo'].changeToggle(False)
            except ZeroDivisionError:
                FileDirectoryofCustomVideo = None
                button['WMPLoadCustomVideo'].changeToggle(False)
            except TypeError:
                FileDirectoryofCustomVideo = None
                button['WMPLoadCustomVideo'].changeToggle(False)



    # Render all windows that are open
    for openWindows in window:
        window[openWindows].render()

    if gameEvent['openingPaint'] == True:
        WindowsRG.blit(Asset["PaintSplash"], (Width / 2 - 468 / 2, Height / 2 - 276 / 2 - 42 / 2))
        if gameEvent['timer'] == -2:
            setTimeBomb(3)
        elif gameEvent['timer'] == 0:
            gameEvent['timer'] = -2
            window['bigWindow'].openWindow(translation['WindowTitle-Paint'])
            gameEvent['openingPaint'] = False

    if window['bigWindow'].checkIfOpen():
        if window['explorerWindow'].checkIfOpen():
            window['explorerWindow'].closeWindow()
        
        if window['bigWindow'].windowTitle() == translation['WindowTitle-Word']:
            pass
        elif window['bigWindow'].windowTitle() == translation['WindowTitle-WindowsUpdate'] or window['bigWindow'].windowTitle() == translation['WindowTitle-Help']:
            WindowsRG.blit(Asset["WindowsRGLogo"], (window['bigWindow'].returnValue('x')+16, window['bigWindow'].returnValue('y', excludeTitleBar=True)+16))
                
            if window['bigWindow'].windowTitle() == translation['WindowTitle-Help']:
                BigWindowBlurb=translation['Subtitle-Help']
            elif window['bigWindow'].windowTitle() == translation['WindowTitle-WindowsUpdate']:
                BigWindowBlurb=translation['Subtitle-WindowsUpdate']

            GenerateText(
                    size=bigfontsize, 
                    text=BigWindowBlurb, 
                    color=color_negro, 
                    font=normalfontstyle, 
                    x=BigWindowSummaryX+10, y=BigWindowSummaryY+10, 
                    window=WindowsRG,
                    bold=True)

            if window['bigWindow'].windowTitle() == translation['WindowTitle-Help']:
                GenerateText(
                        size=normalfontsize, 
                        text=translation['Description-Help-Line1'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=BigWindowSummaryX+10, y=BigWindowSummaryY+70, 
                        window=WindowsRG)

                GenerateText(
                        size=normalfontsize, 
                        text=translation['Description-Help-Line2'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=BigWindowSummaryX+10, y=BigWindowSummaryY+100, 
                        window=WindowsRG)

                GenerateText(
                        size=normalfontsize, 
                        text=translation['Description-Help-Line3'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=BigWindowSummaryX+10, y=BigWindowSummaryY+130, 
                        window=WindowsRG)

            elif window['bigWindow'].windowTitle() == translation['WindowTitle-WindowsUpdate']:
                GenerateText(
                        size=normalfontsize, 
                        text=translation['Description-WindowsUpdate-Line1'],
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=BigWindowSummaryX+10, y=BigWindowSummaryY+70, 
                        window=WindowsRG)

                GenerateText(
                        size=normalfontsize, 
                        text=translation['Description-WindowsUpdate-Line2'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=BigWindowSummaryX+10, y=BigWindowSummaryY+100, 
                        window=WindowsRG)
                    

                # Help
                # The updated Windows Help is so simple to use.
                # Enter one or more words regarding what you need help on and Windows RG
                # will be happy to help.

                # Help 2
                # Please wait while Windows searches the help database

                # Help 3
                # You searched for:
                #   [user input]
                #
                # Sorry - Windows did not find any matches. However, it found 3 possible
                # matches.
                #
                # [View Possible Matches]

                # After user clicks
                # Possible matches:
                #
                # How do I grow bosnia trees?
                # Why can fish swim so well?
                # How do I purchase lime?

                # After user selects an option
                # Please Wait.

                # Crash (do this two times)
                # WINDOWS HAS CAUSED A GENERAL PROTECTION
                # FAULT IN WINHELP.EXE
                #
                # PRESS SPACE TO CONTINUE

                # After that, big window turns into pure blue


        elif window['bigWindow'].windowTitle() == translation['WindowTitle-OrderFood']:

            WindowsRG.blit(Asset["WindowsRGLogo-Small"], (window['bigWindow'].returnValue('x')+16, window['bigWindow'].returnValue('y', excludeTitleBar=True)+16))
                
            # Order Food blurb 1
            # One of the many advancements in Windows RG 
            # is the ability to order food online. 
            # You can order from a huge selection of quality 
            # goods and they will be delivered to your door 
            # within 30 minutes. (45 minutes off-peak). 
            # Click OK to continue
            match gameEvent['orderFoodPage']:
                case 0:
                    if gameEvent['timer'] != 7 or gameEvent['timer'] != -2:
                        gameEvent['timer'] = -2
                    button['OrderFoodOKButton'].showButton()
                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood1-Line1'],
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY, 
                            window=WindowsRG,
                            bold=True)

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood1-Line2'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY+40, 
                            window=WindowsRG,
                            bold=True)

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood1-Line3'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY+80, 
                            window=WindowsRG,
                            bold=True)
                
                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood1-Line4'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY+120, 
                            window=WindowsRG,
                            bold=True)

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood1-Line5'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY+160, 
                            window=WindowsRG,
                            bold=True)

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood1-Line6'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY+200, 
                            window=WindowsRG,
                            bold=True)

                    button['OrderFoodOKButton'].render()
                case 1:
                    if gameEvent['timer'] == -2:
                        setTimeBomb(7)
                    elif gameEvent['timer'] == 0:
                        gameEvent['timer'] = -2
                        gameEvent['orderFoodPage'] += 1

                    # Please wait while we connect to our online
                    # database and retrieve all available meals.
                    # This may take a few minutes.

                    button['OrderFoodOKButton'].hideButton()

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood2-Line1'], 
                            color="#0000FF", 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY, 
                            window=WindowsRG,
                            bold=True)
                        
                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood2-Line2'], 
                            color="#0000FF", 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY+40, 
                            window=WindowsRG,
                            bold=True)

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood2-Line3'], 
                            color="#0000FF", 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY+80, 
                            window=WindowsRG,
                            bold=True)

                case 2:
                    if gameEvent['timer'] == -2:
                        setTimeBomb(4)
                    elif gameEvent['timer'] == 0:
                        gameEvent['timer'] = -2
                        gameEvent['orderFoodPage'] += 1

                        # Files downloaded, please wait a few seconds
                        # while we waste your time.

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood3-Line1'], 
                            color="#0000FF", 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY, 
                            window=WindowsRG,
                            bold=True)
                        
                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood3-Line2'], 
                            color="#0000FF", 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY+40, 
                            window=WindowsRG,
                            bold=True)

                    ButtonXSave=button['OrderFoodQuitButton'].returnValue('x')

                case 3 | 4:
                    button['OrderFoodQuitButton'].changeValue('x', ButtonXSave)
                    button['OrderFoodTryAgainButton'].hideButton()
                        
                    if gameEvent['timer'] == -2 and gameEvent['orderFoodPage'] != 4:
                        setTimeBomb(2)
                    elif gameEvent['timer'] == 0 and gameEvent['orderFoodPage'] != 4:
                        gameEvent['timer'] = -2
                        gameEvent['orderFoodPage'] += 1

                    # Available Food:
                    # Click the button next to anything you want

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood4-Line1'], 
                            color="#0000FF", 
                            font=normalfontstyle, 
                            x=window['bigWindow'].returnValue('x') + 32 + 344, y=window['bigWindow'].returnValue('y', excludeTitleBar=True) + 80 / 2, 
                            window=WindowsRG,
                            bold=True)
                    if gameEvent['orderFoodPage'] == 4:

                        button['OrderFoodQuitButton'].showButton()

                        GenerateText(
                                size=bigfontsize-12, 
                                text=translation['Description-OrderFood4-Line2'], 
                                color="#0000FF", 
                                font=normalfontstyle, 
                                x=BigWindowSummaryX, y=BigWindowSummaryY, 
                                window=WindowsRG,
                                bold=True)
                            
                        for buttonObject in button:
                            if buttonObject.lower().startswith(('foodselection')):
                                button[buttonObject].showButton()
                                button[buttonObject].render()
                                
                                # Prune Juice
                                # Slice Of Ham
                                # Chickpeas

                            GenerateText(
                                    size=bigfontsize-12, 
                                    text=translation['OrderFood-Food1'], 
                                    color="#0000FF", 
                                    font=normalfontstyle, 
                                    x=window['bigWindow'].returnValue('middleX') - window['bigWindow'].returnValue('w') / 2 + 68, 
                                    y=window['bigWindow'].returnValue('middleY', excludeTitleBar = True) - 16 - 42,
                                    window=WindowsRG,
                                    bold=True)

                            GenerateText(
                                    size=bigfontsize-12, 
                                    text=translation['OrderFood-Food2'], 
                                    color="#0000FF", 
                                    font=normalfontstyle, 
                                    x=window['bigWindow'].returnValue('middleX') - window['bigWindow'].returnValue('w') / 2 + 68, 
                                    y=window['bigWindow'].returnValue('middleY', excludeTitleBar = True) - 16,
                                    window=WindowsRG,
                                    bold=True)

                            GenerateText(
                                    size=bigfontsize-12, 
                                    text=translation['OrderFood-Food3'], 
                                    color="#0000FF", 
                                    font=normalfontstyle, 
                                    x=window['bigWindow'].returnValue('middleX') - window['bigWindow'].returnValue('w') / 2 + 68, 
                                    y=window['bigWindow'].returnValue('middleY', excludeTitleBar = True) - 16 + 40,
                                    window=WindowsRG,
                                    bold=True)
                            
                        button['OrderFoodQuitButton'].render()

                case 5:
                    TryAgainButtonPos = ButtonXSave - button['OrderFoodTryAgainButton'].returnValue('w')
                    QuitButtonPos = ButtonXSave + button['OrderFoodTryAgainButton'].returnValue('w')
                    button['OrderFoodQuitButton'].changeValue('x', QuitButtonPos)
                    button['OrderFoodTryAgainButton'].changeValue('x', TryAgainButtonPos)
                    button['OrderFoodTryAgainButton'].showButton()

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood5-Line1'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY, 
                            window=WindowsRG,
                            bold=True)
                        
                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood5-Line2'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY+80, 
                            window=WindowsRG,
                            bold=True)

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFood5-Line3'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY+120, 
                            window=WindowsRG,
                            bold=True)

                    button['OrderFoodTryAgainButton'].render()
                    button['OrderFoodQuitButton'].render()
                    
                case 6:
                    if gameEvent['timer'] == -2:
                        setTimeBomb(5)
                        for buttonObject in button:
                            if buttonObject.lower().startswith(('orderfood')) or buttonObject.lower().startswith(('foodselection')):
                                button[buttonObject].hideButton()
                    elif gameEvent['timer'] == 0:
                        gameEvent['timer'] = -2
                        window['bigWindow'].closeWindow()

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFoodQuit-Line1'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=BigWindowSummaryX, y=BigWindowSummaryY, 
                            window=WindowsRG,
                            bold=True)

                    GenerateText(
                            size=bigfontsize-12, 
                            text=translation['Description-OrderFoodQuit-Line2'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=800, y=600, 
                            window=WindowsRG,
                            bold=True,
                            center=True)
        elif window['bigWindow'].windowTitle() == translation['WindowTitle-Paint']:
            PaintCanvas.enableCanvas()
            GenerateFrame(
                x=window['bigWindow'].returnValue('x') + 12, 
                y=window['bigWindow'].returnValue('y', excludeTitleBar=True) + 12, 
                w=window['bigWindow'].returnValue('w') - 24, 
                h=window['bigWindow'].returnValue('h', excludeTitleBar=True) - 24, 
                screen=WindowsRG)
            PaintCanvas.render()


    else:
        for buttonObject in button:
            if buttonObject.lower().startswith(('orderfood')) or buttonObject.lower().startswith(('foodselection')):
                button[buttonObject].hideButton()

        gameEvent['orderFoodPage'] = 0
        PaintCanvas.disableCanvas()
        PaintCanvas.clearCanvas()
    

    if window['explorerWindow'].checkIfOpen():

        WindowSummaryX=window['explorerWindow'].returnValue('x') + 18
        WindowSummaryY=window['explorerWindow'].returnValue('y', excludeTitleBar=True) + 18

        DescriptionSummaryY=WindowSummaryY + 48

        if window['bigWindow'].checkIfOpen():
            window['bigWindow'].closeWindow()
        window['bigWindow'].closeWindow()
        
        if window['explorerWindow'].windowTitle() == translation['WindowTitle-MediaPlayer']:
            pygame.draw.rect(WindowsRG,color_negro,(134, 56, 648, 404))
            if gameEvent['customVideoLoaded'] == False:
                Asset['Video-MediaPlayer'].draw_to(VideoFrame, (0, 0))
            else:
                Asset['Video-Custom'].draw_to(VideoFrame, (0, 0))

            # Progress Bar
            pygame.draw.rect(WindowsRG,color_negro,(300, 504, 482, 4))
            pygame.draw.rect(WindowsRG,color_negro,(gameEvent['progressBarXPosition'], 490, 30, 30))

            for buttonObject in button:
                if buttonObject.lower().startswith(('wmp')):
                    button[buttonObject].render()
                    button[buttonObject].showButton()

            # Play Button Triangle
            Triangle_x = 160
            Triangle_y = 482
            pygame.draw.polygon(WindowsRG, color_negro, ((0+Triangle_x, 0+Triangle_y), (20+Triangle_x, 20+Triangle_y), (0+Triangle_x, 40+Triangle_y)))

            # Square
            pygame.draw.rect(WindowsRG, color_negro, (228, 482, 40, 40))

            if gameEvent['customVideoLoaded'] == False:
                if Asset['Video-MediaPlayer'].is_paused == True:
                    button['WMPPlayButton'].changeToggle(False)
                elif Asset['Video-MediaPlayer'].is_playing and Asset['Video-MediaPlayer'].is_paused == False:
                    gameEvent['progressBarXPosition']+=0.3

                if Asset['Video-MediaPlayer'].is_playing and Asset['Video-MediaPlayer'].remaining_time < 21833.333333333332:
                    WindowsRG.blit(VideoFrame, (136, 58))

                if Asset['Video-MediaPlayer'].remaining_time <= 100:
                #window['explorerWindow'].enableCloseButton()
                    gameEvent['wmpCrash'] = True
                    Asset['Video-MediaPlayer'].pause()
                    button['WMPPlayButton'].disableButton()
                    button['WMPPauseButton'].disableButton()
            else:
                Asset['Video-MediaPlayer'].stop()
                if Asset['Video-Custom'].is_paused == True:
                    button['WMPPlayButton'].changeToggle(False)
                elif Asset['Video-Custom'].is_playing and Asset['Video-Custom'].is_paused == False:
                    gameEvent['progressBarXPosition']+=0.1

                if Asset['Video-Custom'].is_playing:
                    WindowsRG.blit(VideoFrame, (136, 58))

                if Asset['Video-Custom'].remaining_time <= 100:
                #window['explorerWindow'].enableCloseButton()
                    gameEvent['wmpCrash'] = True
                    Asset['Video-Custom'].pause()
                    button['WMPPlayButton'].disableButton()
                    button['WMPPauseButton'].disableButton()
                    button['WMPLoadCustomVideo'].disableButton()

            if warnings['testWarning'].checkIfOpen() == False and gameEvent['wmpCrash'] == True:
                warnings['testWarning'].openWindow()
        else:
            GenerateFrame(
                x=window['explorerWindow'].returnValue('x') + 12, 
                y=window['explorerWindow'].returnValue('y', excludeTitleBar=True) + 12, 
                w=window['explorerWindow'].returnValue('w') - 24, 
                h=window['explorerWindow'].returnValue('h', excludeTitleBar=True) - 24, 
                screen=WindowsRG)
            GenerateText(
                    size=normalfontsize, 
                    text=window['explorerWindow'].windowTitle(), 
                    color=color_negro, 
                    font=normalfontstyle, 
                    x=WindowSummaryX, y=WindowSummaryY, 
                    window=WindowsRG,
                    bold=True)

        if window['explorerWindow'].windowTitle() == translation['WindowTitle-ADrive'] or window['explorerWindow'].windowTitle() == translation['WindowTitle-DDrive']:
            GenerateText(
                size=normalfontsize-6, 
                    text=translation['Description-RemovableWait'], 
                    color=color_negro, 
                    font=normalfontstyle, 
                    x=WindowSummaryX, y=DescriptionSummaryY, 
                    window=WindowsRG,
                    bold=True)

        if window['explorerWindow'].windowTitle() == translation['WindowTitle-MyComputer']:
            GenerateText(
                size=normalfontsize-6, 
                text=translation['Description-MyComputer-Line1'], 
                color=color_negro, 
                font=normalfontstyle, 
                x=WindowSummaryX, y=DescriptionSummaryY, 
                window=WindowsRG,
                bold=True)

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-MyComputer-Line2'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+20, 
                        window=WindowsRG,
                        bold=True)

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-MyComputer-Line3'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+40, 
                        window=WindowsRG,
                        bold=True)

            for buttonObject in myComputerIcons:
                myComputerIcons[buttonObject].showButton()
                myComputerIcons[buttonObject].render()
        else:
            for buttonObject in myComputerIcons:
                myComputerIcons[buttonObject].hideButton()
                
        if window['explorerWindow'].windowTitle() == translation['WindowTitle-MyDocuments']:
            
            if gameEvent['timer'] == -2 and gameEvent['documentsCrash'] == False:
                setTimeBomb(3)

            elif gameEvent['timer'] == 0:
                gameEvent['documentsCrash'] = True
                gameEvent['timer'] = -2
                

            if gameEvent['documentsCrash']:
                GenerateText(
                            size=normalfontsize-6, 
                            text=translation['Description-MyDocumentsCrash-Line1'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=WindowSummaryX, y=DescriptionSummaryY, 
                            window=WindowsRG,
                            bold=True)

                GenerateText(
                            size=normalfontsize-6, 
                            text=translation['Description-MyDocumentsCrash-Line2'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=WindowSummaryX, y=DescriptionSummaryY+20, 
                            window=WindowsRG,
                            bold=True)

                GenerateText(
                            size=normalfontsize-6, 
                            text=translation['Description-MyDocumentsCrash-Line3'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=WindowSummaryX, y=DescriptionSummaryY+40, 
                            window=WindowsRG,
                            bold=True)

                GenerateText(
                            size=normalfontsize-6, 
                            text=translation['Description-MyDocumentsCrash-Line4'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=WindowSummaryX, y=DescriptionSummaryY+60, 
                            window=WindowsRG,
                            bold=True)

                GenerateText(
                            size=normalfontsize-6, 
                            text=translation['Description-MyDocumentsCrash-Line5'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=WindowSummaryX, y=DescriptionSummaryY+80, 
                            window=WindowsRG,
                            bold=True)

                warnings['documentsCrash'].openWindow()
            else:
                GenerateText(
                            size=normalfontsize-6, 
                            text=translation['Description-MyDocuments-Line1'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=WindowSummaryX, y=DescriptionSummaryY, 
                            window=WindowsRG,
                            bold=True)

                GenerateText(
                            size=normalfontsize-6, 
                            text=translation['Description-MyDocuments-Line2'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=WindowSummaryX, y=DescriptionSummaryY+20, 
                            window=WindowsRG,
                            bold=True)

                GenerateText(
                            size=normalfontsize-6, 
                            text=translation['Description-MyDocuments-Line3'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=WindowSummaryX, y=DescriptionSummaryY+40, 
                            window=WindowsRG,
                            bold=True)

                GenerateText(
                            size=normalfontsize-6, 
                            text=translation['Description-MyDocuments-Line4'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=WindowSummaryX, y=DescriptionSummaryY+60, 
                            window=WindowsRG,
                            bold=True)

                GenerateText(
                            size=normalfontsize-6, 
                            text=translation['Description-MyDocuments-Line5'], 
                            color=color_negro, 
                            font=normalfontstyle, 
                            x=WindowSummaryX, y=DescriptionSummaryY+80, 
                            window=WindowsRG,
                            bold=True)

        if window['explorerWindow'].windowTitle() == translation['WindowTitle-CDrive']:
            GenerateText(
                    size=normalfontsize, 
                    text=window['explorerWindow'].windowTitle(), 
                    color=color_negro, 
                    font=normalfontstyle, 
                    x=WindowSummaryX, y=WindowSummaryY, 
                    window=WindowsRG,
                    bold=True)

            for buttonObject in CDriveIcons:
                CDriveIcons[buttonObject].showButton()
                CDriveIcons[buttonObject].render()
        else:
            for buttonObject in CDriveIcons:
                CDriveIcons[buttonObject].hideButton()
                
        if window['explorerWindow'].windowTitle() == translation['WindowTitle-RecycleBin']:
            
            button['EmptyRecycleBin'].showButton()
                    
            # This is where stuff you don't want gets shoved.
            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line1'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY, 
                        window=WindowsRG,
                        bold=True)

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line2'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+20, 
                        window=WindowsRG,
                        bold=True)

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line3'],
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+40, 
                        window=WindowsRG,
                        bold=True)

            # Also, this is where files that windows has deleted for no reason get sent.
            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line4'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+80, 
                        window=WindowsRG,
                        bold=True)

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line5'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+100, 
                        window=WindowsRG,
                        bold=True)

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line6'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+120, 
                        window=WindowsRG,
                        bold=True)

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line7'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+140, 
                        window=WindowsRG,
                        bold=True)

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line8'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+160, 
                        window=WindowsRG,
                        bold=True)

            # Click the button below to empty the recycle bin.

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line9'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+200, 
                        window=WindowsRG,
                        bold=True)

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line10'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+220, 
                        window=WindowsRG,
                        bold=True)

            GenerateText(
                        size=normalfontsize-6, 
                        text=translation['Description-RecycleBin-Line11'], 
                        color=color_negro, 
                        font=normalfontstyle, 
                        x=WindowSummaryX, y=DescriptionSummaryY+240, 
                        window=WindowsRG,
                        bold=True)

            button['EmptyRecycleBin'].render()
        else:
            button['EmptyRecycleBin'].hideButton()

    else:
            
        for buttonObject in myComputerIcons:
            myComputerIcons[buttonObject].hideButton()

        for buttonObject in CDriveIcons:
            CDriveIcons[buttonObject].hideButton()

        for buttonObject in button:
            if buttonObject.lower().startswith(('wmp')):
                button[buttonObject].hideButton()
                button[buttonObject].enableButton()

        gameEvent['documentsCrash'] = False
        warnings['testWarning'].closeWindow()
        warnings['documentsCrash'].closeWindow()
        gameEvent['wmpCrash'] = False
        gameEvent['progressBarXPosition']=300
        if gameEvent['customVideoLoaded'] == False:
            Asset['Video-MediaPlayer'].stop()
        else:
            Asset['Video-Custom'].stop()
        button['WMPPlayButton'].changeToggle(False)

    for openWindowDialogues in warnings:
        warnings[openWindowDialogues].render()

    if gameEvent['startMenuOpen'] == True and gameEvent['openingPaint'] == False:
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

        WindowsRG.blit(Asset["WindowsRGStartFlag"], (2, 157))
    else:
        StartButton.changeToggle(False)

    # Barra de Tareas
    pygame.draw.rect(WindowsRG,BarraDeTareas,[0,558,800,42]) 

    # Hour
    GenerateText(size=normalfontsize-2, text="3:00 AM", color=color_negro, font=normalfontstyle, x=1480, y=1155, window=WindowsRG, center=True)

    # Start Button
    StartButton.render()
    WindowsRG.blit(Asset["StartMenu"], (8, 564))
    if system() == "Windows":
        GenerateText(size=bigfontsize-18, text=translation['StartButton'], color=color_negro, font=bigfontstyle, x=185, y=1160, window=WindowsRG, center=True, bold=True)
    else:
        GenerateText(size=bigfontsize-6, text=translation['StartButton'], color=color_negro, font=bigfontstyle, x=185, y=1160, window=WindowsRG, center=True)

    # updates the frames of the game 
    clock.tick(120)
    if "--show-fps" in Arguments:
        GenerateText(size=normalfontsize-2, text=f"{int(clock.get_fps())} FPS", color=color_negro, font=normalfontstyle, x=2, y=2, window=WindowsRG)
    pygame.display.update() 