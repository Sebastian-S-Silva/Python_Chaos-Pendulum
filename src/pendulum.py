import numpy as np
import pygame as pg
from scipy.integrate import odeint
import math

from sys import exit

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
		y_start = [self.start_angle, 0.0]
		b = 10.0
		c = 9.81
		self.solutions = odeint(self.physics, y_start, time, args=(b, c))


	def draw_P(self):
		pg.init()
		
		# window setup
		self.screen = pg.display.set_mode((800, 600))
		pg.display.set_caption('Chaos Pendulum')
		icon = pg.image.load('img\pendulum.png')
		pg.display.set_icon(icon)
		clock = pg.time.Clock()

		moment = 0

		running = True
		while running:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					exit()
			self.screen.fill((1, 1, 1))

			pg.draw.circle(self.screen, (255, 255, 255), (400, 150), 25)
			pg.draw.line(self.screen, (255, 255, 255), (400, 150), (400, 450), 6)
			pg.draw.line(self.screen, (255, 255, 255), (360, 450), (440, 450), 8)



			pg.draw.line(self.screen, (0, 100, 0), (400, 150), ((self.length*math.sin(self.solutions[moment][0]) + 400), (self.length*math.cos(self.solutions[moment][0]) + 150)), 6)

			if moment < (len(self.solutions)-1):
				moment += 1

			pg.display.update()
			clock.tick(60)

			

		