import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("LV2/road.jpg")

plt.imshow(img, cmap="gray", alpha=0.75)
plt.title("Posvijetljena slika")
plt.show()

img2 = img[:,img.shape[1]  // 4 : img.shape[1] // 2]
plt.imshow(img2, cmap="gray")
plt.title("Druga četvrtina slike po širini")
plt.show()

img3 = np.rot90(img,k=3)
plt.imshow(img3, cmap="gray")
plt.title("Rotirana slika")
plt.show()

img4 = np.fliplr(img)
plt.imshow(img4, cmap="gray")
plt.title("Zrcaljena slika")
plt.show()