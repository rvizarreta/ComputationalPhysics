#!/usr/bin/env python
# coding: utf-8

# In[2]:


# DECLARING REQUIRED PACKAGES
import numpy as np
import math
from scipy.constants import e, m_p

# DELCARING THE CLASS Particle
from particle import Particle

# DECLARING OUR methods FILE
import methods

# DECLARING OUR 2D-Plotter FILE
import plotter


# In[3]:


#============ FIXED ENERGY OF 200 eV: 2D PLOT ==============


# In[66]:


# DECLARING AN ARRAY TO STORAGE OUR PARTICLES
particles = []
n = 10 #Number of test particles / 2

# ALPHA PARTICLE INFORMATION
m = 2*m_p
q = 2*e
E = 200 #eV

# RANGE OF POSITIONS FOR THE IMPACT PARAMETER b
y0 = 50e-4
y1 = 100e-4

# INITIAL HORIZONTAL DISTANCE TO THE PARTICLES AND THE TARGET
d = -0.02 #meters


# In[67]:


# INSTANCING OUR 20 PARTICLES
for i in range(n):
    b1 = methods.b(y0,y1)
    b2 = - b1
    particles.append(Particle(m,q,[d,b1],E,b1))
    particles.append(Particle(m,q,[d,b2],E,b2))


# In[68]:


# INSTANCING THE TARGET GOLD NUCLEUS AT THE ORIGIN
target = Particle(79*m_p,79*e,[0,0],0,0)


# In[69]:


# DEFINING INITIAL PARAMETERS FOR RK4
t1, t2, steps = 0, 0.00000018, 10000
h = abs(t2-t1)/steps


# In[70]:


# MOVING THE PARTICLES USING RK4 METHOD
particles = methods.rutherford(particles, target,t1,t2,h)


# In[71]:


#plotter.xyPlot(particles,target.getPositions())
plotter.trajectoryPlot(particles,target.getPositions())


# In[ ]:




