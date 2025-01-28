import os
import numpy as np

class gread:
    def __init__(self, fname = "./grid.out"):
        self.fname = fname
        
        with open(self.fname, 'r') as fle:
            i = 1
            xl = []
            xr = []
            for line in fle:
                ln = line.split()
                try:
                    if ln[1] == "DIMENSIONS:":
                        self.dim = int(ln[2])
                except IndexError:
                    pass
                try:
                    if ln[1] == "X1:":
                        self.Nx = int(ln[-4])
                except IndexError:
                    pass
                try:
                    if ln[1] == "X2:":
                        self.Ny = int(ln[-4])
                except IndexError:
                    pass
                try:
                    if ln[1] == "X3:":
                        self.Nz = int(ln[-4])
                except IndexError:
                    pass
                
                try:
                    if ln[0] != "#" and len(ln) == 3 and i < (self.Nx + 1) :
                        xl.append(float(ln[1]))
                        xr.append(float(ln[2]))
                        i = i+1
                except IndexError:
                    pass
        with open(self.fname, 'r') as fle:
            j = 0
            yl = []
            yr = []
            for line in fle:
                ln = line.split()
                try:
                    if ln[0] != "#" and len(ln) == 3:
                        j = j + 1
                        if self.Nx < j < (self.Nx + self.Ny +1):
                            yl.append(float(ln[1]))
                            yr.append(float(ln[2]))
                    
                except IndexError:
                    pass
        with open(self.fname, 'r') as fle:
            k = 0
            zl = []
            zr = []
            for line in fle:
                ln = line.split()
                try:
                    if ln[0] != "#" and len(ln) == 3:
                        k = k+1
                        if self.Nx + self.Ny < k < (self.Nx + self.Ny + self.Nz +1):
                            zl.append(float(ln[1]))
                            zr.append(float(ln[2]))
                except IndexError:
                    pass
        self.xl = np.array(xl)
        self.xr = np.array(xr)
        self.x = (self.xl + self.xr )/2

        self.yl = np.array(yl)
        self.yr = np.array(yr)
        self.y = (self.yl + self.yr)/2

        self.zl = np.array(zl)
        self.zr = np.array(zr)
        self.z = (self.zl + self.zr)/2

        self.limits = np.array( [ self.xl[0], self.xr[-1], self.yl[0], self.yr[-1], self.zl[0], self.zr[-1]])

