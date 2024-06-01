import pygame

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