import streamlit as st
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def random_palette(k=5):
    # return k random pastel-like colors
    return [(random.random(), random.random(), random.random()) for _ in range(k)]

def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    # generate a wobbly closed shape
    angles = np.linspace(0, 2*math.pi, points)
    radii = r * (1 + wobble*(np.random.rand(points)-0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# Streamlit page setup
st.set_page_config(page_title="Generative Abstract Poster", layout="wide")
st.title("🎨 Generative Abstract Poster")

# draw
random.seed()
fig, ax = plt.subplots(figsize=(7, 10))
ax.axis('off')
ax.set_facecolor((0.98, 0.98, 0.97))

palette = random_palette(6)
n_layers = 8
for i in range(n_layers):
    cx, cy = random.random(), random.random()
    rr = random.uniform(0.15, 0.45)
    x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(0.05, 0.25))
    color = random.choice(palette)
    alpha = random.uniform(0.25, 0.6)
    ax.fill(x, y, color=color, alpha=alpha, edgecolor=(0,0,0,0))

# simple typographic label
ax.text(0.05, 0.95, "Generative Poster", fontsize=18, weight='bold', transform=ax.transAxes)
ax.text(0.05, 0.91, "Week 2 • Arts & Advanced Big Data", fontsize=11, transform=ax.transAxes)

ax.set_xlim(0,1)
ax.set_ylim(0,1)

st.pyplot(fig)
