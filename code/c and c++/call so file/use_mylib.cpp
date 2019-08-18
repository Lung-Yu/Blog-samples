#include <iostream>
#include <string>
using namespace std;

//宣告本段是使用C語言實現,編譯時須採用對應的C語言編譯器處理
#ifdef __cplusplus
    extern "C"{
#endif

#include "mylib.h" // for foobar()

#ifdef __cplusplus
    }
#endif

int main()
{
    foobar(100);
    return 0;
}