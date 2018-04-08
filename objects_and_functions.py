import numpy as np
import math

'''
Define the receiver class
'''
class receiver(object):

	'''Intializer
		Arguments are iself, the x, y, and z coordinates
	'''

	def __init__(self, name,x, y, z):
		self.name=name
		self.x = x
		self.y = y
		self.z = z

	def GetX(self):
		return self.x

	def GetY(self):
		return self.y

	def GetZ(self):
		return self.z

	def PrintCoords(self):
		x = self.GetX()
		y = self.GetY()
		z = self.GetZ()
		name = self.name
		print 'Ant %s (X,Y,Z): (%f,%f%f)'%(name,x,y,z)

'''
Define the emitter class
'''
class emitter(object):

	'''Initializer
		Arugments are itself, the theta, phi, and r
	'''

	def __init__(self, name,theta, phi, r):
		self.name=name
		self.theta = theta
		self.phi = phi
		self.r = r

	def GetX(self):
		return self.r * math.sin(math.radians(self.theta)) * math.cos(math.radians(self.phi))

	def GetY(self):
		return self.r * math.sin(math.radians(self.theta)) * math.sin(math.radians(self.phi))

	def GetZ(self):
		return self.r * math.cos(math.radians(self.theta))

	def PrintCoords(self):
		x = self.GetX()
		y = self.GetY()
		z = self.GetZ()
		name = self.name
		print 'Ant %s (X,Y,Z): (%f,%f%f)'%(name,x,y,z)

def dist(receiver, emitter):
	xdif = emitter.GetX()-receiver.GetX()
	ydif = emitter.GetY()-receiver.GetY()
	zdif = emitter.GetZ()-receiver.GetZ()
	dist = math.sqrt(xdif**2 + ydif**2 + zdif**2)
	return dist