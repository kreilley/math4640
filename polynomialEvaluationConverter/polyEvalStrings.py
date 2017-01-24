import re
import math
import argparse

# belongs to Kevin Reilley

def polynomialSplitter(somestringwithnumbers,sourceBase,targetBase):
	alen = len(somestringwithnumbers)
	components = re.split("\.",somestringwithnumbers)
	hasDec = len(components)#print(components[0] + '\n')
	a1 = str(integerPolynomial(components[0],sourceBase,targetBase))
	#print(a1)
	#print(components[1] + '\n')
	if targetBase==2:
		if hasDec > 1:
			a2 = negativePowerPolynomial('0.'+components[1],sourceBase,targetBase)
			newcomps=re.split("\.",a2)
			outNum = a1+'.'+newcomps[1]
		else:
			outNum = a1
		#print(a2)
		return outNum
	elif targetBase==10:
		if hasDec > 1:
			a2 = b10decimals('0.'+components[1],sourceBase,targetBase)
			#print(a2)
			newcomps = re.split("\.",a2)
			outNum = a1+'.'+newcomps[1]
		else:
			outNum = a1
		return outNum
	else:
		return ' Error! Choose Base 10 or 2 as source or target'
	

def integerPolynomial(intString, sourceBase, targetBase):
	theVal = int(intString)
	return positivePowerPolynomial(theVal, sourceBase, targetBase)

def positivePowerPolynomial(num, sourceBase, targetBase):
	anum = num
	if (anum//targetBase) == 0:
		return anum % targetBase
	return (anum % targetBase) + sourceBase*positivePowerPolynomial(anum//targetBase,sourceBase,targetBase)

def negativePowerPolynomial(decString,sourceBase,targetBase):
	upper,lower = float(decString).as_integer_ratio()
	#print(upper)
	#print(lower)
	newUpper = positivePowerPolynomial(upper,sourceBase,targetBase)
	#print(newUpper)
	newLower = positivePowerPolynomial(lower,sourceBase,targetBase)
	#print(newLower)
	newVal = newUpper/newLower
	newVal = str(newVal)
	outArr = []
	for pos,k in enumerate(newVal):
		if k is not '.':
			if int(k)%2==1:
				outArr.append('1')
			else:
				outArr.append('0')
		else:
			outArr.append('.')
	return ''.join(outArr)

def b10decimals(decString,sourceBase,targetBase):
	#print(decString)
	tot = len(decString)
	ndx = 0
	val = 0.0
	for a in decString:
		if a != '.':
			val = val + float(a)*sourceBase**(-1*ndx)
			#print(val)
			ndx += 1
	return str(val)
		
def main():
	outs = list()
	parser = argparse.ArgumentParser(description='convert base from file')
	parser.add_argument('--source_filename',metavar='F',type=str,nargs=1,help='csv file with format num,sourcebase,targetbase')
	args = parser.parse_args()
	fname = ''.join(vars(args)['source_filename'])
	with open(fname,'r') as f:
		allLines = list(f)
	for l in allLines:
		elements = re.split(",",l)
		numString = elements[0]
		sourceB = int(elements[1])
		targetB = int(elements[2])
		outNum = polynomialSplitter(numString,sourceB,targetB)
		newLine = l.rstrip('\n') + ',' + outNum + '\n'
		outs.append(newLine)
	with open(fname,'w') as f:
		f.write(''.join(outs))

if __name__ =="__main__":
	main()
