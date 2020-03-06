import random
import numpy as np
from object import *

class chromosome():
    def __init__(self):
        self.__velocity = [random.uniform(-6,6),random.uniform(-20,20)]

        self.__time = 0
        # fitness is the distance form obj to dest 
        self.__fitness = 0

    def setVelocity(self,vel):
        self.__velocity = vel
    def getVelocity(self):
        return self.__velocity

    def getFitness(self):
        return self.__fitness
    def getTime(self):
        return self.__time
    def setFitness(self, f):
        self.__fitness = f

    def mutation(self):
        self.__velocity[0] += random.uniform(-0.2,0.2)
        self.__velocity[1] += random.uniform(-0.2,0.2)


    # for simulation
    def attract(self, obj1, obj2):
        G = 1

        force = obj1.getPosition() - obj2.getPosition()
        dist = np.sqrt(force[0]**2+force[1]**2)
        force = force/dist  # normalize
        strength = (G * obj1.getMass()*obj2.getMass()/(dist**2))
        force *= strength

        return force

    def calcDistance(self,p1,p2):
        return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    # simulate the mission
    def evalCromozom(self):
        time = 0

        H,W = 600,1300

        Sun = object(W//2,H//2)
        Planet = object(W//3+120,H//2)

        Obj = object(20,200)
        Obj.setMass(2)
        Obj.setVelocity(np.array(self.__velocity, dtype='float64'))


        Sun.setMass(100)

        Planet.setVelocity(np.array([0,-1.2], dtype='float64'))
        Planet.setMass(25)

        posS = Sun.getPosition()
        while True:
            posP = Planet.getPosition()
            posO = Obj.getPosition()

            # Sun attract the Planet0
            force = self.attract(Sun,Planet)
            Planet.applyForce(force)
            Planet.update()

            # Sun attract the rocket
            force = self.attract(Sun,Obj)
            Obj.applyForce(force)
            Obj.update()

            # Planet attract the rocket
            force = self.attract(Planet,Obj)
            Obj.applyForce(force)
            Obj.update()

            #####
            posP = Planet.getPosition()
            posO = Obj.getPosition()

            # TEST finish mission
            if posO[0] >= 1270 and posO[1] >= 160 and posO[1] <= 230:
                break

            # TEST crush
                # border
            if posO[0] < 10 or posO[0] > 590 or posO[1] < 10 or posO[1] > 1300:
                break
                # Sun
            if posO[0] >= posS[0] - 7 and posO[0] <= posS[0] + 7 and posO[1] >= posS[1] - 7 and posO[1] <= posS[1] + 7:
                break
                # Planet
            if posO[0] >= posP[0] - 5 and posO[0] <= posP[0] + 5 and posO[1] >= posP[1] - 5 and posO[1] <= posP[1] + 5:
                break            

            time += 1

        #print(posO)
        self.__fitness = self.calcDistance(posO,[1280,195])
