#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


#============ UNIFORM DISTRIBUTION OF ENERGIES: 2D PLOT ==============


# In[41]:


# DECLARING AN ARRAY TO STORAGE OUR PARTICLES
particles = []
n = 10 #Number of test particles 

# ALPHA PARTICLE INFORMATION
m = 2*m_p
q = 2*e
E = 200/n
#E_low, E_high = 0, 200 #eV

# RANGE OF POSITIONS FOR THE IMPACT PARAMETER b
y0 = 50e-4
y1 = 100e-4

# INITIAL HORIZONTAL DISTANCE TO THE PARTICLES AND THE TARGET
d = -0.02 #meters


# In[42]:


# INSTANCING OUR 10 PARTICLES
b = methods.b(y0,y1)
for i in range(n):
    particles.append(Particle(m,q,[d,b],E,b))
    E += 200/n


# In[43]:


# INSTANCING THE TARGET GOLD NUCLEUS AT THE ORIGIN
target = Particle(79*m_p,79*e,[0,0],0,0)


# In[44]:


# DEFINING INITIAL PARAMETERS FOR RK4
t1, t2, steps = 0, 0.000001, 10000
h = abs(t2-t1)/steps


# In[45]:


# MOVING THE PARTICLES USING RK4 METHOD
particles = methods.rutherford(particles, target,t1,t2,h)


# In[46]:


#plotter.xyPlot(particles,target.getPositions())
plotter.trajectoryPlot2(particles,target.getPositions())


# In[ ]:




