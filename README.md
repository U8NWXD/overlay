# `overlay.py`: Makes Multi-Image Composites

## Usage

* Install dependencies: `pip install -r requirements.txt`
* Usage: `python overlay.py img1 img2 [additional images]`

For usage details, see the program's help output:

```console
$ python overlay/overlay.py -h
usage: overlay.py [-h] [--mean] images [images ...]

overlay: Makes multi-image composites

positional arguments:
  images      Space-separated paths to the images to combine

optional arguments:
  -h, --help  show this help message and exit
  --mean      Combine pixel values by the mean instead of the median

Copyright (c) 2018-2019 U8N WXD (github.com/U8NWXD). Project, including
licensing details, can be found at https://github.com/U8NWXD/overlay.
```

## Legal

Copyright (c) 2018-2019 [U8N WXD](https://www.github.com/U8NWXD)
cs.temporary@icloud.com

Use of this source code is governed by the license in `LICENSE.txt`
