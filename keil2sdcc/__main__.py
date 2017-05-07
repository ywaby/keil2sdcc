import sys
from .c512sdcc import C512SDCC
import argparse


def main():
    parser = argparse.ArgumentParser(prog='keil2sdcc',
                                     description='convert keil program to sdcc',
                                     epilog="project at: https://www.github.ywaby.keil2sdcc")
    parser.add_argument('-v', "--version",
                        help="print version",
                        action='version',
                        version='%(prog)s 0.0.1')
    parser.add_argument('files',
                        help="keil files to convert.",
                        nargs='*')
    args = parser.parse_args()
    for file in args.files:
        C512SDCC(file)


if __name__ == '__main__':
    main()