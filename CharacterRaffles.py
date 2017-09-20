__author__ = 'marcos'


import random
import csv

class CharacterRaffles:

    def escolhoRandom(self):
        lista = ['maria_7_cat','exu_lucifer','lucifer','exu_mirim','ze_pilintra','exu_tata','maria_7_encruz']
        return random.choice(lista)

if __name__ == '__main__':
    e = CharacterRaffles()
    a = e.escolhoRandom()