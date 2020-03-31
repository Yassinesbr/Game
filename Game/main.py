import pygame
import random
import math


pygame.init()
click ="right"
X=800
Y=600
#print("helo")

screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("Skier")
img= pygame.image.load("ski.png")
pygame.display.set_icon(img)


#---------------------player------------------->

playerimg=pygame.image.load("snowboard.png")
playerimgL=pygame.transform.flip(playerimg, True, False)
playerX=370
playerY=80
change =0
def player(x):
    screen.blit(playerimg,(x,playerY))
def turn():
    screen.blit(playerimgL,(playerX,playerY)) 
    #pygame.display.update()


#----------------------Flags--------------------->

flagimg =pygame.image.load("flag.png")
flagX = random.randint(0,740)
flagY = 600      #random.randint(100,650)
changeflag =-0.7
dist=140 #distnace between flags
flag_state="makaynch"

def flags(x,y):
    global flag_state
    flag_state="kayn"
    screen.blit(pygame.transform.flip(flagimg, True, False),(x,y)) 
    screen.blit(flagimg,(x+dist,y))
    
#----------------------pinetree---------------->
pinetreeimg=[]
pinetreeX=[]
pinetreeY= []
changetree = []
pine_state =[]
num_trees=15



for i in range(num_trees):
    pinetreeimg.append(pygame.image.load("winter.png"))
    pinetreeX.append(random.randint(0,740))
    pinetreeY.append(random.randint(600,1050))
    changetree.append(-0.7)
    pine_state.append("makaynch")

def pine_generate(x,y,i):
    #global pine_state
    #pine_state[i] ="kayn"
    screen.blit(pinetreeimg[i],(x,y))

#--------- collision---------------->
def isCol2(playerX,playerY,flagX,flagY):
    distance =math.sqrt((math.pow(playerX-((flagX+70)),2))+(math.pow(playerY-flagY,2)))
    if distance < 50 :
     return True
    else: return False



def isCol(playerX,playerY,pinetreeX,pinetreeY):
    distance =math.sqrt((math.pow(playerX-pinetreeX,2))+(math.pow(playerY-pinetreeY,2)))
    if distance < 30: 
      return True
    else: return False
#--------------------Score----------------->
score_val=0
font=pygame.font.Font('freesansbold.ttf', 20)

textX=10
textY=10

def score(x,y):
    score=font.render("Score : "+str(int(score_val)), True, (200,60,40))
    screen.blit(score,(x,y))


#------------gameover----------->
over_font=pygame.font.Font('freesansbold.ttf', 60)
def game_over():
    gameover=over_font.render("Game Over", True, (250,0,0))
    rect=gameover.get_rect()
    rect.center=((X/2),(Y/2))
    screen.blit(gameover,rect)

#------------------------------------------mainLoop--------------------------------->

test=True
while test:

    screen.fill((229,255,255))
    

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            test=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change = -0.6
                
                click="left"
            if event.key == pygame.K_RIGHT:
                change = 0.6
                click="right"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change = 0
                click="front"
    

    #--------------------------player--------------->
    if playerX >= 740:
        playerX = 740
    if playerX <= 0:
        playerX = 0
    if click is "left":
        turn()    
    else:    
        player(playerX)
    playerX += change 

    #-----------------------flag----------->
    if flagX >= 640:
        flagX = 640
    if flagX <= 0:
        flagX = 0

    if flagY <= 0: 
      flag_state="makaynch" 
      flagY=600 

    if flag_state is "makaynch":
        flagX= random.randint(0,640)
        flags(flagX,flagY)

    if flag_state is "kayn":
       flags(flagX,flagY)
       flagY += changeflag        

    col1 = isCol2(playerX, playerY, flagX, flagY)
    if col1:
        score_val += 0.01


    #-------------------------generate trees--------->
    for i in range(num_trees):
        pinetreeY[i] += changetree[i]
        if pinetreeX[i] >= 740:
            pinetreeX[i] = 740
        if pinetreeX[i] <= 0:
            pinetreeX[i] = 0    
    
        
        if pinetreeX[i] >= flagX-10 and pinetreeX[i] <= flagX+dist+46*2 :
            if  pinetreeY[i] >= flagY-30 and pinetreeY[i] <= flagY+40:
                pinetreeX[i]=random.randint(0,740)
                pinetreeY[i]=random.randint(600,1050)



        if pinetreeY[i] <= -200: 
          pinetreeY[i]=random.randint(600,1050)
          pinetreeX[i]=random.randint(0,740)
          pinetreeY[i] += changetree[i]

        pine_generate(pinetreeX[i],pinetreeY[i],i)   
               
        #--------------collison--------------->
        col= isCol(playerX,playerY,pinetreeX[i],pinetreeY[i])
        if col:
            #for i in range(6):
            #    score=0
            game_over()
            test=False
            
            

        

        

    #score_val += 0.01
    score(textX,textY)

    pygame.display.update()