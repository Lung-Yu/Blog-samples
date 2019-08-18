#include <string>
#include <stdio.h>  
#include <unistd.h>  
#include <sys/types.h>  
#include <sys/socket.h>  
#include <netinet/in.h>  
#include <arpa/inet.h>  

class Connector { 
public: 
	Connector(bool);
	Connector(bool, int);
	Connector(bool, int, std::string&);

	void server_start();

	std::string& getName(){
		return _name;
	}
	void setName(std::string &name){
		_name = name;
	}
	int getPort(){
		return _port;
	}
	void setPort(int port){
		_port = port;
	}
	void setConnectLimit(int count){
		_limit = count;
	}
	int getConnectLimit(){
		return _limit;
	}
	void EableServer(bool start){
		_is_server_loop = start;
	}
private:
	bool _is_server_mode;
	int _port;
	std::string _name;
	
	bool _is_server_loop;
	int _limit;	
};


