add_library('peasycam')
from peasy import PeasyCam
import copy, random

def setup():
    size(400, 400, P3D)
    camera = PeasyCam(this, 10, 10, 10, 150)
    camera.rotateY(-PI/4)
    camera.rotateX(PI/4)
    global colIndex, rot, rotdir, lastdeg, started, cubeFaces, fRate, done
    colIndex = [(255,0,0),(255,165,0),(255,255,255),(255,255,0),(0,255,0),(0,0,255),(20, 20, 20)] #0 = Red, 1 = Orange, 2 = White, 3 = Yellow, 4 = Green, 5 = Blue, 6 = Black
    cubeFaces = [[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1], [5,5,5,5,5,5,5,5,5], [4,4,4,4,4,4,4,4,4]] #Front, Back, Bottom, Top, Right, Left
    rot = None
    rotdir = None
    lastdeg = 0
    started = False
    fRate = 1000
    done = False
    frameRate(fRate)

def draw():
    background(255)
    global started, done, fRate
    if started == False:
        thread("start")
        started = True
    if done:
        fRate = 350
        frameRate(fRate)
        thread("solve")
        done = False
    drawBoxes()
    
def drawBoxes():
    global colIndex, rot, rotdir, lastdeg, cubeFaces
    for x in range(3):
        for y in range(3):
            for z in range(3):
                pushMatrix()
                translate(10*x, 10*y, 10*z)
                val = 0
                if rot != None:
                    val = handleRot(x,y,z)
                if val == 0:
                    newz = abs(z-2)
                    one = 6
                    two = 6
                    three = 6
                    four = 6
                    five = 6
                    six = 6
                    if y == 0:
                        four = cubeFaces[3][x+newz*3]
                    elif y == 2:
                        three = cubeFaces[2][x+newz*3]
                    if newz == 0:
                        one = cubeFaces[0][x+y*3]
                    elif newz == 2:
                        two = cubeFaces[1][x+y*3]
                    if x == 0:
                        six = cubeFaces[5][newz+y*3]
                    elif x == 2:
                        five = cubeFaces[4][newz+y*3]
                    drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                    popMatrix()
        if rot != None:
            lastdeg += 1
            if lastdeg == 90:
                oldlist = copy.deepcopy(cubeFaces)
                lastdeg = 0
                if rot == 'F3':
                    if rotdir == 0:
                        cubeFaces[3][2] = oldlist[1][2]
                        cubeFaces[3][5] = oldlist[1][5]
                        cubeFaces[3][8] = oldlist[1][8]
                        cubeFaces[0][2] = oldlist[3][8]
                        cubeFaces[0][5] = oldlist[3][5]
                        cubeFaces[0][8] = oldlist[3][2]
                        cubeFaces[2][2] = oldlist[0][2]
                        cubeFaces[2][5] = oldlist[0][5]
                        cubeFaces[2][8] = oldlist[0][8]
                        cubeFaces[1][2] = oldlist[2][8]
                        cubeFaces[1][5] = oldlist[2][5]
                        cubeFaces[1][8] = oldlist[2][2]
                        cubeFaces[4][6] = oldlist[4][0]
                        cubeFaces[4][3] = oldlist[4][1]
                        cubeFaces[4][0] = oldlist[4][2]
                        cubeFaces[4][7] = oldlist[4][3]
                        cubeFaces[4][1] = oldlist[4][5]
                        cubeFaces[4][8] = oldlist[4][6]
                        cubeFaces[4][5] = oldlist[4][7]
                        cubeFaces[4][2] = oldlist[4][8]
                    else:
                        cubeFaces[1][2] = oldlist[3][2]
                        cubeFaces[1][5] = oldlist[3][5]
                        cubeFaces[1][8] = oldlist[3][8]
                        cubeFaces[3][8] = oldlist[0][2]
                        cubeFaces[3][5] = oldlist[0][5]
                        cubeFaces[3][2] = oldlist[0][8]
                        cubeFaces[0][2] = oldlist[2][2]
                        cubeFaces[0][5] = oldlist[2][5]
                        cubeFaces[0][8] = oldlist[2][8]
                        cubeFaces[2][8] = oldlist[1][2]
                        cubeFaces[2][5] = oldlist[1][5]
                        cubeFaces[2][2] = oldlist[1][8]
                        cubeFaces[4][0] = oldlist[4][6]
                        cubeFaces[4][1] = oldlist[4][3]
                        cubeFaces[4][2] = oldlist[4][0]
                        cubeFaces[4][3] = oldlist[4][7]
                        cubeFaces[4][5] = oldlist[4][1]
                        cubeFaces[4][6] = oldlist[4][8]
                        cubeFaces[4][7] = oldlist[4][5]
                        cubeFaces[4][8] = oldlist[4][2]
                elif rot == 'F2':
                    if rotdir == 0:
                        cubeFaces[3][1] = oldlist[1][1]
                        cubeFaces[3][4] = oldlist[1][4]
                        cubeFaces[3][7] = oldlist[1][7]
                        cubeFaces[0][1] = oldlist[3][7]
                        cubeFaces[0][4] = oldlist[3][4]
                        cubeFaces[0][7] = oldlist[3][1]
                        cubeFaces[2][1] = oldlist[0][1]
                        cubeFaces[2][4] = oldlist[0][4]
                        cubeFaces[2][7] = oldlist[0][7]
                        cubeFaces[1][1] = oldlist[2][7]
                        cubeFaces[1][4] = oldlist[2][4]
                        cubeFaces[1][7] = oldlist[2][1]
                    else:
                        cubeFaces[1][1] = oldlist[3][1]
                        cubeFaces[1][4] = oldlist[3][4]
                        cubeFaces[1][7] = oldlist[3][7]
                        cubeFaces[3][7] = oldlist[0][1]
                        cubeFaces[3][4] = oldlist[0][4]
                        cubeFaces[3][1] = oldlist[0][7]
                        cubeFaces[0][1] = oldlist[2][1]
                        cubeFaces[0][4] = oldlist[2][4]
                        cubeFaces[0][7] = oldlist[2][7]
                        cubeFaces[2][7] = oldlist[1][1]
                        cubeFaces[2][4] = oldlist[1][4]
                        cubeFaces[2][1] = oldlist[1][7]
                elif rot == 'F1':
                    if rotdir == 0:
                        cubeFaces[3][0] = oldlist[1][0]
                        cubeFaces[3][3] = oldlist[1][3]
                        cubeFaces[3][6] = oldlist[1][6]
                        cubeFaces[0][0] = oldlist[3][6]
                        cubeFaces[0][3] = oldlist[3][3]
                        cubeFaces[0][6] = oldlist[3][0]
                        cubeFaces[2][0] = oldlist[0][0]
                        cubeFaces[2][3] = oldlist[0][3]
                        cubeFaces[2][6] = oldlist[0][6]
                        cubeFaces[1][0] = oldlist[2][6]
                        cubeFaces[1][3] = oldlist[2][3]
                        cubeFaces[1][6] = oldlist[2][0]
                        cubeFaces[5][6] = oldlist[5][0]
                        cubeFaces[5][3] = oldlist[5][1]
                        cubeFaces[5][0] = oldlist[5][2]
                        cubeFaces[5][7] = oldlist[5][3]
                        cubeFaces[5][1] = oldlist[5][5]
                        cubeFaces[5][8] = oldlist[5][6]
                        cubeFaces[5][5] = oldlist[5][7]
                        cubeFaces[5][2] = oldlist[5][8]
                    else:
                        cubeFaces[3][0] = oldlist[0][6]
                        cubeFaces[3][3] = oldlist[0][3]
                        cubeFaces[3][6] = oldlist[0][0]
                        cubeFaces[1][0] = oldlist[3][0]
                        cubeFaces[1][3] = oldlist[3][3]
                        cubeFaces[1][6] = oldlist[3][6]
                        cubeFaces[0][0] = oldlist[2][0]
                        cubeFaces[0][3] = oldlist[2][3]
                        cubeFaces[0][6] = oldlist[2][6]
                        cubeFaces[2][0] = oldlist[1][6]
                        cubeFaces[2][3] = oldlist[1][3]
                        cubeFaces[2][6] = oldlist[1][0]
                        cubeFaces[5][0] = oldlist[5][6]
                        cubeFaces[5][1] = oldlist[5][3]
                        cubeFaces[5][2] = oldlist[5][0]
                        cubeFaces[5][3] = oldlist[5][7]
                        cubeFaces[5][5] = oldlist[5][1]
                        cubeFaces[5][6] = oldlist[5][8]
                        cubeFaces[5][7] = oldlist[5][5]
                        cubeFaces[5][8] = oldlist[5][2]
                elif rot == 'T3':
                    if rotdir == 0:
                        cubeFaces[3][0] = oldlist[4][0]
                        cubeFaces[3][1] = oldlist[4][3]
                        cubeFaces[3][2] = oldlist[4][6]
                        cubeFaces[4][0] = oldlist[2][2]
                        cubeFaces[4][3] = oldlist[2][1]
                        cubeFaces[4][6] = oldlist[2][0]
                        cubeFaces[2][0] = oldlist[5][0]
                        cubeFaces[2][1] = oldlist[5][3]
                        cubeFaces[2][2] = oldlist[5][6]
                        cubeFaces[5][0] = oldlist[3][2]
                        cubeFaces[5][3] = oldlist[3][1]
                        cubeFaces[5][6] = oldlist[3][0]
                        cubeFaces[0][6] = oldlist[0][0]
                        cubeFaces[0][3] = oldlist[0][1]
                        cubeFaces[0][0] = oldlist[0][2]
                        cubeFaces[0][7] = oldlist[0][3]
                        cubeFaces[0][1] = oldlist[0][5]
                        cubeFaces[0][8] = oldlist[0][6]
                        cubeFaces[0][5] = oldlist[0][7]
                        cubeFaces[0][2] = oldlist[0][8]
                    else:
                        cubeFaces[4][6] = oldlist[3][2]
                        cubeFaces[4][3] = oldlist[3][1]
                        cubeFaces[4][0] = oldlist[3][0]
                        cubeFaces[2][0] = oldlist[4][6]
                        cubeFaces[2][1] = oldlist[4][3]
                        cubeFaces[2][2] = oldlist[4][0]
                        cubeFaces[5][0] = oldlist[2][0]
                        cubeFaces[5][3] = oldlist[2][1]
                        cubeFaces[5][6] = oldlist[2][2]
                        cubeFaces[3][0] = oldlist[5][6]
                        cubeFaces[3][1] = oldlist[5][3]
                        cubeFaces[3][2] = oldlist[5][0]
                        cubeFaces[0][0] = oldlist[0][6]
                        cubeFaces[0][1] = oldlist[0][3]
                        cubeFaces[0][2] = oldlist[0][0]
                        cubeFaces[0][3] = oldlist[0][7]
                        cubeFaces[0][5] = oldlist[0][1]
                        cubeFaces[0][6] = oldlist[0][8]
                        cubeFaces[0][7] = oldlist[0][5]
                        cubeFaces[0][8] = oldlist[0][2]
                elif rot == 'T2':
                    if rotdir == 0:
                        cubeFaces[3][3] = oldlist[4][1]
                        cubeFaces[3][4] = oldlist[4][4]
                        cubeFaces[3][5] = oldlist[4][7]
                        cubeFaces[4][1] = oldlist[2][5]
                        cubeFaces[4][4] = oldlist[2][4]
                        cubeFaces[4][7] = oldlist[2][3]
                        cubeFaces[2][3] = oldlist[5][1]
                        cubeFaces[2][4] = oldlist[5][4]
                        cubeFaces[2][5] = oldlist[5][7]
                        cubeFaces[5][1] = oldlist[3][5]
                        cubeFaces[5][4] = oldlist[3][4]
                        cubeFaces[5][7] = oldlist[3][3]
                    else:
                        cubeFaces[4][7] = oldlist[3][5]
                        cubeFaces[4][4] = oldlist[3][4]
                        cubeFaces[4][1] = oldlist[3][3]
                        cubeFaces[2][3] = oldlist[4][7]
                        cubeFaces[2][4] = oldlist[4][4]
                        cubeFaces[2][5] = oldlist[4][1]
                        cubeFaces[5][1] = oldlist[2][3]
                        cubeFaces[5][4] = oldlist[2][4]
                        cubeFaces[5][7] = oldlist[2][5]
                        cubeFaces[3][3] = oldlist[5][7]
                        cubeFaces[3][4] = oldlist[5][4]
                        cubeFaces[3][5] = oldlist[5][1]
                elif rot == 'T1':
                    if rotdir == 0:
                        cubeFaces[3][6] = oldlist[4][2]
                        cubeFaces[3][7] = oldlist[4][5]
                        cubeFaces[3][8] = oldlist[4][8]
                        cubeFaces[4][2] = oldlist[2][8]
                        cubeFaces[4][5] = oldlist[2][7]
                        cubeFaces[4][8] = oldlist[2][6]
                        cubeFaces[2][6] = oldlist[5][2]
                        cubeFaces[2][7] = oldlist[5][5]
                        cubeFaces[2][8] = oldlist[5][8]
                        cubeFaces[5][2] = oldlist[3][8]
                        cubeFaces[5][5] = oldlist[3][7]
                        cubeFaces[5][8] = oldlist[3][6]
                        cubeFaces[1][6] = oldlist[1][0]
                        cubeFaces[1][3] = oldlist[1][1]
                        cubeFaces[1][0] = oldlist[1][2]
                        cubeFaces[1][7] = oldlist[1][3]
                        cubeFaces[1][1] = oldlist[1][5]
                        cubeFaces[1][8] = oldlist[1][6]
                        cubeFaces[1][5] = oldlist[1][7]
                        cubeFaces[1][2] = oldlist[1][8]
                    else:
                        cubeFaces[4][8] = oldlist[3][8]
                        cubeFaces[4][5] = oldlist[3][7]
                        cubeFaces[4][2] = oldlist[3][6]
                        cubeFaces[2][6] = oldlist[4][8]
                        cubeFaces[2][7] = oldlist[4][5]
                        cubeFaces[2][8] = oldlist[4][2]
                        cubeFaces[5][2] = oldlist[2][6]
                        cubeFaces[5][5] = oldlist[2][7]
                        cubeFaces[5][8] = oldlist[2][8]
                        cubeFaces[3][6] = oldlist[5][8]
                        cubeFaces[3][7] = oldlist[5][5]
                        cubeFaces[3][8] = oldlist[5][2]
                        cubeFaces[1][0] = oldlist[1][6]
                        cubeFaces[1][1] = oldlist[1][3]
                        cubeFaces[1][2] = oldlist[1][0]
                        cubeFaces[1][3] = oldlist[1][7]
                        cubeFaces[1][5] = oldlist[1][1]
                        cubeFaces[1][6] = oldlist[1][8]
                        cubeFaces[1][7] = oldlist[1][5]
                        cubeFaces[1][8] = oldlist[1][2]
                elif rot == 'L1':
                    if rotdir == 0:   
                        cubeFaces[0][0] = oldlist[4][0]
                        cubeFaces[0][1] = oldlist[4][1]
                        cubeFaces[0][2] = oldlist[4][2]
                        cubeFaces[4][0] = oldlist[1][2]
                        cubeFaces[4][1] = oldlist[1][1]
                        cubeFaces[4][2] = oldlist[1][0]
                        cubeFaces[1][0] = oldlist[5][0]
                        cubeFaces[1][1] = oldlist[5][1]
                        cubeFaces[1][2] = oldlist[5][2]
                        cubeFaces[5][0] = oldlist[0][2]
                        cubeFaces[5][1] = oldlist[0][1]
                        cubeFaces[5][2] = oldlist[0][0]
                        cubeFaces[3][0] = oldlist[3][2]
                        cubeFaces[3][1] = oldlist[3][5]
                        cubeFaces[3][2] = oldlist[3][8]
                        cubeFaces[3][3] = oldlist[3][1]
                        cubeFaces[3][5] = oldlist[3][7]
                        cubeFaces[3][6] = oldlist[3][0]
                        cubeFaces[3][7] = oldlist[3][3]
                        cubeFaces[3][8] = oldlist[3][6]
                    else:  
                        cubeFaces[4][0] = oldlist[0][0]
                        cubeFaces[4][1] = oldlist[0][1]
                        cubeFaces[4][2] = oldlist[0][2]
                        cubeFaces[1][2] = oldlist[4][0]
                        cubeFaces[1][1] = oldlist[4][1]
                        cubeFaces[1][0] = oldlist[4][2]
                        cubeFaces[5][0] = oldlist[1][0]
                        cubeFaces[5][1] = oldlist[1][1]
                        cubeFaces[5][2] = oldlist[1][2]
                        cubeFaces[0][2] = oldlist[5][0]
                        cubeFaces[0][1] = oldlist[5][1]
                        cubeFaces[0][0] = oldlist[5][2]
                        cubeFaces[3][0] = oldlist[3][6]
                        cubeFaces[3][1] = oldlist[3][3]
                        cubeFaces[3][2] = oldlist[3][0]
                        cubeFaces[3][3] = oldlist[3][7]
                        cubeFaces[3][5] = oldlist[3][1]
                        cubeFaces[3][6] = oldlist[3][8]
                        cubeFaces[3][7] = oldlist[3][5]
                        cubeFaces[3][8] = oldlist[3][2]
                elif rot == 'L2':
                    if rotdir == 0:   
                        cubeFaces[0][3] = oldlist[4][3]
                        cubeFaces[0][4] = oldlist[4][4]
                        cubeFaces[0][5] = oldlist[4][5]
                        cubeFaces[4][3] = oldlist[1][5]
                        cubeFaces[4][4] = oldlist[1][4]
                        cubeFaces[4][5] = oldlist[1][3]
                        cubeFaces[1][3] = oldlist[5][3]
                        cubeFaces[1][4] = oldlist[5][4]
                        cubeFaces[1][5] = oldlist[5][5]
                        cubeFaces[5][3] = oldlist[0][5]
                        cubeFaces[5][4] = oldlist[0][4]
                        cubeFaces[5][5] = oldlist[0][3]
                    else:  
                        cubeFaces[4][3] = oldlist[0][3]
                        cubeFaces[4][4] = oldlist[0][4]
                        cubeFaces[4][5] = oldlist[0][5]
                        cubeFaces[1][5] = oldlist[4][3]
                        cubeFaces[1][4] = oldlist[4][4]
                        cubeFaces[1][3] = oldlist[4][5]
                        cubeFaces[5][3] = oldlist[1][3]
                        cubeFaces[5][4] = oldlist[1][4]
                        cubeFaces[5][5] = oldlist[1][5]
                        cubeFaces[0][5] = oldlist[5][3]
                        cubeFaces[0][4] = oldlist[5][4]
                        cubeFaces[0][3] = oldlist[5][5]
                elif rot == 'L3':
                    if rotdir == 0:   
                        cubeFaces[0][6] = oldlist[4][6]
                        cubeFaces[0][7] = oldlist[4][7]
                        cubeFaces[0][8] = oldlist[4][8]
                        cubeFaces[4][6] = oldlist[1][8]
                        cubeFaces[4][7] = oldlist[1][7]
                        cubeFaces[4][8] = oldlist[1][6]
                        cubeFaces[1][6] = oldlist[5][6]
                        cubeFaces[1][7] = oldlist[5][7]
                        cubeFaces[1][8] = oldlist[5][8]
                        cubeFaces[5][6] = oldlist[0][8]
                        cubeFaces[5][7] = oldlist[0][7]
                        cubeFaces[5][8] = oldlist[0][6]
                        cubeFaces[2][0] = oldlist[2][2]
                        cubeFaces[2][1] = oldlist[2][5]
                        cubeFaces[2][2] = oldlist[2][8]
                        cubeFaces[2][3] = oldlist[2][1]
                        cubeFaces[2][5] = oldlist[2][7]
                        cubeFaces[2][6] = oldlist[2][0]
                        cubeFaces[2][7] = oldlist[2][3]
                        cubeFaces[2][8] = oldlist[2][6]
                    else:  
                        cubeFaces[4][6] = oldlist[0][6]
                        cubeFaces[4][7] = oldlist[0][7]
                        cubeFaces[4][8] = oldlist[0][8]
                        cubeFaces[1][8] = oldlist[4][6]
                        cubeFaces[1][7] = oldlist[4][7]
                        cubeFaces[1][6] = oldlist[4][8]
                        cubeFaces[5][6] = oldlist[1][6]
                        cubeFaces[5][7] = oldlist[1][7]
                        cubeFaces[5][8] = oldlist[1][8]
                        cubeFaces[0][8] = oldlist[5][6]
                        cubeFaces[0][7] = oldlist[5][7]
                        cubeFaces[0][6] = oldlist[5][8]
                        cubeFaces[2][0] = oldlist[2][6]
                        cubeFaces[2][1] = oldlist[2][3]
                        cubeFaces[2][2] = oldlist[2][0]
                        cubeFaces[2][3] = oldlist[2][7]
                        cubeFaces[2][5] = oldlist[2][1]
                        cubeFaces[2][6] = oldlist[2][8]
                        cubeFaces[2][7] = oldlist[2][5]
                        cubeFaces[2][8] = oldlist[2][2]
                rot = None
                rotdir = None
                
