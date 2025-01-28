# Create a separate colorbar axis
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
import numpy as np
def getclbr(fig, axs, img, label = "label", size = "5%", pad = 0.0 ):
    divider = make_axes_locatable(axs)
    cax = divider.append_axes("right", size= size, pad= pad)  # Adjust size and padding
    cbar = fig.colorbar(img, cax=cax)
    cbar.ax.set_ylabel(label, rotation=90, labelpad=0.1)  # Add sideways title
    return cbar

def mkclbr(name = 'obb', clrs = ["orange",   "#0b0930", "slateblue"], nrm = [0,0.5,1]):
    vals = np.linspace(0,1, len(clrs))
    colors = []
    for i in range(len(vals)):
        colors.append((vals[i],clrs[i]))
    cmap = LinearSegmentedColormap.from_list(name, colors)
    norm = TwoSlopeNorm(vmin = nrm[0], vcenter = nrm[1], vmax = nrm[2])
    return cmap, norm
