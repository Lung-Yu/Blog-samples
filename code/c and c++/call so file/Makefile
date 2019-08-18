
all:mylib use_mylib ex_dload_so triangle.so ex_dload_cppso
	@echo done.

mylib : mylib.c
	gcc -fPIC -shared -o mylib.so mylib.c

use_mylib :use_mylib.cpp
	g++ -o use_mylib use_mylib.cpp mylib.so 

ex_dload_so:ex_dload_so.cpp
	g++ -o ex_dload_so ex_dload_so.cpp -ldl

triangle.so:triangle.cpp
	g++ -fPIC -shared -o triangle.so triangle.cpp

ex_dload_cppso:ex_dload_cppso.cpp
	g++ -o ex_dload_cppso ex_dload_cppso.cpp -ldl

.PYTHON:
clean:
	rm mylib.so use_mylib ex_dload_so triangle.so ex_dload_cppso
