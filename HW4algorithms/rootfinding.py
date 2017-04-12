#file by kevin reilley
# started 3/10/2017

import numpy
import json
import matplotlib.pyplot as plt

"""
Each root-finding function and the CT rule output the value found in addition to the iteration history as a string.
The iteration history as a string can be read from the dictionary field and written to a text file or terminal for better readability.
The algorithms included in this document are Composite Trapezoidal Rule, Bisection, Newton's Method, and a central finite difference scheme.
Lambdas are used for the problem functions as a form of anonymous function to make passing the function handle easier for a one-line function.  
"""


def bisect(a,b,e,f):
    """ function to find zero through bisection """
    # a - lower bound (float)
    # b - upper bound (float)
    # e - tolerance (float)
    # f - function handle (lambda expr)
    # not included:  max iterations
    # initialization
    m = (a+b)/2.0
    root = m
    iterRes = ''
    while (b-m)>e:
        # no builtin signum?
        sb = numpy.sign(f(b))
        sm = numpy.sign(f(m))
        if (sb*sm)<=0.0:
            a = m
            # this step was wrong in the lecture notes
            # had a = b from the board
        else:
            b = m
        m = (a+b)/2.0
        iterRes = iterRes + 'current m = {:.3f}\n'.format(m)
    root = m
    return root, iterRes

def newton(x0,maxiter,d,e,f,olist):
    # x0 - initial guess
    # maxiter - maximum iterations
    # d - xvalues tolerance
    # e - f(x) tolerance
    # f - f(x) lambda
    # requires:  numerical difference algorithm
    v = f(x0)
    olist[0].append(x0)
    olist[1].append(abs(v))
    x1 = -42.0*x0
    k = 1
    iterString = ''
    if abs(v)<e:
        return x0, iterString
    while k<maxiter:
        x1 = x0 - v/numericalGradient_modified(f,x0)
        v = f(x1)
        olist[0].append(x1)
        olist[1].append(abs(v))
        iterString = iterString + 'x1 = {:.3f} at k = {}\n'.format(x1,k)
        k += 1
        if (abs(v)<e) or  abs(x1-x0)<d:
            return x1, iterString
        else:# this step was implicit in the notes
            x0 = x1
    return x1, iterString
"""
calcErrList is unneeded as the functions are rearranged to equal 0 at the roots.  
"""
"""
def calcErrList(olist):
    # olist - output list data
    # [xn,fn,en]
    compareVal = olist[1][-1] # the last value for fn
    for f in olist[1]:
        olist[2].append(abs(f-compareVal))
    # no return - olist is aliased in usage. 
"""

def numericalGradient_modified(f,x0):
    """ computes a numerical derivative """
    # modified from 2-year old matlab numerical gradient code
    # originally written for AE8803 optimization, with Prof. German
    # computes 1-d numerical derivative with midpoint method (x0 is midpoint).
    h = 10.0**-5
    # h val by recommendation of http://fermi.la.asu.edu/PHY531/intro/node1.html
    x0plus = x0 + h
    x0minus = x0 - h
    return (f(x0plus) - f(x0minus))/(2.0*h)

def explicitNewton(f,fp,x0,maxiter,d,e,olist):
    # f  - function lambda
    # fp - derivative lambda
    # x0 - initial guess
    # maxiter - maximum iterations
    # d - xvalues tolerance
    # e - f(x) tolerance
    # newton without numerical difference scheme
    v = f(x0)
    olist[0].append(x0)
    olist[1].append(abs(v))
    x1 = -42.0*x0
    k = 1
    iterString = ''
    if abs(v)<e:
        return x0, iterString
    while k<maxiter:
        x1 = x0 - v/fp(x0)
        v = f(x1)
        olist[0].append(x1)
        olist[1].append(abs(v))
        iterString = iterString+'x1 = {:.3f} at k = {}\n'.format(x1,k)
        k += 1
        if (abs(v)<e) or  abs(x1-x0)<d:
            return x1, iterString
        else:# this step was implicit in the notes
            x0 = x1
    return x1, iterString

# implementation of composite trapezoidal rule w/ n subdivisions
# see: http://mathfaculty.fullerton.edu/mathews/n2003/trapezoidalrule/TrapezoidalRuleProof.pdf 
def compositeTrapezoidalRule(a,b,n,f):
    # a - lower bound
    # b - upper bound
    # n - number of subintervals
    # f - function lambda
    h = (b - a)/n
    xs = list(fprange(a,b,h))
    fsum = (h/2)*(f(xs[0])+f(xs[-1]))
    for ndx in range(1,n-1):
        fsum = fsum + h*f(xs[ndx])
    # to verify result:  
    y = [f(x) for x in xs]
    npFsum = numpy.trapz(y,xs)#numpy implements the composite trapezoidal rule 
    ImplementationError = abs(fsum - npFsum)
    return fsum, ImplementationError
        
