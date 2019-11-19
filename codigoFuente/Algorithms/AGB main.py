#!/usr/local/bin/python
# -*- coding: utf-8 -*-


from AGB import AGB
from coins import Coins
import time
from datetime import datetime

def imprimirHistoricos(historicos):
    for historico in historicos:
        print('Selección: {}, suma: {}, generacion: {}'.format(historico[0], historico[1], historico[2]))

def main():

    # AG(cantidad_individuos, alelos, tamano_gen, generaciones, p, problema)

    # pesos = [22, 14, 16, 23, 12, 15, 22, 6, 19, 20, 40, 8, 16, 6, 15, 21, 16]
    # valores = [55, 34, 28, 30, 80, 3, 28, 24, 21, 43, 54, 12, 21, 11, 6, 21, 28]
    # mochila = knapsack.Knapsack(pesos, valores, 100)
    # ag = AG.AG(18, 17, 1, 400, 0.01, mochila)
    # ag.run()

    # coinsVector = [5,1,2,10,6,2]
    # coinsVector = [3, 3, 3, 7, 3, 11, 8, 8, 10, 10, 4, 1, 10, 4, 5]
    # coinsVector = [5, 15, 2, 1, 7, 1, 12, 5, 17, 17, 7, 2, 17, 2, 12, 15, 12, 15, 2, 7]
    coinsVector = [ 1, 20, 5, 1, 2, 5, 5, 1, 5, 2, 2, 1, 10, 5, 10, 5, 20,
                    20, 20, 5, 1, 1, 20, 20, 1, 10, 2, 10, 5, 2, 10, 1, 20, 1,
                    20, 10, 5, 5, 20, 2, 10, 1, 2, 5, 10, 20, 10, 2, 5, 5, 20,
                    1, 1, 5, 10, 10, 10, 1, 5, 2, 1, 2, 10, 20, 2, 10, 10, 20,
                    5, 10, 1, 2, 1, 5, 20, 2, 5, 1, 5, 10, 2, 5, 10, 2, 1,
                    1, 1, 10, 20, 10, 20, 2, 2, 10, 20, 10, 1, 1, 5, 2]
    pesos = Coins(coinsVector)
	# pesos = Coins()
    ag = AGB(32,len(pesos._coinsVector),1,10000,0.01,pesos)
   	# ag = AG(32,100,1,4000,0.01,pesos)
    tIni = time.time()
    ag.run()
    tFin = time.time()
    t = tFin - tIni
    imprimirHistoricos(ag._historicos)
    print('Fila de monedas {}'.format(pesos._coinsVector))
    print('Tiempo de ejecución: {}'.format(datetime.fromtimestamp(t).strftime('%M:%S:%f')))



if __name__ == '__main__':
    main()
