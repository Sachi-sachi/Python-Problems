#Module is a python file u can import to ur other code files to avoid lengthy, messy code.
#u can reuse it in other code files by importing it. and give it a name to use in the code file. like this:
# import module as m
# then u can use m.function() to call the function in the module file.
# u can also add specific functions from the imported file like this:
# from module import function1, function2

#import fibo as f
from fibo import test_func, test2 as t2

#print("Inside main.py", __name__)
#dir(fibo) shows functions and variable in the fibo module
#print(dir(fibo))
#fibo.greet()
t2() #other print statements are also displayed outside the function AS TOP LEVEL CODE IS ALWAYS EXECUTED WHEN THE MODULE IS IMPORTED. SO BE CAREFUL WITH THAT.
