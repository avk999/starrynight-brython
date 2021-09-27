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

BUILDING_MIN_WIDTH=x/20
BUILDING_MAX_HEIGHT=y*0.7
BUILDING_MIN_HEIGHT=20

SAT_WIN=0.97
SAT_STARS=0.01

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
stars_killed=0
windows_killed=0
print(f"win: {SAT_WIN}, stars: {SAT_STARS}")



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
    global stars_killed, windows_killed
    if len(stars)>stars_threshold:
        s=stars.pop(random.randint(0,len(stars)-1))
        s.off()
        stars_killed+=1
   
    if len(windows)> win_threshold:
        w=windows.pop(random.randint(0,len(windows)-1))
        w.off()
        windows_killed+=1
   
    return

def print_stats():
    
    print(f"Stars: {len(stars)}, space {space_for_stars}, {len(stars)/space_for_stars}")
    print(f"windows: {len(windows)}, space {max_windows}, {len(windows)/max_windows}")
    print(f"killed {stars_killed} stars and broke {windows_killed} windows")

timer.set_interval(addstar,100, stars)
timer.set_interval(addwindow,60,buildings,windows)
timer.set_interval(kill,50,stars,windows)
timer.set_interval(print_stats,10000)