convert keil code to sdcc

support
- c51 to sdcc

## install
```sh
git clone git@github.com:ywaby/keil2sdcc.git
python3 setup.py install
```

## usage
import use
```python
import keil2sdcc
keil2sdcc.C512SDCC(keil_file)
```

console use
```sh
keil2sdcc keil_file1 keil_file2
```


## roadmap
- use unittest for test
- a51
- pip
- mdk
- ..