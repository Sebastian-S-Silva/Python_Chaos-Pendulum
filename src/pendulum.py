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
		y_start = [np.pi/2, 0.0]
		b = 10.0
		c = 9.81
		solutions = odeint(self.physics, y_start, time, args=(b, c))

		return solutions

	def draw_P(self):
		pg.init()
		
		# window setup
		self.screen = pg.display.set_mode((800, 600))
		pg.display.set_caption('Chaos Pendulum')
		icon = pg.image.load('img\pendulum.png')
		pg.display.set_icon(icon)
		clock = pg.time.Clock()

		pend_end_x = 100
		pend_end_y = 100

		angle = 0

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



			pg.draw.line(self.screen, (0, 100, 0), (400, 150), (pend_end_x*math.cos(angle) + 400, pend_end_y*math.sin(angle) + 150), 6)

			angle += 0.01

			pg.display.update()
			clock.tick(120)

		