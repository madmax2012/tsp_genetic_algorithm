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
    max_iterations = 150000
    numerOfRuns = 10
    stepsize = 0.1
    learning_rate = 0.1
    precision = 0.0001

    #GA parameter
    popsize = 50
    selectionPopsize=2
    mutationChance =0.5
    crossoverChance = 1.0
    # SETUP FITNESS FUNCTION

    tsm = TSM.RealValued(popsize=popsize, max_iterations = max_iterations, selectionPopsize=selectionPopsize, crossoverChance=crossoverChance, mutationChance=mutationChance)
    #ga.printPop()
    tsm.run()
    #ga.printBestIndividual()



if __name__ == "__main__":
    main()
