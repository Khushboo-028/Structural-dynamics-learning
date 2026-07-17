import numpy as np
import matplotlib.pyplot as plt


def sdof_response(m, k, c, x0, v0, t):

    omega_n = np.sqrt(k / m)

    zeta = c / (2 * np.sqrt(k * m))

    if zeta < 1:

        omega_d = omega_n * np.sqrt(1 - zeta**2)

        A = x0

        B = (v0 + zeta * omega_n * x0) / omega_d

        x = np.exp(-zeta * omega_n * t) * (
            A * np.cos(omega_d * t)
            + B * np.sin(omega_d * t)
        )

    else:
        x = np.zeros_like(t)

    return {
        "x": x,
        "omega_n": omega_n,
        "zeta": zeta,
        "omega_d": omega_d,
    }   


# --------------------------------------------------
# INPUT PARAMETERS
# --------------------------------------------------

m = 1
k = 100
x0 = 0.1
v0 = 0

t = np.linspace(0, 5, 1000)

# Three damping cases
case1 = sdof_response(m, k, 0, x0, v0, t)
case2 = sdof_response(m, k, 1, x0, v0, t)
case3 = sdof_response(m, k, 10, x0, v0, t)

# Plot
plt.figure(figsize=(8,5))

plt.plot(t, case1, label="c = 0")
plt.plot(t, case2, label="c = 1")
plt.plot(t, case3, label="c = 10")

plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Effect of Damping on Free Vibration")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nEffect of Stiffness")

k_values = [50, 100, 200, 500]

plt.figure(figsize=(8,5))

for k in k_values:

    response = sdof_response(m, k, 1, x0, v0, t)

    omega_n = np.sqrt(k/m)

    print(f"k = {k:3d} N/m   "
          f"Natural Frequency = {omega_n:.3f} rad/s")

    plt.plot(t, response, label=f"k = {k}")

plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Effect of Stiffness")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nEffect of Mass")

m_values = [0.5, 1, 2, 5]

plt.figure(figsize=(8,5))

k = 100

for m in m_values:

    response = sdof_response(m, k, 1, x0, v0, t)

    omega_n = np.sqrt(k/m)

    print(f"m = {m:3.1f} kg   "
          f"Natural Frequency = {omega_n:.3f} rad/s")

    plt.plot(t, response, label=f"m = {m}")

plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Effect of Mass")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()