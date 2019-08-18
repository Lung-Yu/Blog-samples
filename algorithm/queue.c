#define MaxSize 10
void *datas[MaxSize];
typedef struct arrayQueueTag{
	int front; //start
	int rear; //end
}aQueueTag;

aQueueTag *aqueueCreate(void){
	aQueueTag *queue;
	queue = malloc(sizeof(aQueueTag));
	if(queue!=NULL){
		queue->front=-1;
		queue->rear=-1;
	}
	return queue;
}
int aqueuePush(aQueueTag *queue,void *data){
	if(isFull(queue)){
	return 0;
	}else{
	queue->rear = (queue->rear+1)%MaxSize; //push data in new point
	datas[(queue->rear)] = data; //push data 
	return 1;
	}
}
void *aqueuePop(aQueueTag *queue){
	if(isEmpty(queue)){
		return NULL;
	}else{
		queue->front = (queue->front+1)%MaxSize;
		return datas[queue->front];
	}
}
int isFull(aQueueTag *queue){
	if((queue->rear+1)%MaxSize == queue->front){
		puts("overflow");
		exit(1);
		return 1;
	}else{
		return 0;
	}
}
int isEmpty(aQueueTag *queue){
	return ((queue->front)==(queue->rear));
}
