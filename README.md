# VideoDigitalWatermarking
(While editing)

Basic watermarking libraries for images and videos with python 3.  

python3で画像・動画の電子透かしを行うための基本的なライブラリです．  

(Edited on 2017/08/16)

## このライブラリでできること
* 画像・動画の入出力
画像や動画ファイルの入力と出力（bmp,png,jpg / mp4,avi など） 
* 画像・動画の分割
動画の各フレームを画像として保存や各種処理が可能  
また，画像をブロックに分割して保存や各種処理が可能  
* ビット置換法による電子透かしの埋め込み/抽出
画像の画素値の任意のビットを変更して情報を埋め込む方式  
* 周波数領域利用型の電子透かしによる埋め込み/抽出
DCT変換を利用して画像の周波数領域に情報を埋め込む方式  
* スペクトル拡散系列を使用した直接拡散法による情報の埋め込み/抽出
スペクトル拡散系列と呼ばれるM系列および完全相補系列の相関特性を利用して情報を埋め込む方式．  

## Install
1. Install OpenCV.

※ If you have already installed OpenCV, you can skip this step.

Use homebrew,

```bash:bash
$ brew install opencv3 --with-python3
```

2. Install this library.

```bash:bash
$ git clone https://github.com/piraaa/VideoDigitalWatermarking.git
```

## Usage
Put a python file in the same directory as "VideoDigitalWatermarking".  

And you write only 

```python
from VideoDigitalWatermarking import *
```

for import.  

You can use all following functions.  

## Functions
<details><summary><strong>__init__</strong> - </summary>

</details>

<details><summary><strong>ber</strong> - Calculate BER(Bit Error Rate).</summary>

* <strong>calcBER()</strong>
Calculate Bit Error Rate.
@param  data1 : result data
@param  data2 : answer data
@return ber   : bit error rate [%]
</details>

<details><summary><strong>ccc</strong> - </summary>

</details>

<details><summary><strong>dct</strong> - For Discrete Cosine Transform.</summary>

* <strong>_get_dctMatrix()</strong>

* <strong>dct_dim1()</strong>
1 dimension DCT.
@param  data : 1 dimension data
@return data : 1 dimension data conversion by DCT (numpy.ndarray)
* <strong>dct_dim2()</strong>
2 dimension DCT.
@param  data : 2 dimension data
@return data : 2 dimension data conversion by DCT (numpy.ndarray)
* <strong>idct_dim1()</strong>
1 dimension IDCT.
@param  data : 1 dimension data
@return data : 1 dimension data conversion by IDCT (numpy.ndarray)
* <strong>idct_dim2()</strong>
2 dimension IDCT.
@param  data : 2 dimension data
@return data : 2 dimension data conversion by IDCT (numpy.ndarray)
</details>

<details><summary><strong>esequence</strong> - E-Sequence (even-shift orthogonal sequence)</summary>

* <strong>generateE()</strong>
Generate E-Sequence. The length l.
@param  l:length
@return e:E-Sequence
</details>

<details><summary><strong>image</strong> - For image processing.</summary>

