# Overlays and Scales two txt data files
from matplotlib import pyplot as pylt
import seaborn as sns
import numpy as np
from pybaselines.whittaker import asls
import os


fileA = np.loadtxt(r"C:\Users\anwar\OneDrive\Desktop\NewFoS\New (Summer) Data\Raman 7_10_25\GeTe2 5 Layer 2000rpm 200uL dep 7_10_25.txt") #Use file paths only
fileB = np.loadtxt(r"C:\Users\anwar\OneDrive\Desktop\NewFoS\New (Summer) Data\Raman 7_14_25\EDA attempt 1.txt")
#fileC as needed

# Array declaration blocks
shiftA = fileA[:,0] # x axis
intensityA = fileA[:, 1] # y axis

shiftB = fileB[:,0] # x axis
intensityB = fileB[:, 1] # y axis

def normalize_array(y): #simple min-max normalization 
    min = np.min(y)
    max = np.max(y)
    return ((y - min) / (max - min))

def baseline_raman(y): #easy, standard baselining function
    baseline, params = asls(y)
    return y - baseline

IA_corrected = baseline_raman(intensityA)
IB_corrected = baseline_raman(intensityB)

IA_normal = normalize_array(IA_corrected) #Graph these for the y axis. IA = IntensityA
IB_normal = normalize_array(IA_corrected)

# IA_normal = IA_normal + x
# IB_normal = IB_normal + x (replace x with a value to shift the spectras up or down)

pylt.plot(shiftA, IA_normal, label='GeTe2', color='red') # Plots files, also assigns a legend name and line color
pylt.plot(shiftB, IB_normal, label='Ge15Te85 Solution', color='blue')

pylt.xlabel("Raman shift (cm⁻¹)")
pylt.ylabel("Intensity (a.u.)")
pylt.title("Raman")

pylt.legend(loc='lower left') #calls the legend and asserts its location
pylt.show()




fileA.close() # Closes txt files at the end
fileB.close()
