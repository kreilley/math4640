
# Divdif and Interp Algorithms
# Kevin Reilley
# 1/31/2017
# using some of code from previous homework.  

import matplotlib.pyplot as plt

class polynomial():
	def __init__(self,x,fx):
		self.coeffs = self.simpleDividedDifference(x,fx)
		self.x = x
		self.fx = fx
		self.t = list()
		self.ft = list()# note that lists must be copied explicitly

	def simpleDividedDifference(self,x,fx):
		d = list()
		n = len(x)
		for fi in fx:
			d.append(fi)
		#print(d)
		#print(x)#debug
		#print(fx)#debug
		for i in range(0,n-1,1):
			#print(i)#debug
			for j in range(n-1,i,-1):
				#print(j)#debug
				if abs(x[j] - x[j-(i+1)])>0:
					d[j] = (d[j] - d[j-1])/(x[j] - x[j-(i+1)])
				else:#for debug purposes
					print("x[j-i] currently: "+str(x[j-i])+"\n")
					print("x[j] currently: "+str(x[j])+"\n")
					print("i currently: "+str(i)+"\n")
					print("j currently: "+str(j)+"\n\n")
				#print("latest element = "+str(d[j])+"\n")
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
			#print("p = ",p)
			#print("t = ",t)
			#print("q = ",q)
			return p
		return p + (t-q)*self.polyevaluator(temp1,temp2,t)


class problemFcn(polynomial):
	def __init__(self,np1):
		self.a = -5
		self.b = 5
		self.np1 = np1
		self.xs = self.equalPoints(np1)
		self.sf3 = list()
		self.compareX = self.equalPoints(100)
		self.ActualVals = list()
		for x in self.xs:
			self.sf3.append(self.selfFunction(x))
		super().__init__(self.xs,self.sf3)


	def equalPoints(self,k):#returns k evenly spaced values.  
		parameter = range(0,k,1)
		outs = list()
		m = (self.b-self.a)/(k-1)
		for t in parameter:
			outs.append(m*t+self.a)
		return outs
	
	def selfFunction(self,x):
		# return value for fcn at x
		return 1./(1.+x**2.0)
	
	def errorArray(self):
		ers = list()
		p = len(self.compareX)
		for e in range(0,p,1):
			ers.append(abs(self.ActualVals[e]-self.ft[e]))
		return ers
	def runcomp(self):
		for t in self.compareX:
			self.EvalForT(t)
			self.ActualVals.append(self.selfFunction(t))
		self.errors = list()
		self.errors = self.errorArray()
		
	def pltfcn(self):
		f,axarr = plt.subplots(1,2)
		axarr[0].set_title("Approximation by Interpolation on {} points".format(self.np1))
		axarr[1].set_title("Interpolating Polynomial Error")
		axarr[0].set_ylabel("Function Value")
		axarr[1].set_ylabel("Absolute Error")
		axarr[0].set_xlabel("X Values")
		axarr[1].set_xlabel("X Values")
		axarr[0].plot(self.compareX,self.ActualVals,"r.")
		axarr[0].plot(self.compareX,self.ft,"b.")
		axarr[1].plot(self.compareX,self.errors,"g.")
		plt.show()
		
		
if __name__=="__main__":
	xvars = [-2.,-1.,0.,1.,2.,3.]
	fvars = [-5.,1.,1.,1.,7.,25.]
	p = polynomial(xvars,fvars)
	print(p.coeffs)
	xvars1 = [1.,3./2,0.,2.]
	fvars1 = [3.,13./4,3.,5./3]
	p1 = polynomial(xvars1,fvars1)
	print(p1.coeffs)
	print("\nNow hw2 coeffs:")
	xvars2 = [-1.,0.,1.,2.,3.]
	fvars2 = [2.,1.,0.,4.,9.]
	p2 = polynomial(xvars2,fvars2)
	print(p2.coeffs)
	print("using recursive eval:  ")
	for t in xvars2:
		p2.EvalForT(t)
	print(p2.ft)
	testit = problemFcn(3)
	testit.runcomp()
	testother = problemFcn(5)
	testother.runcomp()
	#testit.pltfcn()
	testother.pltfcn()



