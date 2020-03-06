
import numpy as np
import cv2
import copy
from collections import deque
from object import *

H,W = 600,1300
G = 1

#
oldObj = deque(maxlen=100)

# 
objArrGen = []

# calculate the force of attraction
def attract(obj1, obj2):
    force = obj1.getPosition() - obj2.getPosition()
    dist = np.sqrt(force[0]**2+force[1]**2)
    force = force/dist  # normalize
    strength = (G * obj1.getMass()*obj2.getMass()/(dist**2))
    force *= strength

    return force

# draw border and star/end point rect
def draw(img):
    shape = img.shape 
    H,W = shape[0], shape[1]

    cv2.line(img,(10,10),(10,H-10),(255,255,255),10)
    cv2.line(img,(10,10),(W-10,10),(255,255,255),10)
    cv2.line(img,(W-10,H-10),(10,H-10),(255,255,255),10)
    cv2.line(img,(W-10,H-10),(W-10,10),(255,255,255),10)

    # start and end point, hardcode position
    img = cv2.rectangle(img, (10,190), (30,210), (255,255,255), 2) 
    img = cv2.rectangle(img, (1270,380), (1290,420), (255,255,255), 2) 

    return img

# read the best(from training) start velocity for every generation
def readVelocityInput():
    input_file = open("out.txt", "r")
    N = int(input_file.readline().strip())

    for i in range(N):
        o = input_file.readline().strip().split(" ")

        Obj = object(20,200)
        Obj.setMass(2)
        Obj.setVelocity(np.array([float(o[0]),float(o[1])], dtype='float64'))

        objArrGen.append(Obj)

def checkStop(posS,posP,posO):
    # TEST crush
        # border
    if posO[1] < 20 or posO[1] > 580 or posO[0] < 20 or posO[0] > 1250:
                return True
        # Sun
    if posO[0] >= posS[0] - 7 and posO[0] <= posS[0] + 7 and posO[1] >= posS[1] - 7 and posO[1] <= posS[1] + 7:
                return True
        # Planet
    if posO[0] >= posP[0] - 5 and posO[0] <= posP[0] + 5 and posO[1] >= posP[1] - 5 and posO[1] <= posP[1] + 5:
                return True            
    return False

def main():

    readVelocityInput()

    # for every generation show the best start velocity
    for i in range(len(objArrGen)):
        Obj = objArrGen[i]

        Sun = object(W//2,H//2)
        Planet = object(W//3+120,H//2)

        Sun.setMass(100)

        Planet.setVelocity(np.array([0,-1.2], dtype='float64'))
        Planet.setMass(25)

        # simulate
        while True:
            img = np.zeros((H,W), np.uint8)
            img = draw(img)
            img = cv2.putText(img, 'Gen: '+str(i), (1150,50), cv2.FONT_HERSHEY_SIMPLEX ,  
                   0.7, (255,255,255), 2, cv2.LINE_AA) 

            posS = Sun.getPosition()
            posP = Planet.getPosition()
            posO = Obj.getPosition()

            cv2.circle(img, (int(posS[0]),int(posS[1])), 15, (255,255,255),5)
            cv2.circle(img, (int(posP[0]),int(posP[1])), 10, (255,255,255),1)
            cv2.circle(img, (int(posO[0]),int(posO[1])), 5, (255,255,255),1)


            force = attract(Sun,Planet)
            Planet.applyForce(force)
            Planet.update()

            force = attract(Sun,Obj)
            Obj.applyForce(force)
            Obj.update()
            force = attract(Planet,Obj)
            Obj.applyForce(force)
            Obj.update()


            if checkStop(posS,posP,posO):
                oldObj.appendleft(copy.deepcopy(posO))
                break

            for j in range(1,len(oldObj)):
                cv2.circle(img, (int(oldObj[j][0]),int(oldObj[j][1])), 5, (255,255,255),1)
            #SunForce = attract(Planet,Sun)
            #Sun.applyForce(SunForce)
            #Sun.update()
            
            cv2.imshow('SpaceTravel-CrRaul', img)
            ch = cv2.waitKey(1)
            if ch == 27:
                break


if __name__ == '__main__':
    main()

cv2.destroyAllWindows()
cv2.waitKey(1)