from population import population
from chromosome import chromosome
import random

noOfGen = 200
popDim = 50

pop = population(popDim)
pop.initPop()

for i in range(noOfGen):
	popAux = []
	pop.fitPop()

	print("pop: "+str(i)+"  best: "+str(pop.getBest().getFitness())+"  vel:  "+str(pop.getBest().getVelocity()))

	for j in range(popDim):
		c1 = pop.selection()
		c2 = pop.selection()
		c = pop.xo(c1,c2)

		if random.uniform(0,1) < 0.3:
			c.mutation()
		popAux.append(c)

	pop.setPop(popAux)

pop.fitPop()

print(pop.getBest().getVelocity())
print(pop.getBest().getFitness())