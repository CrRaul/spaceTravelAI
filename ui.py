
import numpy as np
import cv2
import copy
from collections import deque
from object import *

H,W = 600,1300
G = 1
pathP = deque(maxlen=200)
objects = []

def attract(obj1, obj2):
    force = obj1.getPosition() - obj2.getPosition()
    dist = np.sqrt(force[0]**2+force[1]**2)
    force = force/dist  # normalize
    strength = (G * obj1.getMass()*obj2.getMass()/(dist**2))
    force *= strength

    return force

def draw(img):
    shape = img.shape 
    H,W = shape[0], shape[1]

    cv2.line(img,(10,10),(10,H-10),(255,255,255),10)
    cv2.line(img,(10,10),(W-10,10),(255,255,255),10)
    cv2.line(img,(W-10,H-10),(10,H-10),(255,255,255),10)
    cv2.line(img,(W-10,H-10),(W-10,10),(255,255,255),10)

    # start and end point, hardcode position
    img = cv2.rectangle(img, (10,190), (30,210), (255,255,255), 2) 
    img = cv2.rectangle(img, (1270,160), (1290,230), (255,255,255), 2) 

    return img

def checkObjStop():
    pass

def main():
    Sun = object(W//2,H//2)
    Planet = object(W//3+120,H//2)

    objVel = [[0.12572657125076683, -0.25480909897359877],[1.1066777632079646, -0.13076964672620884],[0.847584502164267, -0.009288920868542466],[0.7116854361940386, 0.0821731965161013]]
    for i in range(0,4):
        Obj = object(20,200)
        Obj.setMass(2)
        Obj.setVelocity(np.array(objVel[i], dtype='float64'))

        objects.append(Obj)

    Sun.setMass(100)

    Planet.setVelocity(np.array([0,-1.2], dtype='float64'))
    Planet.setMass(25)

    while True:
        img = np.zeros((H,W), np.uint8)
        img = draw(img)

        posS = Sun.getPosition()
        posP = Planet.getPosition()

        
        for j in range(1,len(pathP)):
            cv2.line(img,(int(pathP[j-1][0]),int(pathP[j-1][1])),(int(pathP[j][0]),int(pathP[j][1])),(100,100,100),1)
            #line = scale(paForce[j],pathP[j-1],pathP[j])

        pathP.appendleft(copy.deepcopy(posP))

        cv2.circle(img, (int(posS[0]),int(posS[1])), 15, (255,255,255),5)
        cv2.circle(img, (int(posP[0]),int(posP[1])), 10, (255,255,255),1)

        for i in range(0,4):
            posO = objects[i].getPosition()
            cv2.circle(img, (int(posO[0]),int(posO[1])), 5, (255,255,255),1)


        force = attract(Sun,Planet)
        Planet.applyForce(force)
        Planet.update()

        for i in range(4):
            force = attract(Sun,objects[i])
            objects[i].applyForce(force)
            Obj.update()
            force = attract(Planet,objects[i])
            objects[i].applyForce(force)
            objects[i].update()

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