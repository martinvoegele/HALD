import numpy as np
import numpy.linalg as la


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

def Tilt(calpha):
    """
    Purpose:
    calculate the angle between the principal axis of one alpha
    helix and the z-axis
    The principal axis of the helix is calculated using the MDAnalysis
    function
    
    Arguments:
    calpha: alpha atoms object within MDAnalysis
    """
    P1,P2,P3=calpha.principal_axes()
    zaxis=np.array([0,0,1])
    
    """angle"""
    cosang = np.dot(P1, zaxis)d
    sinang = la.norm(np.cross(P1, zaxis))
    return np.arctan2(sinang, cosang)
