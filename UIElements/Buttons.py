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

class Button:
    
    def __init__(self, x, y, screen, label='', function=None, functionArguments=[], h=None, w=None, color=(204,204,204), hoverColor=(204,204,204), holdColor=(204,204,204), holdButtonifPressed=False, functionOnToggleDisable=None, functionArgumentsOnToggleDisable=[], shading=True, shadingColor1=(0,0,0), shadingColor2=(255,255,255), textColor=(0,0,0), bold=False):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
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

        self.shading=shading
        self.buttonHover = False
        if holdButtonifPressed == True:
            self.buttonToggle = False
        else:
            self.buttonToggle = None

        self.label = label
        self.buttonHidden = False

        self.fontstyle=pygame.font.SysFont(normalfontstyle,25)

        if bold == True:
            self.fontstyle.bold=True

        self.actualtext=self.fontstyle.render(label, True, self.textColor)
        self.text_rect = self.actualtext.get_rect(center=(self.x, self.y)) 

        self.textx=self.text_rect[0]
        self.texty=self.text_rect[1]
        self.textweight=self.text_rect[2]
        self.textheight=self.text_rect[3]

        # Button
        if self.h == None and self.w == None:
            self.buttonShade1 = pygame.Rect(self.textx-8, self.texty-2, self.textweight+18, self.textheight+4)
            self.buttonShade2 = pygame.Rect(self.textx-8, self.texty-2, self.textweight+16, self.textheight+2)

            self.button = pygame.Rect(self.textx-6, self.texty, self.textweight+14, self.textheight)
        else:
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
        
            if self.buttonHover == True and self.buttonHeld == True and self.buttonEnabled == True:
                pygame.draw.rect(self.screen, self.holdColor, self.button)
            elif self.buttonHover == True and self.buttonEnabled == True:
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
                if self.button.collidepoint(event.pos):
                    self.buttonHeld = True
                else:
                    self.buttonHeld = False

            if event.type == pygame.MOUSEBUTTONUP:

                if self.buttonHeld == True and self.button.collidepoint(event.pos):
                    self.buttonPressed = True
                    self.buttonHeld = False
                    if self.holdButtonifPressed == True and self.buttonToggle == False:
                        self.buttonToggle = True
                    elif self.holdButtonifPressed == True and self.buttonToggle == True:
                        self.buttonToggle = False
                else:                    
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

    def changeValue(self, variable, value):
        match variable:
            case 'x':
                self.x = int(value)
            case 'y':
                self.y = value
            case 'w':
                self.w = value
            case 'h':
                self.h = value
            case default:
                raise ValueError('Unknown variable or parameter of this button')
        
        if self.h == None and self.w == None:
            self.text_rect = self.actualtext.get_rect(center=(self.x, self.y)) 

            self.textx=self.text_rect[0]
            self.texty=self.text_rect[1]
            self.textweight=self.text_rect[2]
            self.textheight=self.text_rect[3]

            self.buttonShade1 = pygame.Rect(self.textx-8, self.texty-2, self.textweight+18, self.textheight+4)
            self.buttonShade2 = pygame.Rect(self.textx-8, self.texty-2, self.textweight+16, self.textheight+2)

            self.button = pygame.Rect(self.textx-6, self.texty, self.textweight+14, self.textheight)
        else:
            self.buttonShade2 = pygame.Rect(self.x-2, self.y-2, self.w+2, self.h+2)
            self.buttonShade1 = pygame.Rect(self.x-2, self.y-2, self.w+4, self.h+4)
            
            self.button = pygame.Rect(self.x, self.y, self.w, self.h)

    def returnValue(self, value):
        match value:
            case 'x':
                return self.x

            case 'y':
                return self.y

            case 'w':
                if self.w != None:
                    return self.w
                else:
                    return self.textweight + 18

            case 'h':
                if self.h != None:
                    return self.h
                else:
                    return self.textheight + 4

            case 'middleX':
                if self.w != None:
                    self.halftheWeight = int(self.w // 2)
                    return self.x + self.halftheWeight
                else:
                    self.halftheWeight = int(self.textweight // 2)
                    return self.x + self.halftheWeight + 18

            case 'middleY':
                if self.h != None:
                    self.halftheWeight = int(self.h // 2)
                    return self.y + self.halftheHeight
                else:
                    self.halftheWeight = int(self.textheight // 2)
                    return self.y + self.halftheHeight + 4

            case 'color':
                return self.color
            case default:
                raise ValueError('Unknown variable or parameter of this button')


class IconButton:
    def __init__(self, x, y, w, h, icon, screen, label="", color=(255, 255, 255), holdColor=(150, 150, 150), hoverColor=(230, 230, 230), textColor=(0, 0, 0), function=None, functionArguments=[], font=normalfontstyle, fontSize=normalfontsize-6):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.textColor = textColor
        self.label = label
        self.fontSize = fontSize
        self.font = font
        self.iconSize = self.h/2
        self.screen = screen
        self.iconImageSave = icon
        self.iconImage = pygame.transform.scale(self.iconImageSave, (self.iconSize, self.iconSize))
        self.iconButton = Button(
            x=self.x, y=self.y, 
            w=self.w, h=self.h, 
            screen=screen, 
            shading=False, 
            color=color, 
            hoverColor=hoverColor, 
            holdColor=holdColor, 
            function=function, 
            functionArguments=functionArguments)

        self.iconButtonShown = False
        self.iconButtonEnabled = True

        self.fontstyle=pygame.font.SysFont(self.font, self.fontSize)
        self.textPosition=(self.x,self.y)

        self.actualtext=self.fontstyle.render(self.label, True, textColor)

    def render(self):
        if self.iconButtonShown == True:
            self.iconButton.render()
            self.screen.blit(self.iconImage, (self.x+self.w/4, self.y+self.h/8))

            self.text_rect = self.actualtext.get_rect(center=(self.x+self.w/2, self.h+self.y-18))
            self.screen.blit(self.actualtext, self.text_rect) 

    def checkPress(self, event):
        if self.iconButtonShown == True and self.iconButtonEnabled == True:
            self.iconButton.checkPress(event)

    def showButton(self):
        self.iconButtonShown = True
        self.iconButton.showButton()

    def hideButton(self):
        self.iconButtonShown = False
        self.iconButton.hideButton()

    def changeValue(self, variable, value):
        match variable:
            case 'x':
                self.iconButton.changeValue(variable, value)
                self.x = value
            case 'y':
                self.iconButton.changeValue(variable, value)
                self.y = value
            case 'w':
                self.iconButton.changeValue(variable, value)
                self.w = value
            case 'h':
                self.iconButton.changeValue(variable, value)
                self.h = value
            case default:
                raise ValueError('Unknown variable or parameter of this button')

        self.iconSize = self.h/2
        self.iconImage = pygame.transform.scale(self.iconImageSave, (self.iconSize, self.iconSize))

        self.fontstyle=pygame.font.SysFont(self.font, self.fontSize)
        self.textPosition=(self.x,self.y)

        self.actualtext=self.fontstyle.render(self.label, True, self.textColor)

    def enableButton(self):
        self.iconButtonEnabled = True
        self.iconButton.enableButton()

    def disableButton(self):
        self.iconButtonEnabled = False
        self.iconButton.disableButton()