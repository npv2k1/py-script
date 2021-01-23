import time
 
named_tuple = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
 
print(time_string)
