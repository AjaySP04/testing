#! usr/bin/python
import os
import time
import sys
'''
created by: ajays.parmar
dated on: March 05, 2019
'''


def watch():
    ''' function create a clock watch on console.'''
    from datetime import datetime
    while True:
        now = datetime.now()
        print(now.strftime('%m/%d/%Y %H:%M:%S'), flush=True, end="")
        print('\r', flush=True, end="")
        time.sleep(1)


def main():
    '''main function for all functional processing.'''
    watch()  #: calling watch function.


if __name__ == '__main__':
    main()
