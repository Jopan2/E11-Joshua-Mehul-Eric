import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
datafile = r'C:\Users\erich\Downloads\friday.csv'

# Read the CSV file
data = pd.read_csv(datafile)

# Define a time array
time = range(len(data))

# Plot each column against time in a separate plot
for col in data.columns[2:9]:
    plt.plot(time, data[col])
    plt.xlabel('Time')
    plt.ylabel(col)
    plt.title(col)
    plt.show()

