import numpy as np
import matplotlib.pyplot as plt

# Polynomial: x^3 - 9x^2 + 4x + 6
def poly(x):
    return x**3 - 9*x**2 + 4*x + 6

# Smooth curve
x = np.linspace(-2, 6, 400)
y = poly(x)

# 50 noisy points (Gaussian noise)
x_noise = np.linspace(-2, 6, 100)
y_noise = poly(x_noise) + np.random.normal(0, 2, size=x_noise.shape)

plt.figure()
plt.plot(x, y, label=r"$1x^3 - 9x^2 + 4x + 6x^0$")
plt.scatter(x_noise, y_noise, s=2)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cubic regression")
plt.savefig("cubic.png")
