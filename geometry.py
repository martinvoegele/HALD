import numpy as np

def dist_point_line(p,a,n):
    """Calculates the distance of a point to a line
    
    :Arguments:
        *p: (x0,y0,z0) numpy array, One point in space
        *a,n: numpy array, point and vector defining the line
        
    :Returns:
        *distance: The distance between the point and the line
    """
    
    distance = (a-p)-np.dot((a-p),n)*n
    
    return np.linalg.norm(distance)
