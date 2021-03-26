Project under MIT license.

Feature
- Convert keil c51 to sdcc

## install
```sh
git clone git@github.com:ywaby/keil2sdcc.git
python3 setup.py install
```
need python 3.7+


## usage
import usage
```py
import keil2sdcc
keil2sdcc.c51_2_sdcc(keil_file)
```

direct usage without install
```
python3 -m keil2sdcc ./test/reg51.h ./test/test.c
```


cmdline usage
```sh
usage: keil2sdcc [-h] [-v] [-e ENCODE] [-r] [-j n] [files [files ...]]

convert keil c51 to sdcc

positional arguments:
  files                 keil srcs to convert;supprot glob

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         print version
  -e ENCODE, --encode ENCODE
                        assign keil src encode
  -r, --replace         replace keil src with sdcc src
  -j n, --jobs n        number of parallel jobs; match CPU count if value is 0
```

example
```sh
keil2sdcc keil_c51.c # generate keil_c51.sdcc.c at src path
keil2sdcc keil_c51.c --replace # replace keil src
python3 -m keil2sdcc ./test/reg51.h ./test/test.c # header file is need before c
```

more usage see [tasks.py](./tasks.py) test task

## reference
- [keil c51](https://www.keil.com/support/man_c51.htm)
- [sdcc project](http://sdcc.sourceforge.net/snap.php) 
- [ASxxxx Cross Assemblers](https://shop-pdp.net/ashtml/asxxxx.php)