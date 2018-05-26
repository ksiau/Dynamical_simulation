import pygame, math

def sign(num):
    if num >=0:
        return 1
    else:
        return -1

class Ball():

    def __init__(self, radius, velocity, location, color,  mass=1, state=0):
        self.radius = radius
        self.velocity = velocity
        self.location = location
        self.color = color
        self.mass = mass
        # state = 1: roll in y direction
        #         2: roll in x direction
        #         3: still
        self.state = state

    def getSpeed(self):
        return math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)

    def update(self, surface, g, dt, e=1, f=0):
            if self.state == 3:
                return
            sizex, sizey = surface.get_size()
            dty = dt
            ds = self.velocity[1]*dty + 1/2*g[1]*dty**2
        # while self.location[1] + self.radius + ds > sizey or self.location[1] - self.radius + ds < 0:
            if self.state != 2:
                if self.location[1] + self.radius + ds > sizey:
                    ds1 = sizey - self.location[1] - self.radius
                    if g[1] == 0:
                        dt1 = (sizey - self.location[1] - self.radius)/self.velocity[1]
                    else:
                        dt1Tmp = math.sqrt(max((self.velocity[1]/g[1])**2 + 2*ds1/g[1], 0)) - self.velocity[1]/g[1]
                        if dt1Tmp >= 0 and dt1Tmp < dty:
                            dt1 = dt1Tmp
                        else:
                            dt1 = - math.sqrt(max((self.velocity[1]/g[1])**2 + 2*ds1/g[1], 0)) - self.velocity[1]/g[1]
                    v1 = self.velocity[1]
                    self.velocity[1] = -(v1 + g[1]*dt1)*e
                    self.velocity[0] = sign(self.velocity[0])*max(0, abs(self.velocity[0]) - abs(v1)*f*2)
                    self.location[1] = sizey - self.radius
                    dty -= dt1
                    ds = self.velocity[1]*dty + 1/2*g[1]*dty**2
                    if abs(self.velocity[1]) <= abs(g[1]/10):
                        self.velocity[1] = 0
                        self.location[1] = sizey - self.radius
                        self.state = 2
                        if self.velocity[0] == 0:
                            self.state = 3
                    # elif self.state == 1:
                    #     self.velocity[0] = sign(self.velocity[0])*max(0, abs(self.velocity[0]) - g[0]*f*dty)
                elif self.location[1] - self.radius + ds < 0:
                    ds1 = - (self.location[1] - self.radius)
                    if g[1] == 0:
                        dt1 = (self.location[1] - self.radius)/self.velocity[1]
                    else:
                        dt1Tmp = math.sqrt(max((self.velocity[1]/g[1])**2 + 2*ds1/g[1], 0)) - self.velocity[1]/g[1]
                        if dt1Tmp >= 0 and dt1Tmp < dty:
                            dt1 =  dt1Tmp
                        else:
                            dt1 = - math.sqrt(max((self.velocity[1]/g[1])**2 + 2*ds1/g[1], 0)) - self.velocity[1]/g[1]
                    v1 = self.velocity[1]
                    self.velocity[1] = -(v1 + g[1]*dt1)*e
                    self.velocity[0] = sign(self.velocity[0])*max(0, abs(self.velocity[0]) - abs(v1)*f*2)
                    self.location[1] = self.radius
                    dty -= dt1
                    ds = self.velocity[1]*dty + 1/2*g[1]*dty**2
                    if abs(self.velocity[1]) <= abs(g[1]/10):
                        self.velocity[1] = 0
                        self.location[1] = self.radius
                        self.state = 2
                        if self.velocity[0] == 0:
                            self.state = 3
                    # elif self.state == 1:
                    #     self.velocity[0] = sign(self.velocity[0])*max(0, abs(self.velocity[0]) - g[0]*f*dty)

                self.location[1] = self.location[1] + ds
                self.velocity[1] = self.velocity[1] + g[1] * dty
                if self.state == 1:
                    self.velocity[1] = sign(self.velocity[1])*max(0, abs(self.velocity[1]) - abs(g[0])*f*dty)


            if self.state != 1:
                dtx = dt
                ds = self.velocity[0]*dtx + 1/2*g[0]*dtx**2
                while (self.location[0] + self.radius + ds > sizex) or (self.location[0] - self.radius + ds < 0):
                    if self.location[0] + self.radius + ds > sizex:
                        ds1 = sizex - self.location[0] - self.radius
                        if g[0] == 0:
                            dt1 = (sizex - self.location[0] - self.radius)/self.velocity[0]
                        else:
                            dt1Tmp = math.sqrt((self.velocity[0]/g[0])**2 + 2*ds1/g[0]) - self.velocity[0]/g[0]
                            # print('dt1Tmp', dt1Tmp, dtx)
                            if dt1Tmp >= 0 and dt1Tmp < dtx:
                                dt1 = dt1Tmp
                            else:
                                dt1 = - math.sqrt((self.velocity[0]/g[0])**2 + 2*ds1/g[0]) - self.velocity[0]/g[0]
                                # print('dt1',dt1)
                        v1 = self.velocity[0]
                        self.velocity[0] = -(v1 + g[0]*dt1)*e
                        self.velocity[1] = sign(self.velocity[1])*max(0, abs(self.velocity[1]) - abs(v1)*f*2)
                        self.location[0] = sizex - self.radius
                        dtx -= dt1
                        ds = self.velocity[0]*dtx + 1/2*g[0]*dtx**2
                        if abs(self.velocity[0]) <= abs(g[0]/10):
                            self.velocity[0] = 0
                            self.location[0] = sizex - self.radius
                            self.state = 1
                            if self.velocity[1] == 0:
                                self.state = 3
                        # elif self.state == 1:
                        #     self.velocity[1] = sign(self.velocity[1])*max(0, abs(self.velocity[1]) - g[1]*f*dty)
                    elif self.location[0] - self.radius + ds < 0:
                        ds1 = - (self.location[0] - self.radius)
                        if g[0] == 0:
                            dt1 = (self.location[0] - self.radius)/self.velocity[0]
                        else:
                            dt1Tmp = math.sqrt((self.velocity[0]/g[0])**2 + 2*ds1/g[0]) - self.velocity[0]/g[0]
                            if dt1Tmp >= 0 and dt1Tmp < dtx:
                                dt1 =  dt1Tmp
                            else:
                                dt1 = - math.sqrt((self.velocity[0]/g[0])**2 + 2*ds1/g[0]) - self.velocity[0]/g[0]
                        v1 = self.velocity[0]
                        self.velocity[0] = -(v1 + g[0]*dt1)*e
                        self.velocity[1] = sign(self.velocity[1])*max(0, abs(self.velocity[1]) - abs(v1)*f*2)
                        self.location[0] = self.radius
                        dtx -= dt1
                        ds = self.velocity[0]*dtx + 1/2*g[0]*dtx**2
                        if abs(self.velocity[0]) <= abs(g[0]/10):
                            self.velocity[0] = 0
                            self.location[0] = self.radius
                            self.state = 1
                            if self.velocity[0] == 0:
                                self.state = 3
                    # elif self.state == 1:
                    #     self.velocity[1] = sign(self.velocity[1])*max(0, abs(self.velocity[1]) - g[1]*f*dty)
                # print('dtx', dtx)
            # if self.state != 1:
                self.location[0] = self.location[0] + ds
                self.velocity[0] = self.velocity[0] + g[0] * dtx
                if self.state == 2:
                    self.velocity[0] = sign(self.velocity[0])*max(0, abs(self.velocity[0]) - abs(g[1])*f*dty)


        # location = [round(self.location[0]), round(self.location[1])]
        # pygame.draw.circle(surface, self.color, location, self.radius)


    def getGravityEnergy(self, masses, G):
        energy = 1/2*self.mass*(self.velocity[0]**2 + self.velocity[1]**2)
        for mass in masses:
            dis = math.sqrt((self.location[0] - mass.location[0])**2 + (self.location[1] - mass.location[1])**2)
            energy += -G*self.mass*mass.mass/dis
        self.energy = energy



    def updateGravity(self, surface, dt, masses, G):
        sizex, sizey = surface.get_size()
        dty = dt
        g = [0, 0]

        # calculate total g
        for mass in masses:
            dis = math.sqrt((self.location[0] - mass.location[0])**2 + (self.location[1] - mass.location[1])**2)
            gscale = G*self.mass*mass.mass/dis**2
            g1 = [gscale*(mass.location[0] - self.location[0])/dis, gscale*(mass.location[1] - self.location[1])/dis]
            g[0] += g1[0]
            g[1] += g1[1]

        
        # update location
        ds = self.velocity[1]*dty + 1/2*g[1]*dty**2

        self.location[1] = self.location[1] + ds
        self.velocity[1] = self.velocity[1] + dt*g[1]
        dtx = dt
        ds = self.velocity[0]*dtx + 1/2*g[0]*dtx**2
        self.location[0] = self.location[0] + ds
        self.velocity[0] = self.velocity[0] + dt*g[0]

        # midify velocity, according to energe
        energy = self.energy
        for mass in masses:
            dis = math.sqrt((self.location[0] - mass.location[0])**2 + (self.location[1] - mass.location[1])**2) 
            energy -= -G*self.mass*mass.mass/dis

        if energy > 0:
            svelocity = math.sqrt(2*energy/self.mass)
            curentVelocity = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
            if curentVelocity <= 0:
                self.velocity = [svelocity*(mass.location[0] - self.location[0]), svelocity*(mass.location[1] - self.location[1])]
            else:
                scale = svelocity/curentVelocity
                self.velocity = [self.velocity[0]*scale, self.velocity[1]*scale]

        # location = [round(self.location[0]), round(self.location[1])]
        # pygame.draw.circle(surface, self.color, location, self.radius)
        # print(g, self.velocity)