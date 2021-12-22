import openslide
import numpy as np
from tqdm import tqdm

'''
This script reads the .svs file specified in the img_path variable below and then does 2 things.
1. Saves a downsampled copy (at 3% the resolution of the original) of the full slide
2. Makes 10 random crops and saves them.

See here for more on openslide: https://developer.ibm.com/articles/an-automatic-method-to-identify-tissues-from-big-whole-slide-images-pt1/
And here for some docs: https://openslide.org/api/python/
'''

patch_name_fmt = 'patch{}_{}.png'

# read image
img_path = 'path/to/file.svs'
img = openslide.OpenSlide(img_path)


# get bounds
w, h = img.dimensions
print(f'Slide dims are: {w}x{h}')

# save a low res version of input image (10%)
downsample_pct = 0.03
thumbnail_size = (int(w*downsample_pct), int(h*downsample_pct))
print(f'saving thumbnail at {thumbnail_size}')
img.get_thumbnail(thumbnail_size).save('thumbnail.png')

# make patches
num_patches = 10
patch_size = (244, 244)
for i in tqdm(range(num_patches)):
    # get top left of random patch
    tl = (np.random.randint(w), np.random.randint(h))
    patch_save_name = patch_name_fmt.format(i, tl)
    rand_region = img.read_region(location=tl, level=0, size=patch_size).save(patch_save_name)
