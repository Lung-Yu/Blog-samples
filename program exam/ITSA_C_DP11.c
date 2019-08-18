#include <stdlib.h>
#include <stdio.h>
#define FifityRange 30
#define HundredRange 30
void initPath(void);
long int DATA[FifityRange][HundredRange]={0};

int main(){
    int fifity,hundred;
    initPath();
    int i=0,j=0;
    while(scanf("%d,%d",&fifity,&hundred)!=EOF){
    printf("%d\n",DATA[hundred][fifity]);
    }
    return 0;
}
void initPath(void){
    int initNum = 0;
    int col=0,row=0;
    DATA[col][row] = initNum;
    for(row=1;row<FifityRange;row++)
        DATA[0][row] = 1;
    for(col=0;col<HundredRange;col++)
        DATA[col][0] = 0;
    for(col=1;col<HundredRange;col++){
        for(row=1;row<FifityRange;row++){
            if(col>row) DATA[col][row] = 0;
            else DATA[col][row] = DATA[col][row-1] + DATA[col-1][row];
        }
    }
}