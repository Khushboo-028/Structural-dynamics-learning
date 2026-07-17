import numpy as np
import matplotlib.pyplot as plt
# SDOF SYSTEM PARAMETERS
m = 1.0       # Mass (kg)
k = 100.0     # Stiffness (N/m)
c = 1.0       # Damping coefficient (N.s/m)
x0 = 0.1      # Initial displacement (m)
v0 = 0.0      # Initial velocity (m/s)

# DYNAMIC PROPERTIES
omega_n = np.sqrt(k / m)
f_n = omega_n / (2 * np.pi)
zeta = c / (2 * np.sqrt(k * m))
omega_d = omega_n * np.sqrt(1 - zeta**2)

# PRINT RESULTS
print(f"Natural frequency = {omega_n:.4f} rad/s")
print(f"Natural frequency = {f_n:.4f} Hz")
print(f"Damping ratio = {zeta:.4f}")
print(f"Damped natural frequency = {omega_d:.4f} rad/s")

# TIME ARRAY
t = np.linspace(0, 5, 1000)

# FREE VIBRATION RESPONSE
A = x0
B = (v0 + zeta * omega_n * x0) / omega_d
x = np.exp(-zeta * omega_n * t) * (
    A * np.cos(omega_d * t)
    + B * np.sin(omega_d * t)
)

# PLOT RESPONSE
plt.plot(t, x)
plt.xlabel("Time, t (s)")
plt.ylabel("Displacement, x(t) (m)")
plt.title("Free Vibration Response of an SDOF System")
plt.grid(True)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# DAMPING COMPARISON
# --------------------------------------------------

c_values = [0, 1, 10]

for c_case in c_values:

    zeta_case = c_case / (2 * np.sqrt(k * m))

    omega_d_case = omega_n * np.sqrt(1 - zeta_case**2)

    A = x0

    B = (
        v0 + zeta_case * omega_n * x0
    ) / omega_d_case

    x_case = np.exp(-zeta_case * omega_n * t) * (
        A * np.cos(omega_d_case * t)
        + B * np.sin(omega_d_case * t)
    )

    plt.plot(
        t,
        x_case,
        label=f"c = {c_case} N.s/m"
    )


plt.xlabel("Time, t (s)")
plt.ylabel("Displacement, x(t) (m)")
plt.title("Effect of Damping on SDOF Free Vibration")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "sdof_damping_comparison.png",
    dpi=300
)

plt.show() 