# VideoDigitalWatermarking
Basic watermarking libraries for images and videos with python 3.  

python3で画像・動画の電子透かしを行うための基本的なライブラリです．  

(Edited on 2017/08/17)

## Description
You can do following things by using this library.

* Input/Output of images and videos  
You can input and output images or movies such as bmp, png, jpg, mp4, avi and so on.  

* Split images and videos  
You can divide the image into blocks.  
Also, you can divide video into frames as image.  

* Digital watermark by bit replace method  
The bit replace method changes the bit of the image.  
You can embed and extract secret information by bit replace method.  
Humans can not recognize low bit changes.  
It is a simple method, but it is vulnerable to attack.  

* Digital watermark using frequency domain  
You can embed secret information in the frequency domain of the image using DCT transformation.  
It is difficult to recognize changes in the frequency domain than in the time domain.  
* Digital watermark using spread spectrum  
You can embed secret information using correlation properties of spread spectrum sequence.  
It spreads the secret information in a wide band, so it is not affected by noise.  
The spread sequence is the secret key.  
You can use M-Sequence and CCC in this library.  

* Calculate BER or PSNR  
You can calculate BER or PSNR.  
These values evaluate the performance of digital watermark.  

---

このライブラリを使用すると以下のことができます．

* 画像と動画の入出力  
bmp，png，jpg，mp4，aviなどの画像や動画の入力と出力ができます．  

* 画像と動画の分割  
画像をブロックに分割することができます．  
また，動画の各フレームを画像に分けることができます．  

* ビット置換法による電子透かし  
ビット置換法は画像の画素を変更します．  
ビット置換法による秘密情報の埋め込みと抽出ができます  
人間は低いビットの変化を認識できません．  
シンプルな手法ですが，攻撃に対して脆弱です．  

* 周波数領域利用型の電子透かし  
DCT変換を使用して，画像の周波数領域に秘密情報を埋め込みます．  
周波数領域の変化を認識することは，時間領域よりも難しいです．

* スペクトル拡散を利用した電子透かし  
スペクトル拡散系列の相関特性を利用して秘密情報を埋め込みます．  
広帯域に情報を拡散するため，ノイズの影響を受けにくいです．  
拡散系列は秘密鍵になります．  
このライブラリでは，M系列と完全相補系列を使用することができます．  

* BERやPSNRの計算  
BERやPSNRの計算ができます．  
これらの値は電子透かしの性能を評価します．  

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
<details><summary><strong>ber</strong> - Calculate BER(Bit Error Rate).</summary>

* <strong>calcBER(data1, data2)</strong>
Calculate Bit Error Rate.  
@param  data1 : result data  
@param  data2 : answer data  
@return ber   : bit error rate [%]  
</details>

<details><summary><strong>ccc</strong> - For Complete Complementary Code.</summary>

* <strong>generateCCC(N)</strong>
Create CCC.  
@param  N   : CCC size  
@return CCC : CCC(N,N,N**2)  
</details>

<details><summary><strong>dct</strong> - For Discrete Cosine Transform.</summary>

* <strong>dct_dim1(data)</strong>
1 dimension DCT.  
@param  data : 1 dimension data  
@return data : 1 dimension data conversion by DCT  
* <strong>dct_dim2(data)</strong>
2 dimension DCT.  
@param  data : 2 dimension data  
@return data : 2 dimension data conversion by DCT  
* <strong>idct_dim1(data)</strong>
1 dimension IDCT.  
@param  data : 1 dimension data  
@return data : 1 dimension data conversion by IDCT  
* <strong>idct_dim2(data)</strong>
2 dimension IDCT.  
@param  data : 2 dimension data  
@return data : 2 dimension data conversion by IDCT  
</details>

<details><summary><strong>image</strong> - For image processing.</summary>

