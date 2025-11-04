import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_parameters():
    try:
        freq_ghz = float(freq_entry.get())
        er = float(er_entry.get())

        # Constants
        c = 3e8  # Speed of light (m/s)
        f = freq_ghz * 1e9  # Convert GHz to Hz

        # Calculations
        wavelength = c / f  # in meters
        wavelength_cm = wavelength * 100  # convert to cm
        gain = 6 + 20 * math.log10(freq_ghz)  # approximate empirical formula
        bandwidth = (3e8 / (f * math.sqrt(er))) * 100  # percentage approximation

        # Display results
        wavelength_label.config(text=f"Wavelength: {wavelength_cm:.2f} cm")
        gain_label.config(text=f"Estimated Gain: {gain:.2f} dBi")
        bw_label.config(text=f"Approx. Bandwidth: {bandwidth:.2f} %")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

def plot_gain_graph():
    try:
        # Frequency range (1 to 10 GHz)
        freq_range = np.linspace(1, 10, 100)
        gain_values = 6 + 20 * np.log10(freq_range)

        plt.figure(figsize=(6, 4))
        plt.plot(freq_range, gain_values, 'b-', linewidth=2)
        plt.title("Gain vs Frequency", fontsize=14, fontweight='bold')
        plt.xlabel("Frequency (GHz)")
        plt.ylabel("Gain (dBi)")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Plotting error: {e}")

# ---------------- GUI Setup ---------------- #
root = tk.Tk()
root.title("Antenna Parameter Calculator")
root.geometry("420x360")
root.resizable(False, False)

tk.Label(root, text="Antenna Parameter Calculator", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Frequency (GHz):").pack()
freq_entry = tk.Entry(root, width=20)
freq_entry.pack()

tk.Label(root, text="Dielectric Constant (εr):").pack()
er_entry = tk.Entry(root, width=20)
er_entry.pack()

tk.Button(root, text="Calculate", command=calculate_parameters, bg="#007acc", fg="white",
          font=("Arial", 10, "bold")).pack(pady=8)

tk.Button(root, text="Plot Gain vs Frequency", command=plot_gain_graph, bg="#228B22", fg="white",
          font=("Arial", 10, "bold")).pack(pady=5)

wavelength_label = tk.Label(root, text="Wavelength: ", font=("Arial", 10))
wavelength_label.pack()

gain_label = tk.Label(root, text="Estimated Gain: ", font=("Arial", 10))
gain_label.pack()

bw_label = tk.Label(root, text="Approx. Bandwidth: ", font=("Arial", 10))
bw_label.pack()

tk.Label(root, text="© Devavrat Rajendra Choure | Pillai College of Engineering",
         font=("Arial", 8, "italic")).pack(side="bottom", pady=5)

root.mainloop()