def pltfcn(olist):
    f,axarr = plt.subplots(2,4)
    axarr[0,0].set_title("numeric part A guess 1")
    axarr[0,0].set_ylabel("abs Values")
    axarr[0,0].set_xlabel("k")
    axarr[0,0].plot(range(0,len(olist[0][1])),olist[0][1],"k-x")
    axarr[0,1].set_title("guess 2")
    axarr[0,1].set_ylabel("Values")
    axarr[0,1].set_xlabel("k")
    axarr[0,1].plot(range(0,len(olist[1][1])),olist[1][1],"k-x")
    axarr[0,2].set_title("guess 3")
    axarr[0,2].set_ylabel("Values")
    axarr[0,2].set_xlabel("k")
    axarr[0,2].plot(range(0,len(olist[2][1])),olist[2][1],"k-x")
    axarr[0,3].set_title("numeric Part B")
    axarr[0,3].set_ylabel("Values")
    axarr[0,3].set_xlabel("k")
    axarr[0,3].plot(range(0,len(olist[3][1])),olist[3][1],"k-x")
    axarr[1,0].set_title("exact part A guess 1")
    axarr[1,0].set_ylabel("abs Values")
    axarr[1,0].set_xlabel("k")
    axarr[1,0].plot(range(0,len(olist[4][1])),olist[4][1],"k-x")
    axarr[1,1].set_title("guess 2")
    axarr[1,1].set_ylabel("Values")
    axarr[1,1].set_xlabel("k")
    axarr[1,1].plot(range(0,len(olist[5][1])),olist[5][1],"k-x")
    axarr[1,2].set_title("guess 3")
    axarr[1,2].set_ylabel("Values")
    axarr[1,2].set_xlabel("k")
    axarr[1,2].plot(range(0,len(olist[6][1])),olist[6][1],"k-x")
    axarr[1,3].set_title("exact Part B")
    axarr[1,3].set_ylabel("Values")
    axarr[1,3].set_xlabel("k")
    axarr[1,3].plot(range(0,len(olist[7][1])),olist[7][1],"k-x")
    plt.show()


# need floating point range generator
# see:  http://stackoverflow.com/questions/7267226/range-for-floats
def fprange(a,b,h):
    while a < b:
        yield a
        a += h

