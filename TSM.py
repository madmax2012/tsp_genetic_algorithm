#!/usr/bin/env python
import sys
import os
import time
import csv
import random
import logging
import operator
import shutil
import glob
import  math
import individual
from datashape.coretypes import String

import numpy as np

class RunGA():
    def __init__(self, max_iterations, selectionPopsize, mutationChance, crossoverChance):
        self.max_iterations = max_iterations
        self.selectionPopsize=selectionPopsize
        self.crossoverChance=crossoverChance
        self.mutationChance=mutationChance
        self.current_iteration = 0
        self.gen = 0
        # get cities
        citiestxt = 'input/100cities.txt'
        self.city_coordinates = np.loadtxt(citiestxt, skiprows = 1, usecols = (2,3), ndmin = 2)
        self.city_names = np.loadtxt(citiestxt, dtype = String, skiprows = 1, usecols = (0,), ndmin = 1)
        self.cityNamesCoordinates = np.loadtxt(citiestxt, dtype = String, skiprows = 1, usecols = (0,2,3), ndmin = 2)
        self.citiesFull = np.loadtxt(citiestxt, dtype = String, skiprows = 1, ndmin = 2)

        pass

    def step(self):
        pass

    def stop(self):
        pass



    def run(self):
        while True:
            self.step()
            if self.stop():
                break
        return

    def get_current_iteration(self):
        return self.current_iteration

class RealValued(RunGA):
    def __init__(self, popsize, *args, **kwargs):
        # Construct superclass
        RunGA.__init__(self, *args,**kwargs)
        # Gather class variables
        self.popsize = popsize
        #print "ga init start: Creating initial Population"
        #init temparray
        self.population = []#[i for i in range(self.popsize)]# create empty array
        for i in range(0, self.popsize):
            self.numberOfCities = np.r_[0:len(self.city_coordinates)]
            np.random.shuffle(self.numberOfCities)
            self.population.append(individual.individual(position = self.numberOfCities))
            #print self.population[i].position
            #print self.getCityFitness(self.city_coordinates, self.population[i].position)
        #print self.population[i]
        self.stop_reached = False
        pass

    def printPop(self):
        for i in range(0, len(self.population)):
            print "individual "+str(i)+" is at postition \n"+str(self.population[i].position)+"\n and has the fitness "+str(self.getCityFitness(self.city_coordinates, self.population[i].position))+".\n\n"

    def printAvgFitness(self):
        self.totalFitness =0.0
        for i in range(0, len(self.population)):
            self.totalFitness = self.totalFitness + self.getCityFitness(self.city_coordinates, self.population[i].position)
        print "average fitness= "+str(self.totalFitness/len(self.population))

    def printBestIndividual(self):
        self.leader = np.empty
        for i in range(0, len(self.population)):
            if self.leader==np.empty:
                self.leader = i
            elif self.getCityFitness(self.city_coordinates, self.population[i].position) < self.getCityFitness(self.city_coordinates, self.population[self.leader].position):
                self.leader = i
        return (self.getCityFitness(self.city_coordinates, self.population[self.leader].position))

    def returnBestIndividualPOS(self):
        self.leader = np.empty
        for i in range(0, len(self.population)):
            if self.leader==np.empty:
                self.leader = i
            elif self.getCityFitness(self.city_coordinates, self.population[i].position) < self.getCityFitness(self.city_coordinates, self.population[self.leader].position):
                self.leader = i
        return self.leader

    def step(self):
        # Simple stopping condition
        self.current_iteration = self.current_iteration + 1
        if self.current_iteration >= self.max_iterations:
            self.stop_reached = True
################################################### Tournement selection start
        self.tournamentSize = self.selectionPopsize
        self.tempArray = []#[i for i in range(popsize)]# create empty array

        for replacer in range (len(self.population)):
            self.parent1 = np.empty
            self.parent2 = np.empty
            self.numberOfElites = (int((1-self.crossoverChance)*self.popsize))+1
            if  replacer < self.numberOfElites:
                self.tempArray.append(self.population[self.returnBestIndividualPOS()])
                pass
            else:
                for i in range(0,self.tournamentSize):
                    self.randomParentCandidate = self.population[random.randint(0, len(self.population)-1)]
                    if self.parent1==np.empty:
                        self.parent1=self.randomParentCandidate
                        self.parent2=self.parent1
                    elif (self.getCityFitness(self.city_coordinates, self.parent1.position)) > (self.getCityFitness(self.city_coordinates, self.randomParentCandidate.position)):
                        self.parent2=self.parent1
                        self.parent1=self.randomParentCandidate

                arra = []
                for i in range(0, len(self.parent1.position)/2):
                    arra.append(self.parent1.position[i])
                for i in range(len(self.parent2.position)):
                    if self.parent2.position[i] not in arra:
                        arra.append(self.parent2.position[i])
                else:
                    "something went wrong. these parents won't pair."

                if (len(arra)==100):
                        self.tempArray.append(individual.individual(position = arra))
                else:
                    print "array arra to small"


        for i in range(len(self.tempArray)):
             self.population[i]=self.tempArray[i]

        for popMut in range (1, len(self.population)):
            if  popMut < self.numberOfElites:
                pass
            else:
                if (random.uniform(0, 1) <= self.mutationChance):
                    randomPos = random.randint(0, len(self.city_coordinates)-1)
                    randomPos2 = random.randint(0, len(self.city_coordinates)-1)
                    if randomPos != 99:
                        tmp = self.population[popMut].position[randomPos]
                        self.population[popMut].position[randomPos] = self.population[popMut].position[randomPos+1]
                        self.population[popMut].position[randomPos+1] = tmp
                    elif randomPos == 99:
                        tmp = self.population[popMut].position[randomPos]
                        self.population[popMut].position[randomPos] = self.population[popMut].position[0]
                        self.population[popMut].position[0] = tmp
                    else:
                        print "mutation error"



        #self.printAvgFitness()
#        self.printPop()
        if self.current_iteration%10 == 0:
            print"Best individual=; "+str(self.printBestIndividual())+";\tafter only=; "+str(self.current_iteration)+"; Iterations; \t popsize=; "+str(self.popsize)+"; tournamentSize=;"+str(self.selectionPopsize)+";\tmutationChance=; "+str(self.mutationChance)+";\tcrossoverChance=; 0.9"



##numVities 50 posize 30 selectionPressure2 mitationrate 1,15*1/numOfCitiess  mutationPower =0,2 maxGen=500
    def stop(self):
        return self.stop_reached
        pass

    def getCityFitness(self, cities, route):
        cities = cities
        self.totalFitness=0
        for i in range(len(route)-1):
            if (i <= 98):
                self.totalFitness = self.totalFitness+self.getDistance(cities, route[i], route[i+1])
        self.totalFitness = self.totalFitness+self.getDistanceToZero(cities, route[99])
        return self.totalFitness
        pass

    def getDistance(self, city, routei0, routei1):
        #print index
        xDistance = abs(city[routei0, 0])- abs(city[routei1, 0])
        yDistance = abs(city[routei0, 1])- abs(city[routei1, 1])
        return  math.sqrt((xDistance**2)+(yDistance**2))

    def getDistanceToZero(self, city, routei0):
        xDistance = abs(city[routei0, 0])- abs(city[0, 0])
        yDistance = abs(city[routei0, 1])- abs(city[0, 1])
        return  math.sqrt((xDistance**2)+(yDistance**2))
