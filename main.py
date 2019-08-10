#!/usr/bin/env python3
import pygame
import sys
pygame.init()
pygame.font.init()
def hello(args="None"):
	print("hello world!\nArgs: "+str(args))
pxl = 16
class color(object):
	red = 0
	green = 0
	blue = 0
	def __init__(self,red,green,blue):
		self.red = red
		self.green = green
		self.blue = blue
class win:
	class canvas(object):
		scr = None
		width = 0
		height = 0
		def __init__(self,width,height):
			self.width = width
			self.height = height
			self.scr = pygame.display.set_mode((width,height),pygame.RESIZABLE)
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
	class input:
		class btn(object):
			x = 0
			y = 0
			width = 0
			heigth = 0
			text = ""
			call = hello
			c = color(114,137,218)
			def __init__(self,x,y,width,height,text,call=hello,c=color(114,137,218)):
				self.x = x
				self.y = y
				self.width = width
				self.height = height
				self.text = text
				self.call = call
				self.c = c
			def check(self,pointer):
				if (pointer[0] >= self.x) and (pointer[0] <= self.x+self.width):
					if (pointer[1] >= self.y) and (pointer[1] <= self.y+self.height):
						self.call()
			def draw(self,can,xo = 0,yo = 0):
				can.drawrec(self.x+xo,self.y+yo,self.width,self.height,self.c)
				can.drawstring(self.text,self.x + xo,self.y + yo)
		class label(object):
			x = 0
			y = 0
			width = 0
			heigth = 0
			text = ""
			c = color(114,137,218)
			def __init__(self,x,y,width,height,text,c=color(114,137,218)):
				self.x = x
				self.y = y
				self.width = width
				self.height = height
				self.text = text

				self.c = c
			def check(self,pointer):
				print("¯\\_(ツ)_/¯")
			def draw(self,can,xo = 0,yo = 0):
				can.drawstring(self.text,self.x + xo,self.y + yo)

		class txtbox(object):
			x = 0
			y = 0
			width = 0
			heigth = 0
			text = ""
			c = color(114,137,218)
			def __init__(self,x,y,width,height,text,c=color(114,137,218)):
				self.x = x
				self.y = y
				self.width = width
				self.height = height
				self.text = text

				self.c = c
			def check(self,pointer):
				print("¯\\_(ツ)_/¯")
			def draw(self,can,xo = 0,yo = 0):
				can.drawstring(self.text,self.x + xo,self.y + yo)


	class opt(object):
		can = None
		x = 0
		y = 0
		height = 0
		width = 0
		items = []
		enabled = False
		name = ""
		def __init__(self,x,y,height,width,can,name):
			self.height = height
			self.width = width
			self.x = x
			self.y = y
			self.enabled = False
			self.can = can
			self.name = name
		def add(self,item):
			self.items.append(item)
		def draw(self):
			#print(self.name+" - "+str(self.enabled))
			if self.enabled:
				#print(self.name+" - draw")
				self.can.drawrec(self.x,self.y,self.width,self.height,color(44,47,51))
				for i in range(len(self.items)):
					self.items[i].draw(self.can,self.x,self.y+((self.items[i].height+2)*i))
		def check(self,pos):
			for i in range(len(self.items)):
				self.items[i].check([pos[0]-self.x,pos[1]-(self.y+((self.items[i].height+2)*i))])
