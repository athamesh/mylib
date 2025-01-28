import numpy as np

def read(fname, shape):
    ext = fname[-3:]
    if ext == "flt" or ext == "ppm":
        typd = '<f4'
    elif ext == "dbl":
        typd = '<f8'
    print(f" reading file {fname:s}")
    data = np.fromfile(fname, dtype=typd).reshape(shape)
    return data

