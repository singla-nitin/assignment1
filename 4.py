#a)
from PIL import Image
import numpy as np

def img_to_array(path):
        img = Image.open(path)
        img_array = np.array(img)

        if len(img_array.shape) == 3:
            file_name = "image_rgb.txt"
        else:
            file_name = "image_greyscale.txt"

        np.savetxt(file_name, img_array.flatten(), fmt='%d')
        print(f"Image saved as {file_name}")

img_to_array(r"/content/drive/MyDrive/Colab Notebooks/DATASETS/El Gato Sticker.jpeg")

#b)
import matplotlib.pyplot as plt

flattened_array = np.loadtxt('image_rgb.txt', dtype=int)
reshaped_array = flattened_array.reshape((736, 736, 3))

plt.imshow(reshaped_array)
plt.axis('off')
plt.show()