* <strong>colorimage2block(img, size)</strong>
Divide color image into blocks.  
@param  img    : a 3 dimension image like a np.array[height][width][BGR]  
@param  size   : block size list like a [height, width]  
@return blocks : a 5 dimension blocks like a np.ndarray[block_height][block_width][height][width][BGR]  
* <strong>getRgbLayer(img, rgb=RED)</strong>
Read grayscale image.  
@param  img   : a 3 dimension color image like np.ndarray[Height][Width][BGR]  
@param  rgb   : a returned layer number. Blue is 0, Green is 1 and Red is 2. You can also give a colorname like RED.  
@return layer : a color layer of image, only red, green or blue.  
* <strong>get_y(img)</strong>
Get only Y from YCC image.  
@param  img     : 3 dimension np.ndarray[Height][Width][YCC]  
@return y_data  : 2 dimension np.ndarray[Height][Width]. Including only Y.  
* <strong>grayimage2block(img, size)</strong>
Divide gray image into blocks.  
@param  img    : a 2 dimension gray image like a np.array[height][width]  
@param  size   : block size list like a [height, width]  
@return blocks : a 4 dimension blocks like a np.ndarray[block_height][block_width][height][width]  
* <strong>readColorImage(filename)</strong>
Read color image.  
[notice] Grayscale images are treated as RGB image. (ex. if pixel value is 100, it's treated [100][100][100] RGB image.)  
@param  filename : filename  
@return img      : 3 dimension np.ndarray[Height][Width][BGR]  
* <strong>readGrayImage(filename)</strong>
Read grayscale image.  
@param  filename : filename  
@return img      : 2 dimension np.ndarray[Height][Width]  
* <strong>rgb2ycc(img)</strong>
RGB to YCbCr.  
@param  img      : 3 dimension np.ndarray[Height][Width][RGB]  
@return ycc_data : 3 dimension np.ndarray[Height][Width][YCC]  
* <strong>showImage(img)</strong>
Show imsge data.  
@param img : image data  
* <strong>writeImage(filename, img)</strong>
Export image data.  
@param filename : filename for export image data  
@param img      : 2 or 3 dimension image array  
* <strong>ycc2rgb(img)</strong>
YCbCr to BGR.  
@param  img      : 3 dimension np.ndarray[Height][Width][YCC]  
@return rgb_data : 3 dimension np.ndarray[Height][Width][BGR]  
</details>

<details><summary><strong>msequence</strong> - For M-Sequence.</summary>

* <strong>generateM(N)</strong>
Create M-Sequence.  
@param  N : length 2**N-1  
@return m : M-Sequence  
</details>

<details><summary><strong>psnr</strong> - For calculate PSNR(Peak Signal to Noise Ratio).</summary>

* <strong>calcPSNR(cover, stego)</strong>
Calculate PSNR.  
@param  cover : cover image  
@param  stego : stego image  
@return psnr  : PSNR [dB]  
</details>

<details><summary><strong>secret</strong> - For Secret informations.</summary>

* <strong>generateSecret(n)</strong>
Generate 0 or 1 random secret information for simulation.  
@param  n      : length  
@return secret : secret information list  
</details>

<details><summary><strong>video</strong> - For video processing.</summary>

* <strong>video2image(filename, n=0)</strong>
Read mpeg video and divide into jpeg images.  
@param  filename : video filename  
@param  n        : number of export images (if n=0, this function exports all images in video.)  
@return count    : number of exported images  
</details>

<details><summary><strong>watermarking</strong> - For image watermarking.</summary>

* <strong>correlate(data1, data2, cycle=NON_CYCLE)</strong>
Calculate correlate function.  
@param  data1     : data1  
@param  data2     : data2  
@param  cycle     : CYCLE or NON_CYCLE (Default is NON_CYCLE)  
@return correlate : correlate list  

* <strong>createBasicSeq(ccc, secret_length, tau=1, ch=1)</strong>
Create Basic-Sequence using CCC.  
@param  ccc           : (N,N,N**2)CCC  
@param  secret_length : length of secret information  
@param  tau           : shift interval  
@param  ch            : channel of CCC  
@return basic         : basic sequence  

* <strong>createEmbedSeq(basic, secret, a=1, tau=1)</strong>
Create Embed-Sequence using CCC.  
@param  ccc    : (N,N,N**2)CCC  
@param  secret : secret information  
@param  a      : embed strength  
@param  tau    : shift interval  
@return es     : basic sequence  

* <strong>embedBitReplace(cover, secret, bit=1, interval=0)</strong>
Embed secret informations by changing bit.  
@param  cover   : cover data (2 dimension np.ndarray)  
@param  secret  : 0 or 1 secret information list  
@param  bit     : number of replaced bit (It's recommended to be close to the LSB.)  
@param  interval: ebmed interval  
@return stego   : srego data (2 dimension np.ndarray)  

* <strong>embedMseq(cover, secret, m, a=1, tau=1)</strong>
Embed secret informations by spread spectrum using m-sequence.  
@param  cover  : cover data (2 dimensional np.ndarray)  
@param  secret : 0 or 1 secret information  
@param  m      : M-Sequence  
@param  a      : embed stlength  
@param tau     : embed shift interval  
@return stego  : srego data (2 dimension np.ndarray)  

* <strong>extractBitReplace(cover, stego, secret_length, bit=1, interval=0)</strong>
Extract secret informations by chacking LSB.  
@param  cover         : cover data  
@param  stego         : stego data  
@param  secret_length : length of secret information  
@param  bit           : number of replaced bit  
@param  interval      : embed interval  
@return secret        : extracted secret information  

* <strong>extractCCC(ccc, es, secret_length, tau=1, ch=1)</strong>
Extract secret informations by spread spectrum using CCC.  
@param  ccc           : (N,N,N**2)CCC  
@param  es            : embed sequence (excracted from stego data)  
@param  secret_length : length of secret information  
@param  tau           : shift interval  
@param  ch            : channel of CCC  
@return secret_data   : extracted secret information  

* <strong>extractMseq(cover, stego, secret_length, m, tau=1)</strong>
Extract secret informations by spread spectrum using m-sequence.  
@param  cover         : cover data  
@param  stego         : stego data  
@param  secret_length : length of secret information  
@param  m             : M-Sequence  
@param  tau           : embed shift interval  
@return secret        : extracted secret information  

* <strong>minus2zero(minus_data)</strong>
Convert -1 to 0.  
@param  minus_data : secret information represented by -1 and 1  
@return zero_data  : secret information represented by 0 and 1  

* <strong>zero2minus(zero_data)</strong>
Convert 0 to -1.  
@param  zero_data  : secret information represented by 0 and 1  
@return minus_data : secret information represented by -1 and 1  
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

### Embed by M-Sequence.
Embed secret information by spectrum spread using M-Sequence.  
(But mow, you can only use τ=1. I am fixing this.)  

#### Time domain

```python=embed_m_time.py
#
# embed_m_time.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *
import numpy as np

fnin  = 'test.bmp'
fnout = 'test_embeded.bmp'

secret_data = [1,1,1,1,0,0,0]

secret_length = len(secret_data)
N = math.ceil(math.log2(secret_length+1))
m = generateM(N)

print('m =', m, '\n')

rgb_data = readColorImage(fnin)
red_data = getRgbLayer(rgb_data, rgb=RED)
embeded_red_data = embedMseq(red_data, secret_data, m, a=1, tau=1)

#replace red_data to embeded red_data
height = red_data.shape[0]
width  = red_data.shape[1]
for i in np.arange(height):
	for j in np.arange(width):
		rgb_data[i][j][RED] = embeded_red_data[i][j]

writeImage(fnout, rgb_data)
```

#### Frequency domain

```python=embed_m_freq.py
#
# embed_m_freq.py
# Created by pira on 2017/08/16.
#

#coding: utf-8

from VideoDigitalWatermarking import *
import numpy as np

fnin  = 'test.bmp'
fnout = 'test_embeded.bmp'

secret_data = [1,1,1,1,0,0,0]

secret_length = len(secret_data)

N = math.ceil(math.log2(secret_length+1))
m = generateM(N)

print('m =', m, '\n')

rgb_data = readColorImage(fnin)
ycc_data = rgb2ycc(rgb_data)
y_data   = get_y(ycc_data)
dct_data = dct_dim2(y_data)
embeded_dct_y_data = embedMseq(dct_data, secret_data, m, a=100, tau=1)
embeded_y_data = idct_dim2(embeded_dct_y_data)

#replace y_data to embeded_y_data
height = ycc_data.shape[0]
width  = ycc_data.shape[1]
for i in np.arange(height):
	for j in np.arange(width):
		ycc_data[i][j][0] = embeded_y_data[i][j]

embeded_rgb_data = ycc2rgb(ycc_data)

writeImage(fnout, embeded_rgb_data)
```

```
m = [1, 1, -1, 1, -1, -1, 1] 

Read "test.bmp".
Write "test_embeded.bmp".
```

### Ectract by M-Sequence.
Extract secret information by spectrum spread using M-Sequence.

#### Time domain

```python=extract_m_time.py
#
# extract_m_time.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *

fn_cover  = 'test.bmp'
fn_stego = 'test_embeded.bmp'

secret_length = 7 #secret infomation length
N = math.ceil(math.log2(secret_length+1))
m = generateM(N)

print('m =', m, '\n')

rgb_cover = readColorImage(fn_cover)
rgb_stego = readColorImage(fn_stego)

red_cover   = getRgbLayer(rgb_cover, rgb=RED)
red_stego   = getRgbLayer(rgb_stego, rgb=RED)

secret_data = extractMseq(red_cover, red_stego, secret_length, m, tau=1)
print(secret_data)
```

#### Frequency domain

```python=embed_m_freq.py
#
# embed_m_freq.py
# Created by pira on 2017/08/16.
#

#coding: utf-8

from VideoDigitalWatermarking import *
import numpy as np

fnin  = 'test.bmp'
fnout = 'test_embeded.bmp'

secret_data = [1,1,1,1,0,0,0]

secret_length = len(secret_data)

N = math.ceil(math.log2(secret_length+1))
m = generateM(N)

print('m =', m, '\n')

rgb_data = readColorImage(fnin)
ycc_data = rgb2ycc(rgb_data)
y_data   = get_y(ycc_data)
dct_data = dct_dim2(y_data)
embeded_dct_y_data = embedMseq(dct_data, secret_data, m, a=100, tau=1)
embeded_y_data = idct_dim2(embeded_dct_y_data)

#replace y_data to embeded_y_data
height = ycc_data.shape[0]
width  = ycc_data.shape[1]
for i in np.arange(height):
	for j in np.arange(width):
		ycc_data[i][j][0] = embeded_y_data[i][j]

embeded_rgb_data = ycc2rgb(ycc_data)

writeImage(fnout, embeded_rgb_data)
```

```
m = [1, 1, -1, 1, -1, -1, 1] 

Read "test.bmp".
Read "test_embeded.bmp".
[1, 1, 1, 1, 0, 0, 0]
```

### Embed and Extract by CCC.
Embed and Extract secret information by spectrum spread using Complete Complementary Code.  

```python=embed_ccc.py
#
# embed_ccc.py
# Created by pira on 2017/08/14.
#

#coding: utf-8

from VideoDigitalWatermarking import *

secret_data = [1,1,1,1,0,0,0,0]
secret_length = len(secret_data)

print('CCC')
ccc = generateCCC(2)
print(ccc, '\n')

#Embed
basic = createBasicSeq(ccc, secret_length, tau=1)
print('basic = ', basic, '\n')

es = createEmbedSeq(basic, secret_data, a=1, tau=1)
print('Embed Sequence =', es, '\n')

#Extract
secret = extractCCC(ccc, es, secret_length, tau=1, ch=1)
print('secret =', secret)
```

```
CCC
[[[ 1.  1. -1.  1.]
  [-1.  1.  1.  1.]]

 [[ 1.  1.  1. -1.]
  [-1.  1. -1. -1.]]] 

basic =  [1. 1. -1. 1. 0. 0. 0. 0. 0. 0. 0. -1. 1. 1. 1. 0. 0. 0. 0. 0. 0. 0.] 

Embed Sequence = [ 1  2  1  2  0 -2  0 -2 -1  0 -1 -1  0  1  2  4  2  0 -2 -3 -2 -1  0  0  0  0  0  0  0] 

secret = [1, 1, 1, 1, 0, 0, 0, 0]
```

### Divide video into images.
You can input a video and output each frames as images.  

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
You can input an image and divide it into blocks.  

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

### BER
Calculate Bit Error Rate.


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

### PSNR
Calculate Peak Signal-to-Noise Ratio.

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