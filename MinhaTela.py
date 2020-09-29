# *-* coding: utf-8 *-*

import sys
#import pygame.locals
from time import sleep
from ChamarCenario import *
from Controler import *
import time

# operador is  = Avalia a verdade se as variáveis ​​de cada lado do ponto de operador para o mesmo objeto e falso caso contrário.
# operador in  = Avalia a verdade se ele encontrar uma variável na seqüência especificada e falso caso contrário.
#len (lista) retorna o número de elementos de lista

class MinhaTela:

    def __init__(self):
        pass

    x = 1000
    y = 600

    pygame.init()
    tela = pygame.display.set_mode((x, y))
    img_fundo = pygame.image.load('img/fundo2.png').convert()
    tela.blit(img_fundo, [0, 0])

    linha_1 = 250
    linha_2 = 420
    #----------- MENU -----------------

    exu_mirim = pygame.image.load("personagem/exu_mirim_menu.png")
    coluna = 310
    tela.blit(exu_mirim, (coluna, linha_1))
        # -------
    lucifer = pygame.image.load("personagem/lucifer_menu.png")
    coluna = 430
    tela.blit(lucifer, (coluna, linha_1))
        # -------
    maria_pad_sete_cat = pygame.image.load("personagem/maria_7_cat_menu.png")
    coluna = 550
    tela.blit(maria_pad_sete_cat, (coluna, linha_1))
        # -------
    exu_lucifer = pygame.image.load("personagem/exu_lucifer_menu.png")
    coluna = 250
    tela.blit(exu_lucifer, (coluna, linha_2))
        # -------
    ze_pilintra = pygame.image.load("personagem/ze_pilintra_menu.png")
    coluna = 370
    tela.blit(ze_pilintra, (coluna, linha_2))
        # -------
    exu_caveira = pygame.image.load("personagem/exu_tata_menu.png")
    coluna = 490
    tela.blit(exu_caveira, (coluna, linha_2))
        # -------
    maria_pad_sete_encru = pygame.image.load("personagem/maria_7_encruz_menu.png")
    coluna = 610
    tela.blit(maria_pad_sete_encru, (coluna, linha_2))

    #----------- MENU -----------------

    def run(self):
        pathDiretorioPersonagem = "personagem/"
        meuTempo = pygame.time.Clock()

        # som = pygame.mixer.Sound("sound/som_abertura.wav")
        # som.play()
        cenario = ChamarCenario()
        controler = Controler()
        perso_c,perso_l = 0,20

        try:
            pygame.display.set_caption('JOGO')
            temp = 0

            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    '''
                        erro no tempo de escolha, esta sempre pegando o valor 60
                    '''
                    while (temp <= 60) == True:

                        #fonte = pygame.font.Font("fontes/font.ttf", 30) LINUX
                        fonte = pygame.font.Font(pygame.font.get_default_font(), 30)
                        print("PASSEI AQUI >>", temp)
                        textoTempo = fonte.render(str(temp), True, [0,0,0])
                        self.tela.blit(textoTempo, [400, 5])
                        pygame.display.flip()

                        if event.type == MOUSEBUTTONDOWN:
                                '''
                                ERRO
                                    não está apagando o ultimo tempo, está gravando um em cima do outro
                                '''

                                c,l = 750,20

                                # Cria uma tupla com o valor das cordenadas do mause(x,y)
                                curso = pygame.mouse.get_pos()

                                # Representa as posição da imagem no menu
                                if 310 <= curso[0] <= 410 and 255 <= curso[1] <= 405:
                                    exu_mirim = pygame.image.load(pathDiretorioPersonagem+"exu_mirim.png").convert()
                                    self.tela.blit(exu_mirim,(perso_c,perso_l))
                                    exu_mirim_select = pygame.image.load(pathDiretorioPersonagem+"exu_mirim_select.png").convert()
                                    coluna = 310
                                    linha = 250
                                    self.tela.blit(exu_mirim_select, (coluna, linha))

                                    '''
                                        ERRO
                                        Não está colocando o lutador, está colocando o personagem grande e o 
                                        persongem escolhido no cenário
                                        TALVEZ colocando Thead possa resolver o problema
                                        
                                        ERRO
                                        O botao enter(teclado) não está funcionando
                                    '''

                                    if temp >= 60 or pygame.key == K_KP_ENTER:
                                        grande = pygame.image.load(pathDiretorioPersonagem + "exu_mirim.png").convert()
                                        self.tela.blit(grande, (c, l))
                                        pygame.display.update()

                                        sleep(2)
                                        pygame.display.flip()

                                        cenario.chamarCenario('exu_mirim')


                                        controler.controlerPersonagen(MinhaTela.x, MinhaTela.y, '../lutador/exu_mirim_lutador.png')

                                elif 435 <= curso[0] <= 535 and 255 <= curso[1] <= 405:
                                    lucifer = pygame.image.load(pathDiretorioPersonagem+"lucifer.png").convert()
                                    self.tela.blit(lucifer,(perso_c,perso_l))
                                    lucifer_select = pygame.image.load(pathDiretorioPersonagem+"lucifer_select.png").convert()
                                    coluna = 430
                                    linha = 250
                                    self.tela.blit(lucifer_select, (coluna, linha))

                                    if temp >= 60 or pygame.key == K_KP_ENTER:
                                        grande = pygame.image.load(pathDiretorioPersonagem+"exu_mirim.png").convert()
                                        self.tela.blit(grande,(c,l))
                                        pygame.display.update()
                                        sleep(2)
                                        cenario.chamarCenario('lucifer')
                                        controler.controlerPersonagen(MinhaTela.x, MinhaTela.y, 'lutador/lucifer_lutador.png')

                                elif 550 <= curso[0] <= 650 and 285 <= curso[1] <= 405:
                                    maria_7_cat = pygame.image.load(pathDiretorioPersonagem+"maria_7_cat.png").convert()
                                    self.tela.blit(maria_7_cat,(perso_c,perso_l))
                                    maria_pad_sete_cat = pygame.image.load(pathDiretorioPersonagem+"maria_7_cat_select.png").convert()
                                    coluna = 550
                                    linha = 250
                                    self.tela.blit(maria_pad_sete_cat, (coluna, linha))

                                    if temp >= 60 or pygame.key == K_KP_ENTER:
                                        grande = pygame.image.load(pathDiretorioPersonagem+"exu_mirim.png").convert()
                                        self.tela.blit(grande,(c,l))
                                        pygame.display.update()
                                        sleep(2)
                                        cenario.chamarCenario('maria_7_cat')
                                        controler.controlerPersonagen(MinhaTela.x, MinhaTela.y, 'maria_7_cat_lutador.png')

                                elif 250 <= curso[0] <= 350 and 425 <= curso[1] <= 575:
                                    exu_lucifer = pygame.image.load(pathDiretorioPersonagem+"exu_lucifer.png").convert()
                                    self.tela.blit(exu_lucifer,(perso_c,perso_l))
                                    exu_lucifer_select = pygame.image.load(pathDiretorioPersonagem+"exu_lucifer_select.png").convert()
                                    coluna = 250
                                    linha = 420
                                    self.tela.blit(exu_lucifer_select, (coluna, linha))

                                    if temp >= 60 or pygame.key == K_KP_ENTER:
                                        grande = pygame.image.load(pathDiretorioPersonagem+"exu_mirim.png").convert()
                                        self.tela.blit(grande,(c,l))
                                        pygame.display.update()
                                        sleep(2)
                                        cenario.chamarCenario('exu_lucifer')
                                        controler.controlerPersonagen(MinhaTela.x, MinhaTela.y, 'exu_lucifer_lutador.png')

                                elif 370 <= curso[0] <= 470 and 425 <= curso[1] <= 575:
                                    ze_pilintra = pygame.image.load(pathDiretorioPersonagem+"ze_pilintra.png").convert()
                                    self.tela.blit(ze_pilintra,(perso_c,perso_l))
                                    ze_pilintra_select = pygame.image.load(pathDiretorioPersonagem+"ze_pilintra_select.png").convert()
                                    coluna = 370
                                    linha = 420
                                    self.tela.blit(ze_pilintra_select, (coluna, linha))

                                    if temp >= 60 or pygame.key == K_KP_ENTER:
                                        grande = pygame.image.load(pathDiretorioPersonagem+"exu_mirim.png").convert()
                                        self.tela.blit(grande,(c,l))
                                        pygame.display.update()
                                        sleep(2)
                                        cenario.chamarCenario('ze_pilintra')
                                        controler.controlerPersonagen(MinhaTela.x, MinhaTela.y, 'ze_pilintra_lutador.png')

                                elif 490 <= curso[0] <= 590 and 425 <= curso[1] <= 575:
                                    perso_grande = pygame.image.load(pathDiretorioPersonagem+"exu_tata.png").convert()
                                    self.tela.blit(perso_grande,(perso_c,perso_l))
                                    exu_caveira = pygame.image.load(pathDiretorioPersonagem+"exu_tata_select.png").convert()
                                    coluna = 490
                                    linha = 420
                                    self.tela.blit(exu_caveira, (coluna, linha))

                                    if temp >= 60 or pygame.key == K_KP_ENTER:
                                        grande = pygame.image.load(pathDiretorioPersonagem+"exu_mirim.png").convert()
                                        self.tela.blit(grande,(c,l))
                                        pygame.display.update()
                                        sleep(2)
                                        cenario.chamarCenario('exu_tata')
                                        controler.controlerPersonagen(MinhaTela.x, MinhaTela.y, 'exu_tata_lutador.png')

                                elif 610 <= curso[0] <= 710 and 425 <= curso[1] <= 575:
                                    perso_grande = pygame.image.load(pathDiretorioPersonagem+"maria_7_encruz.png").convert()
                                    self.tela.blit(perso_grande,(perso_c,perso_l))
                                    maria_pad_sete_encru = pygame.image.load(pathDiretorioPersonagem+"maria_7_encruz_select.png").convert()
                                    coluna = 610
                                    linha = 420
                                    self.tela.blit(maria_pad_sete_encru, (coluna, linha))

                                    if temp >= 60 or pygame.key == K_KP_ENTER:
                                        grande = pygame.image.load(pathDiretorioPersonagem+"exu_mirim.png").convert()
                                        self.tela.blit(grande,(c,l))
                                        pygame.display.update()
                                        sleep(2)
                                        cenario.chamarCenario('maria_7_encruz')
                                        controler.controlerPersonagen(MinhaTela.x, MinhaTela.y, 'maria_7_encruz_lutador.png')

                                break
                    temp = 1
                pygame.display.update()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    o = MinhaTela()
    o.run()