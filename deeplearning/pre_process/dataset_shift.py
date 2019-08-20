import random

filename = "source_file_name"

def shift(filename,train_rate,test_rate,hasValid=False):
    source = open(filename + ".txt","r")

    f_train = open(filename + "_train.txt","w")
    f_test = open(filename + "_test.txt","w")

    if hasValid == True:
        f_valid = open(filename + "_valid.txt","w")

    src_ls = source.readlines()
    size = len(src_ls)
    size = len(src_ls)

    print ("train = ",int(train_rate * size) ,
     "valid = ",int((1.0-train_rate-test_rate))*size ,
     "test = ",int(test_rate* size)
    random.shuffle(src_ls)

    for i in range(size):
        data = src_ls[i]
        if i < size * train_rate :
            f_train.write(data)
            pass
        elif i < size * (test_rate + train_rate):
            f_test.write(data)
            pass
        elif hasValid == True:
            f_valid.write(data)
            pass
    

def main():

    shift(filename,train_rate=0.1 ,test_rate = 0.1,hasValid = False)
    pass

if __name__ == '__main__':
    main()