from time import localtime, strftime, mktime

start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")

input("Press 'Enter' to stop the script")
stop_time = localtime()


differnce_time = mktime(stop_time) -mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {differnce_time} seconds")