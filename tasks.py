import os
from invoke import task

@task
def test(ctx):
    print("\ntest: argparse")
    os.system("python3 -m keil2sdcc -h")

    print("\ntest: cli usage")
    os.system("python3 -m keil2sdcc ./tests/reg51.h ./tests/test.c")
    os.remove("tests/reg51.sdcc.h")
    os.remove("tests/test.sdcc.c")
    os.system("python3 -m keil2sdcc ./tests/*.[hc]")

    print("\ntest: module usage") 
    from keil2sdcc import C51_2_SDCC
    C51_2_SDCC("tests/test.c","tests/test.import_usage.sdcc.c","utf8")
    os.remove("tests/test.import_usage.sdcc.c")
