import pygame
from pygame.locals import * 

#varijable ekrana
hight  = int(input("Enter hight: "))
width  = int(input("Enter width: "))

pokretanje = True


#igrac
#polozaj na ekranu
x = hight/2 - 32
y = width/2 - 32

#premakud se krece
naprijed = False
dolje = False
desno = False
lijevo = False

while pokretanje == True:

    
    #display
    window = pygame.display.set_mode((hight, width))

    window.fill((255, 0, 0))


    #igrac
    igrac = pygame.image.load("ase48.png").convert()
    window.blit(igrac, (x, y))
    
    pygame.display.flip()
    
    #micanje igraca
    if(naprijed):
        y -= 0.1
    
    elif(dolje):
        y += 0.1

    elif(desno):
        x += 0.1

    elif(lijevo):
        x -= 0.1


    for event in pygame.event.get():

        #provjerava koja je tipka pritisnuta
        if(event.type == KEYDOWN):

            if(event.key == K_w):
                if(dolje):
                    pokretanje = False
                
                else:
                    naprijed = True
                    dolje = False
                    desno = False
                    lijevo = False

            elif(event.key == K_s):
                if(naprijed):
                    pokretanje = False

                else:
                    naprijed = False
                    dolje = True
                    desno = False
                    lijevo = False

            elif(event.key == K_d):
                if(lijevo):
                    pokretanje = False
                
                else:
                    naprijed = False
                    dolje = False
                    desno = True
                    lijevo = False

            elif(event.key == K_a):
                if(desno):
                    pokretanje = False

                else:
                    naprijed = False
                    dolje = False
                    desno = False
                    lijevo = True


            #ako je ovo pritisnuto zaustavlja igru
            if(event.key == K_ESCAPE):
                pokretanje = False