def drawColouredBox(bsize, col1, col2, col3, col4, col5, col6): #Front, Back, Bottom, Top, Right, Left
    r1,g1,b1 = col1
    r2,g2,b2 = col2
    r3,g3,b3 = col3
    r4,g4,b4 = col4
    r5,g5,b5 = col5
    r6,g6,b6 = col6
    weight = 4
    beginShape(QUADS)
    fill(r1,g1,b1)
    strokeWeight(weight)
    vertex(-bsize, -bsize,  bsize)
    vertex( bsize, -bsize,  bsize)
    vertex( bsize,  bsize,  bsize)
    vertex(-bsize,  bsize,  bsize)
    endShape()
    beginShape(QUADS)
    fill(r2,g2,b2)
    strokeWeight(weight)
    vertex( bsize, -bsize, -bsize)
    vertex(-bsize, -bsize, -bsize)
    vertex(-bsize,  bsize, -bsize)
    vertex( bsize,  bsize, -bsize)
    endShape()
    beginShape(QUADS)
    fill(r3,g3,b3)
    strokeWeight(weight)
    vertex(-bsize,  bsize,  bsize)
    vertex( bsize,  bsize,  bsize)
    vertex( bsize,  bsize, -bsize)
    vertex(-bsize,  bsize, -bsize)
    endShape()
    beginShape(QUADS)
    fill(r4,g4,b4)
    strokeWeight(weight)
    vertex(-bsize, -bsize, -bsize)
    vertex( bsize, -bsize, -bsize)
    vertex( bsize, -bsize,  bsize)
    vertex(-bsize, -bsize,  bsize)
    endShape()
    beginShape(QUADS)
    fill(r5,g5,b5)
    strokeWeight(weight)
    vertex( bsize, -bsize,  bsize)
    vertex( bsize, -bsize, -bsize)
    vertex( bsize,  bsize, -bsize)
    vertex( bsize,  bsize,  bsize)
    endShape()
    beginShape(QUADS)
    fill(r6,g6,b6)
    strokeWeight(weight)
    vertex(-bsize, -bsize, -bsize)
    vertex(-bsize, -bsize,  bsize)
    vertex(-bsize,  bsize,  bsize)
    vertex(-bsize,  bsize, -bsize)
    endShape()
    
