/*******************************************************/
/* 10019 - Funny Encryption Method                     */
/* Author: Lung-Yu,Tsai                                */
/* Version: 2017/10/30                                 */
/*******************************************************/

#include <stdio.h>
#include <stdlib.h>
int decToBinary(int);
int hexToBinary(int);
int main(){
	int n,m,i,b1,b2;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&m);
		b1=decToBinary(m);
		b2=hexToBinary(m);
		printf("%d %d\n",b1,b2);
		//printf("%d\n",b1);
	}
	return 0;
}

int decToBinary(int m){
	int oneCount=0;
	while(m>0){
		oneCount+=(m%2==0)?0:1;
		m/=2;
	}
	return oneCount;
}

int hexToBinary(int m){
	int oneCount=0;
	int a,b,c,d;
	a=m/1000;
	b=(m%1000)/100;
	c=((m%1000)%100)/10;
	d=m%10;
	oneCount+=decToBinary(a*16);
	oneCount+=decToBinary(b*16);
	oneCount+=decToBinary(c*16);
	oneCount+=decToBinary(d*16);
	return oneCount;
}
 
