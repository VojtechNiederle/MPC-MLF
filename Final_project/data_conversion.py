import numpy as np
from PIL import Image
import os

def load_images(directory,grayscale):
    images = []
    i=0
    for filename in os.listdir(directory):
        i += 1
        print(i)
        img = Image.open(os.path.join(directory, filename))
        if grayscale:
            img = img.convert('L')
            img_array = np.array(img) / 255.0
        else:
            img_array = np.array(img)
        images.append(img_array)
    return images

images = load_images("Data/test_data_unlabeled",False)
np.savez_compressed('Data/NPZ/images.npz', images=images)
