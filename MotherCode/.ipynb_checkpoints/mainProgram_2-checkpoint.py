#!/usr/bin/env python
# coding: utf-8

# In[11]:


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


# In[12]:


#============ FIXED ENERGY OF 200 eV: 2D ANIMATION ==============


# In[13]:


# DECLARING AN ARRAY TO STORAGE OUR PARTICLES
particles = []
n = 5 #Number of test particles / 2

# ALPHA PARTICLE INFORMATION
m = 2*m_p
q = 2*e
E = 200 #eV

# RANGE OF POSITIONS FOR THE IMPACT PARAMETER b
y0 = 50e-4
y1 = 100e-4

# INITIAL HORIZONTAL DISTANCE TO THE PARTICLES AND THE TARGET
d = -0.02 #meters


# In[14]:


# INSTANCING OUR 10 PARTICLES
for i in range(n):
    b1 = methods.b(y0,y1)
    b2 = - b1
    particles.append(Particle(m,q,[d,b1],E,b1))
    particles.append(Particle(m,q,[d,b2],E,b2))


# In[15]:


# INSTANCING THE TARGET GOLD NUCLEUS AT THE ORIGIN
target = Particle(79*m_p,79*e,[0,0],0,0)


# In[16]:


# DEFINING INITIAL PARAMETERS FOR RK4
t1, t2, steps = 0, 0.00000018, 10000
h = abs(t2-t1)/steps


# In[17]:


# MOVING THE PARTICLES USING RK4 METHOD
particles = methods.rutherford(particles, target,t1,t2,h)


# In[18]:


# GENERATING THE ANIMATION
plotter.animation(particles, target, steps)


# In[ ]:




