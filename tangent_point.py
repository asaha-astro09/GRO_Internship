import numpy as np

R0 = 8.5    #distance between sun and galactic center (in kPc)
l = float(input('Enter Galactic longitude (degrees): '))    #(in degree)  
l_rad = np.deg2rad(l)   #converting degree to radian

#R=R0*np.sin(l) (tangent point distance)

def tpd (R0,l_rad):
    R=R0*np.sin(l)
    return R
    
R = tpd(R0, l_rad)

print('Tangent point distance of the gas cloud is =', R, 'kPc')
