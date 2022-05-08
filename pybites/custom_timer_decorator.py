from logger import log

from functools import wraps
from time import time, sleep

def timing(f):
    '''Decorator to time a function execution'''
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        log.info(f'Elapsed time for [{f.__name__}] = [{end - start}]')
        return result
    return wrapper

@timing
def sleepy():
    sleep(2)
    print('done - should say elapsed ~2s!')

sleepy()