class grid(object):
	paint = False
	grid = {}
	fg = color(255,255,255)
	bg = color(255,255,255)
	width = 0
	height = 0
	def __init__(self,width,height,c):
		self.grid = {}
		self.bg = c
		self.width = width
		self.height = height
		for x in range(width):
			for y in range(self.height):
				self.grid[str(x)+","+str(y)] = self.bg
	def get(self,x,y):
		if (self.grid[str(x)+","+str(y)] != None):
			return self.grid[str(x)+","+str(y)]
	def get_tuple(self,x,y):
		if (self.grid[str(x)+","+str(y)] != None):
			c =  self.grid[str(x)+","+str(y)]
			return (c.red,c.green,c.blue)
	def set(self,x,y):
		self.grid[str(x)+","+str(y)] = self.fg
	def setx(self,x,y,c):
		self.grid[str(x)+","+str(y)] = c
	def save(self,out):
		t = open(out+".pd",'wb')
		b = bytearray()
		b.append(0)
		b.append(self.width)
		b.append(self.height)
		for y in range(self.height):
			for x in range(self.width):
				c = self.get(x,y)
				b.append((c.red))
				b.append((c.green))
				b.append((c.blue))
		t.write(b)
		t.close()
		print('save')
	def read(self,out):
		t = open(out+".pd",'rb')
		data = bytearray(t.read())
		print(int(str(data[1]))+1)
		cou=3
		for y in range(self.height):
			for x in range(self.width):
				r = 0
				g = 0
				b = 0
				for c in range(3):
					if c == 0:
						r = int(data[cou])
					elif c == 1:
						g  = int(data[cou])
					elif c == 2:
						b = int(data[cou])
					cou+=1
				col=color(r,g,b)
				print(str(x)+","+str(y)+": "+str(r)+" - "+str(g)+" - "+str(b))
				self.setx(x,y,col)
		t.close()
		print('save')
cps = [color(255,255,255),color(0,0,0),color(255,0,0),color(0,255,0),color(0,0,255),color(255,255,0),color(0,255,255),color(255,0,255)]
class colors:
	cps0 = [color(72,72,72),color(0,8,88),color(0,8,120),color(0,8,128),color(56,0,80),color(88,0,16),color(88,0,0),color(64,0,0),color(16,0,0),color(0,24,0),color(0,30,0),color(0,30,0),color(0,24,32),color(0,0,0),color(0,0,0),color(0,0,0)]
	cps1 = [color(160,160,160),color(0,72,184),color(8,48,224),color(88,24,216),color(160,8,168),color(208,0,88),color(208,16,0),color(160,32,0),color(96,64,0),color(8,88,0),color(0,104,0),color(0,104,16),color(0,96,112),color(0,0,0),color(0,0,0),color(0,0,0)]
	cps2 = [color(248,248,248),color(32,160,248),color(80,120,248),color(152,104,248),color(248,104,248),color(248,112,176),color(248,112,104),color(248,128,24),color(192,152,0),color(112,176,0),color(40,192,32),color(0,200,112),color(0,192,208),color(0,0,0),color(0,0,0),color(0,0,0)]
	cps3 = [color(248,248,248),color(160,216,248),color(176,192,248),color(208,184,248),color(248,192,248),color(248,192,224),color(248,192,192),color(248,200,160),color(232,216,136),color(200,224,144),color(168,232,160),color(144,232,200),color(144,244,232),color(168,168,168),color(0,0,0),color(0,0,0)]
scr = win.canvas(1000,700)
class var:
	g = grid(4,4,color(0,0,0))
	settings = win.opt(scr.width/2-128,scr.height/2-128,256,256,scr,"Settings")
	custom = win.opt(scr.width/2-128,scr.height/2-128,256,256,scr,"Cool")
	save = win.opt(scr.width/2-128,scr.height/2-128,256,256,scr,"Save")
## button functions
class btnfunc:
	def c16():
		var.g = grid(16,16,color(0,0,0))
		var.settings.enabled = False
		print("16")
	def c32():
		var.g = grid(32,32,color(0,0,0))
		var.settings.enabled = False

		print("32")
	def c64():
		var.g = grid(64,64,color(0,0,0))
		var.settings.enabled = False

	def c128():
		var.g = grid(128,128,color(0,0,0))
		var.settings.enabled = False

		print("128")
	def c256():

		var.g = grid(256,256,color(0,0,0))
		var.settings.enabled = False

		print("256")

	def none():
		print("¯\_(ツ)_/¯")

