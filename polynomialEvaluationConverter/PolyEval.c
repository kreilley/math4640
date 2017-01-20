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
int polyeval(int,int);
int b10toarb(int,int);
int convertBase(int,int,int);
float convertBaseDEC(float,float,float);
void testPolyEval(int,int);
void testBarb(int,int);
void testConvertBase(int,int,int);
void testConvertBaseDEC(float,float,float);


int main(){
    
    printf("\nbeginning test of base converter algorithms\n\n");
    
    // polyeval cases
    printf("testing polyeval\n");
    printf("anum = number to convert, beta = base of anum, converting to base 10:\n");
    // case 1
    int at1 = 10101;
    int bt1 = 2;
    testPolyEval(bt1,at1);
    //case 2
    int at2 = 1111111;
    int bt2 = 2;
    testPolyEval(bt2,at2);
    //case 3
    int at3 = 180;
    int bt3 = 16;
    testPolyEval(bt3,at3);
    //case 4
    int at4 = 71;
    int bt4 = 8;
    testPolyEval(bt4,at4);
    //case 5
    int at5 = -10101;
    int bt5 = 2;
    testPolyEval(bt5,at5);
    
    //b10toarb cases
    printf("\ntesting b10toarb\n");
    printf("anum = number to convert, beta = target base, converting from base 10:\n");
    //case 1
    int att1 = 21;
    int btt1 = 2;
    testBarb(btt1, att1);
    //case 2
    int att2 = -21;
    int btt2 = 2;
    testBarb(btt2,att2);
    //case 3
    int att3 = 384;
    int btt3 = 16;
    testBarb(btt3,att3);
    //case 4
    int att4 = 57;
    int btt4 = 8;
    testBarb(btt4,att4);
    //case 5
    int att5 = 127;
    int btt5 = 2;
    testBarb(btt5,att5);
    
    //convertBase cases
    printf("\ntesting convertBase\n");
    //case 1
    int attt1 = 10111;
    int bstt1 = 2;
    int bttt1 = 8;
    testConvertBase(attt1,bstt1,bttt1);
    //case 2
    int attt2 = -100;
    int bstt2 = 16;
    int bttt2 = 10;
    testConvertBase(attt2,bstt2,bttt2);
    //case 3
    int attt3 = 12345;
    int bstt3 = 10;
    int bttt3 = 2;
    testConvertBase(attt3,bstt3,bttt3);
    //case 4
    int attt4 = -127;
    int bstt4 = 10;
    int bttt4 = 2;
    testConvertBase(attt4,bstt4,bttt4);
    //case 5
    int attt5 = 1111111;
    int bstt5 = 2;
    int bttt5 = 10;
    testConvertBase(attt5,bstt5,bttt5);
    
    //convertBaseDEC cases
    printf("\ntesting convertBaseDEC\n");
    //case 1
    float num1f = 0.101;
    float base1s = 2.0;
    float basetarget1 = 10.0;
    testConvertBaseDEC(num1f,base1s,basetarget1);
    //case 2
    float num2f = 0.11101010101;
    float base2s = 2.0;
    float basetarget2 = 10.0;
    testConvertBaseDEC(num2f,base2s,basetarget2);
    //case 3
    float num3f = 0.109375;
    float base3s = 10.0;
    float basetarget3 = 2.0;
    testConvertBaseDEC(num3f,base3s,basetarget3);
    
    
    
    
    return 0;
}

// convert an integer in anum of base beta to base 10
//- iteration by recursion
// fixed for negative case
int polyeval(int beta, int anum)
{
    int num = anum;
    if(num/beta ==0)
        return num;
    return (num % 10) + polyeval(beta,(num/10))*beta;
}
// test fcn for polynomial evaluation function
void testPolyEval(int beta, int anum)
{
    int outnum = polyeval(beta,anum);
    printf("res = %d for beta = %d and anum = %d\n",outnum,beta,anum);
    return;
}

// change number of base 10 to number in arbitrary base
//- encoding the long-division scheme
int b10toarb(int base, int anum)
{
    int num = anum;
    if(num/base == 0)
        return num % base;
    return (num % base) + 10*b10toarb(base,num/base);
}

void testBarb(int base, int anum)
{
    int outnum = b10toarb(base,anum);
    printf("res = %d in base %d for anum = %d in base 10\n",outnum,base,anum);
    return;
}

// overall algorithm from any base to any base on integers,
//generic of the above
// works for positive and negative case
int convertBase(int sourceNum, int sourceBase, int targetBase)
{
    int num = sourceNum;
    if(num/targetBase ==0)
        return num % targetBase;
    return (num % targetBase) +
    convertBase(num/targetBase,sourceBase,targetBase)*sourceBase;
}

void testConvertBase(int sourceNum, int sourceBase, int targetBase)
{
    int outnum = convertBase(sourceNum, sourceBase, targetBase);
    printf("res = %d in base %d for anum = %d in base %d\n",outnum,targetBase,sourceNum,sourceBase);
    return;
}

//current testing

float convertBaseDEC(float sourceNum, float sourceBase, float targetBase)
{
    float num = sourceNum;
    float CurrentFraction, CurrentIntegerPart;
    
    if(fabsf(num)<1.0){
        CurrentFraction = modff(num,&CurrentIntegerPart);
    }else{
        CurrentFraction = modff(num,&CurrentIntegerPart);
        float test = floor(num/targetBase);
        int testAsInt = (int) test;
        if(testAsInt==0)
            return CurrentIntegerPart;
    }
    return CurrentIntegerPart + convertBaseDEC(CurrentFraction*targetBase,sourceBase,targetBase)/sourceBase;
}

void testConvertBaseDEC(float sourceNum, float sourceBase, float targetBase)
{
    float outnum = convertBaseDEC(sourceNum,sourceBase,targetBase);
    printf("res = %f in base %f for anum = %f in base %f\n",outnum,targetBase,sourceNum,sourceBase);
    return;
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
 double f1 = 0.01;
 int b1 = 2;
 int b2 = 10;
 double fpnum = convertBaseFP(f1,b1,b2);
 printf("number %f in base %d is number %f in base %d\n",f1,b1,fpnum,b2);
 */
/*
 //double convertBaseFP(double,int,int);
 int a = 1111111;
 int b = 2;
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
 
 int testingfcn = convertBaseDEC(1.0,1.0,1.0);
 
 */

