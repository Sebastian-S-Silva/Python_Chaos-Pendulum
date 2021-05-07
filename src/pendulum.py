import numpy as np
import pygame as pg
from scipy.integrate import odeint

class Pendulum():


	def __init__(self, length: float, mass: float = 1, start_angle: float, friction: float = 0):
		"""
		initialize a single point pendulum.
		"""
		self.start_angle = start_angle
		self.position = 
		self.length = length
		self.mass = mass
		self.friction = friction

	def physics(y, t, b, c):
		theta, omega = y
		dydt = [omega, -b*omega - c*np.sin(theta)]
		
		return dydt


	def simulate(self, time):
		y_start = [np.pi/2, 0]
		b = 0
		c = 9.81
		solutions = odeint(self.physics, y_start, time, args = (b, c))

		return solutions



