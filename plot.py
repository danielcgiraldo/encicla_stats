import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
import numpy as np
import matplotlib.dates as mdates

HORARIO = (datetime.strptime("5:30:00", "%H:%M:%S"), datetime.strptime("22:00:00", "%H:%M:%S"))
FECHA = "2023-05-17"
ESTACION = "Campus Nacional" # Estaciones: ['Suramericana', 'Colombia', 'Carlos E. Restrepo', 'Campus Nacional']

# Read data from file
data = defaultdict(lambda: defaultdict(dict))
with open("data.txt") as file:
    for line in file:
        row = line.strip().split(",")
        data[row[0]][row[2]][row[3]] = int(row[1])

print("Estaciones:", list(data.keys()))

# Extract x and y values
x = list(data[ESTACION][FECHA].keys())
x = [datetime.strptime(time_str, "%H:%M:%S") for time_str in x] # Convert to datetime
y = list(data[ESTACION][FECHA].values())

# Plot
fig, ax = plt.subplots(figsize=(300, 20))
ax.step(x, y, linewidth=2.5)
ax.set(xlim=HORARIO, xticks=x, ylim=(0, max(y)), yticks=np.arange(0, max(y) + 1, 1))

# Format x-axis tick labels as time only
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))

# Save and show the plot
plt.savefig(f'/plots/{ESTACION}-{FECHA}.png', bbox_inches='tight', dpi=150)