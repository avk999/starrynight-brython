from browser import document, window, timer, html
import random
import time
from shapes import Star, Building, Window
x=window.innerWidth
y=window.innerHeight
print(f"X={x}, Y={y}")
document <= html.CANVAS(id='mycanvas', width=str(x), height=str(y), 
                        style={'background-color': 'rgba(0,0,0,1)'})
canvas=document['mycanvas']

BUILDING_MIN_WIDTH=30
BUILDING_MIN_HEIGHT=150
SAT_WIN=0.95
SAT_STARS=0.05

buildings=[]
skyline=dict()
windows=[]
stars=[]
max_windows=0
max_stars=0

bx=0
while bx < x:
    bldg=Building(canvas,bx)
    if bldg.width<BUILDING_MIN_WIDTH or bldg.height<BUILDING_MIN_HEIGHT: 
        
        continue
    for i in range(bx, bldg.x1):
        skyline[i]=y - bldg.height
    bx=bldg.x1
    buildings.append(bldg)
    max_windows+=bldg.n_floors*bldg.window_columns
building_footprints=list(map(lambda x: x.width, buildings))
    
print("Built {} buildings".format(len(buildings)))
print(f"Max number of windows: {max_windows}")
space_for_stars=x*y-sum(skyline.values())
print(f"Space for stars: {space_for_stars}")

stars_threshold=space_for_stars*SAT_STARS
win_threshold=max_windows*SAT_WIN




def addstar(stars):
    sx,sy=(random.randint(0,x),random.randint(0,y))
    if skyline[sx]<sy:
        return
    s=Star(canvas,sx,sy)
    s.on()
    stars.append(s)
    # if len(stars)%10 == 0:
    #     print("{} stars in the sky".format(len(stars)))

def addwindow(buildings, windows):
    #bldg=random.choices(buildings, weights=building_footprints, k=1)[0]
    bldg=random.choices(buildings, k=1)[0]

    win=Window(canvas,bldg)
    windows.append(win)

def kill(stars,windows):
   
    if len(stars)>stars_threshold:
        s=stars.pop(random.randint(0,len(stars)-1))
        s.off()
   
    if len(windows)> win_threshold:
        w=windows.pop(random.randint(0,len(windows)-1))
        w.off()
   
    return

timer.set_interval(addstar,50, stars)
timer.set_interval(addwindow,40,buildings,windows)
timer.set_interval(kill,430,stars,windows)
