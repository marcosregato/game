# *-* coding: utf-8 *-*

import pygame
from pygame.locals import *
from MinhaTela import *

class ChamarCenario():

    def __init__(self):
        pass

    x = 1000
    y = 600

    def chamarCenario(sef,personagem):
       #controler = Controler()

       '''
       ERRO
       update requires a rectstyle or sequence of recstyles(procurar na internet)
       '''

       listaPersonagem = ['exu_mirim','lucifer','maria_7_cat','exu_lucifer','ze_pilintra','exu_tata','maria_7_encruz']

       try:
           for id, item in enumerate(listaPersonagem):
               while personagem == listaPersonagem[id]:
                   pygame.init()
                   tela = pygame.display.set_mode((ChamarCenario.x, ChamarCenario.y))
                   img_fundo = pygame.image.load("cenarios/"+personagem+"_cena.jpg").convert()
                   tela.blit(img_fundo, [0, 0])
                   som = pygame.mixer.Sound("sound/"+personagem+"_som.wav")
                   som.play()
                   pygame.display.flip()
                   break

       except ChamarCenario as e:
           print ('EXCEPT cenario >>>> '+ e.value)
       except IOError as ex:
           print ('IOError >>>> '+ ex.value)