#include <string>
#include <string.h>
#include "socket_server.h"

Connector::Connector(bool is_server){
	_is_server_mode = is_server;
	_port = 8889;
	_name = "server";
	_limit = 5;
	_is_server_loop = true;
}

Connector::Connector(bool is_server, int port){
	_is_server_mode = is_server;
	_port = port;
	_name = "server";
	_is_server_loop = true;
	_limit = 5;
}

Connector::Connector(bool is_server, int port, std::string &name){
	_is_server_mode = is_server;
	_port = port;
	_name = name;
	_limit = 5;
	_is_server_loop = true;
}

void Connector::server_start(){
	int clinet_count = 0;
	
	/* socket service start ... */
	int sock0;  
	struct sockaddr_in addr;  
	struct sockaddr_in client;  
	socklen_t len;  
	int sock_client;  

	/* make socket */  
	sock0 = socket(AF_INET, SOCK_STREAM, 0);  

	/* setting socket */  
	addr.sin_family = AF_INET;  
	addr.sin_port = htons(12345);  
	addr.sin_addr.s_addr = INADDR_ANY;  
	bind(sock0, (struct sockaddr*)&addr, sizeof(addr));  
	printf("\t[Info] binding...\n");  

	/* wait connect from client by TCP , limit 5*/  
	listen(sock0, _limit);  
	printf("\t[Info] listening...\n");
	while(_is_server_loop){
		/* 接受來自 TCP 用戶端地連線要求*/  
		printf("\t[Info] wait for connection...\n");  
		len = sizeof(client);  
		sock_client = accept(sock0, (struct sockaddr *)&client, &len);  
		printf("\t[Info] Testing...\n");  
		char *paddr_str = inet_ntoa(client.sin_addr);  
		printf("\t[Info] Receive connection from %s...\n", paddr_str);  

		/* 傳送 5 個字元 */  
		printf("\t[Info] send server name back...\n");
		
		write(sock_client, _name.c_str(), _name.length());  

		/* 結束 TCP 對話 */  
		printf("\t[Info] Close client connection...\n");  
		close(sock_client);
		
		clinet_count++;
		if(clinet_count > 5){
			_is_server_loop = false;
		}
	}
	/* 結束 listen 的 socket */  
	printf("\t[Info] Close self connection...\n");  
	close(sock0); 
}
