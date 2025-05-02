
# Fresnel-Frenzy: s-Polarized Reflection & Transmission

Ever stared at a beam of light hitting a glass surface and thought, *“I wonder how much of that got in?”* This repository is here to answer that, specifically for **s-polarized** light (where the electric field is perpendicular to the plane of incidence).

This Python script computes and plots the **reflectance (R)** and **transmittance (T)** of electromagnetic waves using the **Fresnel equations**, assuming:
- The incident wave is **s-polarized**
- \( n_1 = 1.0 \) (air)
- \( n_2 = 1.5 \) (glass, because who doesn’t love transparency?)

## 📈 What This Project Does

- Implements the Fresnel equations for s-polarized light
- Uses Snell’s law to calculate transmission angles
- Plots \( R \) and \( T \) versus the angle of incidence \( \theta_i \)
- Produces a beautiful plot that you can show off to your optics professor

## 🧠 Background

The reflection and transmission of light at an interface between two dielectrics depends on the polarization of the electric field. For s-polarization:

\[
r_s = \frac{n_1 \cos\theta_i - n_2 \cos\theta_t}{n_1 \cos\theta_i + n_2 \cos\theta_t}, \quad
t_s = \frac{2n_1 \cos\theta_i}{n_1 \cos\theta_i + n_2 \cos\theta_t}
\]

Reflectance and transmittance (i.e., power ratios) are then:

\[
R = |r_s|^2, \quad
T = \left( \frac{n_2 \cos\theta_t}{n_1 \cos\theta_i} \right) |t_s|^2
\]

Fear not — all equations are handled for you. Just run the script and enjoy the plot.

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/fresnel-frenzy.git
cd fresnel-frenzy
python reflection_transmission_s_polarization.py
