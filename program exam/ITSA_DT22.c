#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define StrLength 100

int main(){
    char buf[StrLength];
    int i=0,count=0;
    scanf("%s",buf);
    while(strcmp(buf,"end")!=0){
        count=0;
        for(i=0;i<strlen(buf);i++){
            if(buf[i]=='(')
            count++;
            else if(buf[i]==')')
            count--;
        }

        if(count!=0)
            puts("-1");
        else 
            puts("1");

        scanf("%s",buf);
    }
}