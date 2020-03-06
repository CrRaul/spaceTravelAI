from population import population
from chromosome import chromosome
import random

noOfGen = 25
popDim = 25

pop = population(popDim)
pop.initPop()

f = open("out.txt", "w")
bestArr = []

for i in range(noOfGen):
	popAux = []
	pop.fitPop()

	best = pop.getBest()
	bestArr.append(best.getVelocity())

	print(best.getFitness())

	for j in range(popDim):
		c1 = pop.selection()
		c2 = pop.selection()
		c = pop.xo(c1,c2)

		if random.uniform(0,1) < 0.15:
			c.mutation()
		popAux.append(c)

	pop.setPop(popAux)

pop.fitPop()

bestArr.append(pop.getBest().getVelocity())

f.write(str(noOfGen)+"\n")
for i in range(0,noOfGen):
	f.write(str(bestArr[i][0])+" "+str(bestArr[i][1])+"\n")

f.close()