from os import system
from time import sleep
import pygame

def main():
    x = 120
    for i in range(x + 1):
        sleep(1)
        print(formatTime(x))
        x -= 1
def formatTime(x):
    minutes = int(x / 60)
    seconds_rem = int(x % 60)
    if (seconds_rem < 10):
        return(str(minutes) + ":0" + str(seconds_rem))
    else:
        return(str(minutes) + ":" + str(seconds_rem))
main()


'''

def main():
    tempo = 1
    
    # Vai diminuindo de 1 em 1 minuto
    for minuto in range(tempo - 1, -1, -1):
        # Vai diminuindo de 1 em 1 segundo 
        for segundo in range(59, -1, -1):
            #system("clear") # Comando para limpar a tela (Linux)
            # Use system("cls") se for executar no Windows
            print "Restam: %02d:%02d" %(minuto, segundo)
            sleep(1)
         
    return 0



tempo = 2 # tempo de escolha do personagem (minutos)
for minuto in range(tempo - 1, -1, -1):# Vai diminuindo de 1 em 1 minuto
    for segundo in range(59, -1, -1):# Vai diminuindo de 1 em 1 segundo
        pygame.display.update()
        fonte = pygame.font.Font("fontes/font.ttf",30)
        #texto = fonte.render(output_string, True,(0,0,0))
       # tela.blit(texto,[405,5])

        sleep(1)

if __name__ == "__main__": main()
'''