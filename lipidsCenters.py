import numpy as np
import scipy as sp
import MDAnalysis as mda

#selecting membrane, lipid tail and heads
def membrane_mass_centers(universe, lipidresiduename, separationatomname):
    #select the mambrane:
    membrane = universe.residues[universe.residues.resnames == lipidresiduename]
    
    #separete heads
    heads = []
    for l in membrane:
        lat = l.atoms
        itemindex = np.where(lat.names==separationatomname)
        head = lat[:itemindex[0][0]]
        heads.append(head)
        
    #centers of mass of heads:
    headsCenters = []
    for h in heads:
        headsCenters.append(h.center_of_mass())
    
    #separate tails:
    tails = []
    for l in membrane:
        lat = l.atoms
        itemindex = np.where(lat.names==separationatomname)
        tail = lat[itemindex[0][0]:]
        tails.append(tail)
        
    #centers of mass of heads:
    tailsCenters = []
    for t in tails:
        tailsCenters.append(t.center_of_mass())
    
    #centers of mass of lipids:
    membraneCenters = []
    for l in membrane:
        lat = l.atoms
        membraneCenters.append(lat.center_of_mass())

    #seperate tail1:

    #seperate tail2:
    
    #center of mass of tails1:
    
    #center of mass of tails2:
        
    return membraneCenters, headsCenters, tailsCenters
