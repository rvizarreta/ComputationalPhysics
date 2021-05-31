#!/usr/bin/env python
# coding: utf-8

import numpy as np
import math
from scipy.constants import epsilon_0

# DEFINING A FUNCTION THAT RETURNS THE LAST DISTANCE BETWEEN TWO PARTICLES
def distance(particle1, particle2):
    pos1 = particle1.getPositions()[-1]
    pos2 = particle2.getPositions()[-1] 
    return np.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

# DEFINING A FUNCTION THAT RETURNS THE IMPACT PARAMETER b IN METERS FROM THE RANGE a,b
b = lambda a,b : np.random.rand()*(b-a)

# DEFINING A FUNCTION FOR dv_x/dt
f_vx = lambda q, targetCharge, x, y, m : (1/(4*np.pi*epsilon_0*m))*(q*targetCharge/(x**2+y**2)**3/2)*x

# DEFINING A FUNCTION FOR dv_y/dt
f_vy = lambda q, targetCharge, x, y, m :(1/(4*np.pi*epsilon_0*m))*(q*targetCharge/(x**2+y**2)**3/2)*y

# DEFINING A FUNCTION FOR dx/dt
f_x = lambda vx : vx

# DEFINING A FUNCTION FOR dy/dt
f_y = lambda vy : vy

# DEFINING A FUNCTION THAT CALCULATES x(t+h) USING RUNGE-KUTTA 4rd ORDER METHOD
def function(data,q, targetCharge, r, m):
    vx, vy, x, y = data[0], data[1], data[2], data[3]
    return np.array([f_vx(q, targetCharge, x,y, m), f_vy(q, targetCharge, x, y, m), f_x(vx), f_y(vy)], float)


# DEFINING THE 4TH ORDER RUNGE-KUTTA METHOD
def rk4(data,q, targetCharge, r, m,h):
    k1 = h*function(data,q, targetCharge, r, m) 
    k2 = h*function(data+0.5*k1,q, targetCharge, r, m)
    k3 = h*function(data+0.5*k2,q, targetCharge, r, m)
    k4 = h*function(data+k3,q, targetCharge, r, m)
    data += (1/6)*(k1+2*k2+2*k3+k4)
    return data

# DEFINING A FUNCTION THAT SIMULATES THE RUTHERFORD SCATTERING 
def rutherford(particles, target,t1,t2,h):
    for particle in particles:
        vx = particle.initVel()
        vy = 0
        coord = particle.getPositions()
        x, y = coord[0][0], coord[0][1]
        data = np.array([vx, vy, x, y], float)
        for t in np.arange(t1+h,t2,h):
            data = rk4(data,particle.getCharge(),target.getCharge(),distance(particle,target),particle.getMass(),h)
            particle.savePosition(np.array([data[2],data[3]]))
        particle.saveScatteringAngle(calculateScatteringAngle(particle))
    return particles

# DEFINING A FUNCTION THAT CALCULATES THE SCATTERING ANGLE
def calculateScatteringAngle(particle):
    pos1 = particle.getPositions()[-1]
    pos2 = particle.getPositions()[-2]
    x1, y1 = pos1[0], pos1[1]
    x2, y2 = pos2[0], pos2[1]
    return np.arctan2(y2-y1,x2-x1)


