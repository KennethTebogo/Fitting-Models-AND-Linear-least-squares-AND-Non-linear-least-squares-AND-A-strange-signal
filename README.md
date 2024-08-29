#Question 1: Fitting models

Fitting a model to data is a crucial skill for any modern scientist. In this prac, we will explore methods of model
fitting starting with the least squares method.

This is a really great video explaining the method of least squares for a linear model: https://www.youtube.com/
watch?v=PaFPbb66DxQ. The method of least squares is just one method to fit a model to data (also known as curve
fitting or regression) and to estimate the value of the parameters of that model. Remember a lot of stuff you find
online will only be about the linear case and very few things follow straight lines in the real world! In this prac,
we will use python to fit complicated models to data very easily.
Watch the video, then give written answers for the questions below.

1. Why does minimising the sum of the residuals squared result in the best fitting model?
2. Linear least squares is easy because the parameters can be obtained analytically for any set of data. What
method(s) could you use to minimise the sum of the residuals squared for any arbitrary parametric model?
3. Give an example from physics of a model that has been fit to data (using least squares or some other method).
What are the parameters of that model (give the names or symbols not the values)? How are they estimated?
Computational Physics 322

#Question 2: Linear least squares

Imagine you find a resistor and don’t know its value. Well since you’re a physicist, you realise that it’s easy to
perform an experiment to figure it out! You apply a current to the resistor and measure the potential difference
across it. But you feel you should be a good physicist and take some repeat measurements at different values of
current to reliably estimate the resistance. You diligently record your data in a file (which I’ve provided) called
data1.csv which has the current (in mA) in the first column and the voltage (in V) in the second column. The goal
of this question is to use the method of linear least squares to determine the resistance, given this set of measured
current and voltage values.

1. Assume the readings of current are given by a set of values I1, I2 .... IN . These have corresponding voltages
V1, V2 .... VN . Use the method of linear least squares to derive an analytic expression for the resistance, R,
in terms of sums over Ik and Vk.
2. Now let’s get started with reading in the data. Numpy has a function called loadtxt which lets you read data
files. Look at the documentation for this function: https://numpy.org/doc/1.20/reference/generated/
numpy.loadtxt.html.

It might look confusing! But that’s because it’s a very flexible function. We’re going to need the keyword
‘delimiter’. This tells python when each element in the data are separated by. In this case, it’s a comma.
Make sure the data file is in the same directory where you are running your code. Use this line of code to
read the data in: current, voltage = np.loadtxt(’data1.csv’, delimiter=’,’, unpack=True)
You’ll see that this has read the data into two different arrays (of equal length), containing the current and
voltage values.

Make a plot with the current on the x axis and the voltage on the y axis. Be sure to label your axes correctly
and use points instead of lines. 

Make sure to comment your code and include your plot in your report!
4. Now that you’ve read in the current and voltage values, use the equation you derived in the first part of this
question to calculate the resistor value using the method of linear least squares. Make sure to include the
final answer for R in your report.

5. Most models you’ll be fitting to data will not be linear and probably won’t have an analytic solution. Fortunately, python has some powerful and easy to use numerical methods that can fit any kind of model to data.
You will now use one of these to solve the same problem numerically, and see if you get the same answer as
your analytic solution.

The function we will use is called curve_fit and you import it like this:
from scipy.optimize import curve_fit.
curve_fit essentially uses the method of least square numerically, by trying a set of values for the parameters,
evaluating the residuals between the model and the data, adjusting the parameter values and repeating the
evaluation. It uses a gradient descent algorithm to rapidly find the set of values of the model parameters
which minimise the sum of the least squares. You can read more about curve_fit in the documentation:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

To use curve_fit, you will have to write a function that implements Ohm’s law for any given value of current
and resistance. Note that this function must take the current as the first argument and the resistance as the
second since curve_fit assumes that the model’s first argument is the independent variable. You then pass
Computational Physics 322
this function, the x and y data (in this case the measured current and voltage) and an initial guess for the
resistance to curve_fit and it will return a list of the best-fitting parameters (although in this case, there’s
only one parameter). Use a value of 1Ω for the initial guess of the resistance.
Here’s a nice example of how to use curve_fit to help you get started:
https://www.datatechnotes.com/2020/09/curve-fitting-with-curve-fit-function-in-python.html
Be sure to include your well-commented code and the value of the resistance that you get in your report.

7. Make a plot of the data, using points, with the best-fitting model “overplotted” as a straight line. To do this,
you simply call plt.plot twice for the same figure, the first time plotting data and the second time plotting
the model for the same x-values. This should give you a quick visual indication of how well your model fits
your data.

#Question 3: Non-linear least squares

Some objects don’t follow Ohm’s law. In particular, as the current that passes through a light bulb is increased,
the light bulb gets hotter thus increasing its resistance. The file data2.csv contains more data1 , with the first
column as the current in mA and the second column as the voltage in volts. But if you plot this data, you’ll find
it is not linear. However it does appear to follow a power law relationship: V = αIβ
(1)
Where I is the current in amps (not mA). For this question, you will use python and least squares to find the
best-fitting values for α and β.

You might realise that you can in fact turn this equation into one that can be solved using linear least squares
by taking the log of both sides. You may solve this problem this way if you wish. However, you will only get
a maximum of 30 marks. To get full marks, you must use the non-linear form of the equation and curve_fit to
determine the best fitting values for α and β.

1. Start by reading in and plotting the data from data2.csv with the current in mA on the x-axis and the voltage
on the y-axis. Use points not lines in the plot.
2. Write a python function which implements the power law above. Your function should take the current (in
amps) as the first argument, and α and β as the second and third arguments and return the voltage. Test
your function for a current of 0.5 amps, α = 200, β = 3. You should get 25.00V.
3. Now use curve_fit to fit this function to the data and determine the best-fitting values for α and β. Remember
to convert to amps. You can use the starting values of [1,1] for the parameters. Be aware that the code
should look very similar to the previous question, but the use of curve_fit changes in a couple of small ways
when using a model with more than one parameter. Look at the documentation and examples online to help
you.
4. Report the best fitting values for α and β.
5. Make a plot of the data with the best-fitting curve overplotted.
6. Does it fit the data perfectly or do you notice any problems? If so, what could these by caused by?
1
If you’re interested, this data comes from a real paper which investigated the current-voltage relationship for several light bulbs.
I’m not sure why the authors thought this was interesting but I’m glad they did.
Computational Physics 322

#Question 4: A strange signal

I have provided you with a text file that contains a secret signal you need to decode. Every 1000 samples changes
amplitude, the peak of the signal within those 1000 samples corresponds to a letter (see the plot below).
At the end of this question, I have included tables that will help you match the amplitude to a letter (note that
amplitude 27 is a space).
1. Decode the secret signal hidden in the varying amplitude. Remember to include your well-commented code
and the final message that you decode.
2. I’ve also added a second hidden message in this signal: the frequency also changes every 1000 samples. Using
the Fast Fourier Transform or any other method, decode the message hidden in the frequency and write down
the message. 