def distBetweenPoints(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    trianglex = x1-x2
    triangley = y1-y2
    return sqrt(trianglex**2+triangley**2)
    
def polarToCartesian(r, deg):
    return (r*cos(radians(deg)), r*sin(radians(deg)))

def getAngle(xy):
    x, y = xy
    x = x//10
    y = y//10
    if y < 0:
        b = distBetweenPoints((x, y), (0, 0))
        a = distBetweenPoints((x, y), (1, 0))
        angle = -degrees(acos((b**2 + 1 - a**2) / 2 / b))
        return angle
    elif xy == (0, 0):
        return 0
    else:
        b = distBetweenPoints((x, y), (0, 0))
        a = distBetweenPoints((x, y), (1, 0))
        angle = degrees(acos((b**2 + 1 - a**2) / 2 / b))
        return angle

def start():
    global rot, rotdir, fRate, done
    moves = ['T1', 'T3', 'F1', 'F3', 'L1', 'L3']
    delay(1000)
    for x in range(100):
        rot = random.choice(moves)
        rotdir = random.randint(0,1)
        delay(90000/fRate)
    done = True
    
def solve():
    delay(1000)
    doWhiteCross()
    delay(1000)
    doWhiteFace()
    delay(1000)
    F2L()
    delay(1000)
    PermuteYellow()
    delay(1000)
    YellowEdges()
    delay(1000)
    YellowCorners()
    delay(1000)
    PermuteYellowCorners()
       
def handleRot(x,y,z):
    global cubeFaces
    popMatrix()
    pushMatrix()
    if rot == 'T1':
        if z == 0:
            if rotdir == 0:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, y*10-10))
                newx, newy = polarToCartesian(distBetweenPoints((x*10+5,y*10+5),(15,15)), inc-lastdeg-1)
                translate(newx+10, newy+10, z*10)
                rotateZ(TWO_PI-radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+znew*3]
                elif y == 2:
                    three = cubeFaces[2][x+znew*3]
                if znew == 0:
                    one = cubeFaces[0][x+y*3]
                elif znew == 2:
                    two = cubeFaces[1][x+y*3]
                if x == 0:
                    six = cubeFaces[5][znew+y*3]
                elif x == 2:
                    five = cubeFaces[4][znew+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
            else:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, y*10-10))
                newx, newy = polarToCartesian(distBetweenPoints((x*10+5,y*10+5),(15,15)), inc+lastdeg+1)
                translate(newx+10, newy+10, z*10)
                rotateZ(radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+znew*3]
                elif y == 2:
                    three = cubeFaces[2][x+znew*3]
                if znew == 0:
                    one = cubeFaces[0][x+y*3]
                elif znew == 2:
                    two = cubeFaces[1][x+y*3]
                if x == 0:
                    six = cubeFaces[5][znew+y*3]
                elif x == 2:
                    five = cubeFaces[4][znew+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
        else:
            translate(10*x, 10*y, 10*z)
            return 0
    elif rot == 'T2':
        if z == 1:
            if rotdir == 0:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, y*10-10))
                newx, newy = polarToCartesian(distBetweenPoints((x*10+5,y*10+5),(15,15)), inc-lastdeg-1)
                translate(newx+10, newy+10, z*10)
                rotateZ(TWO_PI-radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+znew*3]
                elif y == 2:
                    three = cubeFaces[2][x+znew*3]
                if znew == 0:
                    one = cubeFaces[0][x+y*3]
                elif znew == 2:
                    two = cubeFaces[1][x+y*3]
                if x == 0:
                    six = cubeFaces[5][znew+y*3]
                elif x == 2:
                    five = cubeFaces[4][znew+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
            else:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, y*10-10))
                newx, newy = polarToCartesian(distBetweenPoints((x*10+5,y*10+5),(15,15)), inc+lastdeg+1)
                translate(newx+10, newy+10, z*10)
                rotateZ(radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+znew*3]
                elif y == 2:
                    three = cubeFaces[2][x+znew*3]
                if znew == 0:
                    one = cubeFaces[0][x+y*3]
                elif znew == 2:
                    two = cubeFaces[1][x+y*3]
                if x == 0:
                    six = cubeFaces[5][znew+y*3]
                elif x == 2:
                    five = cubeFaces[4][znew+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
        else:
            translate(10*x, 10*y, 10*z)
            return 0
    elif rot == 'T3':
        if z == 2:
            if rotdir == 0:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, y*10-10))
                newx, newy = polarToCartesian(distBetweenPoints((x*10+5,y*10+5),(15,15)), inc-lastdeg-1)
                translate(newx+10, newy+10, z*10)
                rotateZ(TWO_PI-radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+znew*3]
                elif y == 2:
                    three = cubeFaces[2][x+znew*3]
                if znew == 0:
                    one = cubeFaces[0][x+y*3]
                elif znew == 2:
                    two = cubeFaces[1][x+y*3]
                if x == 0:
                    six = cubeFaces[5][znew+y*3]
                elif x == 2:
                    five = cubeFaces[4][znew+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
            else:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, y*10-10))
                newx, newy = polarToCartesian(distBetweenPoints((x*10+5,y*10+5),(15,15)), inc+lastdeg+1)
                translate(newx+10, newy+10, z*10)
                rotateZ(radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+znew*3]
                elif y == 2:
                    three = cubeFaces[2][x+znew*3]
                if znew == 0:
                    one = cubeFaces[0][x+y*3]
                elif znew == 2:
                    two = cubeFaces[1][x+y*3]
                if x == 0:
                    six = cubeFaces[5][znew+y*3]
                elif x == 2:
                    five = cubeFaces[4][znew+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
        else:
            translate(10*x, 10*y, 10*z)
            return 0
    elif rot == 'F1':
        if x == 0:
            if rotdir == 0:
                znew = abs(z - 2)
                inc = getAngle((znew*10-10, y*10-10))
                newz, newy = polarToCartesian(distBetweenPoints((znew*10+5,y*10+5),(15,15)), inc+lastdeg + 1)
                translate(0, newy+10, newz+10)
                rotateX(TWO_PI-radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
            else:
                znew = abs(z - 2)
                inc = getAngle((znew*10-10, y*10-10))
                newz, newy = polarToCartesian(distBetweenPoints((znew*10+5,y*10+5),(15,15)), inc - lastdeg - 1)
                translate(0, newy+10, newz+10)
                rotateX(radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
        else:
            translate(10*x, 10*y, 10*z)
            return 0
    elif rot == 'F2':
        if x == 1:
            if rotdir == 0:
                znew = abs(z - 2)
                inc = getAngle((znew*10-10, y*10-10))
                newz, newy = polarToCartesian(distBetweenPoints((znew*10+5,y*10+5),(15,15)), inc+lastdeg + 1)
                translate(10, newy+10, newz+10)
                rotateX(TWO_PI-radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
            else:
                znew = abs(z - 2)
                inc = getAngle((znew*10-10, y*10-10))
                newz, newy = polarToCartesian(distBetweenPoints((znew*10+5,y*10+5),(15,15)), inc-lastdeg-1)
                translate(10, newy+10, newz+10)
                rotateX(radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
        else:
            translate(10*x, 10*y, 10*z)
            return 0
    elif rot == 'F3':
        if x == 2:
            if rotdir == 0:
                znew = abs(z - 2)
                inc = getAngle((znew*10-10, y*10-10))
                newz, newy = polarToCartesian(distBetweenPoints((znew*10+5,y*10+5),(15,15)), inc+lastdeg + 1)
                translate(20, newy+10, newz+10)
                rotateX(TWO_PI-radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
            else:
                znew = abs(z - 2)
                inc = getAngle((znew*10-10, y*10-10))
                newz, newy = polarToCartesian(distBetweenPoints((znew*10+5,y*10+5),(15,15)), inc-lastdeg-1)
                translate(20, newy+10, newz+10)
                rotateX(radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
        else:
            translate(10*x, 10*y, 10*z)
            return 0
    elif rot == 'L1':
        if y == 0:
            if rotdir == 0:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, znew*10-10))
                newx, newz = polarToCartesian(distBetweenPoints((x*10+5,znew*10+5),(15,15)), inc+lastdeg+1)
                translate(newx+10, y*10, newz+10)
                rotateY(TWO_PI-radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
            else:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, znew*10-10))
                newx, newz = polarToCartesian(distBetweenPoints((x*10+5,znew*10+5),(15,15)), inc-lastdeg-1)
                translate(newx+10, y*10, newz+10)
                rotateY(radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
        else:
            translate(10*x, 10*y, 10*z)
            return 0
    elif rot == 'L2':
        if y == 1:
            if rotdir == 0:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, znew*10-10))
                newx, newz = polarToCartesian(distBetweenPoints((x*10+5,znew*10+5),(15,15)), inc+lastdeg+1)
                translate(newx+10, y*10, newz+10)
                rotateY(TWO_PI-radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
            else:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, znew*10-10))
                newx, newz = polarToCartesian(distBetweenPoints((x*10+5,znew*10+5),(15,15)), inc-lastdeg-1)
                translate(newx+10, y*10, newz+10)
                rotateY(radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
        else:
            translate(10*x, 10*y, 10*z)
            return 0
    elif rot == 'L3':
        if y == 2:
            if rotdir == 0:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, znew*10-10))
                newx, newz = polarToCartesian(distBetweenPoints((x*10+5,znew*10+5),(15,15)), inc+lastdeg+1)
                translate(newx+10, y*10, newz+10)
                rotateY(TWO_PI-radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
            else:
                znew = abs(z - 2)
                inc = getAngle((x*10-10, znew*10-10))
                newx, newz = polarToCartesian(distBetweenPoints((x*10+5,znew*10+5),(15,15)), inc-lastdeg-1)
                translate(newx+10, y*10, newz+10)
                rotateY(radians(lastdeg+1))
                one = 6
                two = 6
                three = 6
                four = 6
                five = 6
                six = 6
                if y == 0:
                    four = cubeFaces[3][x+z*3]
                elif y == 2:
                    three = cubeFaces[2][x+z*3]
                if znew == 0:
                    two = cubeFaces[1][x+y*3]
                elif znew == 2:
                    one = cubeFaces[0][x+y*3]
                if x == 0:
                    six = cubeFaces[5][z+y*3]
                elif x == 2:
                    five = cubeFaces[4][z+y*3]
                drawColouredBox(5, colIndex[one], colIndex[two], colIndex[three], colIndex[four], colIndex[five], colIndex[six])
                popMatrix()
                return True
        else:
            translate(10*x, 10*y, 10*z)
            return 0
        
def doWhiteCross():
    global rot, rotdir, fRate, cubeFaces
    edges = [1]
    othercol = []
    edgeAssocDict = {(0,1):(3,1),(0,3):(5,3),(0,5):(4,3),(0,7):(2,1),(1,1):(3,7),(1,3):(5,5),(1,5):(4,5),(1,7):(2,7),(2, 1):(0,7),(2,3):(5,7),(2,5):(4,7),(2,7):(1,7),(3,1):(0,1),(3,3):(5,1),(3,5):(4,1),(3,7):(1,1),(4,1):(3,5),(4,3):(0,5),(4,5):(1,5),(4,7):(2,5),(5,1):(3,3),(5,3):(0,3),(5,5):(1,3),(5,7):(2,3)}
    while len(edges)>0:
        edges = []
        for x in range(6):
            for y in range(9):
                if cubeFaces[x][y] == 2 and (y in [1,3,5,7]):
                    if x == 0:
                        otherface = edgeAssocDict[(x,y)]
                        if otherface[0] == 2 and cubeFaces[otherface[0]][otherface[1]] != 0:
                            edges.append((x,y))
                            othercol.append(cubeFaces[otherface[0]][otherface[1]])
                        elif otherface[0] == 3 and cubeFaces[otherface[0]][otherface[1]] != 1:
                            edges.append((x,y))
                            othercol.append(cubeFaces[otherface[0]][otherface[1]])
                        elif otherface[0] == 4 and cubeFaces[otherface[0]][otherface[1]] != 5:
                            edges.append((x,y))
                            othercol.append(cubeFaces[otherface[0]][otherface[1]])
                        elif otherface[0] == 5 and cubeFaces[otherface[0]][otherface[1]] != 4:
                            edges.append((x,y))
                            othercol.append(cubeFaces[otherface[0]][otherface[1]])
                    else: 
                        edges.append((x,y))
                        othercol.append(cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]])
        if len(edges) > 0:
            cubeFacesOld = copy.deepcopy(cubeFaces)
            x = 0
            firstcol = othercol[x]
            #move to bottom layer
            if edges[x][0] in [2,3,4,5]:
                isNormWhite = True
            elif edges[x][0] in [0,1]:
                isNormWhite = False
            if edges[x][0] in [0,1]:
                edges[x] = edgeAssocDict[edges[x]]
            if edges[x][0] != 1 and edgeAssocDict[edges[x]][0] != 1:
                if edges[x][0] == 2:
                    if edges[x][1] == 1:
                        rot = 'L3'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'L3'
                        rotdir = 0
                        delay(90000/fRate)
                    elif edges[x][1] == 3:
                        rot = 'L3'
                        rotdir = 0
                        delay(90000/fRate)
                    elif edges[x][1] == 5:
                        rot = 'L3'
                        rotdir = 0
                        delay(90000/fRate)
                elif edges[x][0] == 3:
                    if edges[x][1] == 1:
                        rot = 'L1'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'L1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif edges[x][1] == 3:
                        rot = 'L1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif edges[x][1] == 5:
                        rot = 'L1'
                        rotdir = 0
                        delay(90000/fRate)
                elif edges[x][0] == 4:
                    if edges[x][1] == 1:
                        rot = 'F3'
                        rotdir = 1
                        delay(90000/fRate)
                    elif edges[x][1] == 3:
                        rot = 'F3'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'F3'
                        rotdir = 0
                        delay(90000/fRate)
                    elif edges[x][1] == 7:
                        rot = 'F3'
                        rotdir = 1
                        delay(90000/fRate)
                elif edges[x][0] == 5:
                    if edges[x][1] == 1:
                        rot = 'F1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif edges[x][1] == 3:
                        rot = 'F1'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'F1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif edges[x][1] == 7:
                        rot = 'F1'
                        rotdir = 0
                        delay(90000/fRate)
            #move to correct face
            targetColor = cubeFacesOld[edges[x][0]][edges[x][1]]
            if edges[x][0] == 2 and cubeFacesOld[edges[x][0]][edges[x][1]] != 0 and cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]] != 0:
                if isNormWhite:
                    targetColor = cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]]
                    if targetColor == 1:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 4:
                        rot = 'T1'
                        rotdir = 1
                        delay(90000/fRate)
                    elif targetColor == 5:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                else:
                    if targetColor == 1:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 4:
                        rot = 'T1'
                        rotdir = 1
                        delay(90000/fRate)
                    elif targetColor == 5:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
            elif edges[x][0] == 3 and cubeFacesOld[edges[x][0]][edges[x][1]] != 1 and cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]] != 1:
                if isNormWhite:
                    targetColor = cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]]
                    if targetColor == 0:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 4:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 5:
                        rot = 'T1'
                        rotdir = 1
                        delay(90000/fRate)
                else:
                    if targetColor == 0:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 4:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 5:
                        rot = 'T1'
                        rotdir = 1
                        delay(90000/fRate)
            elif edges[x][0] == 4 and cubeFacesOld[edges[x][0]][edges[x][1]] != 5 and cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]] != 5:
                if isNormWhite:
                    targetColor = cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]]
                    if targetColor == 0:
                        rot = 'T1'
                        rotdir = 1
                        delay(90000/fRate)
                    elif targetColor == 4:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 1:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                else:
                    if targetColor == 0:
                        rot = 'T1'
                        rotdir = 1
                        delay(90000/fRate)
                    elif targetColor == 4:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 1:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
            elif edges[x][0] == 5 and cubeFacesOld[edges[x][0]][edges[x][1]] != 4 and cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]] != 4:
                if isNormWhite:
                    targetColor = cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]]
                    if targetColor == 0:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 5:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 1:
                        rot = 'T1'
                        rotdir = 1
                        delay(90000/fRate)
                else:
                    if targetColor == 0:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 5:
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                        rot = 'T1'
                        rotdir = 0
                        delay(90000/fRate)
                    elif targetColor == 1:
                        rot = 'T1'
                        rotdir = 1
                        delay(90000/fRate)
            if edgeAssocDict[edges[x]][0] in [0, 1]:
                edges[x] = edgeAssocDict[edges[x]]
            #move to white face
            if cubeFacesOld[edges[x][0]][edges[x][1]] == 0 or cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]] == 0:
                if isNormWhite:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0
                else:
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
            elif cubeFacesOld[edges[x][0]][edges[x][1]] == 1 or cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]] == 1:
                if isNormWhite:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 1
                else:
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 0
            elif cubeFacesOld[edges[x][0]][edges[x][1]] == 5 or cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]] == 5:
                if isNormWhite:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                else:
                    rot = 'F3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0  
            elif cubeFacesOld[edges[x][0]][edges[x][1]] == 4 or cubeFacesOld[edgeAssocDict[edges[x]][0]][edgeAssocDict[edges[x]][1]] == 4:
                if isNormWhite:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                else:
                    rot = 'F1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 0  
            edges = [1]
            delay(90000/fRate)
        else:
            edges = []
            
