import pygame, math
class Ball():

    def __init__(self, radius, velocity, location, color):
        self.radius = radius
        self.velocity = velocity
        self.location = location
        self.color = color

    def update(self, surface, g, dt):
        sizex, sizey = surface.get_size()
        dty = dt
        ds = self.velocity[1]*dty + 1/2*g*dty**2
        # 碰下壁
        if self.location[1] + self.radius + ds > sizey:
            ds1 = sizey - self.location[1] - self.radius
            dt1 = math.sqrt((self.velocity[1]/g)**2 + 2*ds1/g) - self.velocity[1]/g 
            self.velocity[1] = -(self.velocity[1] + g*dt1)
            self.location[1] = sizey - self.radius
            dty -= dt1
            ds = self.velocity[1]*dty + 1/2*g*dty**2
        # 碰上壁
        elif self.location[1] - self.radius + ds < 0:
            ds1 = self.location[1] - self.radius
            dt1 = math.sqrt((self.velocity[1]/g)**2 + 2*ds1/g) + self.velocity[1]/g 
            self.velocity[1] = -(self.velocity[1] + g*dt1)
            self.location[1] = self.radius
            dty -= dt1
            ds = self.velocity[1]*dty + 1/2*g*dty**2
        self.location[1] = self.location[1] + ds
        self.velocity[1] = self.velocity[1] + g * dty

        # 碰右壁或左壁
        ds = self.velocity[0]*dt
        if self.location[0] + self.radius + ds > sizex:
            dt1 = (sizex - self.location[0] - self.radius)/self.velocity[0]
            self.location[0] = sizex - self.radius
            dt -= dt1
            self.velocity[0] = -self.velocity[0]
            ds = self.velocity[0]*dt
        elif self.location[0] - self.radius + ds < 0:
            dt1 = (self.location[0] - self.radius)/self.velocity[0]
            self.location[0] = self.radius
            dt -= dt1
            self.velocity[0] = -self.velocity[0]
            ds = self.velocity[0]*dt

        self.location[0] = self.location[0] + ds



        location = [round(self.location[0]), round(self.location[1])]
        pygame.draw.circle(surface, self.color, location, self.radius)