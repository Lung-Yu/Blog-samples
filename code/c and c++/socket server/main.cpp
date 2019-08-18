#include "socket_server.h"
#include <stdio.h>
#include <stdlib.h>

int main(){
	Connector conn(true);
	conn.setPort(12345);
	conn.server_start();


	return 0;
}
