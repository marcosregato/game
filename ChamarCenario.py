# *-* coding: utf-8 *-*

import pygame
from pygame.locals import *
import logging

# Configurar logging para melhor debug
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


class ChamarCenario:
    """Gerencia carregamento e exibição de cenários do jogo."""

    PERSONAGENS_VALIDOS = ['exu_mirim', 'lucifer', 'maria_7_cat', 'exu_lucifer', 'ze_pilintra', 'exu_tata', 'maria_7_encruz']
    CAMINHO_CENARIOS = "cenarios/"
    CAMINHO_SONS = "sound/"
    EXTENSAO_CENARIO = "_cena.jpg"
    EXTENSAO_SOM = "_som.wav"

    def __init__(self):
        """Inicializa o gerenciador de cenários."""
        self.tela = None

    def set_tela(self, tela: pygame.Surface) -> None:
        """Define a superfície de exibição para desenhar cenários."""
        self.tela = tela

    def chamar_cenario(self, personagem: str) -> bool:
        """
        Carrega e exibe cenário do personagem.
        
        Args:
            personagem: Nome do personagem (deve estar em PERSONAGENS_VALIDOS)
            
        Returns:
            bool: True se cenário foi carregado com sucesso, False caso contrário
        """
        if not self.tela:
            logging.error("Superfície de exibição não configurada!")
            return False

        if personagem not in self.PERSONAGENS_VALIDOS:
            logging.warning(f"Personagem '{personagem}' não é válido.")
            return False

        try:
            # Carregar e exibir imagem do cenário
            caminho_img = f"{self.CAMINHO_CENARIOS}{personagem}{self.EXTENSAO_CENARIO}"
            img_fundo = pygame.image.load(caminho_img).convert()
            self.tela.blit(img_fundo, [0, 0])

            # Carregar e reproduzir som do cenário
            caminho_som = f"{self.CAMINHO_SONS}{personagem}{self.EXTENSAO_SOM}"
            som = pygame.mixer.Sound(caminho_som)
            som.play()

            pygame.display.flip()
            logging.info(f"Cenário '{personagem}' carregado com sucesso.")
            return True

        except FileNotFoundError as e:
            logging.error(f"Arquivo não encontrado ao carregar cenário '{personagem}': {e}")
            return False
        except pygame.error as e:
            logging.error(f"Erro do Pygame ao carregar cenário '{personagem}': {e}")
            return False
        except Exception as e:
            logging.error(f"Erro inesperado ao carregar cenário '{personagem}': {e}")
            return False
