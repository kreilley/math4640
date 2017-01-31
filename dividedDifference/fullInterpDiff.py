
# Divdif and Interp Algorithms
# Kevin Reilley
# 1/31/2017
# using some of code from previous homework.  

class polynomial():
	def __init__(self,x,fx):
		self.coeffs = self.simpleDividedDifference(x,fx)
		self.x = x
		self.fx = fx
		self.t = list()
		self.ft = list()

	def simpleDividedDifference(self,x,fx):
		d = list()
		n = len(x)
		for fi in fx:
			d.append(fi)
		#print(d)
		print(x)#debug
		print(fx)#debug
		for i in range(0,n-1,1):
			print(i)#debug
			for j in range(n-1,i,-1):
				print(j)#debug
				if abs(x[j] - x[j-(i+1)])>0:
					d[j] = (d[j] - d[j-1])/(x[j] - x[j-(i+1)])
				else:#for debug purposes
					print("x[j-i] currently: "+str(x[j-i])+"\n")
					print("x[j] currently: "+str(x[j])+"\n")
					print("i currently: "+str(i)+"\n")
					print("j currently: "+str(j)+"\n\n")
				print("latest element = "+str(d[j])+"\n")
		return d

	def EvalForT(self,t):
		self.t.append(t)
		n = len(self.x)-1
		print("n = {}",n)
		P = self.coeffs[-1]
		print("highest order coeff = {}",P)
		for i in range(n,0,-1):
			P = self.coeffs[i]+(t-self.x[i])*P
			print(self.coeffs[i])
			print(self.x[i])
			print(P)
			print("\n")
		self.ft.append(P)


if __name__=="__main__":
	xvars = [-2.,-1.,0.,1.,2.,3.]
	fvars = [-5.,1.,1.,1.,7.,25.]
	p = polynomial(xvars,fvars)
	print(p.coeffs)
	xvars1 = [1.,3./2,0.,2.]
	fvars1 = [3.,13./4,3.,5./3]
	p1 = polynomial(xvars1,fvars1)
	print(p1.coeffs)
	xvars2 = [-1.,0.,1.,2.,3.]
	fvars2 = [2.,1.,0.,4.,9.]
	p2 = polynomial(xvars2,fvars2)
	print(p2.coeffs)
	p2.EvalForT(0.)
	print(p2.ft)