def doWhiteFace():
    global rot, rotdir, fRate
    corners = [1]
    othercol = []
    cornerPieces = [[(0,0),(3,0),(5,0)],[(0,2),(3,2),(4,0)],[(0,6),(2,0),(5,6)],[(0,8),(2,2),(4,6)],[(1,0),(3,6),(5,2)],[(1,2),(3,8),(4,2)],[(1,6),(2,6),(5,8)],[(1,8),(2,8),(4,8)]]
    while len(corners)>0:
        corners = []
        for x in range(6):
            for y in range(9):
                if cubeFaces[x][y] == 2 and (y in [0,2,6,8]):
                    if x == 0:
                        if y == 0 and cubeFaces[3][0] != 1 and cubeFaces[5][0] != 4:
                            corners.append((x, y))
                        elif y == 2 and cubeFaces[3][2] != 1 and cubeFaces[4][0] != 5:
                            corners.append((x, y))
                        elif y == 6 and cubeFaces[2][0] != 0 and cubeFaces[5][6] != 4:
                            corners.append((x, y))
                        elif y == 8 and cubeFaces[2][2] != 0 and cubeFaces[4][6] != 5:
                            corners.append((x, y))
                    else:
                        corners.append((x, y))
        if len(corners) > 0:
            cubeFacesOld = copy.deepcopy(cubeFaces)
            isOnTop = False
            for x in cornerPieces:
                if corners[0] in x:
                    if x[0][0] == 0:
                        isOnTop = True
            if isOnTop:
                if corners[0][1] == 0:
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 1
                elif corners[0][1] == 2:
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 1
                elif corners[0][1] == 6:
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 1
                elif corners[0][1] == 8:
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 1
            delay(90000/fRate)
            twoColors = []
            which = 0
            for x in cornerPieces:
                if corners[0] in x:
                    for y in range(3):
                        if x[y] != corners[0]:
                            twoColors.append(cubeFacesOld[x[y][0]][x[y][1]])
                        if x[y][0] in [0, 1]:
                            which = x[y][1]
                    break
            print("0 = Red, 1 = Orange, 2 = White, 3 = Yellow, 4 = Green, 5 = Blue, 6 = Black")
            print(twoColors)
            if (4 in twoColors) and (1 in twoColors) and which != 0:
                if which == 2:
                    rot = 'T1'
                    rotdir = 0
                elif which == 6:
                    rot = 'T1'
                    rotdir = 1
                elif which == 8:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
            elif (5 in twoColors) and (1 in twoColors) and which != 2:
                if which == 0:
                    rot = 'T1'
                    rotdir = 1
                elif which == 6:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif which == 8:
                    rot = 'T1'
                    rotdir = 0
            elif (4 in twoColors) and (0 in twoColors) and which != 6:
                if which == 0:
                    rot = 'T1'
                    rotdir = 0
                elif which == 2:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif which == 8:
                    rot = 'T1'
                    rotdir = 1
            elif (5 in twoColors) and (0 in twoColors) and which != 8:
                if which == 0:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif which == 2:
                    rot = 'T1'
                    rotdir = 1
                elif which == 6:
                    rot = 'T1'
                    rotdir = 0
            delay(90000/fRate)
            if (4 in twoColors) and (1 in twoColors):
                while cubeFaces[0][0] != 2 or cubeFaces[3][0] != 1 or cubeFaces[5][0] != 4:
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 1
                    delay(90000/fRate)
            elif (5 in twoColors) and (1 in twoColors):
                while cubeFaces[0][2] != 2 or cubeFaces[3][2] != 1 or cubeFaces[4][0] != 5:
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
            elif (4 in twoColors) and (0 in twoColors):
                while cubeFaces[0][6] != 2 or cubeFaces[2][0] != 0 or cubeFaces[5][6] != 4:
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
            elif (5 in twoColors) and (0 in twoColors):
                while cubeFaces[0][8] != 2 or cubeFaces[2][2] != 0 or cubeFaces[4][6] != 5:
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 1
                    delay(90000/fRate)
            corners = [1]
        else:
            corners = []
            
