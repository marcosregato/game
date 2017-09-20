__author__ = 'marcos'


import random
import csv

class EventoConfig:

    def escolhoRandom(self):
        lista = ['maria_7_cat_select','exu_lucifer_select','lucifer_select','exu_mirim_select','ze_pilintra_select','exu_tata_select','maria_7_encruz_select']
        for indice, fruta in map(None, range(len(lista)), lista):
            print indice, "=", fruta

if __name__ == '__main__':
    e = EventoConfig()
    e.escolhoRandom()