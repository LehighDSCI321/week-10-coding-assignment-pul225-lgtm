import numpy as np
import matplotlib.pyplot as plt

# define the function
def f_z(z):
    if 0 < z <1:
        return 2 * (1 - z)
    else:
        return 0
    
# generate the points
z_values = np.linspace(-1, 2, 1000)
f_values = [f_z(z) for z in z_values]

# plot
plt.plot(z_values, f_values)
plt.xlabel('z')
plt.ylabel('f_Z(z)')
plt.title('Probability Density Function of Z')
plt.grid(True)
plt.show()

def f_Y(y):
    if y > 0:
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-(np.log(y))**2 / 2) / y
    else:
        return 0

y_values = np.linspace(0.1, 5, 1000)
f_values = [f_Y(y) for y in y_values]

plt.plot(y_values, f_values)
plt.xlabel('y')
plt.ylabel('f_Y(y)')
plt.title('PDF of Y = e^X where X ~ N(0,1)')
plt.grid(True)
plt.show()

x = np.random.normal(0, 1, 10000)
y = np.exp(x)

# plot
def f_Y(y_val):
    if y_val > 0:
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-(np.log(y_val))**2 / 2) / y_val
    else:
        return 0
y_pdf = np.linspace(0.1, 5, 1000)
f_vals = [f_Y(y) for y in y_pdf]


plt.hist(y, bins=50, density=True, alpha=0.6, label='Histogram of y')
plt.plot(y_pdf, f_vals, 'r-', label='Theoretical PDF')
plt.xlabel('y')
plt.ylabel('Density')
plt.title('Histogram of y vs Theoretical PDF')
plt.legend()
plt.grid(True)
plt.show()
