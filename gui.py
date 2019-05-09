import matplotlib as mpl
import numpy as np
from numpy import array
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
import networkx as nx

# Create a canvas
w, h = 1000, 500
window = tk.Tk()
window.title("Instant Insanity")
canvas = tk.Canvas(window, width=w, height=h)
canvas.pack()
 
l = [1.0, 2.0, 3.0]
a = array(l)
print(a)

# Let Tk take over
tk.mainloop()