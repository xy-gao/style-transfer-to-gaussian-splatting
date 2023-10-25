# style-transfer-to-gaussian-splatting

## step 1
Prepare your own image sequence (or any other nerf dataset like https://jonbarron.info/mipnerf360/) and make a dataset.

```
dataset
|---input
    |---<image 0>
    |---<image 1>
    |---...
```

## step 2
Process dataset for gaussian splatting training.

```
git clone https://github.com/graphdeco-inria/gaussian-splatting --recursive
```
Follow [gaussian splatting](https://github.com/graphdeco-inria/gaussian-splatting) for setup. 

you also need to install colmap, or executable can be found here. https://demuc.de/colmap/
```
python .\gaussian-splatting\convert.py -s path\to\your\dataset --colmap_executable path\to\your\COLMAP.bat
```
now your dataset will be like
```
dataset
|---images
|   |---<image 0>
|   |---<image 1>
|   |---...
|---sparse
    |---0
        |---cameras.bin
        |---images.bin
        |---points3D.bin
|---input
|---...
```
## step 3
style transfer each images and put them back (overwrite) to `dataset/images` folder keeping same image names (you must keep same image names for camera info consistency).
```
dataset
|---images #stylized images
|   |---<image 0>
|   |---<image 1>
|   |---...
|---sparse
    |---0
        |---cameras.bin
        |---images.bin
        |---points3D.bin
|---input
|---...
```

For image style transfer, you can use whatever tool you like.
In my case i installed https://github.com/crowsonkb/style-transfer-pytorch. 
```
git clone https://github.com/crowsonkb/style-transfer-pytorch.git
pip install -e .
```
And I wrote a script to do style transfer and overwrite image files this step.
```
python main.py path\to\your\dataset\images path\to\your\style\image.jpg path\to\your\dataset\images
```

# step 4
The dataset is set and you can train your gaussian splatting model.
```
python .\gaussian-splatting\train.py -s path\to\your\dataset
```
There will be an output folder for trained gaussian splatting and you can use [viewers](https://github.com/graphdeco-inria/gaussian-splatting#pre-built-windows-binaries) to checkout the result. 
