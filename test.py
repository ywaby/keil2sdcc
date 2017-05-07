import os
from keil2sdcc import C512SDCC
os.system("python -m keil2sdcc -h")
os.system("python -m keil2sdcc ./test/test.c")
os.remove("./test/test.sdcc.c")
C512SDCC("test/test.c")