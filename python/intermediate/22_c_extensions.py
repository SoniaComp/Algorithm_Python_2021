'''
There are three key methods developers use to call C functions from their python code - ctypes, SWIG and Python/C API. 
'''
'''
You want speed and you know C is about 50x faster than Python.
Certain legacy C libraries work just as well as you want them to, so you don’t want to rewrite them in python.
Certain low level resource access - from memory to file interfaces.
Just because you want to.
'''

# 1. CTypes
'''
//sample C file to add 2 numbers - int and floats

int add_int(int, int);
float add_float(float, float);

int add_int(int num1, int num2){
    return num1 + num2;
}

float add_float(float num1, float num2){
    return num1 + num2;
}
'''


#load the shared object file
adder = CDLL('./adder.so')

#Find sum of integers
res_int = adder.add_int(4,5)
print "Sum of 4 and 5 = " + str(res_int)

#Find sum of floats
a = c_float(5.5)
b = c_float(4.1)

add_float = adder.add_float
add_float.restype = c_float
print "Sum of 5.5 and 4.1 = ", str(add_float(a, b))

# 2. SWIG
'''
Simplified Wrapper and Interface Generator, or SWIG for short is another way to interface C code to Python. 
복잡해서 잘 안쓰는 편
''''


# 3. Python/C API
#Though it looks like an ordinary python import, the addList module is implemented in C
import addList

l = [1,2,3,4,5]
print "Sum of List - " + str(l) + " = " +  str(addList.add(l))