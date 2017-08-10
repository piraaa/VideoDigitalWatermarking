# VideoDigitalWatermarking
(While editing)

Basic watermarking libraries for images and videos with python 3.  
Functions will be added in the future.  

python3で画像・動画の電子透かしを行うための基本的なライブラリです．  
今後も機能を追加していく予定です．  

(Edited on 2017/08/08)

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

* **calcBER(data1, data2)**
Calculate Bit Error Rate.
@param  data1 : result data
@param  data2 : answer data
@return ber: bit error rate [%].</details>

<details><summary><strong>dct</strong> - For Discrete Cosine Transform.</summary>

* **dct_dim1(data)**
1 dimension DCT.
@param  data : 1 dimension data
@return data : 1 dimension data conversion by DCT
*
*
*
</details>

#### For more information, please install this library and refer to "VideoDigitalWatermarking/html/index.html" with your browser.

## Samples
* sample programs will be added.

## License
* MIT License.  
Please see [LICENSE](https://github.com/piraaa/VideoDigitalWatermarking/blob/master/LICENSE).   

## Library
This program is using [OpenCV](http://opencv.org) for input and output.  
Please read [here](http://opencv.org/license.html) about OpenCV license.  

## About Sphinx
Sphinx is a documentation tool for Python.  
HTML documents in this library was created using Sphinx.  
* [Sphinx](http://www.sphinx-doc.org/ja/stable/#) - Sphinx HP
* [#sphinxjp](http://sphinx-users.jp/index.html#) - Sphinx-Users community