* <strong>colorimage2block()</strong>
Divide color image into blocks.
@param  img    : a 3 dimension image like a np.array[height][width][BGR]
@param  size   : block size list like a [height, width]
@return blocks : a 5 dimension blocks like a np.ndarray[block_height][block_width][height][width][BGR]
* <strong>getRgbLayer()</strong>
Read grayscale image.
@param  img   : a 3 dimension color image like np.ndarray[Height][Width][BGR]
@param  rgb   : a returned layer number. Blue is 0, Green is 1 and Red is 2. You can also give a colorname like RED.  
@return layer : a color layer of image, only red, green or blue.
* <strong>get_y()</strong>
Get only Y from YCC image.
@param  img     : 3 dimension np.ndarray[Height][Width][YCC]
@return y_data  : 2 dimension np.ndarray[Height][Width]. Including only Y.
* <strong>grayimage2block()</strong>
Divide gray image into blocks.
@param  img    : a 2 dimension gray image like a np.array[height][width]
@param  size   : block size list like a [height, width]
@return blocks : a 4 dimension blocks like a np.ndarray[block_height][block_width][height][width]
* <strong>readColorImage()</strong>
Read color image. [notice] Grayscale images are treated as RGB image. (ex. if pixel value is 100, it's treated [100][100][100] RGB image.)
@param  filename : filename
@return img      : 3 dimension np.ndarray[Height][Width][BGR]
* <strong>readGrayImage()</strong>
Read grayscale image.
@param  filename : filename
@return img      : 2 dimension np.ndarray[Height][Width]
* <strong>rgb2ycc()</strong>
RGB to YCbCr.
@param  img      : 3 dimension np.ndarray[Height][Width][RGB]
@return ycc_data : 3 dimension np.ndarray[Height][Width][YCC]
* <strong>showImage()</strong>
Show imsge data.
@param img : image array
* <strong>writeImage()</strong>
Export image data.
@param filename : filename for export image data
@param img      : 2 or 3 dimension image array
* <strong>ycc2rgb()</strong>
YCbCr to BGR.
@param  img      : 3 dimension np.ndarray[Height][Width][YCC]
@return rgb_data : 3 dimension np.ndarray[Height][Width][BGR]
</details>

<details><summary><strong>msequence</strong> - For M-Sequence.</summary>

* <strong>generateM()</strong>
Create M-Sequence.
@param  N : length 2**N-1
@return m : M-Sequence
</details>

<details><summary><strong>psnr</strong> - For calculate PSNR(Peak Signal to Noise Ratio).</summary>

* <strong>_calcMSE()</strong>

* <strong>calcPSNR()</strong>
Calculate PSNR.
@param  cover : cover image
@param  stego : stego image 
@return psnr  : PSNR [dB]
* <strong>getRgbLayer()</strong>
Read grayscale image.
@param  img   : a 3 dimension color image like np.ndarray[Height][Width][BGR]
@param  rgb   : a returned layer number. Blue is 0, Green is 1 and Red is 2. You can also give a colorname like RED.  
@return layer : a color layer of image, only red, green or blue.
</details>

<details><summary><strong>secret</strong> - For Secret informations.</summary>

* <strong>bi2str()</strong>
Convert binary to string.
@param  secret_bi : binary secret information
@return secret_str : string secret information 
* <strong>generateSecret()</strong>
Generate 0 or 1 random secret information for simulation.
@param  n : length
@return secret : secret information list
* <strong>str2bi()</strong>
Convert string to binary.
@param  secret_str : string secret information
@return secret_bi : binary secret information 
</details>

<details><summary><strong>video</strong> - For video processing.</summary>

* <strong>image2video()</strong>

* <strong>showVideo()</strong>

* <strong>video2image()</strong>
Read mpeg video and divide into jpeg images.
@param  filename:video filename
@param  n       :number of export images (if n=0, this function exports all images in video.)  
@return count   :number of exported images
</details>

<details><summary><strong>watermarking</strong> - For image watermarking.</summary>

* <strong>_addBitReplace()</strong>
Embed 1 bit secret information by changing LSB.
@param  cover  :1 pixel cover data
@param  secret :i bit secret information
@param  bit    :number of replaced bit
@return stego  :1 pixel srego data
* <strong>_checkBitReplace()</strong>
Extract 1 bit secret information by chacking LSB.
@param  data   :stego data
@param  bit    :number of replaced bit
@return secret :1 bit secret information
* <strong>_image2vrctor()</strong>
Convert image to vector.
@param  img   :2 dimension image data
@return vector:1 dimension image data
* <strong>_vector2image()</strong>
Convert vector to image.
@param  vector:1 dimension image data
@return image :2 dimension image data
* <strong>embedBitReplace()</strong>
Embed secret informations by changing bit.
@param  cover   :cover data (2 dimension np.ndarray)
@param  secret  :0 or 1 secret information list
@param  bit     :number of replaced bit (It's recommended to be close to the LSB.)
@param  interval:ebmed interval
@return stego   :srego data (2 dimension np.ndarray)
* <strong>extractBitReplace()</strong>
Extract secret informations by chacking LSB.
@param  cover        :cover data (2 dimension np.ndarray)
@param  stego        :stego data (2 dimension np.ndarray)
@param  secret_length:length of secret information
@param  bit          :number of replaced bit 
@param  interval     :embed interval
@return secret       :extracted secret information
* <strong>minus2zero()</strong>
Convert -1 to 0.
@param  minus_data:secret information represented by -1 and 1.
@return zero_data :secret information represented by 0 and 1.
* <strong>zero2minus()</strong>
Convert 0 to -1.
@param  zero_data :secret information represented by 0 and 1.
@return minus_data:secret information represented by -1 and 1.
</details>



#### For more information, please install this library and refer to "VideoDigitalWatermarking/html/index.html" with your browser.

## Samples
Some program samples.  

### Sample image
![test.bmp](https://github.com/piraaa/VideoDigitalWatermarking/blob/samples/samples/test.bmp "Lenna")

### Embeded in time domain.
Change the bit of the red layer in the time domain by the bit replace method. We use the LSB to minimize the effect on the image.  

```python:embed_in_time.py
# 
# embed_in_time.py
# Created by pira on 2017/08/09.
#

#coding: utf-8

from VideoDigitalWatermarking import *

fnin  = 'test.bmp'
fnout = 'test_embeded.bmp'

secret_data = [1,1,1,1,0,0,0,0]

rgb_data = readColorImage(fnin)
red_data = getRgbLayer(rgb_data, rgb=RED)
embeded_red_data = embedBitReplace(red_data, secret_data, bit=1, interval=0)

#replace red_data to embeded_red_data
height = red_data.shape[0]
width  = red_data.shape[1]
for i in np.arange(height):
	for j in np.arange(width):
		rgb_data[i][j][RED] = embeded_red_data[i][j]

writeImage(fnout, rgb_data)
```

### Extract from time domain.
Extract secret information from the LSB of the red layer in the time domain.  

```python:extract_from_time.py
#
# extract_from_time.py
# Created by pira on 2017/08/09.
#

#coding: utf-8

from VideoDigitalWatermarking import *

fn_cover  = 'test.bmp'
fn_stego = 'test_embeded.bmp'

rgb_cover = readColorImage(fn_cover)
rgb_stego = readColorImage(fn_stego)

red_cover   = getRgbLayer(rgb_cover, rgb=RED)
red_stego   = getRgbLayer(rgb_stego, rgb=RED)

secret_data = extractBitReplace(red_cover, red_stego, 8, bit=1, interval=0)
print(secret_data)
```

```
Read "test.bmp".
Read "test_embeded.bmp".
[ 1.  1.  1.  1.  0.  0.  0.  0.]
```

### Embed in frequency domain.
Change the any bit of the Y layer in the frequency domain by the bit replace method. We use the high bit to avoid the "quantization error".  

```python:embed_in_freq.py
# 
# embed_in_freq.py
# Created by pira on 2017/08/01.
#

#coding: utf-8

from VideoDigitalWatermarking import *

fnin  = 'test.bmp'
fnout = 'test_embeded.bmp'

secret_data = [1,1,1,1,0,0,0,0]

rgb_data = readColorImage(fnin)
ycc_data = rgb2ycc(rgb_data)
y_data   = get_y(ycc_data)
dct_data = dct_dim2(y_data)
embeded_dct_y_data = embedBitReplace(dct_data, secret_data, bit=5, interval=100)
embeded_y_data = idct_dim2(embeded_dct_y_data)

#replace y_data to embeded_y_data
height = ycc_data.shape[0]
width  = ycc_data.shape[1]
for i in np.arange(height):
	for j in np.arange(width):
		ycc_data[i][j][0] = embeded_y_data[i][j]

embeded_rgb_data = ycc2rgb(ycc_data)

#print(rgb_data[0][0], embeded_rgb_data[0][0])

writeImage(fnout, embeded_rgb_data)
```

### Extract from frequency domain.
Extract secret information from the any bit of the Y layer in the frequency domain.  

```python:extract_from_freq.py
#
# extract_from_freq.py
# Created by pira on 2017/08/04.
#

#coding: utf-8

from VideoDigitalWatermarking import *

fn_cover  = 'test.bmp'
fn_stego = 'test_embeded.bmp'

rgb_cover = readColorImage(fn_cover)
rgb_stego = readColorImage(fn_stego)

#print(rgb_cover[0][0], rgb_stego[0][0])

ycc_cover = rgb2ycc(rgb_cover)
ycc_stego = rgb2ycc(rgb_stego)
y_cover   = get_y(ycc_cover)
y_stego   = get_y(ycc_stego)
dct_cover = dct_dim2(y_cover)
dct_stego = dct_dim2(y_stego)

#print(dct_cover[0][0], dct_stego[0][0])

secret_data = extractBitReplace(dct_cover, dct_stego, 8, bit=5, interval=100)
print(secret_data)
```

```
Read "test.bmp".
Read "test_embeded.bmp".
[ 1.  1.  1.  1.  0.  0.  0.  0.]
```

### Divide video into images.

```python:divide_video.py
# 
# divide_video.py
# Created by pira on 2017/08/07.
#

#coding: utf-8

from VideoDigitalWatermarking import *
import numpy as np

filename  = 'test.mp4'
video2image(filename, n=5)
```

```
frame num = 5
fps       = 30
hright    = 1080
width     = 1920 

Export 5 jpeg Images.
```

### Divide image into blocks.

```python:divide_image_into_blocks.py
#
# divide_image_into_blocks.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *

filename = 'test.bmp'
image = readColorImage(filename)

blocks = colorimage2block(image, [128,128])
#print(blocks.shape)

for i in np.arange(blocks.shape[0]):
	for j in np.arange(blocks.shape[1]):
		writeImage(str(i*blocks.shape[1]+j+1) + '.bmp', blocks[i][j])
```

![1.bmp](https://github.com/piraaa/VideoDigitalWatermarking/blob/samples/samples/1.bmp "Lenna1") ![2.bmp](https://github.com/piraaa/VideoDigitalWatermarking/blob/samples/samples/2.bmp "Lenna2")  
![3.bmp](https://github.com/piraaa/VideoDigitalWatermarking/blob/samples/samples/3.bmp "Lenna3") ![4.bmp](https://github.com/piraaa/VideoDigitalWatermarking/blob/samples/samples/4.bmp "Lenna4")

### Correlate function
Calculate correlate function.

```python=correlate.py
#
# correlate.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *

#test
x=[1,-1,1]
y=[1,-1,1]

cycle = correlate(x, y, CYCLE)
noncylcle = correlate(x, y, NON_CYCLE)

print('CYCLE     =', cycle)
print('NON CYCLE =', noncylcle)
```

```
CYCLE     = [-1 -1  3 -1 -1]
NON CYCLE = [ 1 -2  3 -2  1]
```

### Calculate Bit Error Rate.

```python=BER.py
#
# BER.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *

data1 = [1,0,1,0,1,0,1,0]
data2 = [1,1,1,1,0,0,0,0]
ber = calcBER(data1, data2)
print('BER =', ber, '[%]')
```

```
BER = 50.0 [%]
```

### Calculate PSNR.

```python=PSNR.py
#
# PSNR.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *
import numpy as np

a = np.array([[[11,10,10],[20,20,20],[30,30,30]],[[10,10,10],[20,20,20],[30,30,30]],[[10,10,10],[20,20,20],[30,30,30]]])
b = np.array([[[10,10,10],[20,20,20],[30,30,30]],[[10,10,10],[20,20,20],[30,30,30]],[[10,10,10],[20,20,20],[30,30,30]]])
c = np.array([[[10,10,10],[20,20,20],[30,30,30]],[[10,10,10],[20,20,20],[30,30,30]],[[10,10,10],[20,20,20],[30,30,30]]])

psnr = calcPSNR(a, b)
print('PSNR =', psnr, '[dB]')

psnr = calcPSNR(b, c)
print('PSNR =', psnr, '[dB]')
```

```
PSNR = 38.37903944592942 [dB]
PSNR = -inf [dB]
```

## License
* MIT License.  
Please see [LICENSE](https://github.com/piraaa/VideoDigitalWatermarking/blob/master/LICENSE).   

## Library
This program is using [OpenCV](http://opencv.org) for input and output.  
Please read [here](http://opencv.org/license.html) about OpenCV license.  

## About Sphinx
Sphinx is a documentation tool for Python.  
HTML documents in this library were created using Sphinx.  
* [Sphinx](http://www.sphinx-doc.org/ja/stable/#) - Sphinx HP
* [#sphinxjp](http://sphinx-users.jp/index.html#) - Sphinx users community