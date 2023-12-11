import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Function to generate live data (replace this with your own data source)

def generate_live_data():
    with open('data_file.txt', 'r') as file:
        data = list(map(float,file.read().split(' ')))
        print(data)
    time.sleep(1)
    return data

# Initialize data and plot
x_values = []
y_values = []
start_time = dt.datetime.now()

fig, ax = plt.subplots(6)

# Function to update the plot with new data
def update(frame, x_values, y_values):
    x_values.append((dt.datetime.now()-start_time).total_seconds())
    y_values.append(generate_live_data())

    # Limit the number of data points to display (adjust as needed)
    max_points = 40
    x_values = x_values[-max_points:]
    y_values = y_values[-max_points:]


    for i in range(6):
        y_vals = []
        for data in y_values:
            y_vals.append(data[i])            
        ax[i].clear()
        ax[i].plot(x_values, y_vals)
    
    ax[0].axhline(y=500, color='red', linestyle='--', linewidth = 0.75 , label='Curl Threshold') #thumb
    ax[1].axhline(y=200, color='red', linestyle='--', linewidth = 0.75 , label='Curl Threshold') #index
    ax[2].axhline(y=420, color='red', linestyle='--', linewidth = 0.75 , label='Curl Threshold') #middle
    ax[3].axhline(y=1000, color='red', linestyle='--', linewidth = 0.75 , label='Curl Threshold') #ring
    ax[4].axhline(y=1000, color='red', linestyle='--', linewidth = 0.75 , label='Curl Threshold') #pinky
    ax[5].axhline(y=1000, color='red', linestyle='--', linewidth = 0.75 , label='Curl Threshold') #wrist

    ax[0].set_title('Sensor Readings', fontsize = '20')
    ax[0].legend(bbox_to_anchor = (1.0, 1), loc = 'lower right')
    ax[5].set_xlabel('Time')
    ax[0].set_ylabel('Thumb')
    ax[1].set_ylabel('Index')
    ax[2].set_ylabel('Middle')
    ax[3].set_ylabel('Ring')
    ax[4].set_ylabel('Pinky')
    ax[5].set_ylabel('Wrist')

# Create animation
ani = FuncAnimation(fig, update, fargs=(x_values, y_values), interval=100, cache_frame_data=False)  # Update every 500 milliseconds (0.5 second)

# Get the current figure manager
fig_manager = plt.get_current_fig_manager()

# Maximize the window (works on most systems)
fig_manager.window.state('normal') # For Windows

# Show the plot
plt.show()
