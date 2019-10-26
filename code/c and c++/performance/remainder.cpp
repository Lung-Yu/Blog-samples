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
	int a = 994981658331;
	int m = 8;
	int b = 7;
	int c = 0;
	time_start();
	
	
	for (int i=1;i<=MAG;i++) c = a % m;
	time_end("% , ");
	cout << c << endl;
	
	c = 0;
	time_start();
	for (int i=1;i<=MAG;i++) c = a & b;
	time_end("& , ");
	cout << c << endl;
	
	return 0;
}

void time_start(){
	START = clock();
}
void time_end(char *str){
    END = clock();
    cout << endl << str << "進行運算所花費的時間：" << (END - START) / CLOCKS_PER_SEC << " S" << endl;
}
