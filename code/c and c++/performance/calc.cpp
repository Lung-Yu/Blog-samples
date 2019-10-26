#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <time.h>
#include <math.h>

#define MAG  1000000

using namespace std;

void time_start();
void time_end(char*);

double START,END;
    
int main(){
	int a = 554464;
	float b = 0.76546;
	
	time_start();
	int a_2 = 0;
	float a_2_p = 0.0;
	float b_2 = 0.0;
	float b_b_p = 0.0;
	
	for (int i=1;i<=MAG;i++) a_2 += a * a;
	time_end("a*a, ");
	
	time_start();
	for (int i=1;i<=MAG;i++) a_2_p += pow(a,2);
	time_end("pow(a,2), ");
	
	time_start();
	for (int i=1;i<=MAG;i++) b_2 += b * b;
	time_end("b*b, ");
	
	time_start();
	for (int i=1;i<=MAG;i++) b_b_p += pow(b,2);
	time_end("pow(b,2), ");
	return 0;
}

void time_start(){
	START = clock();
}
void time_end(char *str){
    END = clock();
    cout << endl << str << "進行運算所花費的時間：" << (END - START) / CLOCKS_PER_SEC << " S" << endl;
}
