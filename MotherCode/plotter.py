#!/usr/bin/env python
# coding: utf-8

# DECLARING REQUIRED PACKAGES
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import e
from IPython import display
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import Label, LabelSet
#output_notebook()

# DEFINING A FUNCTION THAT SHOWS A 2D XY PLOT USING MATPLOTLIB
def xyPlot(particles,target_pos):
    plt.scatter(target_pos[:,0], target_pos[:,1], s=20, c='r', marker="o")
    for particle in particles:
        rgb = np.random.rand(3,)
        positions = particle.getPositions()
        plt.scatter(positions[:,0], positions[:,1], s=1, c=rgb, marker=".")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title('Rutherford Scattering 2D representation')
    #plt.xlim([-0.2,0.2])
    #plt.ylim([0,0.1e-20])
    plt.show()

# DEFINING A FUNCTION THAT SHOWS A 2D XY PLOT USING BOKEH LIBRARY
def trajectoryPlot(particles, target_pos):
    p = figure(title="Rutherford Scattering 2D Representation", x_axis_label='X(m)', y_axis_label='Y(m)')
    p.circle_x(target_pos[:,0], target_pos[:,1], size=20, color="black", alpha=0.5)
    for particle in particles:
        positions = particle.getPositions()
        p.line(positions[:,0], positions[:,1], line_width=2, color=particle.getColor())
    citation = Label(x=395, y=225, x_units='screen', y_units='screen',
                 text='Gold Nucleus', render_mode='css',
                 background_fill_color='white', background_fill_alpha=1.0)
    p.add_layout(citation)
    show(p)

# DEFINING A FUNCTION THAT SHOWS A 2D XY PLOT FOR A UNIFORM DISTRIBUTION OF ENERGIES
def trajectoryPlot2(particles, target_pos):
    p = figure(title="Rutherford Scattering 2D Representation for uniform distribution of energies", x_axis_label='X(m)', y_axis_label='Y(m)')
    p.circle_x(target_pos[:,0], target_pos[:,1], size=20, color="black", alpha=0.5)
    for particle in particles:
        positions = particle.getPositions()
        energy = str(round(particle.getEnergy()/e,1))
        angle = str(round(particle.getScatteringAngle()*180/np.pi+180 ,1))
        p.line(positions[:,0], positions[:,1], line_width=2, color=particle.getColor(), legend_label = energy + ' eV • θ = ' + angle + '°')
    p.legend.location = "top_right"
    show(p)

# DEFINING A FUNCTION THAT GENERATES AN ANIMATION OF THE SCATTERING PROCESS
def animation(particles, target, steps):
    fig1 = plt.figure()
    positionTarget = target.getPositions()

    for i in range(steps):
        plt.title('Rutherford Scattering')
        plt.xlim([-0.02, 0.0025])
        plt.ylim([-0.01, 0.01])
        for particle in particles:
            positions = particle.getPositions()[i,:]
            plt.plot(positionTarget[0,0], positionTarget[0,1], 'o', color='black', markersize = 10)
            plt.plot(positions[0], positions[1], 'o', color=particle.getColorRGBA(), markersize = 3)
        display.clear_output(wait=True)
        display.display(plt.gcf())
        plt.clf()
    plt.clf()
