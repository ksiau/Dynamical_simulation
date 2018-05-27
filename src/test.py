from random import random
import math
def sign(num):
    if num >=0:
        return 1
    else:
        return -1
def getAngleByVector(v):
    v=[v[0], v[1]]
    angle0 = 0
    if v[0] < 0:
    	v = [-v[0], -v[1]]
    	angle0 += math.pi
    angle = math.asin(v[1]/math.sqrt(v[0]**2 + v[1]**2))
    return angle + angle0


print(getAngleByVector([-1, 1])/math.pi)