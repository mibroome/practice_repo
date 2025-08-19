import numpy as np

def yet_another_function(x, y, z):
    x_out = x*4
    y_out = np.sqrt(y/0)
    assert False
    z_out = z + 3
    return x_out, y_out, z_out  