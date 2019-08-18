#define MAXENTRY 10
void *dataptrs[MAXENTRY];
typedef struct astackTag{
    int top;
}ASTACK;

ASTACK *astackCreate(void){
    ASTACK *stack = malloc(sizeof(struct astackTag ));
    if(stack!=NULL) stack->top=-1;
    return stack;
}
int astackPush(ASTACK *stack,void *dataptr){
    if(isFull(stack)) return 0;
    else{
        (stack->top)++;
        dataptrs[stack->top] = dataptr;
        return 1;
    }
}

void *astackPop(ASTACK *stack){
    void *dataptr;
    if(isEmpty(stack)){
        return NULL;
    }else{
        dataptr = dataptrs[stack->top];
        (stack->top)--;
        return dataptr;
    }
}
void *astackPeek(ASTACK *stack){
    if(isEmpty(stack)) return NULL;
    else return dataptrs[stack->top];
}
int isEmpty(ASTACK *stack){
    return (stack->top)==-1;
}
int isFull(ASTACK *stack){
    return ((stack->top)==(MAXENTRY-1));
}
