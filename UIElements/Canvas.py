import pygame

class Canvas:

    def __init__(self, x, y, w, h, screen, color=(0, 0, 0), bgColor=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.color = color
        self.bgColor = bgColor
        self.paint = []
        self.canvasEnabled = True
        self.mouseHeld = False

        self.canvasArea = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        if self.canvasEnabled == True:
            try:
                if len(self.paint) != 0:
                    for thing in self.paint:
                        if thing.left + 4 == self.MouseX and thing.top + 4 == self.MouseY:
                            return
                    self.paint.append(pygame.Rect(self.MouseX - 4, self.MouseY - 4, 8, 8))
                else:
                    self.paint.append(pygame.Rect(self.MouseX - 4, self.MouseY - 4, 8, 8))
            except AttributeError:
                self.paint.append(pygame.Rect(self.MouseX - 4, self.MouseY - 4, 8, 8))

    def checkPress(self, event):
        if self.canvasEnabled == True:
            if self.canvasArea.collidepoint(pygame.mouse.get_pos()):
                self.MousePos=pygame.mouse.get_pos()
                self.MouseX=self.MousePos[0]
                self.MouseY=self.MousePos[1]

                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouseHeld = False
                    return

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseHeld = True
                    self.draw()
                    
                if self.mouseHeld == True and event.type == pygame.MOUSEMOTION:
                    self.draw()
            else:
                self.mouseHeld = False
                return

    def enableCanvas(self):
        self.canvasEnabled = True
    
    def disableCanvas(self):
        self.canvasEnabled = False

    def clearCanvas(self):
        self.paint = []

    def render(self):
        if self.canvasEnabled == True:
            pygame.draw.rect(self.screen, self.bgColor, self.canvasArea)
            if len(self.paint) == 0:
                pass
            else:
                for thing in self.paint:
                    pygame.draw.rect(self.screen, self.color, thing)

    def changeValue(self, variable, value):
        match variable:
            case 'color':
                self.color = value