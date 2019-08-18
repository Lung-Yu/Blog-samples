#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define iSize 26
void init(int*,const int);
int main(){
    int _array[iSize],i;
    char buf[512];
    
    while(scanf("%[^\n]",buf)){
        //printf("%s\n",buf);
        init(_array,iSize);
        for(i=0;i<=strlen(buf);i++){
            if((buf[i]-'a')<iSize && (buf[i]-'a') >=0)
                _array[buf[i]-'a']++;
            else if((buf[i]-'A')<iSize && (buf[i]-'A')>=0 )
                _array[buf[i]-'A']++;
        }

        printf("%d",_array[0]);

        for(i=1;i<iSize;i++)
            printf(" %d",_array[i]);
        printf("\n");
    }
    return 1;
}
void init(int *array,const int end){
    int i=0;
    for(i=0;i<end;i++){
    array[i] = 0;
    }
}
