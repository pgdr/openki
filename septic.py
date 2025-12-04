import numpy as np
import matplotlib.pyplot as plt


# Polynomial: x^3 - 9x^2 + 4x + 6
def poly(x):
    return (
        - 0.0001 * x**7
        + 0.009 * x**6
        - 0.05 * x**5
        - 0.02 * x**4
        + 0.01 * x**3
        - 0.09 * x**2
        + 0.14 * x
        + 6
    )



# Smooth curve
x = np.linspace(-4, 6, 400)
y = poly(x)

# 50 noisy points (Gaussian noise)
x_noise = np.linspace(-4, 6, 80)
y_noise = poly(x_noise) + np.random.normal(0, 2, size=x_noise.shape)

plt.figure()
plt.plot(x, y, label=r"$.01 x^7 + .09 x^6 - .5 x^5 - .2 x^4 + .1 x^3 - .9 x^2 + .4 x + 6$")
plt.scatter(x_noise, y_noise, s=2)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Septic regression")
plt.savefig("septic.png")
