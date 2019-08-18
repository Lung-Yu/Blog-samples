/* leetcode_7_Reverse Integer */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int reverse(int x);

int main(){
    printf("%d\n",reverse(15566));
    printf("%d\n",reverse(-145612));

    return 0;
}

int reverse(int x) {
    long int ans = 0;
    while(x){
        ans *= 10;
        ans += x%10;
        if(ans > INT_MAX || ans < INT_MIN)  return 0;
        x /= 10;
    }
    return (int)ans;
}