def F2L():
    global rot, rotdir, fRate
    edges = [1]
    othercol = []
    edgeAssocDict = {(0,1):(3,1),(0,3):(5,3),(0,5):(4,3),(0,7):(2,1),(1,1):(3,7),(1,3):(5,5),(1,5):(4,5),(1,7):(2,7),(2, 1):(0,7),(2,3):(5,7),(2,5):(4,7),(2,7):(1,7),(3,1):(0,1),(3,3):(5,1),(3,5):(4,1),(3,7):(1,1),(4,1):(3,5),(4,3):(0,5),(4,5):(1,5),(4,7):(2,5),(5,1):(3,3),(5,3):(0,3),(5,5):(1,3),(5,7):(2,3)}
    while len(edges)>0:
        edges = []
        for x in range(6):
            for y in range(9):
                if y in [1,3,5,7]:
                    if cubeFaces[x][y] == 0 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 4 and (x != 2 or y != 3):
                        #R/G Edge, R side
                        edges.append((x,y,1))
                    elif cubeFaces[x][y] == 0 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 5 and (x != 2 or y != 5):
                        #R/B Edge, R side
                        edges.append((x,y,2))
                    elif cubeFaces[x][y] == 1 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 4 and (x != 3 or y != 3):
                        #O/G Edge, O side
                        edges.append((x,y,3))
                    elif cubeFaces[x][y] == 1 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 5 and (x != 3 or y != 5):
                        #O/B Edge, O side
                        edges.append((x,y,4))
        if len(edges) > 0:
            if (edges[0][0] == 3 and edges[0][1] == 3) or (edgeAssocDict[(edges[0][0],edges[0][1])][0] == 3 and edgeAssocDict[(edges[0][0],edges[0][1])][1] == 3):
                rot = 'F1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 1
            elif (edges[0][0] == 3 and edges[0][1] == 5) or (edgeAssocDict[(edges[0][0],edges[0][1])][0] == 3 and edgeAssocDict[(edges[0][0],edges[0][1])][1] == 5):
                rot = 'F3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 0
            elif (edges[0][0] == 2 and edges[0][1] == 3) or (edgeAssocDict[(edges[0][0],edges[0][1])][0] == 2 and edgeAssocDict[(edges[0][0],edges[0][1])][1] == 3):
                rot = 'F1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 1
            elif (edges[0][0] == 2 and edges[0][1] == 5) or (edgeAssocDict[(edges[0][0],edges[0][1])][0] == 2 and edgeAssocDict[(edges[0][0],edges[0][1])][1] == 5):
                rot = 'F3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 0
            delay(90000/fRate)
            pos = ()
            for x in range(6):
                for y in range(9):
                    if y in [1,3,5,7]:
                        if cubeFaces[x][y] == 0 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 4 and edges[0][2] == 1 and x == 1:
                            pos = (y, 4, 0)
                        elif cubeFaces[x][y] == 0 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 4 and edges[0][2] == 1 and edgeAssocDict[(x,y)][0] == 1:
                            pos = (edgeAssocDict[(x,y)][1], 0, 4)
                        elif cubeFaces[x][y] == 0 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 5 and edges[0][2] == 2 and x == 1:
                            pos = (y, 5, 0)
                        elif cubeFaces[x][y] == 0 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 5 and edges[0][2] == 2 and edgeAssocDict[(x,y)][0] == 1:
                            pos = (edgeAssocDict[(x,y)][1], 0, 5)
                        elif cubeFaces[x][y] == 1 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 4 and edges[0][2] == 3 and x == 1:
                            pos = (y, 4, 1)
                        elif cubeFaces[x][y] == 1 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 4 and edges[0][2] == 3 and edgeAssocDict[(x,y)][0] == 1:
                            pos = (edgeAssocDict[(x,y)][1], 1, 4)
                        elif cubeFaces[x][y] == 1 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 5 and edges[0][2] == 4 and x == 1:
                            pos = (y, 5, 1)
                        elif cubeFaces[x][y] == 1 and cubeFaces[edgeAssocDict[(x,y)][0]][edgeAssocDict[(x,y)][1]] == 5 and edges[0][2] == 4 and edgeAssocDict[(x,y)][0] == 1:
                            pos = (edgeAssocDict[(x,y)][1], 1, 5)
            if pos[0] == 1 and pos[1] != 1:
                if pos[1] == 5:
                    rot = 'T1'
                    rotdir = 1
                elif pos[1] == 4:
                    rot = 'T1'
                    rotdir = 0
                elif pos[1] == 0:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
            elif pos[0] == 3 and pos[1] != 4:
                if pos[1] == 1:
                    rot = 'T1'
                    rotdir = 1
                elif pos[1] == 0:
                    rot = 'T1'
                    rotdir = 0
                elif pos[1] == 5:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
            elif pos[0] == 5 and pos[1] != 5:
                if pos[1] == 0:
                    rot = 'T1'
                    rotdir = 1
                elif pos[1] == 1:
                    rot = 'T1'
                    rotdir = 0
                elif pos[1] == 4:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
            elif pos[0] == 7 and pos[1] != 0:
                if pos[1] == 1:
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif pos[1] == 5:
                    rot = 'T1'
                    rotdir = 0
                elif pos[1] == 4:
                    rot = 'T1'
                    rotdir = 1
            delay(90000/fRate)
            if pos[1] == 0 and pos[2] == 5:
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 0
            elif pos[1] == 0 and pos[2] == 4:
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 1
            elif pos[1] == 1 and pos[2] == 5:
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 0
            elif pos[1] == 1 and pos[2] == 4:
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 1
            elif pos[1] == 4 and pos[2] == 0:
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 1
                delay(90000/fRate)
            elif pos[1] == 4 and pos[2] == 1:
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 0
            elif pos[1] == 5 and pos[2] == 1:
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 0
            elif pos[1] == 5 and pos[2] == 0:
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 1
            delay(90000/fRate)
            edges = [1]
        else:
            edges = []
        
