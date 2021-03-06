from visual import * 
from math import sin, cos 
import numpy as np 

# ------------------------------Parameters-----------------------------------
# User inputs
velocityVector = vector(50,50,10) # input initial velocity of ball
angularVelocityVector = vector(1, 1, 0)
# Constant parameters
dt = .0001                # time step 
g  = 9.81                 # acceleration due to gravity in m/s^2
m  = 0.145                # baseball mass in kg
Cd = 0.29                 # drag coefficient Cd
rho= 0.9846               # density of air in kg/m^3
D  = 7.45/100.0           # baseball diameter in m
R  = D/2                  # baseball radius in m
A  = pi*(R**2)            # baseball cross-sectional area in m^2
Dm = .00065               # coefficient for Magnus force 
t  = np.linspace(0,dt,5)  # vector of times
N  = np.vectorize(t)      # number of time steps

#----------------------------Interface-----------------------------------------------
# Set up the display window
scenel= display(title= "Baseball Simulation",
	x=0, y=0, width=1000, height=1000, 
	range=5, backgound=color.black, 
	center= (0, 0.8, 0))

#create our objects 
ball = sphere(pos=(2, 1, 2), radius=R, color= color.white, make_trail=true)
floor= box(pos=(0, 0, 0), size=(5, 0.01, 5), color=color.green)

#----------------------------Functions----------------------------------------------
#function to compute acceleration given velocity
def acceleration(v,Cd,rho,A,m,g,Dm,w):
	InitialVelocity= vector(v[0], v[1], v[2])
	InitialVelocityMagnitude= mag(InitialVelocity)

	Magnus= m*Dm*cross(w,v)
	ForceVector = (-0.5*Cd*rho*A*InitialVelocityMagnitude*v[0] + Magnus[0], 
		-0.5*Cd*rho*A*InitialVelocityMagnitude*v[1] + Magnus[1], 
		-0.5*Cd*rho*A*InitialVelocityMagnitude*v[2] - m*g + Magnus[2])

	accel = vector(ForceVector[0]/m,ForceVector[1]/m,ForceVector[2]/m)

	return accel
#---------------------------Algorithm------------------------------------------------------------

accelerationVector= acceleration(velocityVector,Cd,rho,A,m,g,Dm,angularVelocityVector)

#This loop puts it in to motion 
while True:
		rate(10) # speeds it up 
		velocityVector=velocityVector+accelerationVector
		ball.pos+=velocityVector*dt
		print(ball.pos)
		if ball.y<0: # when ball hits the ground...
			print "ball.pos=", ball1.pos, "t=" , t
			break
		
		t+=dt



