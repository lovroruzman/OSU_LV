import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans
from PIL import Image as im

# ucitaj sliku
img = Image.imread("test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w, h, d = img.shape
img_array = np.reshape(img, (w * h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

plt.figure
plt.scatter(img_array[:, 0], img_array[:, 1])
plt.show()
