import pygame
from platform import system

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
        print(self.title)

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