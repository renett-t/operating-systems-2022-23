#!/usr/bin/python3
import os
import random
import sys

def fork_child():
    kid = os.fork()
    if kid > 0:
        print(f'Parent[{os.getpid()}]: I ran children process with PID {kid}')
    else:
        num = random.randint(5, 10)
        os.execl('./child.py', './child.py', str(num))

    return kid


n = int(sys.argv[1])
count = n

while count > 0:
    child = fork_child()
    if child > 0:
        count = count - 1

count = n

while count > 0:
    child_pid, status = os.wait()
    if status != 0:
        child = fork_child()
    else:
        print(f'Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.')
        count = count - 1

os._exit(os.EX_OK)
