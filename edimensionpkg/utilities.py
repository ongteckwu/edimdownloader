import functools
import time
import os.path
import sys


def copyfileobjprint(fsrc, fdst, length=16 * 1024):
    """copy data from file-like object fsrc to file-like object fdst"""
    start = time.time()
    time_interval = 0.1
    prev_tick = start

    while 1:
        buf = fsrc.read(length)
        new_tick = time.time()
        if new_tick - prev_tick >= time_interval:
            prev_tick = new_tick
            time_elapsed = time.time() - start
            sys.stdout.write('\r[Time elapsed:{0:.2f}] '.format(time_elapsed))
            sys.stdout.flush()
        if not buf:
            break
        fdst.write(buf)
    print()
    print("Time taken: {0:.2f}".format(time.time() - start))


def timeit(func):
    """
    This function is used to time function executions.

    Usage:

    @timeit
    def func():
        pass

    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Function {0} took {1} secs to run.".format(
            func.__name__, end - start))
        return result
    return wrapper


def getFileDir(file=__file__):
    """get dir of file"""
    return os.path.dirname(os.path.realpath(file))
