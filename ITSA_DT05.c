#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#define iArrayMax 100
int* splitToIntArray(char *string,const char *delim,int *size);
void printAns(int*);
int main()
{
    char *delim = ",";
    char *iBuf = malloc(sizeof(char)*iArrayMax);
    int size,i;
    int *iArray;

    while(scanf("%s",iBuf)!=EOF){
        iArray = splitToIntArray(iBuf,delim,&size); 
        for(i=0;i<size;i++){

        }
        printAns(iArray);
    }
    return 0;
}

int* splitToIntArray(char *string,const char *delim,int *iSize){
    char * pch;
    int iArray[iArrayMax];
    pch = strtok(string,delim);
    while (pch != NULL){
    iArray[(*iSize)++]= atoi(pch);
    pch = strtok (NULL, delim);
    }
    return iArray;
}

void printAns(int*iArray){
    int min,max,i;
    min = 0;
    max = 0;
    printf("%d",*(iArray+min));
    
    for(i = min+1;i<max;i++){
        printf(",%d",*(iArray+i));
    }
}