import openslide
import numpy as np
from tqdm import tqdm

patch_name_fmt = 'patch{}_{}.png'

# read image
img_path = '/Users/user/Desktop/tomac/0c59c32a-ce9a-4557-be21-90d72ddc34b4/TCGA-AU-3779-01Z-00-DX1.4134005A-8A79-46DC-8737-B3C8AAC2DFCA.svs'
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
