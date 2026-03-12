# *-* coding: utf-8 *-*

import sys
import time
from time import sleep
import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN
from ChamarCenario import ChamarCenario
from Controler import *


class MinhaTela:

    def __init__(self):

        pygame.init()

        self.x = 1000

        self.y = 600

        self.tela = pygame.display.set_mode((self.x, self.y))

        self.img_fundo = pygame.image.load('img/fundo2.png').convert()

        #----------- MENU -----------------
        # Personagens do menu (pré-carregados)
        # carrega imagens de menu com tratamento de erro
        try:
            self.exu_mirim = pygame.image.load("personagem/exu_mirim_menu.png").convert_alpha()
            self.lucifer = pygame.image.load("personagem/lucifer_menu.png").convert_alpha()
            self.maria_pad_sete_cat = pygame.image.load("personagem/maria_7_cat_menu.png").convert_alpha()
            self.exu_lucifer = pygame.image.load("personagem/exu_lucifer_menu.png").convert_alpha()
            self.ze_pilintra = pygame.image.load("personagem/ze_pilintra_menu.png").convert_alpha()
            self.exu_caveira = pygame.image.load("personagem/exu_tata_menu.png").convert_alpha()
            self.maria_pad_sete_encru = pygame.image.load("personagem/maria_7_encruz_menu.png").convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar imagem de menu: {e}")
            # Usar uma surface vazia como placeholder para evitar AttributeError
            self.exu_mirim = pygame.Surface((0,0))
            self.lucifer = pygame.Surface((0,0))
            self.maria_pad_sete_cat = pygame.Surface((0,0))
            self.exu_lucifer = pygame.Surface((0,0))
            self.ze_pilintra = pygame.Surface((0,0))
            self.exu_caveira = pygame.Surface((0,0))
            self.maria_pad_sete_encru = pygame.Surface((0,0))
        #----------- MENU -----------------

    def _handle_character_selection(self, character: str, curso: tuple, temp: int, c: int, l: int, perso_c: int, perso_l: int, path_dir: str, cenario, controler) -> bool:
        """Manipula a seleção de personagem com exibição e transição para o cenário.

        Retorna True quando o cenário foi acionado, sinalizando para encerrar.
        """
        char_img = pygame.image.load(f"{path_dir}{character}.png").convert()
        self.tela.blit(char_img, (perso_c, perso_l))

        char_select_img = pygame.image.load(f"{path_dir}{character}_select.png").convert()
        self.tela.blit(char_select_img, curso)

        if temp >= 60:
            large_img = pygame.image.load(f"{path_dir}{character}.png").convert()
            self.tela.blit(large_img, (c, l))
            pygame.display.update()
            sleep(2)
            pygame.display.flip()

            cenario.chamar_cenario(character)
            controler.controler_personagem(self.x, self.y, f'lutador/{character}_lutador.png')
            # sinaliza saída
            return True
        return False

    def run(self):
        pathDiretorioPersonagem = "personagem/"
        meuTempo = pygame.time.Clock()

        # som = pygame.mixer.Sound("sound/som_abertura.wav")
        # som.play()
        cenario = ChamarCenario()
        cenario.set_tela(self.tela)
        controler = Controler()
        perso_c,perso_l = 0,20

        try:
            pygame.display.set_caption('JOGO')
            temp = 0

            while True:
                # desenha fundo e menu a cada frame
                self.tela.blit(self.img_fundo, (0, 0))
                # posições padronizadas para figuras do menu
                menu_positions = [(310, 255), (435, 255), (550, 285),
                                  (250, 425), (370, 425), (490, 425), (610, 425)]
                menu_images = [self.exu_mirim, self.lucifer, self.maria_pad_sete_cat,
                               self.exu_lucifer, self.ze_pilintra, self.exu_caveira,
                               self.maria_pad_sete_encru]
                for img, pos in zip(menu_images, menu_positions):
                    self.tela.blit(img, pos)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                    if temp <= 60:
                        fonte = pygame.font.Font(pygame.font.get_default_font(), 30)
                       #  print("PASSEI AQUI >>", temp)
                        textoTempo = fonte.render(str(temp), True, [0, 0, 0])
                        self.tela.blit(textoTempo, [400, 5])
                        pygame.display.flip()

                    if event.type == MOUSEBUTTONDOWN:
                        c, l = 750, 20
                        curso = pygame.mouse.get_pos()

                        if 310 <= curso[0] <= 410 and 255 <= curso[1] <= 405:
                            ended = self._handle_character_selection('exu_mirim', curso, temp, c, l, perso_c, perso_l, pathDiretorioPersonagem, cenario, controler)
                        elif 435 <= curso[0] <= 535 and 255 <= curso[1] <= 405:
                            ended = self._handle_character_selection('lucifer', curso, temp, c, l, perso_c, perso_l, pathDiretorioPersonagem, cenario, controler)
                        elif 550 <= curso[0] <= 650 and 285 <= curso[1] <= 405:
                            ended = self._handle_character_selection('maria_7_cat', curso, temp, c, l, perso_c, perso_l, pathDiretorioPersonagem, cenario, controler)
                        elif 250 <= curso[0] <= 350 and 425 <= curso[1] <= 575:
                            ended = self._handle_character_selection('exu_lucifer', curso, temp, c, l, perso_c, perso_l, pathDiretorioPersonagem, cenario, controler)
                        elif 370 <= curso[0] <= 470 and 425 <= curso[1] <= 575:
                            ended = self._handle_character_selection('ze_pilintra', curso, temp, c, l, perso_c, perso_l, pathDiretorioPersonagem, cenario, controler)
                        elif 490 <= curso[0] <= 590 and 425 <= curso[1] <= 575:
                            ended = self._handle_character_selection('exu_tata', curso, temp, c, l, perso_c, perso_l, pathDiretorioPersonagem, cenario, controler)
                        elif 610 <= curso[0] <= 710 and 425 <= curso[1] <= 575:
                            ended = self._handle_character_selection('maria_7_encruz', curso, temp, c, l, perso_c, perso_l, pathDiretorioPersonagem, cenario, controler)
                        else:
                            ended = False
                        if ended:
                            return
                    temp += 1
                pygame.display.update()

        except KeyboardInterrupt:
            print("\nJogo interrompido pelo usuário.")
            pygame.quit()
            sys.exit(0)
        except Exception as e:
            print(f"Erro durante execução: {e}")
            import traceback
            traceback.print_exc()
        finally:
            pygame.quit()

if __name__ == '__main__':
    try:
        tela = MinhaTela()
        tela.run()
    except KeyboardInterrupt:
        print("\nJogo finalizado.")
    except Exception as e:
        print(f"Erro fatal: {e}")
        import traceback
        traceback.print_exc()
    finally:
        pygame.quit()
        sys.exit(0)