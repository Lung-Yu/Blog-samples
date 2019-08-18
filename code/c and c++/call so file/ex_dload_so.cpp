// ex_dload_so.cpp
#include <iostream>
using namespace std;
#include <dlfcn.h>
int main()
{
    // 为上面生成的.so文件的绝对路径
    const char *MYLIB_PATH = "~/Desktop/c_call_lib/mylib.so";

    // 加载指定的 .so 文件
    void *handle = dlopen(MYLIB_PATH, RTLD_NOW);
    if (handle == NULL)
    {
        cerr << "Open library " << MYLIB_PATH << " error: " << dlerror() << endl;
        return -1;
    }

    // 查找函数foobar，并返回函数指针
    void (*fn_foobar)(int);
    fn_foobar = (void (*)(int))dlsym(handle, "foobar");
    char *error = NULL;
    if ((error = dlerror()) != NULL)
    {
        cerr << "Symbol foobar not found: " << error << endl;
        dlclose(handle);
        return -2;
    }

    // 调用对应的foobar函数打印输出
    fn_foobar(123);

    dlclose(handle);
    return 0;
}