import numpy as np 

y=[21,2,98,8,3,8,0,9,0]
#choose randomly 2 no.s from y
x1=np.random.choice(y,2)
print(x1)

n,p,k=100,0.2,5
#no. of heads if n coins fliped, probability of success 0.2 in k trial
x2 = np.random.binomial(n,p,k)
print(x2)
