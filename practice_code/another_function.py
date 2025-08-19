from practice_code.yet_another_function import yet_another_function

def wrapper_for_yet_another_function(x,y,z):
    x *= 10
    y = y**2
    y[y>850] = -100
    z /= 2
    x_out,y_out,z_out = yet_another_function(x,y,z)
    return x_out,y_out,z_out