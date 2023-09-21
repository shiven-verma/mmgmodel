import numpy as np
from math import pi,sqrt,sin,cos
import matplotlib.pyplot as plt
from matplotlib import animation
from __init__ import circle

c = circle()

xp = c.xp
yp = c.yp
xs = c.xs
ys = c.ys

######################################################
#  Choose which manuevering turn you want to plot    #
#  1 -> Port or 2 -> Starboard                       #
#  'Name' is the name of the animation               #
#  file format will be in gif, you can change        #
#  it to webm or change the encoder for more formats #
######################################################

turn = 1
Name = "PortSideTurn.gif"
if turn == 1:
    a = [-3.5,0.5]
    x0 = xp
    y0 = yp
else:
    a = [-0.5,3.5]
    x0 = xs
    y0 = ys




def transform(ar,tr,theta):
    if type(tr)==list:
        pass
    else:
        raise TypeError("tr should be a list containing coordinates")
    theta = theta*pi/180
    rot = np.array([[cos(theta),sin(theta)],[-sin(theta),cos(theta)]])
    return ar@rot+tr

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

points = np.array([[-0.25,0.06],[0.15,0.10],[0.28,0],[0.15,-0.10],[-0.25,-0.06],[-0.25,0.06]])

ax = plt.axes(xlim=a, ylim=[0, 3.5],)
patch = plt.Polygon(points,fill = None,edgecolor='r')

line, = ax.plot([], [], lw = 2)

xdata = []
ydata = []

def init():
    patch.set_xy(points)
    ax.add_patch(patch)
    line.set_data([], [])
    return line, patch,

def animate(i):
    i = i*1330
    if i==0:
        x = 0.00001
        x_prev = 0
        y_prev = 0
    else:
        x = y0[i]
        x_prev = y0[i-1]
        y_prev = x0[i-1]
        
    
    #xy = patch.get_xy()
#     y = 2+2*sin(x)
#     y_prev = 2+2*sin(x_prev)
    y = x0[i]
    
    ydif = (y-y_prev)
    xdif = x-x_prev
    theta = (np.arctan2((ydif),(xdif)))*180/pi
    poin = transform(points,[x,y],theta)
    patch.set_xy(poin)
    xdata.append(x) 
    ydata.append(y) 
    line.set_data(xdata, ydata)
    return patch, line
plt.grid()

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=120, 
                               interval=20,
                               blit=True)

anim.save(Name, writer = 'pillow', fps = 20)