def main(ds):
    # ds - Data Structure
    # main function to run HW4 code
    # fcns from hw are encoded as lambdas
    # lambdas:  
    p4afcn = lambda x : numpy.exp(-1.0*(x**2))
    p4bfcn = lambda x : 1.0/(2.0+numpy.cos(x))
    problem5fcn = lambda x : 2.0*x**3 - 3.0*x - 4.0
    p6afcn = lambda x : numpy.exp(x) - 3*x**2
    p6aDerivative = lambda x : numpy.exp(x) - 6.0*x
    p6bfcn = lambda x : 1 - x + 0.3*numpy.cos(x)
    p6bDerivative = lambda x : -1*(1+0.3*numpy.sin(x))
    # problem 4:
    # part a:  
    a = ds['p4']['a']['lower']# lower bound
    b = ds['p4']['a']['up']# upper bound
    ns = [128,256,512]# number of subdivisions
    for n in ns:
        (res,err) = compositeTrapezoidalRule(a,b,n,p4afcn)
        thisKey = 'n{}'.format(n)
        ds['p4']['a'][thisKey] = 'problem 4a, n = {}, result = {:.6f}, impl. error = {:.6f}\n'.format(n,res,err)
    # part b:  
    a = ds['p4']['b']['lower']
    b = ds['p4']['b']['up']
    for n in ns:
        (res,err) = compositeTrapezoidalRule(a,b,n,p4bfcn)
        thisKey = 'n{}'.format(n)
        ds['p4']['b'][thisKey] = 'problem 4b, n = {}, result = {:.6f}, impl. error = {:.6f}\n'.format(n,res,err)
    # problem 5
    a = ds['p5']['a']# lower bound
    b = ds['p5']['b']# upper bound
    e = ds['p5']['e']# error
    (num,iterString) = bisect(a,b,e,problem5fcn)
    ds['p5']['zero'] = num
    ds['p5']['iterations'] = iterString
    # problem 6
    # numerical derivatives
    # part a:
    #outputs
    #[xn,fn,en]
    allOutLists = list()
    maxiter = ds['p6']['maxiter']
    d = ds['p6']['d']
    e = ds['p6']['e']
    guesses = [1,2,3]
    for g in guesses:
        p6outs1 = [list(),list()]
        thisGuess = 'guess{}'.format(g)
        thisRes = 'res{}'.format(g)
        inputVal = ds['p6']['a'][thisGuess]
        (xo,aString) = newton(inputVal,maxiter,d,e,p6afcn,p6outs1)
        ds['p6']['a'][thisRes]['zero'] = xo
        ds['p6']['a'][thisRes]['iter'] = aString
        allOutLists.append(p6outs1)
    # part b:  
    p6bGuess = ds['p6']['b']['guess']
    p6outs2 = [list(),list()]
    (ds['p6']['b']['zero'],ds['p6']['b']['iter']) = newton(p6bGuess,maxiter,d,e,p6bfcn,p6outs2)
    allOutLists.append(p6outs2)
    #print(allOutLists)
    # problem 6 with exact derivatives
    #
    maxiter = ds['p6exact']['maxiter']
    d = ds['p6exact']['d']
    e = ds['p6exact']['e']
    guesses = [1,2,3]
    for g in guesses:
        p6outs3 = [list(),list()]
        thisGuess = 'guess{}'.format(g)
        thisRes = 'res{}'.format(g)
        inputVal = ds['p6exact']['a'][thisGuess]
        # modified explicit netwon method...
        xo,aString = explicitNewton(p6afcn,p6aDerivative,inputVal,maxiter,d,e,p6outs3)
        #explicitNewton(f,fp,x0,maxiter,d,e)
        ds['p6exact']['a'][thisRes]['zero'] = xo
        ds['p6exact']['a'][thisRes]['iter'] = aString
        allOutLists.append(p6outs3)
    # part b:  
    p6bGuess = ds['p6exact']['b']['guess']
    p6outs4 = [list(),list()]
    (ds['p6exact']['b']['zero'],ds['p6']['b']['iter']) = explicitNewton(p6bfcn,p6bDerivative,p6bGuess,maxiter,d,e,p6outs4)
    allOutLists.append(p6outs4)
    #
    # write output
    with open('outfile.json','w') as of:
        json.dump(ds,of)
    # end code
    return allOutLists

if __name__=='__main__':
    # data structure for hw4 results
    hw4data = {
            'p4':{
                'a':{
                    'up':1.0,
                    'lower':0.0,
                    'n128':str(),# tuple to string of result and implementation error by comparison with the numpy trapezoidal implementation
                    'n256':str(),
                    'n512':str()
                    },
                'b':{
                    'up':2.0*numpy.pi,
                    'lower':0.0,
                    'n128':str(),
                    'n256':str(),
                    'n512':str()
                    }
                },
            'p5':{
                'a':0.0,
                'b':5.0,
                'e':0.001,
                'zero':float(),
                'iterations':str()# iterate results
                },
            'p6':{
                'maxiter':100,
                'd':0.000001,
                'e':0.000001,
                'a':{
                    'guess1':-1.0,
                    'res1':{
                        'zero':float(),
                        'iter':str()#record of iterations
                        },
                    'guess2':1.0,
                    'res2':{
                        'zero':float(),
                        'iter':str()
                        },
                    'guess3':4.5,
                    'res3':{
                        'zero':float(),
                        'iter':str()
                        }
                    },
                'b':{
                    'guess':2.0,
                    'zero':float(),
                    'iter':str()
                    }
                },
            'p6exact':{
                'maxiter':100,
                'd':0.000001,
                'e':0.000001,
                'a':{
                    'guess1':-1.0,
                    'res1':{
                        'zero':float(),
                        'iter':str()#record of iterations
                        },
                    'guess2':1.0,
                    'res2':{
                        'zero':float(),
                        'iter':str()
                        },
                    'guess3':4.5,
                    'res3':{
                        'zero':float(),
                        'iter':str()
                        }
                    },
                'b':{
                    'guess':2.0,
                    'zero':float(),
                    'iter':str()
                    }
                }
            }
    outList = main(hw4data)
    print('\nhw 4 complete\n')
    pltfcn(outList)# plot to show convergence rate
    #