class this:
	g = grid(4,4,color(0,0,0))
	click = False
	class settings:
		def setup():
			var.settings.items = []
			#form = win.opt(scr.width/2-128,scr.height/2-128,256,256,scr)
			var.settings.add(win.input.btn(0,0,256,32,"Create Custom",this.settings.cust ))
			var.settings.add(win.input.btn(0,0,256,32,"Create 16x16",btnfunc.c16 ))
			var.settings.add(win.input.btn(0,0,256,32,"Create 32x32",btnfunc.c32 ))
			var.settings.add(win.input.btn(0,0,256,32,"Create 64x64",btnfunc.c64 ))
			var.settings.add(win.input.btn(0,0,256,32,"Create 128x128",btnfunc.c128 ))
			var.settings.add(win.input.btn(0,0,256,32,"Create 256x256",btnfunc.c256 ))
			var.settings.enabled = False
		def cust():

#			this.custom.setup()

			var.settings.enabled = False
			var.custom.enabled = True
	class save:
		def setup():
			var.save.items = []
			var.save.add(win.input.btn(0,0,256,32,"New",this.save.new ))

			var.save.add(win.input.btn(0,0,256,32,"Save",btnfunc.none ))
			var.save.add(win.input.btn(0,0,256,32,"Open", btnfunc.none))
			var.save.add(win.input.btn(0,0,256,32,"Settings",btnfunc.none ))
			var.save.add(win.input.btn(0,0,256,32,"Close",this.save.close ))
			var.save.add(win.input.btn(0,0,256,32,"Exit",this.save.exitapp ))

			var.save.add(win.input.btn(0,0,256,32,"Kill App!",exit))
			var.save.enabled = True
		def close():
			var.save.enabled = False
		def new():
#			this.settings.setup()
			var.save.enabled = False
			var.settings.enabled = True
		def exitapp():
			print("Exitting")
			exit()
	class custom():
		def xadd():
			plc = this.custom
			plc.x +=1
			plc.update()
		def xsub():
			plc = this.custom
			plc.x -=1
			plc.update()
		def yadd():
			plc = this.custom
			plc.y +=1
			plc.update()
		def ysub():
			plc = this.custom
			plc.y -=1
			plc.update()
		def make():
			plc = this.custom
			x = plc.x
			y = plc.y
			var.g = grid(x,y,color(0,0,0))
			var.custom.enabled = False

		x = 32
		y = 32
		sizelb = win.input.label(0,0,256,32,"32x32",(255,255,255))
		def update():
			plc = this.custom
			plc.sizelb.text = str(plc.x)+"x"+str(plc.y)
		def setup():
			var.custom.items = []

			var.custom.add(this.custom.sizelb)
			var.custom.add(win.input.btn(0,0,256,32,"+x",this.custom.xadd ))
			var.custom.add(win.input.btn(0,0,256,32,"-x",this.custom.xsub ))
			var.custom.add(win.input.btn(0,0,256,32,"+y",this.custom.yadd ))
			var.custom.add(win.input.btn(0,0,256,32,"-y",this.custom.ysub ))
			var.custom.add(win.input.btn(0,0,256,32,"Make Custom",this.custom.make ))
this.custom.setup()
this.settings.setup()
this.save.setup()

class bubbles:
	array = []




for i in range(len(var.settings.items)):
	print(var.settings.items[i].text)

