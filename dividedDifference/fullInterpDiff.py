
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
		self.ft = list()# note that lists 

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
		self.ft.append(self.polyevaluator(self.coeffs,self.x,t))

	def polyevaluator(self,c,x,t):
		temp1 = c[:]# copy arrays
		temp2 = x[:]
		p = temp1.pop(0)# shorten arrays and get first element
		q = temp2.pop(0)
		if len(temp1)==0:
			print("p = ",p)
			print("t = ",t)
			print("q = ",q)
			return p*(t-q)
		return p + (t-q)*self.polyevaluator(temp1,temp2,t)

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
	for t in xvars2:
		p2.EvalForT(t)
	print(p2.ft)

