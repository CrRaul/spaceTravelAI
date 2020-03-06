from chromosome import chromosome
import random

class population():
    def __init__(self, dim):
        self.__dimension = dim
        self.__population = []

    def initPop(self):
        for i in range(0, self.__dimension):
            self.__population.append(chromosome())

    def fitPop(self):
        for i in range(0, self.__dimension):
            self.__population[i].evalCromozom()

    def getBest(self):
        bestCr = chromosome()
        bestCr.setFitness(99999999)
        for i in range(1, self.__dimension):
            if bestCr.getFitness() > self.__population[i].getFitness():
                bestCr = self.__population[i]
        return bestCr

    def getDim(self):
        return self.__dimension

    def setPop(self, pop):
        for i in range(0, self.__dimension):
            self.__population[i] = pop[i]

    def selection(self):
        pos1 = random.randint(0, self.__dimension-1)
        pos2 = random.randint(0, self.__dimension-1)

        if(self.__population[pos1].getFitness() < self.__population[pos2].getFitness()):
            return self.__population[pos1]
        return self.__population[pos2]

    def xo(self,M, F):
        c = chromosome()

        v1 = M.getVelocity()
        v2 = F.getVelocity()

        vxo = [(v1[0]+v2[0])/2,(v1[1]+v2[1])/2]

        c.setVelocity(vxo)
        return c