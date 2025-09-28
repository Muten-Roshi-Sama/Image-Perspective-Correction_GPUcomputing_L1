# import numpy as np


# x = [1, -1, -1,  1, 1,  1, -1, -1,  1,  1, -1, -1, -1, -1,  1,  1]
# y = [1,  1, -1, -1, 1,  1,  1, -1, -1,  1,  1,  1, -1, -1, -1, -1]
# z = [1,  1,  1,  1, 1, -1, -1, -1, -1, -1, -1,  1,  1, -1, -1,  1]

# #  Create the 3D coordinates of the vertices of a cube:
# M = np.array([[1, 2, 3], [4, 5, 6]])
# Xcube = np.array([x, y, z, [1]*16])
# print(Xcube)

# # The mutliplication between two matrices is done with the `@` operator:
# N = np.array([[1], [0], [0]])
# print(M @ N)


# # %matplotlib ipympl
# from matplotlib import pyplot as plt

# xi = Xcube[0, :]/Xcube[3, :]  # first row (index0) of cubeX divided by row 3 (i4)
# yi = Xcube[1, :]/Xcube[3, :]

# factor = 2.5
# plt.figure(figsize=(4*factor, 3*factor))  # taille de l'image en pouces
# plt.axis([0, 640, 480, 0])
# plt.plot([50, 50, 100, 100, 50], [50, 100, 100, 50, 50], "-o")  # "-o" pour traits et cercle
# plt.show()

# import to load images
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

# image loading
img = mpimg.imread('cover.jpg')

fig = plt.figure()
points = [[], []]

# function to be called on each click on the image
def onclick(event):
    # save the point
    print(f'Pixel Coordinates (x, y): ({int(event.xdata)}, {int(event.ydata)})')
    points[0].append(event.xdata)
    points[1].append(event.ydata)
    # show a cross
    plt.plot([event.xdata], [event.ydata], "x")

# register the click listener
fig.canvas.mpl_connect('button_press_event', onclick)

# display the image
plt.imshow(img)
plt.show()

