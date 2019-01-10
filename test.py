# python3 ./test.py
import os

print("\ntest: module usage") 
from keil2sdcc import C51_2_SDCC
C51_2_SDCC("test/test.c","test/test.sdcc.c","utf8")


print("\ntest: argparse")
os.system("python3 -m keil2sdcc -h")


print("\ntest: cli usage")
os.system("python3 -m keil2sdcc ./test/reg51.h ./test/test.c")
os.remove("test/reg51.sdcc.h")
os.remove("test/test.sdcc.c")
os.system("python3 -m keil2sdcc ./test/*.[hc]")
