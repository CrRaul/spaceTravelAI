
import numpy as np
import cv2
import copy
from collections import deque
from object import *

H,W = 600,1300
G = 1
pathP = deque(maxlen=200)


def attract(obj1, obj2):
    force = obj1.getPosition() - obj2.getPosition()
    dist = np.sqrt(force[0]**2+force[1]**2)
    force = force/dist  # normalize
    strength = (G * obj1.getMass()*obj2.getMass()/(dist**2))
    force *= strength

    return force

def drawBorder(img):
    shape = img.shape 
    H,W = shape[0], shape[1]

    cv2.line(img,(10,10),(10,H-10),(255,255,255),10)
    cv2.line(img,(10,10),(W-10,10),(255,255,255),10)
    cv2.line(img,(W-10,H-10),(10,H-10),(255,255,255),10)
    cv2.line(img,(W-10,H-10),(W-10,10),(255,255,255),10)


    return img

def main():
    Sun = object(W//2,H//2)
    Planet = object(W//2,H//3-20)

    Obj = object(20,200)
    Obj.setMass(2)
    Obj.setVelocity(np.array([0.4,0], dtype='float64'))


    Sun.setMass(100)

    Planet.setVelocity(np.array([1,0], dtype='float64'))
    Planet.setMass(10)

    while True:
        img = np.zeros((H,W), np.uint8)
        img = drawBorder(img)

        posS = Sun.getPosition()
        posP = Planet.getPosition()
        posO = Obj.getPosition()

        
        for j in range(1,len(pathP)):
            cv2.line(img,(int(pathP[j-1][0]),int(pathP[j-1][1])),(int(pathP[j][0]),int(pathP[j][1])),(100,100,100),1)
            #line = scale(paForce[j],pathP[j-1],pathP[j])

        pathP.appendleft(copy.deepcopy(posP))

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

        #SunForce = attract(Planet,Sun)
        #Sun.applyForce(SunForce)
        #Sun.update()
        
        cv2.imshow('gravity-CrRaul', img)
        ch = cv2.waitKey(1)
        if ch == 27:
            break


if __name__ == '__main__':
    main()

cv2.destroyAllWindows()
cv2.waitKey(1)