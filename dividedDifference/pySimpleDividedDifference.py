# Simple divided difference algorithm in python3
# Kevin Reilley
# 1/24/2017
# based on lecture notes...

import math

def simpleDividedDifference(x,fx):
	d = list()
	n = len(x)
	for fi in fx:
		d.append(fi)
	#print(d)
	print(x)
	print(fx)
	for i in range(0,n-1,1):
		print(i)
		for j in range(n-1,i,-1):
			print(j)
			if abs(x[j] - x[j-(i+1)])>0:
				d[j] = (d[j] - d[j-1])/(x[j] - x[j-(i+1)])
			else:
				print("x[j-i] currently: "+str(x[j-i])+"\n")
				print("x[j] currently: "+str(x[j])+"\n")
				print("i currently: "+str(i)+"\n")
				print("j currently: "+str(j)+"\n\n")
			print("latest element = "+str(d[j])+"\n")
	return d

def main():
	xvars = [-2.,-1.,0.,1.,2.,3.]
	fvars = [-5.,1.,1.,1.,7.,25.]
	print(simpleDividedDifference(xvars,fvars))
	xvars1 = [1.,3./2,0.,2.]
	fvars1 = [3.,13./4,3.,5./3]
	print(simpleDividedDifference(xvars1,fvars1))
	xvars2 = [-1.,0.,1.,2.,3.]
	fvars2 = [2.,1.,0.,4.,9.]
	print(simpleDividedDifference(xvars2,fvars2))


if __name__ == "__main__":
	main()




