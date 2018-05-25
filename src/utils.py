import math
from random import random
import ball


def impact2Ball(ball1, ball2, dt, g=[0, 0], e=1):
    v1  = (ball1.location[0] - ball2.location[0], ball1.location[1] - ball2.location[1])
    v2 = (ball1.velocity[0] - ball2.velocity[0], ball1.velocity[1] - ball2.velocity[1])
    dis = math.sqrt(v1[0]**2 + v1[1]**2)
    velocity = math.sqrt(v2[0]**2 + v2[1]**2)
    if velocity <= 0.0: return 0
    cs = (v1[0]*v2[0] + v1[1]*v2[1])/dis/velocity
    if cs >= 0: return 0
    s1 = math.sqrt(1 - min(1, cs**2))*dis
    if s1 - ball1.radius - ball2.radius > 0: return 0    
    dt1 = (math.sqrt(dis**2 - s1**2) - math.sqrt((ball1.radius + ball2.radius)**2 - s1**2))*-cs/velocity
    if dt1 > dt:
        return 0
    ball1.location[0] += ball1.velocity[0]*dt1
    ball1.location[1] += ball1.velocity[1]*dt1
    ball2.location[0] += ball2.velocity[0]*dt1
    ball2.location[1] += ball2.velocity[1]*dt1
    dt2 = dt - dt1
    v1  = (ball1.location[0] - ball2.location[0], ball1.location[1] - ball2.location[1])
    dis = math.sqrt(v1[0]**2 + v1[1]**2)
    # print
    dvscale = (v1[0]*v2[0] + v1[1]*v2[1])/dis
    dv = (-dvscale*v1[0]/dis, -dvscale*v1[1]/dis)
    ball1.velocity[0] = (ball1.velocity[0] + dv[0]*2*(ball2.mass/(ball1.mass + ball2.mass)))*e + dt*g[0]
    ball1.velocity[1] = (ball1.velocity[1] + dv[1]*2*(ball2.mass/(ball1.mass + ball2.mass)))*e + dt*g[1]
    ball2.velocity[0] = (ball2.velocity[0] - dv[0]*2*(ball1.mass/(ball1.mass + ball2.mass)))*e + dt*g[0]
    ball2.velocity[1] = (ball2.velocity[1] - dv[1]*2*(ball1.mass/(ball1.mass + ball2.mass)))*e + dt*g[1]
    ball1.velocity[0] += ball1.velocity[0]*dt2
    ball1.location[1] += ball1.velocity[1]*dt2
    ball2.location[0] += ball2.velocity[0]*dt2
    ball2.location[1] += ball2.velocity[1]*dt2
    return 1


def generateRandomBalls(num, maxv, minv, radius, resolution):
    balls = []
    for i in range(num):
        while 1:
            location = [resolution[0]*random(), resolution[1]*random()]
            if location[0] + radius > resolution[0] or location[0] - radius < 0 \
                or location[1] + radius > resolution[1] or location[1] - radius < 0: continue
            sig = 0
            for eachBall in balls:
                if math.sqrt((location[0] - eachBall.location[0])**2 + (location[1] - eachBall.location[1])**2) - radius - eachBall.radius < 0: 
                    sig = 1
                    break
            if sig == 1: continue
            vx = minv + (maxv - minv)*random()
            vy = minv + (maxv - minv)*random()
            balls.append(ball.Ball(radius, [vx, vy], location, [255*random(), 255*random(), 255*random()]))
            break
    return balls