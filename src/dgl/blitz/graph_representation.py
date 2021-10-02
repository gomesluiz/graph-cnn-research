import dgl
import numpy as np
import torch

g = dgl.graph([0, 0, 0, 0, 0], [1, 2, 3, 4, 5])
print(g.edges())