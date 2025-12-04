import numpy as np
import matplotlib.pyplot as plt

# Polynomial: x^3 - 9x^2 + 4x + 6
def poly(x):
    return 4*x - 6

# Smooth curve
x = np.linspace(-2, 6, 400)
y = poly(x)

# 50 noisy points (Gaussian noise)
x_noise = np.linspace(-2, 6, 100)
y_noise = poly(x_noise) + np.random.normal(0, 1, size=x_noise.shape)

plt.figure()
plt.plot(x, y, label=r"$4x - 6$")
plt.scatter(x_noise, y_noise, s=2)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear regression")
plt.savefig("linear.png")
