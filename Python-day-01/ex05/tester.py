from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
from matplotlib import pyplot as plt


array = ft_load("landscape.jpg")
invrt = ft_invert(array)
red = ft_red(array)
green = ft_green(array)
blue = ft_blue(array)
grey = ft_grey(array)


# print(ft_invert.__doc__)
# print(ft_red.__doc__)
# print(ft_green.__doc__)
# print(ft_blue.__doc__)
# print(ft_grey.__doc__)

# # # Display Both images
fig = plt.figure(figsize=(10, 10))
fig.add_subplot(3, 2, 1)
plt.imshow(array)
plt.title("Figure VIII.1: Original")
plt.axis('off')
###
fig.add_subplot(3, 2, 2)
plt.imshow(invrt)
plt.title("Figure VIII.2: Invert")
plt.axis('off')
##
fig.add_subplot(3, 2, 3)
plt.imshow(red)
plt.title("Figure VIII.3: Red")
plt.axis('off')
##
fig.add_subplot(3, 2, 4)
plt.imshow(green)
plt.title("Figure VIII.3: Green")
plt.axis('off')
##
fig.add_subplot(3, 2, 5)
plt.imshow(blue)
plt.title("Figure VIII.3: Blue")
plt.axis('off')
##
fig.add_subplot(3, 2, 6)
plt.imshow(grey, cmap='gray')
plt.title("Figure VIII.3: Grey")
plt.axis('off')
plt.show()
