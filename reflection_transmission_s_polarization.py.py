# reflection_transmission_s_polarization.py
# computes and plots reflectance and transmittance for s-polarized light
# at an interface between two dielectric media using Fresnel equations.

import numpy as np
import matplotlib.pyplot as plt

# refractive indices for the two media
n1 = 1.0  # incident medium (air)
n2 = 1.5  # transmission medium (glass)

# incident angles (in radians)
theta_i = np.linspace(0, np.pi / 2, 500)

# transmitted angles from Snell's Law: n1 * sin(theta_i) = n2 * sin(theta_t)

sin_theta_t = np.clip((n1 / n2) * np.sin(theta_i), -1, 1)
theta_t = np.arcsin(sin_theta_t)

# Fresnel equations for s-polarized light
# reflection coefficient (amplitude)
rs = (n1 * np.cos(theta_i) - n2 * np.cos(theta_t)) / (n1 * np.cos(theta_i) + n2 * np.cos(theta_t))

# transmission coefficient (amplitude)
ts = (2 * n1 * np.cos(theta_i)) / (n1 * np.cos(theta_i) + n2 * np.cos(theta_t))

# reflectance and transmittance (power coefficients)
R = rs**2
T = (n2 * np.cos(theta_t)) / (n1 * np.cos(theta_i)) * ts**2

# plotting
plt.figure(figsize=(8, 5))
plt.plot(np.degrees(theta_i), R, label='Reflectance (R)', color='orange')
plt.plot(np.degrees(theta_i), T, label='Transmittance (T)', color='red')
plt.xlabel(r'Angle of Incidence $\theta_i$ (degrees)')
plt.ylabel('Coefficient')
plt.title('Reflection and Transmission Coefficients (s-polarization)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("reflection_transmission_s_polarization.png", dpi=300)
plt.show()
