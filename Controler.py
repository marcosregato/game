# *-* coding: utf-8 *-*
import pygame

from ChamarCenario import *

class Controler():

    '''
        Não está funcionando
    '''
    def controlerPersonagen(self,tela_x, tela_y,personagem):
        crashed = False


        try:
            posicao_x = (tela_x * 0.11)
            posicao_y = (tela_y * 0.65)

            '''
            ERRO
                está setando o valor ERRO boneco : <Surface(110x120x32 SW)> 
                na variavél boneco
            '''
            boneco = pygame.display.update('lutador/'+personagem) # ERRO boneco : <Surface(110x120x32 SW)>
            #pygame.display.set_mode = altura e largura da janela
            gameDisplay = pygame.display.flip(posicao_x, posicao_y, boneco)

            while not crashed:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        crashed = True
                    ############################
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            movi_x = -5
                        elif event.key == pygame.K_RIGHT:
                            movi_x = 5
                    if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                        movi_x = 0
                #x += tela_x
        except Exception, e:
            print e

if __name__=='__name__':
    c = Controler()
    c.controlerPersonagen(2,2,'asdf')