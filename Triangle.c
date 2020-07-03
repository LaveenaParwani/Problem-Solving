#include <stdio.h>

int main()  
{  
    int s1, s2, s3;     //are three sides of a triangle  
  
    /* 
     * Reads all sides of a triangle 
     */  

    printf("Input three sides of triangle: ");  
    scanf("%d %d %d", &s1, &s2, &s3);  
  
    if(s1==s2 && s1==s3) //check whether all sides are equal  
    {  
        printf("This is an equilateral triangle.\n");  
    }  
    else if(s1==s2 || s1==s3 || s2==s3) //check whether two sides are equal  
    {  
        printf("This is an isosceles triangle.\n");  
    }  
    else if((s1*s1==s2*s2+s3*s3) ||  (s2*s2==s1*s1+s3*s3) || (s3*s3==s2*s2+s1*s1))
    {
     printf("This is an right angle triangle.\n");  
    }  
    else //check whether no sides are equal  
    {  
        printf("This is a scalene triangle.\n");  
    }  
  
    return 0;  
} 
