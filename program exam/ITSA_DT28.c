#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#define ArraySize 100

typedef struct priority{
    char *_workName; //工作名稱
    int _priority; //優先權
    int _workLong; //執行長度
}PRIORITY;

typedef enum keyWork{
    EXECUTE=1, //execute -> print High priority WorkName and EndTime
    INSERT=2, //insert a job -> insert into [workName],[priority],[workLong] VALUE(a,b,c)
    QUIT=3 //quit -> print all work , priority and endTime then endWork
}KeyWork;

typedef struct heapTag{
    void **data;
    int last;
    int size;
    int (*compare)(void *arg1,void *arg2);
    int maxSize;
}HEAP;

HEAP* heapCreate(int maxsize,int(*compare)(void *arg1,void *arg2));
void ReheapUp(HEAP *,int); // -20 ~ 19 ( High to Low ) -> minHeap
int heapInsert(HEAP *heap,void* dataptr);
void ReheapDown(HEAP *heap,int root);
int heapRemove(HEAP *heap,void **dataptr); //dataptr is output
void heapPrintAll(HEAP*,int);
int compare(void *arg1,void *arg2);
int isEmpty(HEAP*);
void heapPrintAll(HEAP*,int);

int main(){
    int optation=0,priority,workLong,response,workCounter=0;
    char bufWork[100],*workName;
    HEAP *heap = heapCreate(ArraySize,compare);
    PRIORITY *dataptr;

    while(scanf("%d",&optation)!=EOF){
        switch(optation){
            case EXECUTE:
                //remove work
                response = heapRemove(heap,(void**)&dataptr);
                // if response = true then print workName and finished at endWorkTime
                // else print 'the CPU is no program'
                if(response){
                    workCounter += dataptr->_workLong;
                    printf("%s finished at time %d\n",dataptr->_workName,workCounter);
                }else
                    printf("the CPU is no program\n");
                break;

            case INSERT:
                // insert data into heap
                scanf("%s %d %d",bufWork,&priority,&workLong);
                dataptr =(PRIORITY*) malloc(sizeof(PRIORITY));
                dataptr->_priority = priority;
                dataptr->_workLong = workLong;
                workName =(char*) malloc(sizeof(bufWork));
                strcpy(workName,bufWork);
                dataptr->_workName = workName;
                heapInsert(heap,dataptr);
                break;

            case QUIT:
                //print all data in HeapQueue and release heap work
                heapPrintAll(heap,workCounter);
                workCounter = 0;
                break;

            default:
                puts("none");
                break;
        }
        //fflush(stdin);
    }
    return 0;
}

HEAP* heapCreate(int maxsize,int(*compare)(void *arg1,void *arg2)){
    HEAP *heap;
    heap = malloc(sizeof(HEAP));
    if(heap==NULL) return NULL;
    heap->last = -1;
    heap->size = 0;
    heap->compare = compare;
    heap->maxSize = (int)pow(2,ceil(log10(maxsize)/log10(2)))-1;
    heap->data = (void *)calloc(heap->maxSize,sizeof(void*));
    return heap;
}

void ReheapUp(HEAP*heap,int child){
 int parent;
 void **data;
 void **temp;
 if(child!=0){
    data = heap->data;
    parent = (child-1)/2;
    if(heap->compare(data[child],data[parent]) <= 0){
        temp = data[parent];
        data[parent] = data[child];
        data[child] = temp;
    }
 }
 return;
}

void ReheapDown(HEAP *heap,int root){
    void *temp,*left,*right;
    int child,last;
    last = heap->last;
    if( (root * 2 + 1) <= last){
        left = heap->data[root*2+1];
        if( (root * 2 + 2) <= last)
            right = heap->data[root*2+2];
        else
            right = NULL;

        if(right==NULL || heap->compare(left,right) < 0)
            child = root * 2 + 1;
        else
            child = root * 2 + 2;
        if(heap->compare(heap->data[root],heap->data[child]) >= 0){
            temp = heap->data[root];
            heap->data[root] = heap->data[child];
            heap->data[child] = temp;
            ReheapDown(heap,child);
        }
    }
    return;
}

int heapInsert(HEAP *heap,void* dataptr){
    if(isEmpty(heap)){
        heap->size = 1;
        heap->last = 0;
        heap->data[heap->last] = dataptr;
        return 1;
    }else if(heap->last == heap->maxSize-1) return 0;
    else{
        (heap->last)++;
        (heap->size)++;
        heap->data[heap->last] = dataptr;
        ReheapUp(heap,heap->last);
        return 1;
    }
}

int heapRemove(HEAP *heap,void **dataptr){
    if(isEmpty(heap)) return 0;
    *dataptr = heap->data[0];
    heap->data[0] = heap->data[heap->last];
    (heap->last)--;
    (heap->size)--;
    ReheapDown(heap,0);
    return 1;
}

void heapPrintAll(HEAP *heap,int workCounter){
    int response=1;
    PRIORITY *dataptr;
    while(response){
    response = heapRemove(heap,(void**)&dataptr);
    if (response){
        workCounter += dataptr->_workLong;
        printf("%s finished at time %d\n",dataptr->_workName,workCounter);
    }
    else return;
    }
    return;
}

int isEmpty(HEAP *heap){
    if(heap->size == 0)
    return 1;
    else
    return 0;
}

int compare(void *arg1,void *arg2){
    return ((PRIORITY*)arg1)->_priority - ((PRIORITY*)arg2)->_priority;
}
