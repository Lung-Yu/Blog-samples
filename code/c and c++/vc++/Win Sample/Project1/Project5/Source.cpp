#include <Windows.h>
#include <iostream>

class A {

};

int N = 10;

void func(int p) {
	int _int = 1;
	float _float = 2.0;
	A _obj_A;
	A* _ptr_obj_A = new A();
	static int _static_int_1 = 23;
	static int _static_int_2 = 24;

	std::cout << "& _obj_A: \t" << &_obj_A << std::endl;
	std::cout << "& _ptr_obj_A: \t" << _ptr_obj_A << std::endl;
	std::cout << "& _int: \t" << &_int << std::endl;
	std::cout << "& _float: \t" << &_float << std::endl;
	std::cout << "& _static_int_1: \t" << &_static_int_1 << std::endl;
	std::cout << "& _static_int_2: \t" << &_static_int_2 << std::endl;
	std::cout << "& p: \t" << &p << std::endl;
}

int main(){
	int _int = 0;
	A* _obj_A;
	A* _obj_A_Inst = new A();


	std::cout << "-------------Main-----------------" << std::endl;
	std::cout << "& main func =\t" << (int*)&main << std::endl; 
	std::cout << "& f func =\t" << (void*)&func << std::endl;
	std::cout << "& _obj_A: \t" << &_obj_A << std::endl;
	std::cout << "& _obj_A_Inst: \t" << _obj_A_Inst << std::endl;
	std::cout << "& _int: \t" << &_int << std::endl;
	std::cout << "&gl_N:\t" << &N << std::endl;
	std::cout << "-------------Func-----------------" << std::endl;
	func(10);

	system("pause");
	return 0;
}