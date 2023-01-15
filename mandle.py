from matplotlib import pyplot as plt
import math
import numpy as np

#define size of the dots on the graph
dotszie = 1
# how accurate do you want the "is this point in the mandlebrot set" function to be?
accuracy = 30

# how many points to draw on each axis (for example density of 10 would be 100 points total assuming xrange,yrange=1,1)
density = 300
# the degree of the mandlebrot iteration
degree = math.e

# how much to zoom in: usually xrange=2,yrange=1 would do the trick with mandlebrots.
xrange = 2
yrange = 1


def draw_point(z: complex) -> None:
    plt.plot(z.real,z.imag,marker='.', markersize=dotszie)

def is_mandlebrot(point: complex) -> bool:
    z = 0
    c = point
    for i in range(accuracy):
        try :
            z = z**degree + c
        except OverflowError:
            # if we overflowed, it DEFINETLY converges
            return False
    # distance from origin. Does this diverge?
    return (math.hypot(z.real, z.imag) < xrange*yrange)

def calc_points():
    arr = np.linspace(-1*xrange,yrange,num=density)
    for a in arr:
        for b in arr:
            c = complex(a,b)
            if(is_mandlebrot(c)):
                draw_point(c)

    # it's mandlebroting time!
    plt.grid()
    plt.axis([-1*xrange, 1, -1*yrange, yrange])
    plt.title(f'mandlebrot set of degree {degree}')
    plt.show()


calc_points()
