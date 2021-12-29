import math,sys
import pygame
from pygame.locals import *

#exit game if window is closed
def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

#create window
w,h = 720,720
pygame.init()
CLOCK = pygame.time.Clock()
FPS = 120
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Robot Game")

#Colors
BLACK = (0,0,0,255)
WHITE = (255,255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

RobotX,RobotY = w/2,h/2 #Robot position at center 
PmouseX, PmouseY = RobotX,RobotY #Mouse position
dx,dy = 0,0 #Robot movement
totalDistance = 0 #Total distance traveled

while True:
    events()
    #Get mouse position
    m = pygame.mouse.get_pressed()
    if m[0] and totalDistance == 0:
        mouseX,mouseY = pygame.mouse.get_pos()
        theta = math.atan2(mouseY-PmouseY,mouseX-PmouseX) #Angle between previous mouse and new mouse
        dx,dy = math.cos(theta),math.sin(theta) #Robot movement
        thetaSend = 90+theta*180/math.pi
        if thetaSend >180:
            thetaSend = thetaSend - 360
        print(dx,dy,thetaSend)
        totalDistance = int(math.sqrt((mouseX-PmouseX)**2+(mouseY-PmouseY)**2)) #Total distance to mouse
        
        PmouseX,PmouseY = mouseX,mouseY #mouse new position
    if totalDistance > 0:
        totalDistance -= 1
        RobotX += dx
        RobotY += dy
    pygame.draw.circle(screen,BLUE,(int(RobotX),int(RobotY)),25,0)
    if totalDistance > 0:
        pygame.draw.circle(screen,RED,(PmouseX,PmouseY),5)
        pygame.draw.line(screen,RED,(int(RobotX),int(RobotY)),(int(PmouseX),int(PmouseY)))
    pygame.display.update()
    CLOCK.tick(FPS)
    screen.fill(BLACK)
    