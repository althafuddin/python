import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(
            f'Running {func.__name__} with arguments {args}')
        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add(3,4))
# sub_logger = logger(sub)

# add_logger(3,4)
# sub_logger(10,5)