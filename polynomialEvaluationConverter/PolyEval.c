//
//  PolyEval.c
//  
//
//  Created by Kevin Reilley on 1/11/17.
//
//

#include <stdio.h>
#include "PolyEval.h"
#include <math.h>

int main(){
    int polyeval(int,int);
    int b10toarb(int,int);
    int convertBase(int,int,int);
    //double convertBaseFP(double,int,int);
    int a = 11;
    int b = 16;
    int pofb = convertBase(a,b,10);
    printf("number %d in base %d is number %d in base 10\n",a,b,pofb);
    int pofpofb = convertBase(pofb,10,2);
    printf("number %d in base 10 is number %d in base 2\n",pofb,pofpofb);

    int numofb = convertBase(pofb,2,b);
    printf("number %d in base 2 is number %d in base %d\n",pofb,numofb,b);
    
    int number1 = 9;
    int number2 = 10;
    int number3 = number1/number2;
    printf("result of 9/10 integer is %d\n",number3);
    
    int origNum = convertBase(convertBase(a,b,8),8,b);
    printf("convertBase should be reversible such that \n %d should equal %d\n",a,origNum);
    printf("end integer test, start float test\n");
    
    
    
    /*
    double f1 = 0.01;
    int b1 = 2;
    int b2 = 10;
    double fpnum = convertBaseFP(f1,b1,b2);
    printf("number %f in base %d is number %f in base %d\n",f1,b1,fpnum,b2);
    */
    return 0;
}

// convert an integer in anum of base beta to base 10 - iteration by recursion
// fails on negative case
int polyeval(int beta, int anum)
{
    int num = anum;
    if(num < 10)
        return num;
    return (num % 10) + polyeval(beta,(num/10))*beta;
    
}

// change number of base 10 to number in arbitrary base - encoding the long-division scheme
// fail on negative case
int b10toarb(int base, int anum)
{
    int num = anum;
    if(num/base == 0)
        return num % base;
    return (num % base) + 10*b10toarb(base,num/base);
    
}

// overall algorithm from any base to any base on integers, generic of the above
// works for positive and negative case
int convertBase(int sourceNum, int sourceBase, int targetBase)
{
    int num = sourceNum;
    if(num/targetBase ==0)
        // integer division is automatically floor!
        return num % targetBase;
    return (num % targetBase) + convertBase(num/targetBase,sourceBase,targetBase)*sourceBase;
}

/*
// handle floats
// broken
double convertBaseFP(double sourceNum, int sourceBase, int targetBase)
{
    double num = sourceNum;
    if(floor(num/targetBase)==0)
	return num % targetBase;
    return (num % targetBase) + convertBaseFP(num/targetBase,sourceBase,targetBase)*sourceBase;
}
*/
/*
 * What we really need is a means for 
 */

