# *-* coding: utf-8 *-*

import pygame
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


class Controler:
    """Controla movimentação e comportamento do personagem durante o jogo."""

    def __init__(self):
        """Inicializa o controlador de personagem."""
        self.jogador = None
        self.movimento_x = 0
        self.movimento_y = 0
        self.velocidade = 5

    def controler_personagem(self, tela_x: int, tela_y: int, personagem_path: str) -> None:
        """
        Controlador principal do personagem no cenário.
        
        Args:
            tela_x: Largura da tela
            tela_y: Altura da tela
            personagem_path: Caminho para a imagem do personagem
        """
        if not pygame.display.get_surface():
            logging.error("Superfície de exibição não encontrada!")
            return

        try:
            # Carregar imagem do personagem
            self.jogador = pygame.image.load(personagem_path).convert_alpha()
            posicao_x = tela_x * 0.11
            posicao_y = tela_y * 0.65
            
            # Obter superfície de exibição (já criada)
            tela = pygame.display.get_surface()
            clock = pygame.time.Clock()

            game_running = True
            while game_running:
                clock.tick(60)  # 60 FPS

                # Processar eventos
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.movimento_x = -self.velocidade
                        elif event.key == pygame.K_RIGHT:
                            self.movimento_x = self.velocidade
                        elif event.key == pygame.K_UP:
                            self.movimento_y = -self.velocidade
                        elif event.key == pygame.K_DOWN:
                            self.movimento_y = self.velocidade

                    if event.type == pygame.KEYUP:
                        if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                            self.movimento_x = 0
                        if event.key in (pygame.K_UP, pygame.K_DOWN):
                            self.movimento_y = 0

                # Atualizar posição
                posicao_x += self.movimento_x
                posicao_y += self.movimento_y

                # Limitar ao tamanho da tela
                posicao_x = max(0, min(posicao_x, tela_x - self.jogador.get_width()))
                posicao_y = max(0, min(posicao_y, tela_y - self.jogador.get_height()))

                # Desenhar personagem
                tela.blit(self.jogador, (posicao_x, posicao_y))
                pygame.display.update()

            pygame.quit()

        except FileNotFoundError:
            logging.error(f"Arquivo de personagem não encontrado: {personagem_path}")
        except pygame.error as e:
            logging.error(f"Erro do Pygame: {e}")
        except Exception as e:
            logging.error(f"Erro inesperado no controle de personagem: {e}")


if __name__ == '__main__':
    try:
        pygame.init()
        tela = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Teste Controler')
        
        controler = Controler()
        controler.controler_personagem(1000, 600, 'personagem/exu_mirim.png')
    except Exception as e:
        logging.error(f"Erro na inicialização: {e}")
    finally:
        pygame.quit()
