convert keil code to sdcc
license under MIT

feature
- c51 to sdcc

## install
```sh
git clone git@github.com:ywaby/keil2sdcc.git
python3 setup.py install
```
use python 3.7

## usage
import use
```py
import keil2sdcc
keil2sdcc.C512SDCC(keil_file)
```

console use
```sh
keil2sdcc keil_c51_1.c keil_c51_2.c
# generate keil_c51_1.sdcc.c keil_c51_2.sdcc.c at file dir
```