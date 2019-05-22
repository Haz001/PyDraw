import pygame
import sys
pygame.init()
pygame.font.init()


pxl = 16
class color(object):
	red = 0
	green = 0
	blue = 0
	def __init__(self,red,green,blue):
		self.red = red
		self.green = green
		self.blue = blue

class win(object):
	scr = None
	width = 0
	height = 0
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.scr = pygame.display.set_mode((width,height))

	def drawrec(self,x,y,width,height,c):
		if str(type(c)) == "<class '__main__.color'>":
			col = (c.red,c.green,c.blue)

		elif str(type(c)) == "<class 'tuple'>":
			col = c
		else:
			col = (255,255,255)
		pygame.draw.rect(self.scr,col,pygame.Rect(x,y,width,height))
	def drawstring(self,string,x,y):
		font = pygame.font.SysFont('Monospace', 30)
		text = font.render(string, True, (10, 10, 10))
		self.scr.blit (text,(x,y))
scr = win(1000,700)
class grid(object):
	grid = {}
	fg = color(255,255,255)
	bg = color(255,255,255)
	width = 0
	height = 0
	def __init__(self,width,height,c):
		self.bg = c
		self.width = width
		self.height = height
		for x in range(width):
			for y in range(height):
				self.grid[str(x)+","+str(y)] = self.bg
	def get(self,x,y):
		if (self.grid[str(x)+","+str(y)] != None):
			return self.grid[str(x)+","+str(y)]
	def get_tuple(self,x,y):
		if (self.grid[str(x)+","+str(y)] != None):
			c =  self.grid[str(x)+","+str(y)]
			return (c.red,c.green,c.blue)
	def set(self,x,y,c):
		self.grid[str(x)+","+str(y)] = self.fg
g = grid(32,32,color(0,0,0))
cps = [color(255,255,255),color(0,0,0),color(255,0,0),color(0,255,0),color(0,0,255),color(255,255,0),color(0,255,255),color(255,0,255)]
class colors:
	cps0 = [color(160,160,160),color(0,72,184),color(8,48,224),color(88,24,216),color(160,8,168),color(208,0,88),color(208,16,0),color(160,32,0),color(8,88,0),color(0,104,0),color(0,104,16),color(0,96,112)]
	cps1 = [color(160,160,160),color(0,72,184),color(8,48,224),color(88,24,216),color(160,8,168),color(208,0,88),color(208,16,0),color(160,32,0),color(8,88,0),color(0,104,0),color(0,104,16),color(0,96,112)]
	cps2 = [color(160,160,160),color(0,72,184),color(8,48,224),color(88,24,216),color(160,8,168),color(208,0,88),color(208,16,0),color(160,32,0),color(8,88,0),color(0,104,0),color(0,104,16),color(0,96,112)]
	cps3 = [color(160,160,160),color(0,72,184),color(8,48,224),color(88,24,216),color(160,8,168),color(208,0,88),color(208,16,0),color(160,32,0),color(8,88,0),color(0,104,0),color(0,104,16),color(0,96,112)]
def settings():
	run = True
	scr = win(200,200)
	while run:
		for event in pygame.event.get():
			if event.type == (pygame.QUIT):
				run = False
		scr.drawrec(10,10,180,50,(168,182,165))
		scr.drawstring("Settings",10,10)
		pygame.display.update()
#settings()
scr = win(1000,700)
import time
t = time.time()
fps = []
while True:

	for event in pygame.event.get():
		if event.type == (pygame.QUIT):
			print("Exiting!")
			sys.exit()
			quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print(event.pos)
				if(event.pos[0] <= 512-8):
					if(event.pos[1] <= 512):
						print("Paint")
						print(str(int(event.pos[0]/32))+", "+str(int(event.pos[1]/32)))
						g.set(int(event.pos[0]/pxl),int(event.pos[1]/pxl),color(255,255,255))
				if(event.pos[0] >= scr.width-16):
					if(event.pos[1] <= scr.width):
						if (event.pos[1]/16 <= len(cps)):
							g.fg = cps[int(event.pos[1]/16)]
						else:
							g.fg = color(0,0,0)
			elif(event.button == 4):
				pxl = pxl*2
			elif(event.button == 5):
				if pxl > 1:
					pxl = pxl/2
			else:
				print (event.button)
	pygame.draw.rect(scr.scr,(35,39,42),pygame.Rect(0,0,scr.width,scr.height))
	for x in range(int(g.width)):
		for y in range(int(g.height)):
			c = g.get_tuple(x,y)
			scr.drawrec(x*pxl,y*pxl,1*pxl,1*pxl,c)

	c = 0
	for x in range(int(pxl/8)):
		for y in range(int(scr.width/8)):
			if c in range(len(cps)):
				scr.drawrec(scr.width-16,y*16,16,16,cps[c])

			c+=1

	pygame.display.update()
	#print("update")
