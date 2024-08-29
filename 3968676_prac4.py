################################################################################################################################################################

### PRAC 4 ###

################################################################################################################################################################

# Put your full name here:Kenneth
# Put your student number here:3968676 
# Don't forget to rename this file with your student number!
# For instance, my file would be named 1234567_prac4.py 
# Also don't forget to comment your code or you get no marks! 

################################################################################################################################################################

### Question 1 ###

################################################################################################################################################################

### Q1.1 

### This question is written only, no code required.

### Q1.2 

### This question is written only, no code required.

### Q1.3 

### This question is written only, no code required.

################################################################################################################################################################

### Question 2 ###

################################################################################################################################################################

### Q2.1 

### This question is written only, no code required.

### Q2.2 

# Put your code here 
#2. Reading and Plotting the Data
'''
We'll read the data from data1.csv and plot it.

'''

import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV
current, voltage = np.loadtxt('data1.csv', delimiter=',', unpack=True)

# Plot current vs voltage
plt.figure(figsize=(8, 6))
plt.plot(current, voltage, 'o', label='Measured Data')
plt.xlabel('Current (mA)')
plt.ylabel('Voltage (V)')
plt.title('Current vs Voltage')
plt.legend()
plt.grid(True)
plt.show()

### Q2.3 

# Put your code here 
#3. Calculating Resistance Using Linear Least Squares

'''
We use the derived formula to compute the resistance:

'''

# Calculate resistance
R = np.sum(current * voltage) / np.sum(current ** 2)
print(f"Calculated Resistance (Analytic) (R): {R:.2f} Ohms")


### Q2.4 

# Put your code here 
#4. Numerical Fitting with curve_fit

'''
We'll use curve_fit to find the resistance numerically:

'''

from scipy.optimize import curve_fit

# Define the model function
def ohms_law(current, resistance):
    return resistance * current

# Perform curve fitting
popt, pcov = curve_fit(ohms_law, current, voltage, p0=[1.0])

# Extract the resistance value
R_fit = popt[0]
print(f"Fitted Resistance (R): {R_fit:.2f} Ohms")


### Q2.5 

# Put your code here 
#5. Plotting Data with Best-Fitting Line
'''
Finally, plot the data with the best-fitting line overlaid:

'''

# Plot current vs voltage with best-fitting line
plt.figure(figsize=(8, 6))
plt.plot(current, voltage, 'o', label='Measured Data')

# Generate values for the fitted line
current_fit = np.linspace(min(current), max(current), 100)
voltage_fit = ohms_law(current_fit, R_fit)

plt.plot(current_fit, voltage_fit, '-', color='red', label='Best-Fitting Line')
plt.xlabel('Current (mA)')
plt.ylabel('Voltage (V)')
plt.title('Current vs Voltage with Best-Fitting Line')
plt.legend()
plt.grid(True)
plt.show()

################################################################################################################################################################

### Question 3 ###

################################################################################################################################################################
### Q3.1 

# Put your code here 
#1Reading and Plotting the Data
'''
First, we need to read the data from data2.csv, plot it, and check its characteristics.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Read the data from CSV file
data = pd.read_csv('data2.csv', header=None)
current_mA = data[0]
voltage_V = data[1]

# Convert current from mA to A
current_A = current_mA / 1000

# Plot the data
plt.figure(figsize=(8, 6))
plt.scatter(current_mA, voltage_V, color='blue', label='Data')
plt.xlabel('Current (mA)')
plt.ylabel('Voltage (V)')
plt.title('Current vs Voltage')
plt.legend()
plt.grid(True)
plt.show()

### Q3.2 

# Put your code here 
#2.Implementing the Power Law Function
'''We need to define a function that models the power-law relationship:
V=α*I**β
'''
 

#Here’s how you can define and test this function:

def power_law(current, alpha, beta):
    return alpha * current**beta

# Test the function with given values
current_test = 0.5  # in amps
alpha_test = 200
beta_test = 3
voltage_test = power_law(current_test, alpha_test, beta_test)
print(f"Test Voltage: {voltage_test} V")

### Q3.3 

# Put your code here 
#3. Using curve_fit to Determine Best-Fitting Values
'''We’ll use curve_fit from scipy.optimize to fit the power-law model to the data:'''

from scipy.optimize import curve_fit
import numpy as np

# Define the model function
def power_law_model(current, alpha, beta):
    return alpha * current**beta

# Fit the model to the data
popt, pcov = curve_fit(power_law_model, current_A, voltage_V, p0=[1, 1])

# Extract the fitted parameters
alpha_best, beta_best = popt
print(f"Best-fitting α: {alpha_best}")
print(f"Best-fitting β: {beta_best}")

### Q3.4 

# Put your code here 
#4. Plotting the Data with Best-Fitting Curve
'''After obtaining the best-fitting parameters, you can plot the data along with the fitted curve:'''

# Generate points for the fitted curve
current_fit = np.linspace(min(current_A), max(current_A), 500)
voltage_fit = power_law_model(current_fit, alpha_best, beta_best)

# Plot the original data and the fitted curve
plt.figure(figsize=(8, 6))
plt.scatter(current_mA, voltage_V, color='blue', label='Data')
plt.plot(current_fit * 1000, voltage_fit, color='red', label='Fitted Curve')
plt.xlabel('Current (mA)')
plt.ylabel('Voltage (V)')
plt.title('Current vs Voltage with Fitted Power Law Curve')
plt.legend()
plt.grid(True)
plt.show()

### Q3.5 

# Put your code here 
#5. Analysis of the Fit
'''To determine if the fit is perfect or if there are issues, visually inspect the plot and check if the fitted curve follows the data closely. If there are noticeable discrepancies:

Model Limitations: The power-law model may not capture all nuances of the data.
Measurement Errors: Data might have noise or measurement errors affecting the fit.
Non-ideal Behavior: Real-world components may not perfectly follow theoretical models.
Complete Code
Here's the entire process encapsulated in a script:
'''

import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Load and preprocess data
data = pd.read_csv('data2.csv', header=None)
current_mA = data[0]
voltage_V = data[1]
current_A = current_mA / 1000

# Plot data
plt.figure(figsize=(8, 6))
plt.scatter(current_mA, voltage_V, color='blue', label='Data')
plt.xlabel('Current (mA)')
plt.ylabel('Voltage (V)')
plt.title('Current vs Voltage')
plt.legend()
plt.grid(True)
plt.show()

# Define power law model
def power_law_model(current, alpha, beta):
    return alpha * current**beta

# Fit the model to the data
popt, pcov = curve_fit(power_law_model, current_A, voltage_V, p0=[1, 1])
alpha_best, beta_best = popt
print(f"Best-fitting α: {alpha_best}")
print(f"Best-fitting β: {beta_best}")

# Plot the data with the fitted curve
current_fit = np.linspace(min(current_A), max(current_A), 500)
voltage_fit = power_law_model(current_fit, alpha_best, beta_best)

plt.figure(figsize=(8, 6))
plt.scatter(current_mA, voltage_V, color='blue', label='Data')
plt.plot(current_fit * 1000, voltage_fit, color='red', label='Fitted Curve')
plt.xlabel('Current (mA)')
plt.ylabel('Voltage (V)')
plt.title('Current vs Voltage with Fitted Power Law Curve')
plt.legend()
plt.grid(True)
plt.show()

### Q3.6 

### This question is written only, no code required.
''' 
6. Consider Data Quality
Sometimes, the fit may be affected by the quality of data:
Ensure data accuracy and consistency.
Use more data if available to improve fit reliability.
As the current that passes through a light bulb is increased.
'''

################################################################################################################################################################

### Question 4 ###

################################################################################################################################################################

### Q4.1 

# Put your code here 
import numpy as np

# Load the signal data from the provided text file
file_path = 'signal.txt'  # Update with the correct path
signal_data = np.loadtxt(file_path)

# Step 2: Split the data into segments of 1000 samples each
segments = np.split(signal_data, len(signal_data) // 1000)

# Step 3: Identify the peak amplitude in each 1000-sample segment
peak_amplitudes = [np.max(np.abs(segment)) for segment in segments]

# Provided amplitude to character mapping
amplitude_to_char = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
    20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' ',
    33: '0', 34: '1', 35: '2', 36: '3', 37: '4', 38: '5', 39: '6', 40: '7', 41: '8', 42: '9',
    43: 'A', 44: 'B', 45: 'C', 46: 'D', 47: 'E', 48: 'F', 49: 'G', 50: 'H', 51: 'I',
    52: 'J', 53: 'K', 54: 'L', 55: 'M', 56: 'N', 57: 'O', 58: 'P', 59: 'Q', 60: 'R',
    61: 'S', 62: 'T', 63: 'U', 64: 'V', 65: 'W', 66: 'X', 67: 'Y', 68: 'Z'
}

# Round the peak amplitudes to match the table
rounded_amplitudes = [round(amp) for amp in peak_amplitudes]

# Step 4: Map the rounded amplitudes to their corresponding characters
decoded_amplitude_message = ''.join([amplitude_to_char.get(amp, '?') for amp in rounded_amplitudes])

print("Decoded Amplitude Message:", decoded_amplitude_message)


### Q4.2 

# Put your code here 
import numpy as np
from scipy.fft import fft

# Load the signal data from the provided text file
signal_data = np.loadtxt("signal.txt")

# Define the number of samples per segment
samples_per_segment = 1000

# Split the signal data into segments of 1000 samples each
segments = [signal_data[i:i + samples_per_segment] for i in range(0, len(signal_data), samples_per_segment)]

# Frequency Table (Provided in your assignment)
Frequency_to_char = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
    21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' ', 33: '0', 34: '1', 35: '2',
    36: '3', 37: '4', 38: '5', 39: '6', 40: '7', 41: '8', 42: '9', 43: 'A', 44: 'B', 45: 'C',
    46: 'D', 47: 'E', 48: 'F', 49: 'G', 50: 'H', 51: 'I', 52: 'J', 53: 'K', 54: 'L', 55: 'M',
    56: 'N', 57: 'O', 58: 'P', 59: 'Q', 60: 'R', 61: 'S', 62: 'T', 63: 'U', 64: 'V', 65: 'W',
    66: 'X', 67: 'Y', 68: 'Z'
}

# Decode the Frequency-based message
Frequency_message = ""
for i, segment in enumerate(segments):
    peak_Frequency = int(np.max(np.abs(segment)))  # Get the peak amplitude in the segment
    char = Frequency_to_char.get(peak_Frequency, '?')
    Frequency_message += char
    print(f"Segment {i}: Peak Frequency = {peak_Frequency}, Mapped Character = {char}")

print("Decoded Frequency-Based Message:")
print(Frequency_message)
################################################################################################################################################################

################################################################################################################################################################
