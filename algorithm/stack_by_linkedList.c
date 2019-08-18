#include <stdio.h>
#include <stdlib.h>
typedef struct node{
    void *dataptr;
    struct node *next;
}NODE;
typedef struct STACK{
    int count;
    NODE *node;
}STACK;
STACK *stackCreate(){
    STACK *stack;
    stack = malloc(sizeof(STACK));
    stack->count=0;
    stack->node=NULL;
    return stack;
}
int stackPush(STACK *stack,void *dataptr){
    NODE *node;
    node =(NODE *) malloc(sizeof(NODE));
    if(node==NULL){
        puts("overflow");
        exit(1);
    }else{
        node->dataptr = dataptr;
        node->next = stack->node;
        stack->node = node;
        (stack->count)++;
        return 1;
    } 
}
void *stackPop(STACK *stack){
    NODE *node;
    void *dataptr;
    if(stack->count==0){
        return NULL;
    }else{
        node = stack->node;
        stack->node = node->next;
        dataptr = node->dataptr;
        free(node);
        (stack->count)--;
        return dataptr;
    }
}
void *stackPeek(STACK *stack){
    return stack->node->dataptr;
}
int isEmpty(STACK *stack){
    return (stack->node==NULL);
}
int isFull(STACK *stack){
    NODE *node;
    node = malloc(sizeof(NODE));
    if(node==NULL) return 1;
    else{
        free(node);
        return 0;
    }
}
