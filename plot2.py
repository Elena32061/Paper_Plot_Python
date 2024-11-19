import matplotlib.pyplot as plt
import numpy as np

# Data for the x-axis (bit stream length)
bit_stream_length = [2**6, 2**7, 2**8]

# Realistic data for accuracy and efficiency
accuracy_1 = [90, 93.08, 94.45]  # Accuracy 1 (%)
accuracy_2 = [89.46, 92.46, 94.31]  # Accuracy 2 (%)
efficiency_1 = [306, 76.6, 19.15]  # Efficiency 1
efficiency_2 = [345.46, 86.366, 21.59]  # Efficiency 2

# Convert bit stream length to string for scientific notation
bit_stream_labels = [f"$2^{{{int(i.bit_length() - 1)}}}$" for i in bit_stream_length]

# Prepare data for bar positions
x = np.arange(len(bit_stream_length))  # Bar positions
bar_width = 0.35  # Width of bars

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot efficiency as bar charts (Adjust color to match the circled area)
ax.bar(x - bar_width / 2, efficiency_1, bar_width, label='DS-CIM1 Efficiency', color="#BAC8FF")  # Light purple-blue
ax.bar(x + bar_width / 2, efficiency_2, bar_width, label='DS-CIM2 Efficiency', color="#D6E4FF")  # Lighter purple-blue

# Plot accuracy as line plots (Red colors with larger markers)
ax2 = ax.twinx()
ax2.scatter(x, accuracy_1, label='DS-CIM1 Accuracy', color="#FF5733", s=80)  # Bright red with size 80
ax2.plot(x, accuracy_1, 'o-', color="#FF5733", linewidth=1)  # Line for DS-CIM1 Accuracy
ax2.scatter(x, accuracy_2, label='DS-CIM2 Accuracy', color="#C70039", s=80)  # Dark red with size 80
ax2.plot(x, accuracy_2, 'o--', color="#C70039", linewidth=1)  # Line for DS-CIM2 Accuracy

# Configure x-axis
ax.set_xticks(x)
ax.set_xticklabels(bit_stream_labels)
ax.set_xlabel('Bit Stream Length (Scientific Notation)', fontsize=12, color='black')

# Configure y-axis for efficiency
ax.set_ylabel('Efficiency (TOPS/W * TOPS/mm$^{2}$)', fontsize=12, color='black')
ax.set_ylim(0, 400)  # Adjust for better visualization
ax.tick_params(axis='y', colors='black')

# Configure y-axis for accuracy
ax2.set_ylabel('Accuracy (%)', fontsize=12, color='black')
ax2.set_ylim(88, 96)  # Adjust for better visualization
ax2.tick_params(axis='y', colors='black')

# Add legends for both axes
ax.legend(loc='upper left')
ax2.legend(loc='upper right')

# Add grid for better readability
ax.grid(visible=True, linestyle='--', alpha=0.6)

# Title
plt.title('Accuracy (Line) and Efficiency (Bar) vs Bit Stream Length', fontsize=14, color='black')

# Adjust layout and save
plt.tight_layout()
plt.savefig('accuracy_line_efficiency_bar_custom_blue.png', dpi=600)
plt.show()
