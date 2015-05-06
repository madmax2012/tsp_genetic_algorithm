#!/usr/bin/env python
# Example main

import sys
import os
import time
import csv
import psutil
import logging
import individual
import random
import numpy as np
import TSM


def main():

    # Data file and path definitions

    # Optimization parameters
    max_iterations = 15

    popsize = [30, 60, 100]#50
    selectionPopsize= [2, 3, 4, 5, 6, 7]
    mutationChance =[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    crossoverChance = 1.0
    # SETUP FITNESS FUNCTION


    #ga.printPop()
   #tsm.run()
    #ga.printBestIndividual()
    '''
    for i in range(len(popsize)):
        print i
        for j in range(len(selectionPopsize)):
            for k in range(len(mutationChance)):
                for l in range(2):
                     tsm = TSM.RealValued(popsize=popsize[i], max_iterations = max_iterations, selectionPopsize=selectionPopsize[j], mutationChance=mutationChance[k], crossoverChance=crossoverChance)
                     #ga.printPop()
                     tsm.run()

    ##BatchRun'''

    tsm2 = TSM.RealValued(popsize=popsize[1], max_iterations = max_iterations, selectionPopsize=selectionPopsize[1], mutationChance=mutationChance[1], crossoverChance=crossoverChance)
    tsm2.fitnessCaller()



if __name__ == "__main__":
    main()
