import numpy as np
import matplotlib.pyplot as plt

# 1: smooth persuit
# 2: reading

time_1 = np.load('time_1.npy')
time_2 = np.load('time_2.npy')
coordinates_1 = np.load('coordinates_1.npy')
coordinates_2 = np.load('coordinates_2.npy')
coordinates_1y = np.load('coordinates_1y.npy')
coordinates_2y = np.load('coordinates_2y.npy')

speed1 = np.gradient(coordinates_1, time_1)
speed2 = np.gradient(coordinates_2, time_2)
speed1y = np.gradient(coordinates_1y, time_1)
speed2y = np.gradient(coordinates_2y, time_2)


# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plotting x-coordinates on the same plot
axs[0, 0].plot(time_1, coordinates_1, label='Smooth Persuit', marker='o', linestyle='-')
axs[0, 0].plot(time_2, coordinates_2, label='Reading', marker='o', linestyle='-')
axs[0, 0].set_title('X Coordinates')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('Position')
axs[0, 0].legend()

# Plotting x-speeds on the same plot
axs[1, 0].plot(time_1, speed1, label='Smooth Persuit', marker='o', linestyle='-')
axs[1, 0].plot(time_2, speed2, label='Reading', marker='o', linestyle='-')
axs[1, 0].set_title('X Coordinates Speed')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('Speed')
axs[1, 0].legend()

# Plotting y-coordinates on the same plot
axs[0, 1].plot(time_1, coordinates_1y, label='Smooth Persuit', marker='o', linestyle='--')
axs[0, 1].plot(time_2, coordinates_2y, label='Reading', marker='o', linestyle='--')
axs[0, 1].set_title('Y Coordinates')
axs[0, 1].set_xlabel('Time')
axs[0, 1].set_ylabel('Position')
axs[0, 1].legend()

# Plotting y-speeds on the same plot
axs[1, 1].plot(time_1, speed1y, label='Smooth Persuit', marker='o', linestyle='--')
axs[1, 1].plot(time_2, speed2y, label='Reading', marker='o', linestyle='--')
axs[1, 1].set_title('Y Coordinates Speed')
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel('Speed')
axs[1, 1].legend()

# Adjust layout for better appearance
plt.tight_layout()

# Show the plots
plt.show()