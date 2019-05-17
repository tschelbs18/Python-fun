import matplotlib.pyplot as plt
import numpy as np


##### Simple linear plot #####
# Optional 3rd argument for style of plot
# o = circle, -- = dashes, s = square, ^ = triangle
# colors r = red, g = green, b = blue, etc.
plt.plot([1,2,3,4],[4,3,2,1], 'y^') #Where the first list is the X, second is the Y
plt.ylabel('some numbers')
plt.show()

# Multiple sets of data on one plot
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') # red dashes, blue squares and green triangles
plt.show()

##### Data Keyword Argument #####
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

# Plot A in relation to B with the color determined by C and size determined by D
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


##### Categorical Variables and Subplots #####
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(1, figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

# Can also edit line properties, make subplots for a figure, save images, and uses nonlinear curves
# For more info check out https://matplotlib.org/tutorials/introductory/pyplot.html


