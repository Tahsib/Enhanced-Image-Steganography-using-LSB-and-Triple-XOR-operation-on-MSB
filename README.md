# Enhanced-Image-Steganography-using-LSB-and-Triple-XOR-operation-on-MSB
Improved LSB Image Steaganography to hide text in image.

## Installing
* ```Python 3``` need to be installed, if not visit https://www.python.org/downloads/ to install python for your OS.
* Install ```Pip 3``` to install ```Python3``` packages. 
* Install ```OpenCV-Python``` ```numpy``` ```argparse``` ```matplotlib```

## Running the Project
### 1 bit LSB using XOR
* Embedding
```python 1lsbxor_embed.py -c [cover_image] -m [msg_file]```
* Extraction
```python 1lsbxor_ext.py -s [stego_image]```

### 2 bit LSB using XOR
* Embedding
```python 2lsbxor_embed.py -c [cover_image] -m [msg_file]```
* Extraction
```python 2lsbxor_ext.py -s [stego_image]```

### Traditional 1 bit LSB
* Embedding
```python 1lsb_embed.py -c [cover_image] -m [msg_file]```
* Extraction
```python 1lsb_ext.py -s [stego_image]```

### Traditional 2 bit LSB
* Embedding
```python 2lsb_embed.py -c [cover_image] -m [msg_file]```
* Extraction
```python 2lsb_ext.py -s [stego_image]```

### PSNR value
```python psnr.py -c [cover_image] -s [stego_image]```

### Histogram
```python hist.py [cover/stego image]```

## Built With
* Python 3
* OpenCV
