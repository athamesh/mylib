import os
import numpy as np
import glob
class tm:
    def __init__(self):
        self.dfn = "./dbl.out"
        self.ffn = "./flt.out"
        self.pfn = "./ppm.out"

        ffnames = []
        ffnum = []
        for ff in glob.glob("vx3.*.flt"):
            ffnames.append(ff)
            ffnum.append(int(ff[4:8]))
        self.ffnames = (sorted(ffnames))
        self.ffnum = (sorted(ffnum))
        
        pfnames = []
        pfnum = []
        for pf in glob.glob("particles*_ch00.flt"):
            pfnames.append(pf)
            pfnum.append(int(pf[10:14]))
        self.pfnames = (sorted(pfnames))
        self.pfnum = (sorted(pfnum))

    def get_header(self, pfile = 'default' , lnum = 16):
        if pfile == 'default':
            pfile = self.pfnames[0]
        with open(pfile, 'rb') as f:
            buffr = f.read(600)
        lines = buffr.splitlines()
        header = []
        try:
            for i in range(lnum):
                header.append(lines[i].decode("utf-8"))
        except UnicodeDecodeError:
            print(" unicodedecodeError: Reduce lnum by 1 and try again")
        return header

    def get_ptime(self):
        time = []
        for pf in self.pfnames:
            header = self.get_header(pfile = pf)

            for line in header:
                ln = line.split()
                if ln[1] == 'time':
                    time.append(float(ln[2]))
        return np.array(time)

    def get_ftime(self):
        ftime = []
        with open(self.ffn, 'r') as fle:
            for line in fle:
                ln = line.split()
                if int(ln[0]) in self.ffnum:
                    ftime.append(float(ln[1]))
        return np.array(ftime)
