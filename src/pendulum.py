import numpy as np
import pygame as pg
from scipy.integrate import odeint

class Pendulum():


	def __init__(self, length: float, start_angle: float, mass: float = 1, friction: float = 0):
		"""
		initialize a single point pendulum.
		"""
		self.start_angle = start_angle
		self.length = length
		self.mass = mass
		self.friction = friction
		
	# @staticmethod
	def physics(self, y, t, b, c):
		theta, omega = y
		dydt = [omega, -b*omega - c*np.sin(theta)]
		
		return dydt


	def simulate(self, time):
		y_start = [np.pi/2, 0.0]
		b = 10.0
		c = 9.81
		solutions = odeint(self.physics, y_start, time, args=(b, c))

		return solutions



