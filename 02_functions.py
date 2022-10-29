# data into functions as arguments

from gzip import FNAME


# def my_func():
#     print('hello machine world')
    
# my_func()




def my_func(FNAME,LNAME,age):
    print('my name is '+ FNAME + ' ' +LNAME + ' my age is',age)

my_func("john","cena","40")