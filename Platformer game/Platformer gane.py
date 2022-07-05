"python.suggest.autoImports: false"#disables autoImports for python in vscode file
import pygame
import sys
import random

pygame.init()
screenHeight=(1080)
screenWidth=(1920)
background=pygame.image.load("C:\VsCode\Platformer game\Game.png")
red=(255,0,0)
screen=pygame.display.set_mode((screenWidth,screenHeight),pygame.RESIZABLE)
clock=pygame.time.Clock()

#creating floor rect
Ground=pygame.Rect(0,825,screenWidth,500)#defines Ground width and height along with spawning coordinates

class Steve(pygame.sprite.Sprite):
    def __init__(self,width,height,color,pos_x,pos_y):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image=pygame.image.load("C:\VsCode\Platformer game\Goblin.png")
        self.rect=self.image.get_rect()
        self.rect.center = [pos_x,pos_y]#tells rect to follow postion x and y
        
    def updateLeft(self):
       self.rect.x+=5
    
    def updateRight(self):
        self.rect.x-=5

    def jumpUp(self):#moves up by increments of 1 so it looks smoother
        self.rect.y-=2 
        self.rect.y-=2
        self.rect.y-=2
        self.rect.y-=2
        self.rect.y-=2
        self.rect.y-=2
        self.rect.y-=2
        global Gravity
        Gravity=1
  


    def Vertical_vel(self):
        global Gravity
        self.rect.y+=Gravity

    def collisionFloor(self):
        if self.rect.colliderect(Ground):
            global Gravity
            Gravity=0
            print("steve")
   
        




       
        
steve=Steve(10,10,(255,255,255),screenWidth/2,screenHeight/2)

#making an instance of class with arguments NOTE CANNOT DRAW SPRITES INDIVUALLY HAVE TO GROUP THEM

Steve_group=pygame.sprite.Group() 
#adds steve to group
Steve_group.add(steve)


while True:
    Stevex=steve.rect.x
    Gravity=9.8*((300-20)/(Stevex-screenWidth))
    steve.Vertical_vel()
    x,y=screen.get_size()
    steve.collisionFloor()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                steve.updateLeft()
              
        
        
            if event.key ==pygame.K_LEFT:
                steve.updateRight()

            if event.key ==pygame.K_SPACE:
                    steve.jumpUp()
                    direction=random.randint(1,2)
                    if direction==1:
                        steve.updateLeft()
                        steve.updateLeft()
                        steve.updateLeft()
                        steve.updateLeft() 


                    if direction==2:
                        steve.updateRight()
                        steve.updateRight()
                        steve.updateRight()
                        steve.updateRight()
           
        if event.type ==pygame.KEYUP:

             if event.key ==pygame.K_RIGHT:
                steve.updateLeft()
                
            
             if event.key ==pygame.K_LEFT:
                steve.updateRight()

             



    pygame.display.flip()
    screen.blit(background,(0,0))
    Steve_group.draw(screen)
    
    clock.tick(60)#sets frame rate
