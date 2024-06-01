import pygame
from .Buttons import Button
from platform import system
import os

ProgramDirectory=os.path.dirname(__file__,)
SoundDirectory=os.path.join(ProgramDirectory, '..', 'Assets', 'Sound')

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

class Window:

    closeText=pygame.font.SysFont(normalfontstyle,bigfontsize-19)
    closeTexttoBlit=closeText.render("X", True, (0, 0, 0))

    def __init__(self, x, y, w, h, screen, title='', color=(204, 204, 204)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = "#0000FF"
        self.screen = screen

        self.closeButtonEnabled = True
        
        self.title = title
        self.titleSave = title

        # Main Window
        self.window = pygame.Rect(x+2, y+32, w-4, h-34)

        # Frame Decorations
        self.frame2 = pygame.Rect(x+2, y+2, w-2, h-2) # Black Shading
        self.frame1 = pygame.Rect(x, y, w, h) # White Shading

        # Title Bar
        self.bar = pygame.Rect(x+2, y+2, w-4, 28)

        self.closeButtonX = self.x+self.w-28
        self.closeButtonY = self.y+4
        self.closeButtonHeight = 24
        self.closeButtonWeight = 24

        self.titleBarText = pygame.Rect(self.closeButtonX+2, self.closeButtonY+2, self.closeButtonHeight-4, self.closeButtonWeight-4)

        # Close Button
        self.closeButtonShade2 = pygame.Rect(self.closeButtonX, self.closeButtonY, self.closeButtonWeight-2, self.closeButtonHeight-2)
        self.closeButtonShade1 = pygame.Rect(self.closeButtonX, self.closeButtonY, self.closeButtonWeight, self.closeButtonHeight)

        self.closeButton = pygame.Rect(self.closeButtonX+2, self.closeButtonY+2, self.closeButtonHeight-4, self.closeButtonWeight-4)

        self.closeButtonHeld = False
        self.closeButtonPressed = False
        self.closed = True

        self.fontstyle = pygame.font.SysFont(bigfontstyle,bigfontsize-10)
        self.actualtext = self.fontstyle.render(self.title, True, self.white)
        

    def openWindow(self, title=''):
        self.closed = False
        if len(title) == 0:
            self.title = self.titleSave
        else:
            self.title = title
    
    def closeWindow(self):
        self.closed = True
        self.title = ''
    
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

            self.screen.blit(self.closeTexttoBlit, (self.closeButtonX + (self.closeButtonWeight / 8), self.y + self.closeButtonHeight / 8)) 
            self.actualtext = self.fontstyle.render(self.title, True, self.white)
            self.screen.blit(self.actualtext, (self.x + 4, self.y + 6)) 

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

    def returnValue(self, value, excludeTitleBar=False):
        match value:
            case 'x':
                return self.x
            case 'y':
                if excludeTitleBar:
                    return self.y+32
                else:
                    return self.y
            case 'w':
                return self.w
            case 'h':
                if excludeTitleBar:
                    return self.h-32
                else:
                    return self.h
            case 'middleX':
                self.halftheWeight=int(self.w // 2)
                return self.x+self.halftheWeight
            case 'middleY':
                self.halftheHeight=int(self.h // 2)
                if excludeTitleBar:
                    return self.y+self.halftheHeight+32
                else:
                    return self.y+self.halftheHeight
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

class ErrorMessage:

    pygame.mixer.music.load(os.path.join(SoundDirectory, 'Chord.wav'))

    def __init__(self, x, y, screen, title="", buttonLabel="OK", message="This is a warning message.", function="", functionArguments=[], wordWrap=False):
        self.x = x
        self.y = y
        self.windowWeight=460
        self.windowHeight=240
        self.color = (0,0,0)
        self.screen = screen
        self.lineCharLimit = 38
        
        if wordWrap == True:
            self.message = message.rstrip().split()
            for word in self.message:
                if len(word) >= self.lineCharLimit:
                    raise NotImplementedError(f"The word '{word}' is longer or equal than {self.lineCharLimit} characters (it has {len(word)} characters)")

            self.message.append('123456789012345678901234567890123456123456789012345678901234567890123456')
        else:
            self.message = message

        self.fontstyle=pygame.font.SysFont(normalfontstyle,normalfontsize-2)

        # 38 characters is the limit of one line
        
        self.lines = []
        self.textToRender = []

        if wordWrap == True:
            self.aux = ""
            self.auxiliarVariable = 0
            
            for i in range(0, len(self.message)+1):
                if len(self.aux) + len(self.message[i - self.auxiliarVariable]) < self.lineCharLimit:
                    self.aux += f"{self.message[i - self.auxiliarVariable]} "                   
                else:
                    self.lines.append(self.aux.rstrip())
                    self.aux = ""
                    self.auxiliarVariable+=1

            self.lines.append(self.aux.rstrip())

            if len(self.lines[-1]) == 0:
                self.lines.pop(-1)
        else:
            for m in range(0, len(self.message), self.lineCharLimit):
                self.lines.append(self.message[m: m+self.lineCharLimit])

        for item in self.lines:
            self.textToRender.append(self.fontstyle.render(item, True, self.color))

        self.ErrorMessageWindow = Window(self.x, self.y, self.windowWeight, self.windowHeight, screen, title)
        self.ErrorMessageButton = Button(x=self.ErrorMessageWindow.returnValue('middleX'), y=self.ErrorMessageWindow.returnValue('y') + self.windowHeight - 32, screen=self.screen, label=buttonLabel, holdButtonifPressed=True, function=function, functionArguments=functionArguments, bold=True)
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
            TextX=self.ErrorMessageWindow.returnValue('x')+94
            TextY=self.ErrorMessageWindow.returnValue('y')+42

            self.separation = 0

            for item in self.textToRender:
                self.screen.blit(item, (TextX, TextY+self.separation)) 
                self.separation+=24
                
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