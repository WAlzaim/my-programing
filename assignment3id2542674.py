# Programming in Science - Assignment 3
# Student ID: 2542674

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D 

# -------------------------------
# Part 0 - Student ID Values
# -------------------------------

student_id = "2542674"

d1 = int(student_id[-2])
d2 = int(student_id[-1])

k = (d1 + d2) % 4 + 2
shift = d1 - d2
n_points = 20 + d1
frame_step = d2 + 1

print("Student ID:", student_id)
print("d1 =", d1)
print("d2 =", d2)
print("k =", k)
print("shift =", shift)
print("n_points =", n_points)
print("frame_step =", frame_step)

# -------------------------------
# Component A1 - Line Plot
# -------------------------------

x = list(range(1, n_points + 1))
y = []

for i in x:
    y.append(i ** 2)

if len(x) > 0 and len(x) == len(y):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.title("Line Plot of x and x squared")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -------------------------------
# Component A2 - Distribution Plot
# -------------------------------

# Histogram helps show how the repeated data is spread out.

np.random.seed(1)
data_values = np.random.normal(50, 10, 50)

print("First 10 values:")
print(data_values[:10])

plt.figure(figsize=(8, 5))
plt.hist(data_values, bins=10, edgecolor="black")
plt.title("Distribution of Data Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# -------------------------------
# Component B1 - Personalized 2D Plot
# -------------------------------

y2 = []

for i in x:
    y2.append(k * i + shift)

print("First 5 (x, y2) pairs:")

for i in range(5):
    print(x[i], y2[i])

plt.figure(figsize=(8, 5))
plt.plot(x, y2, "ro--")
plt.title("Student ID 2542674  k=5  shift=3")
plt.xlabel("x values")
plt.ylabel("y2 values")
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# Component B2 - 3D Scatter Plot
# -------------------------------

x3 = []
y3 = []
z3 = []

for i in range(1, n_points + 1):
    x3.append(i)
    y3.append(i + shift)
    z3.append(k * i)

print("First 5 (x, y, z) points:")

for i in range(5):
    print(x3[i], y3[i], z3[i])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(x3, y3, z3)

ax.set_title("3D Scatter Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.tight_layout()
plt.show()

# -------------------------------
# Component B3 - Animation
# -------------------------------

x_anim = np.arange(0, n_points)
y_anim = k * x_anim + shift

fig, ax = plt.subplots(figsize=(8, 5))
line, = ax.plot([], [], "g-")

ax.set_xlim(0, n_points)
ax.set_ylim(min(y_anim) - 5, max(y_anim) + 5)

ax.set_title("Animated Graph")
ax.set_xlabel("x")
ax.set_ylabel("y")

def update(frame):
    print("Animating frame:", frame)
    line.set_data(x_anim[:frame], y_anim[:frame])
    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=range(1, n_points + 1, frame_step),
    interval=300,
    repeat=False
)

plt.tight_layout()
plt.show()

