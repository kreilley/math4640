//
//  PolyEval.c
//  
//
//  Created by Kevin Reilley on 1/11/17.
//
//

#include <stdio.h>
#include "PolyEval.h"


int main(){
    int polyeval(int,int);
    int b10toarb(int,int);
    int convertBase(int,int,int);
    int a = -11011;
    int b = 2;
    int pofb = convertBase(a,b,10);
    printf("number %d in base %d is number %d in base 10\n",a,b,pofb);
    int numofb = convertBase(pofb,10,b);
    printf("number %d in base 10 is number %d in base %d\n",pofb,numofb,b);
    
    int number1 = 9;
    int number2 = 10;
    int number3 = number1/number2;
    printf("result of 9/10 integer is %d\n",number3);
    
    int origNum = convertBase(convertBase(a,b,10),10,b);
    printf("convertBase should be reversible such that \n %d should equal %d\n",a,origNum);
    
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