def PermuteYellow():
    global rot, rotdir, fRate
    while cubeFaces[1][1] != 3 or cubeFaces[1][3] != 3 or cubeFaces[1][5] != 3 or cubeFaces[1][7] != 3:          
        if cubeFaces[1][1] != 3 and cubeFaces[1][3] == 3 and cubeFaces[1][5] != 3 and cubeFaces[1][7] == 3:
            rot = 'T1'
            rotdir = 0
        elif cubeFaces[1][1] == 3 and cubeFaces[1][3] == 3 and cubeFaces[1][5] != 3 and cubeFaces[1][7] != 3:
            rot = 'T1'
            rotdir = 0
            delay(90000/fRate)
            rot = 'T1'
            rotdir = 0
        elif cubeFaces[1][1] == 3 and cubeFaces[1][3] != 3 and cubeFaces[1][5] == 3 and cubeFaces[1][7] != 3:
            rot = 'T1'
            rotdir = 1
        elif cubeFaces[1][1] != 3 and cubeFaces[1][3] == 3 and cubeFaces[1][5] == 3 and cubeFaces[1][7] != 3:
            rot = 'T1'
            rotdir = 0
        delay(90000/fRate)
        rot = 'F1'
        rotdir = 0
        delay(90000/fRate)
        rot = 'L1'
        rotdir = 0
        delay(90000/fRate)
        rot = 'T1'
        rotdir = 0
        delay(90000/fRate)
        rot = 'L1'
        rotdir = 1
        delay(90000/fRate)
        rot = 'T1'
        rotdir = 1
        delay(90000/fRate)
        rot = 'F1'
        rotdir = 1
        delay(90000/fRate)
        
