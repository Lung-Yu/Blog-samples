/*******************************************************/
/* UVa 100 The 3n+1 problem                            */
/* Author: Lung-Yu,Tsai                                */
/* Version: 2017/10/30                                 */
/*******************************************************/

#include <stdlib.h> 
#include <stdio.h>

int func_cycle_length(int n);

int main(){
	int i,j,max,start,end;
	while(scanf("%d %d",&i,&j) != EOF){
		max = 0;
		if(i < j){
			start = i;
			end = j;
		}else{
			start = j;
			end = i;
		}
		
		while(start <= end){
			int t_count = func_cycle_length(start++);
			if(t_count > max)
				max = t_count;
		}
		printf("%d %d %d\n",i,j,max);
	}
	return 0;
}

int func_cycle_length(int n){
	int count = 1;
	while(n!=1){
		if(n%2!=0)	n = 3 * n + 1;	
		else	n /= 2;

		count++;
	}
	return count;
}


