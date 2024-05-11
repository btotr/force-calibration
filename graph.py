import matplotlib.pyplot as plt
import os

# Create a named pipe
pipe_name = '/tmp/pw'

# Plot live data
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
line, = ax.plot([], [])

with open(pipe_name, 'r') as pipe:
    while True:
        data = pipe.readline().strip()
        if data:
            # Process data and update the plot
            # For example, assuming data is a single value
            y = float(data)
            x = range(len(line.get_ydata()) + 1)
            line.set_data(x, list(line.get_ydata()) + [y])
            ax.relim()
            ax.autoscale_view()
            plt.draw()
            plt.pause(0.01)  # Adjust the pause time as needed