def YellowEdges():
    global rot, rotdir, fRate
    edges = [1]
    othercol = []
    edgeAssocDict = {(0,1):(3,1),(0,3):(5,3),(0,5):(4,3),(0,7):(2,1),(1,1):(3,7),(1,3):(5,5),(1,5):(4,5),(1,7):(2,7),(2, 1):(0,7),(2,3):(5,7),(2,5):(4,7),(2,7):(1,7),(3,1):(0,1),(3,3):(5,1),(3,5):(4,1),(3,7):(1,1),(4,1):(3,5),(4,3):(0,5),(4,5):(1,5),(4,7):(2,5),(5,1):(3,3),(5,3):(0,3),(5,5):(1,3),(5,7):(2,3)}
    while len(edges)>0:
        edges = []
        for y in range(9):
            if y in [1,3,5,7]:
                if cubeFaces[edgeAssocDict[(1,y)][0]][edgeAssocDict[(1,y)][1]] != 1 and y == 1:
                    edges.append(y)
                elif cubeFaces[edgeAssocDict[(1,y)][0]][edgeAssocDict[(1,y)][1]] != 4 and y == 3:
                    edges.append(y)
                elif cubeFaces[edgeAssocDict[(1,y)][0]][edgeAssocDict[(1,y)][1]] != 5 and y == 5:
                    edges.append(y)
                elif cubeFaces[edgeAssocDict[(1,y)][0]][edgeAssocDict[(1,y)][1]] != 0 and y == 7:
                    edges.append(y)
        if len(edges) > 0:
            if edges[0] == 1 and cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] != 1:
                if cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 0:
                    rot = 'F3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 4:
                    rot = 'F3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 5:
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
            elif edges[0] == 3 and cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] != 4:
                if cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 0:
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 1:
                    rot = 'F3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 5:
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
            elif edges[0] == 5 and cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] != 5:
                if cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 0:
                    rot = 'F1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 1:
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 4:
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
            elif edges[0] == 7 and cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] != 0:
                if cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 1:
                    rot = 'F1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L3'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 4:
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'L1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                elif cubeFaces[edgeAssocDict[(1,edges[0])][0]][edgeAssocDict[(1,edges[0])][1]] == 5:
                    rot = 'F1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
                    delay(90000/fRate)
                    rot = 'F1'
                    rotdir = 1
                    delay(90000/fRate)
                    rot = 'T1'
                    rotdir = 0
            delay(90000/fRate)
            edges = [1]
        else:
            edges = []
            
