#!/usr/bin/env python
# coding: utf-8

import numpy as np
from scipy.constants import e

class Particle:
        
    # DEFINING THE CONSTRUCTOR OF THE PARTICLE
    def __init__(self, mass, charge, position, energy, impactParameter):
        self.mass = mass #in Kg
        self.charge = charge #in Coulomb
        self.energy = energy*e #Changing from eV to Joules
        self.b = impactParameter # in meters
        self.positions = []
        self.positions.append(position)
        self.positions = np.array(self.positions)
        self.color = tuple(np.random.randint(255, size=3))
        self.colorRGBA = tuple(np.random.rand(3))

        
    # DEFINING get METHODS FOR THE INTRINSICAL ATTRIBUTES OF THE PARTICLE
    def getPositions(self):
        return self.positions

    def getMass(self):
        return self.mass
    
    def getCharge(self):
        return self.charge
    
    def getEnergy(self):
        return self.energy
    
    def getScatteringAngle(self):
        return self.scatteringAngle

    def getImpactParameter(self):
        return self.b
    
    def getColor(self):
        return self.color
    
    def getColorRGBA(self):
        return self.colorRGBA
    
    # DEFINING A METHOT THAT SETS THE SCATTERING ANGLE
    def saveScatteringAngle(self, angle):
        self.scatteringAngle = angle
    
    # DEFINING A METHOD THAT SAVES THE POSITION OF THE PARTICLE
    def savePosition(self, position):
        self.positions = np.append(self.positions, [position], axis=0)

    # DEFINING A METHOD THAT RETURNS THE INITIAL VELOCITY OF THE PARTICLE
    
    def initVel(self):
        return np.sqrt(2*self.energy/self.mass)



