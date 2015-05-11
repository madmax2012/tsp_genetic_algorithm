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
    max_iterations = 2000
    numberOfRuns = 10

    popsize = [30]#50
    selectionPopsize= [3]
    mutationChance =[0.001, 0.0025, 0.04]
    crossoverChance = 0.9
    # SETUP FITNESS FUNCTION



    i=0
    for j in range(len(mutationChance)):
        tsm2 = TSM.RealValued(popsize=30, max_iterations = max_iterations, selectionPopsize=3, mutationChance=mutationChance[j], crossoverChance=0.9, runval=i)
        tsm2.run()

    #ga.printPop()

if __name__ == "__main__":
    main()