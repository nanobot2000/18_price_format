# Price Formatter

The script formats price from float or integer number in format `3245.000000` to `3 245`.

# Quickstart

The script requires the installed Python interpreter version 3.x.

You have to run the script with the `-p`, `--price` argument with the float or integer number that reflects price value. 

To call the help, run the script with the `-h` or `--help` option.

```bash
$ python3 format_price.py -h
usage: format_price.py [-h] [-p PRICE]

optional arguments:
  -h, --help            show this help message and exit
  -p PRICE, --price PRICE
                        set price
```
Example of script launch on Linux, Python 3.6:

```bash
$ python3 format_price.py -p 4843435.53000
4 843 435.53
```

Run the tests: 
```bash
$ python3 tests.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
