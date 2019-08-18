#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(){
    char buf[512];
    int i;
    while(scanf("%s",buf)!=EOF){
        for(i=strlen(buf)-1;i>=0;i--){
            printf("%c",buf[i]);
        }
        printf("\n");
    }
} 