def YellowCorners():
    global rot, rotdir, fRate
    no = 0
    while no != 4:
        corners = [[cubeFaces[1][0],cubeFaces[3][6],cubeFaces[5][2]],[cubeFaces[1][2],cubeFaces[3][8],cubeFaces[4][2]],[cubeFaces[1][6],cubeFaces[2][6],cubeFaces[5][8]],[cubeFaces[1][8],cubeFaces[2][8],cubeFaces[4][8]]]
        no = 0
        correct = 0
        if (corners[0][0] in [1,3,4]) and (corners[0][1] in [1,3,4]) and (corners[0][2] in [1,3,4]):
            correct = 1
            no += 1
        if (corners[1][0] in [1,3,5]) and (corners[1][1] in [1,3,5]) and (corners[1][2] in [1,3,5]):
            correct = 2
            no += 1
        if (corners[2][0] in [0,3,4]) and (corners[2][1] in [0,3,4]) and (corners[2][2] in [0,3,4]):
            correct = 3
            no += 1
        if (corners[3][0] in [0,3,5]) and (corners[3][1] in [0,3,5]) and (corners[3][2] in [0,3,5]):
            correct = 4
            no += 1
        if no == 0:
            rot = 'L1'
            rotdir = 0
            delay(90000/fRate)
            rot = 'T1'
            rotdir = 1
            delay(90000/fRate)
            rot = 'L3'
            rotdir = 0
            delay(90000/fRate)
            rot = 'T1'
            rotdir = 0
            delay(90000/fRate)
            rot = 'L1'
            rotdir = 1
            delay(90000/fRate)
            rot = 'T1'
            rotdir = 1
            delay(90000/fRate)
            rot = 'L3'
            rotdir = 1
            delay(90000/fRate)
            rot = 'T1'
            rotdir = 0
        elif no == 1:
            if correct == 1:
                rot = 'F3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
            elif correct == 2:
                rot = 'L3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
            elif correct == 3:
                rot = 'L1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'L3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
            elif correct == 4:
                rot = 'F1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'F1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'F3'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
        delay(90000/fRate)
        
def PermuteYellowCorners():
    global rot, rotdir, fRate
    corners = [1]
    othercol = []
    while len(corners)>0:
        corners = []
        if cubeFaces[1][0] != 3:
            corners.append((1, 0))
        elif cubeFaces[1][2] != 3:
            corners.append((2, 2))
        elif cubeFaces[1][6] != 3:
            corners.append((3, 6))
        elif cubeFaces[1][8] != 3:
            corners.append((4, 8))
        if len(corners)>0:
            if corners[0][0] == 2:
                rot = 'T1'
                rotdir = 0
            elif corners[0][0] == 3:
                rot = 'T1'
                rotdir = 1
            elif corners[0][0] == 4:
                rot = 'T1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T1'
                rotdir = 0
            delay(90000/fRate)
            while cubeFaces[1][0] != 3:
                rot = 'L1'
                rotdir = 1
                delay(90000/fRate)
                rot = 'T3'
                rotdir = 0
                delay(90000/fRate)
                rot = 'L1'
                rotdir = 0
                delay(90000/fRate)
                rot = 'T3'
                rotdir = 1
                delay(90000/fRate)
    while cubeFaces[3][7] != 1:
        rot = 'T1'
        rotdir = 0
        delay(90000/fRate)
