import pygame
from pygame.locals import *
from math import *
from random import *

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

w, h = 500, 500

fps = 50

screen = pygame.display.set_mode((w,h))

c = pygame.time.Clock()

class Bird():
	def __init__(self):
		self.x = 100
		self.y = 200
		self.w = 25
		self.h = 30
		self.gravity = 1
		self.velocity = 0
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
	def paint(self):
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
		self.velocity += self.gravity
		self.y += self.velocity
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			self.velocity = -10
		pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 20)
			
		
class Platform():
	def __init__(self, x):
		self.x = x
		self.h = randint(50, 300) #height
		self.w = 50  # width
		self.dx = -5
		self.dy = 0
		self.y = w - self.h
		self.rect = pygame.Rect(self.x, 0, self.w, self.h)
	
	def paint(self):
		self.rect = pygame.Rect(self.x, 0, self.w, self.h)
		self.rect2 = pygame.Rect(self.x, self.h + 150, self.w, 500 - (self.h+150))
		
		pygame.draw.rect(screen, (255, 255, 255), self.rect)
		pygame.draw.rect(screen, (255, 255, 255), self.rect2)
		self.x += self.dx
		self.y += self.dy

'''
class Platform2():
	def __init__(self, x):
		self.x = x
		self.h = randint(250, 450) #height
		self.w = 50  # width
		self.dx = -5
		self.dy = 0
		self.y = w - self.h
		self.rect = pygame.Rect(self.x, 0, self.w, 500)
	
	def paint(self):
		self.rect = pygame.Rect(self.x, self.y, self.w, 500)
		
		pygame.draw.rect(screen, (255, 255, 255), self.rect)
		self.x += self.dx
		self.y += self.dy
'''

class Main():
	def loop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			screen.fill((0, 0, 0))
			self.update()
			c.tick(fps)
			pygame.display.update()
	
	def update(self):
		textsurface = myfont.render('Score: ' + str(self.score), False, (255, 255, 255))
		screen.blit(textsurface,(0,0))
		if self.time % self.interval == 0 and self.interval > 0:
			self.p.append(Platform(w))
			#self.p.append(Platform2(w))
		self.b.paint() 
		for i in self.p:
			i.paint()
			if i.rect.colliderect(self.b.rect) or i.rect2.colliderect(self.b.rect) :
				pygame.quit()
				quit()
			if i.x == self.b.x:
				self.score+=1
		self.time += 1
		if self.b.y >= 500:
			pygame.quit()
			quit()
		

		
	def init(self):
		self.time = 0
		self.p = list()
		self.interval = 50
		self.b = Bird()
		self.score = 0
	
	def __init__(self):
		self.init()
		self.loop()
		
def main():
	a = Main()

if __name__ == "__main__":
	main()
