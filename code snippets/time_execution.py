import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def check_time(n):
    a = 0
    for i in range(n):
        a += i
    return a
        
n = raw_input("Enter n:") 
x = n.split()
num = int(x[0])
print time_execution('check_time(num)')

raw_input()
