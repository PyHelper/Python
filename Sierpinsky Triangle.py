import pygame
import random

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Sierpinsky Triangle")
#Трикутник (a,b,c).
#Розміри.
widht=10
height=10
widhtr=1
heightr=1


#a

x=250
y=0

#b
x1=0
y1=490

#c
x2=490
y2=490

#Рандомна точка.
xr=random.randint(0,500)
yr=random.randint(0,500)
############
a=2

#ДРЕВНЯ МАГІЯ НЕ ЧІПАЄМО ТУТ НІЧОГО.
run = True
while  run:
          pygame.time.delay(1)
          for ivent in pygame.event.get():
                    if ivent.type == pygame.QUIT:
                              run = False
          r=random.randint(1,3)
          if r<=1:
                    xr=(xr+x)/a
                    yr=(yr+y)/a
          elif r<=2:
                    xr=(xr+x1)/a
                    yr=(yr+y1)/a
          elif r<=3:
                    xr=(xr+x2)/a
                    yr=(yr+y2)/a

          pygame.draw.rect(win,(0,225,0), (x, y, widht, height))
          pygame.draw.rect(win,(225,0,0), (x1, y1, widht, height))
          pygame.draw.rect(win,(0,0,225), (x2, y2, widht, height))                    
          pygame.draw.rect(win,(random.randint(0,225),random.randint(0,225),random.randint(0,225)), (xr, yr, widhtr, heightr))
          pygame.display.update()

pygame.quit()


