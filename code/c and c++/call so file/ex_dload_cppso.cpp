#include <iostream>
#include <string>
#include <dlfcn.h>

using namespace std;
#include "polygon.hpp"

int main()
{
    // load triangle library
    void *triangle = dlopen("./triangle.so", RTLD_LAZY);
    if (!triangle)
    {
        cerr << "Can not load library: " << dlerror() << endl;
        return -1;
    }

    // reset errors
    dlerror();

    // load the symbols "create"
    create_t *create_triangle = (create_t *)dlsym(triangle, "create");
    const char *dlsym_err = dlerror();
    if (dlsym_err)
    {
        cerr << "Can not load symbol create: " << dlsym_err << endl;
        return -2;
    }

    // load the symbols "destroy"
    destroy_t *destroy_triangle = (destroy_t *)dlsym(triangle, "destroy");
    dlsym_err = dlerror();
    if (dlsym_err)
    {
        cerr << "Can not load symbol destroy: " << dlsym_err << endl;
        return -2;
    }

    // create an instance of class <Trangle>
    Polygon *poly = create_triangle();

    // set side length of <Triagle>
    poly->set_side_len(8);
    cout << "The area is " << poly->area() << endl;

    // destroy the class
    destroy_triangle(poly);

    // unload the triangle.so library
    dlclose(triangle);

    return 0;
}