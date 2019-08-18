#include <stdlib.h>
#include <stdio.h>
typedef struct dataNode{
 void *data;
 struct dataNode *next;
}Node;
typedef struct LinkList{
 int count;
 struct dataNode *dataptr;
}List;
List*initLinkList();
void insertData(List*,void*);
void* PopData(List*);
void printLinkList(List*); 
int main(){ 
 int in[100],i=0;
 List* list = initLinkList();
 while(scanf("%d",&in[i])!=EOF){
 insertData(list,&in[i]);
 i++;
 }
 printLinkList(list);
 puts("");
 return i;
} 
List*initLinkList(){
 List *list = (List*)malloc(sizeof(List));
 list->count=0;
 list->dataptr = NULL;
 return list;
}
void insertData(List* list,void* dataptr){
 Node *nNode = (Node*)malloc(sizeof(Node)); 
 nNode->data = dataptr; //將資料到新Node的data 
 nNode->next = list->dataptr;
 list->dataptr = nNode;
 list->count++;
// printf("tData = %d\n",(list->dataptr->data));
}
void* PopData(List*list){
// printf("tData = %d\n",(list->dataptr->data));
 void *data;
 data = list->dataptr->data;
 list->dataptr = list->dataptr->next;
 list->count--; 
 return data;
}
void printLinkList(List* list){
 int *data;
 if(list->count!=0){
 data = (int*)PopData(list);
 printf("%d",*data);
 }
 while(list->count!=0){
 data = (int*)PopData(list);
 printf(" %d",*data);
 }
}