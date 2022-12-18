#!/usr/bin/python3
import os
import random
import sys
import time

s = int(sys.argv[1])

print(f'Сhild[{os.getpid()}]: I am started. My PID {os.getpid()}. Parent PID {os.getppid()}.')

time.sleep(s)

print(f'Child[{os.getpid()}]: I am ended. PID {os.getpid()}. Parent PID {os.getppid()}.')

os._exit(random.randint(0, 1))
