from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

from dynamics_circle import _mmgder
from params import fsparam

p = fsparam()

Lpp = p.Lpp
Np = p.Np

X0 = [7.97319,0,0,0,0,0,0,Np]
funcp = lambda t,x:_mmgder(t,x,-35)
funcs = lambda t,x:_mmgder(t,x,35)
Tmax = 1600
tspan = [0,Tmax]
t_eval = np.arange(0,Tmax,0.01)


sol_port = solve_ivp(funcp,tspan,X0,t_eval=t_eval)
sol_stbd = solve_ivp(funcs,tspan,X0,t_eval=t_eval)


x_port = sol_port.y[3,:]/Lpp
y_port = sol_port.y[4,:]/Lpp

x_stbd = sol_stbd.y[3,:]/Lpp
y_stbd = sol_stbd.y[4,:]/Lpp

class circle():
    def __init__(self):
        self.xp = x_port
        self.yp = y_port
        self.xs = x_stbd
        self.ys = y_stbd


u = sol_port.y[0,:]/p.U0
v = sol_port.y[1,:]



t = t_eval


plt.figure(1)
plt.plot(y_port,x_port)
plt.plot(y_stbd,x_stbd)

plt.xlabel("y")
plt.ylabel("x")
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.grid()
plt.show()

plt.figure(2)
plt.plot(t,u)
plt.xlabel("t")
plt.ylabel("u")



plt.grid()
plt.show()