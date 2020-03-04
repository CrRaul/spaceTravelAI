from NeuralNetwork import NeuralNetwork
import random


class Chromosome():
    def __init__(self):
        # 10 inputs - 1 =  distance from elem to leftLimit
        #             2 =  distance from elem to upLimit
        #             3 =  distance from elem to rightLimit
        #             4 =  distance from elem to downLimit
        #             5 =  distance from elem to first opponent  ( X axis)
        #             6 =  distance from elem to first opponent ( Y axis)
        #             7 =  distance from elem to second opponent ( X axis)
        #             8 =  distance from elem to second opponent ( Y axis)
        #             9 =  distance from elem to third opponent ( X axis)
        #             10 = distance from elem to third opponent ( Y axis)
        #             11 = speed
        #             12 = dimension
        

        # 8 hidden
        # 5 outputs - 1  = move to up
        #             2  = move to right
        #             2  = move to right
        #             3  = move to down
        #             4  = move to left
        #             5  = stay
        # 
        self.__nn = NeuralNetwork(12 , 8, 5)
        self.__time = 0
        # fitness is how long "time" elem survive
        self.__fitness = 0

    def getFitness(self):
        return self.__fitness
    def getTime(self):
        return self.__time
    def setFitness(self, f):
        self.__fitness = f

    def getWeightsIHPos(self, posI, posJ):
        return self.__nn.getWeightsIHPos(posI, posJ)
    def getWeightsHOPos(self, posI, posJ):
        return self.__nn.getWeightsHOPos(posI, posJ)

    def getDimensionWeightsIH(self):
        return self.__nn.getDimensionWeightsIH()
    def getDimensionWeightsHO(self):
        return self.__nn.getDimensionWeightsHO()

    def setWeightsIHPos(self, posI, posJ, val):
        self.__nn.setWeightIHPos(posI, posJ, val)
    def setWeightsHOPos(self, posI, posJ, val):
        self.__nn.setWeightHOPos(posI, posJ, val)

    


    def evalCromozom(self, winWidht, winHeight, winMiddleLimit, speed, dimension):
        pass