import time
t = time.time()
fps = []
while True:
	for event in pygame.event.get():
		if event.type == (pygame.QUIT):
			sys.exit()
			quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if this.click == False:
					if (var.settings.enabled == True):
						var.settings.check(event.pos)
					elif (var.custom.enabled == True):
						var.custom.check(event.pos)
					elif (var.save.enabled == True):
						var.save.check(event.pos)
					this.click=True
				if(event.pos[0] <= scr.width-(16*4)):
					var.g.paint = True

				if(event.pos[0] >= scr.width-(16*5)):
					if(event.pos[1] <= scr.width):
						temp = cps
						##<summary>
						##Stupidly long way to choose which line of color
						##</summary>
						if(event.pos[0] >= scr.width-(16*4)):
							temp = colors.cps0
							if(event.pos[0] >= scr.width-(16*3)):
								temp = colors.cps1
								if(event.pos[0] >= scr.width-(16*2)):
									temp = colors.cps2
									if(event.pos[0] >= scr.width-(16*1)):
										temp = colors.cps3
						if ((event.pos[1]+1)/16 <= len(temp)):
							try:
								var.g.fg = temp[int((event.pos[1])/16)]
							except:
								print("Error")
							print(int((event.pos[1])/16))
							print(event.pos[1])
						else:
							var.g.fg = color(0,0,0)
			elif(event.button == 3):

				hello()
			elif(event.button == 2):

				hello()
			elif(event.button == 4):
				pxl = pxl*2
				print (pxl)
			elif(event.button == 5):
				if pxl > 1:
					pxl = pxl/2
			else:
				print (event.button)
		elif event.type == pygame.MOUSEBUTTONUP:
			this.click = False
			if event.button == 1:

				var.g.paint = False
		elif event.type == pygame.KEYDOWN:
			print(event.key)
			if (event.key == 27):
				var.custom.enabled == False
				var.settings.enabled == False
				var.save.enabled = True
				print("Menu")

				if (var.settings.enabled == True):
					var.settings.check(event.pos)
				elif (var.settings.enabled == False):
					var.g.paint = False

	pygame.draw.rect(scr.scr,(35,39,42),pygame.Rect(0,0,scr.width,scr.height))
	for x in range(int(var.g.width)):
		for y in range(int(var.g.height)):
			c = var.g.get_tuple(x,y)
			scr.drawrec(x*pxl,y*pxl,1*pxl,1*pxl,c)
			mx = pygame.mouse.get_pos()[0]
			my = pygame.mouse.get_pos()[1]
			if( mx > x*pxl and mx <(x*pxl + pxl) ):
				if( my > y*pxl and my <(y*pxl + pxl) ):
					if (var.g.paint):
						c = var.g.get_tuple(x,y)
						var.g.set(int(event.pos[0]/pxl),int(event.pos[1]/pxl))
						scr.drawrec(x*pxl,y*pxl,1*pxl,1*pxl,c)

					ic = (255-c[0],255-c[1],255-c[2])
					for b in range(3):
						if(ic[b] >112 and ic[b] <144):
							if (ic[b]< 128):
								ic[b] = ic[b] + 32
					scr.drawrec(x*pxl+int(pxl*0.25),y*pxl + int(pxl*0.25),int(pxl*0.5),int(pxl*0.5),(255-c[0],255-c[1],255-c[2]))


	c = 0
	for y in range(int(scr.height/8)):
		for x in range(16):
			if c in range(len(cps)):
				scr.drawrec(scr.width-16*(5),y*16,16,16,cps[c])
			if c in range(len(colors.cps0)):
				scr.drawrec(scr.width-16*(4),y*16,16,16,colors.cps0[c])
			if c in range(len(colors.cps1)):
				scr.drawrec(scr.width-16*(3),y*16,16,16,colors.cps1[c])
			if c in range(len(colors.cps2)):
				scr.drawrec(scr.width-16*(2),y*16,16,16,colors.cps2[c])
			if c in range(len(colors.cps3)):
				scr.drawrec(scr.width-16*(1),y*16,16,16,colors.cps3[c])
		c+=1
	for i in range(len(bubbles.array)):
		point = bubbles.array[i]
		s = pygame.Surface((2,2), pygame.SRCALPHA)  # the size of your rect
		a =int( (i/len(bubbles.array))*128)
		#s.set_alpha(a)                # alpha level
		s.fill((255,255,255,a))           # this fills the entire surface
		scr.scr.blit(s, (point[0],point[1]))    # (0,0) are the top-left coordinates

	mx = pygame.mouse.get_pos()[0]
	my = pygame.mouse.get_pos()[1]
	bubbles.array.append((mx,my))
	if len(bubbles.array)>15:
		bubbles.array.pop(0)

	if var.settings.enabled:
		var.settings.draw()
	if var.custom.enabled:
		var.custom.draw()
	if var.save.enabled:
		var.save.draw()
	pygame.display.update()
