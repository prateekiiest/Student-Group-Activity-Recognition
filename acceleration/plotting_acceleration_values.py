#Reading Accelerometer values

%matplotlib inline
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from statsmodels.nonparametric.smoothers_lowess import lowess
from sklearn import preprocessing
import numpy as np

fil = open('pr.txt')

lines = []
lines.append(fil.readlines())

# dividing one minute into 4 parts
timedict = {'00': 0, '15' : 1, '30' : 2, '45' :3}


string = '23:Mon May' # Search for this string as the file contains acceleration values where this string is present
accel = []
accely = []
accelz = []
timelist = []
for i in range(len(lines[0])):
    if(lines[0][i][0:2] == '2:'): # acceleration along x axis has id 2:
        for k in range(len(lines[0][i]) - 10):
            if(string == lines[0][i][k:k+10]):
                z = (lines[0][i][k+14:k+10+12])  # if 2: found extract the time from that line
                exp = timedict[z[6:8]] + (4 * int(z[3:5])) + (4 * 60 * int(z[0:2]))
                timelist.append(exp)
                #print(exp)
                j = 3
                while(lines[0][i][j] != ','):  # Example 2: some x value, 3: some y value, 4: some z value
                    j += 1
                accel.append(lines[0][i][2:j-1]) # so till a ',' is found starting from 2: we are actually looking at 3: value
        
                l =j + 2
                while(lines[0][i][l] != ','):
                    l+=1
                accely.append(lines[0][i][j+3:l])
        
                v = l+3
                while(lines[0][i][v] != ','):
                    v+=1
                accelz.append(lines[0][i][l+3:v])
                p = timelist
        


acceleration_x = []

for k in range(len(accel)):
    acceleration_x.append(float(accel[k]))  # acceleration values along x axis


acceleration_y = []

for k in range(len(accely)):
    acceleration_y.append(float(accely[k]))  # acceleration values along y axis

acceleration_z = []
for k in range(len(accely)):
    acceleration_z.append(float(accelz[k]))  # acceleration values along z axis

tim = []
for k in range(len(p)):
    tim.append(p[k])  # appending time values at which acceleration values were found
    
x_axis = [timelist[b] for b in range(len(tim))]
y_axis = [acceleration_x[b] for b in range(len(acceleration_x))]
y_axis2 = [acceleration_y[b] for b in range(len(acceleration_y))]
y_axis3 = [acceleration_z[b] for b in range(len(acceleration_z))]


x_ax = [m for m in range(5760)]
y_ax = [0 for m in range(5760)]
y_ax2 = [0 for m in range(5760)]
y_ax3 = [0 for m in range(5760)]


for r in range(len(timelist)):
    y_ax[timelist[r]] = acceleration_x[r]


for r in range(len(timelist)):
    y_ax2[timelist[r]] = acceleration_y[r]

for r in range(len(timelist)):
    y_ax3[timelist[r]] = acceleration_z[r]

    
## Plotting acceleration values along 3 axes.    
    
plt.title('For acceleration along X axis')
plt.plot(x_ax, y_ax, '-') 
plt.xlabel('Time')
plt.ylabel('Magnitude of Acceleration')
plt.show()

plt.title('For acceleration along Y axis')
plt.plot(x_ax, y_ax2, '-') 
plt.xlabel('Time')
plt.ylabel('Magnitude of Acceleration')
plt.show()

plt.title('For acceleration along Z axis')
plt.plot(x_ax, y_ax3, '-') 
plt.xlabel('Time')
plt.ylabel('Magnitude of Acceleration')
plt.show()    


## Normalize

X_scale = preprocessing.scale(x_ax)   # Normalizing acceleration value for time axis
Y_scale = preprocessing.scale(y_ax)  # Normalizing acceleration value for x axis

Y_scale2 = preprocessing.scale(y_ax2)   # Normalizing acceleration value for y axis
Y_scale3 = preprocessing.scale(y_ax3)    # Normalizing acceleration value for z axis

def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    r"""Smooth (and optionally differentiate) data with a Savitzky-Golay filter.
    The Savitzky-Golay filter removes high frequency noise from data.
    It has the advantage of preserving the original shape and
    features of the signal better than other types of filtering
    approaches, such as moving averages techniques.
    Parameters
    ----------
    y : array_like, shape (N,)
        the values of the time history of the signal.
    window_size : int
        the length of the window. Must be an odd integer number.
    order : int
        the order of the polynomial used in the filtering.
        Must be less then `window_size` - 1.
    deriv: int
        the order of the derivative to compute (default = 0 means only smoothing)
    Returns
    -------
    ys : ndarray, shape (N)
        the smoothed signal (or it's n-th derivative).
    Notes
    -----
    The Savitzky-Golay is a type of low-pass filter, particularly
    suited for smoothing noisy data. The main idea behind this
    approach is to make for each point a least-square fit with a
    polynomial of high order over a odd-sized window centered at
    the point.
     """
    
    from math import factorial

    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError, msg:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')


xhat = savitzky_golay(Y_scale, 111, 10) # window size 111, polynomial order
yhat = savitzky_golay(Y_scale2, 111, 10)
zhat = savitzky_golay(Y_scale3, 111, 10)

# Plotting the acceleration values bu smoothing data

plt.title('For acceleration along X axis')
plt.plot(X_scale,xhat,'r')
plt.xlabel('Time')
plt.ylabel('Magnitude of Acceleration')
plt.show()



plt.title('For acceleration along Y axis')
plt.plot(X_scale,yhat,'r')
plt.xlabel('Time')
plt.ylabel('Magnitude of Acceleration')
plt.show()


plt.title('For acceleration along Z axis')
plt.plot(X_scale,zhat,'r')
plt.xlabel('Time')
plt.ylabel('Magnitude of Acceleration')
plt.show()


