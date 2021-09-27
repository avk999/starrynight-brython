import random

class Building:
    
    MAX_HEIGHT = 0.4
    MU_HEIGHT = 0.2
    SIGMA_HEIGHT = 0.3
    MAX_WIDTH = 0.05
    MU_WIDTH = 0.04
    SIGMA_WIDTH = 0.02
    
    MU_FLOOR_HEIGHT=12
    SIGMA_FLOOR_HEIGHT=0.2

    WINDOW_INTERVAL=8

    """Skyscraper class - canwas width, height, building width and height, floor height, window interval"""
    def __init__(self, canvas, x0, pctwidth=None, pctheight=None,  floor_height= None, window_interval=None) -> None:
        """ all measurements are in pct of canvas height and width.
         None values on constructors - random within limits in the class definition"""
        self.canvas=canvas
        if not pctheight:
            pctheight=random.normalvariate(self.MU_HEIGHT,self.SIGMA_HEIGHT)
        if not pctwidth:
            pctwidth=random.normalvariate(self.MU_WIDTH,self.SIGMA_WIDTH)
        self.height=int(abs(pctheight*canvas.height))
        self.width=int(abs(pctwidth*canvas.width))
        
        if not floor_height:
            floor_height=random.normalvariate(self.MU_FLOOR_HEIGHT, self.SIGMA_FLOOR_HEIGHT)
        self.floor_height=floor_height

        if not window_interval:
            window_interval=self.WINDOW_INTERVAL 
        self.window_interval=window_interval

        self.x0=x0
        self.x1=x0+self.width

        self.window_columns=int(self.width/self.window_interval)
        self.n_floors=int(self.height/floor_height)
        #self.build()
        return
    def build(self):
        ctx=self.canvas.getContext("2d")
        ctx.fillStyle="#202020"
        ctx.strokeStyle="white"
        ctx.fillRect(self.x0,self.canvas.height-self.height,self.width,self.height)
        #ctx.fill()
        ctx.stroke()


class Star:
    def __init__(self,canvas,x=None,y=None,color=None,dia=None) -> None:
        self.canvas=canvas
        if not color:
            color='#'
            for i in 'r g b'.split():
                color+='{:02X}'.format(random.randint(100,255))
        self.color=color
        if not dia:
            dia=random.randint(1,19)
        self.x=x
        self.y=y 
        self.dia=dia 
        return

    def on(self):
        """ if stars are turned on then someone needs them"""    
        ctx = self.canvas.getContext("2d")
        #ctx.beginPath()
        
        #ctx.arc(self.x,self.y,self.dia,0,math.pi*2)
        ctx.fillStyle=self.color 
        #ctx.fill()
        ctx.fillRect(self.x,self.y,2,2)
        ctx.fill()
        #ctx.closePath()
        ctx.stroke()
        return
    
    def off(self):
        self.color="#000000"
        self.on()

    

class Window:
    WINDOW_WIDTH=4
    WINDOW_HEIGHT=4
    def __init__(self, canvas, building):
        self.canvas=canvas
        self.x=int(random.randint(0,building.window_columns)*building.window_interval+building.x0)
        y=int(random.randint(0,building.n_floors)*building.floor_height)
        self.y=canvas.height-y
        # define color
        r=random.randint(150,220)
        g=random.randint(150,210)
        b=random.randint(60,100)
        self.height=random.choices([self.WINDOW_HEIGHT-1,self.WINDOW_HEIGHT], 
            weights=[0.25,0.75])[0]
        self.width=random.choices([self.WINDOW_WIDTH-1,self.WINDOW_WIDTH], 
            weights=[0.25,0.75])[0]
        self.color="#"
        for i in [r,g,b]:
            self.color+='{:02X}'.format(i)
        self.on()
        pass

    def on(self):
        ctx = self.canvas.getContext("2d")
        ctx.fillStyle=self.color
        ctx.fillRect(self.x,self.y,self.width,self.height)
        ctx.fill()
        ctx.stroke()

    def off(self):
        self.color='#000000'
        self.on()

    
