import numpy as np
import matplotlib.pyplot as plt

# Polynomial: x^3 - 9x^2 + 4x + 6
def poly(x):
    return x**3 - 9*x**2 + 4*x + 6

# Smooth curve
x = np.linspace(-2, 6, 400)
y = poly(x)

# 50 noisy points (Gaussian noise)
x_noise = np.linspace(-2, 6, 50)
y_noise = poly(x_noise) + np.random.normal(0, 10, size=x_noise.shape)

plt.figure()
plt.plot(x, y, label=r"$1x³ - 9x² + 4x + 6x°$")
plt.scatter(x_noise, y_noise)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cubic regression")
plt.savefig("cubic.png")
