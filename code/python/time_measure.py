import time

def measure_function_performance(func,*args, **kwargs):
    start = time.time()

    res = func(*args, **kwargs)

    end = time.time()
    elapsed = end - start
    print ("Time taken: ", elapsed, "seconds.")

    return res

def func_hello(name):
    print ("hello",name)
    return "hello !!!"

res = measure_function_performance(func_hello,name="tygr")
print (res)