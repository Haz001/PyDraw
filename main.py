import pygame
import sys
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((512,512))
pxl = 8
class color(object):
	red = 0
	green = 0
	blue = 0
	def __init__(self,red,green,blue):
		self.red = red
		self.green = green
		self.blue = blue


class grid(object):
	grid = {}
	def __init__(self,width,height,c):
		for x in range(width):
			for y in range(height):
				self.grid[str(x)+","+str(y)] = c
	def get(self,x,y):
		if (self.grid[str(x)+","+str(y)] != None):
			return self.grid[str(x)+","+str(y)]
	def get_tuple(self,x,y):
		if (self.grid[str(x)+","+str(y)] != None):
			c =  self.grid[str(x)+","+str(y)]
			return (c.red,c.green,c.blue)
	def set(self,x,y,c):
		self.grid[str(x)+","+str(y)] = c
g = grid(1000,1000,color(0,0,0))
cps = [color(255,255,255),color(255,0,0),color(0,255,0),color(255,255,0),color(0,0,255),color(255,0,255),color(0,255,255),color(255,255,255)]
while True:

	for event in pygame.event.get():
		if event.type == (pygame.QUIT):
			print("Exiting!")
			sys.exit()
			quit()


		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print(event.pos)
				if(event.pos[0] <= 512-pxl):
					if(event.pos[1] <= 512):
						print("set")
						print(str(int(event.pos[0]/32))+", "+str(int(event.pos[1]/32)))
						g.set(int(event.pos[0]/pxl),int(event.pos[1]/pxl),color(255,255,255))
	for x in range(int(512/pxl)-1):
		for y in range(int(512/pxl)):
			c = g.get_tuple(x,y)
			pygame.draw.rect(screen, c, pygame.Rect(x*pxl,y*pxl,1*pxl,1*pxl))

	c = 0
	for x in range(int(pxl/8)):
		for y in range(int(512/pxl)):
			c+=1
			if c in range(len(cps)):
				pygame.draw.rect(screen,(cps[c].red,cps[c].green,cps[c].blue) , pygame.Rect(512-pxl,y*pxl,1*pxl,1*pxl))


	pygame.display.update()
	#print("update")
