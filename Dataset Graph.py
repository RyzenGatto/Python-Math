# Overlays and Scales two txt data files
from matplotlib import pyplot as pylt
import seaborn as sns
import numpy as np
from scipy.signal import find_peaks
from scipy.interpolate import interp1d
from pybaselines.whittaker import asls
import os


fileA = np.loadtxt(r"C:\Users\anwar\Desktop\NEWFOS DR.LUCAS GROUP FOLDER\Anwar Full Data (7-19\New (Summer) Data\Raman 7_10_25\GeTe2 3 Layer 200uL 2000rpm Dep 7_10_25.txt") #Use file paths only
fileB = np.loadtxt(r"C:\Users\anwar\Desktop\NEWFOS DR.LUCAS GROUP FOLDER\Anwar Full Data (7-19\New (Summer) Data\Raman 7_14_25\Raman_Ge15Te85 Solution_7_3_25.txt")
#fileC = np.loadtxt(r"C:\Users\anwar\Desktop\NEWFOS DR.LUCAS GROUP FOLDER\Anwar Full Data (7-19\New (Summer) Data\Raman 7_14_25\Butylamine.txt")

lableA = 'GeTe2 5 layer'
lableB = 'Ge15Te85 in Butylamine'

# Array declaration blocks
shiftA = fileA[:,0] # x axis
intensityA = fileA[:, 1] # y axis

shiftB = fileB[:,0] # x axis
intensityB = fileB[:, 1] # y axis

'''
shiftButyl = fileC[:,0] # x axis
intensityButyl = fileC[:, 1] # y axis
'''

def normalize_array(y):
    min = np.min(y)
    max = np.max(y)
    return ((y - min) / (max - min))

def baseline_raman(y): #easy, standard baselining function
    baseline, params = asls(y, lam=1e3, p=0.001)
    return y - baseline

def peakpick(y):
    peaks, properties = find_peaks(y, prominence=0.1, distance=5) #Turn prominance up with messy data. Distance is low since we're plotting multiple spectras
    print(peaks)
    return peaks

def background_sub(backX, backY, foreX, foreY):
    # Baseline correction
    back_corr = baseline_raman(backY)
    fore_corr = baseline_raman(foreY)

    # Normalize both
    back_norm = normalize_array(back_corr)
    fore_norm = normalize_array(fore_corr)

    # Interpolate background to match foreground x-axis
    interp_func = interp1d(backX, back_norm, kind='linear', bounds_error=False, fill_value=0)
    back_interp = interp_func(foreX)

    # Subtract and baseline again
    result = fore_norm - back_interp
    return baseline_raman(result)



IA_corrected = baseline_raman(intensityA)
IB_corrected = baseline_raman(intensityB)


#Final Y axis!!!
IA_normal = normalize_array(IA_corrected) #Graph these for the y axis. IA = IntensityA
IB_normal = normalize_array(IB_corrected)

#IB_normal = background_sub(shiftButyl, intensityButyl, shiftB, intensityB) # This line should ONLY be used if fileC is a background and B is a foreground spectra

# (replace x with a value to shift the spectras up or down)
# IA_normal = IA_normal + x
# IB_normal = IB_normal + x 

# Peak picking block
peakA = peakpick(IA_normal)
peakB = peakpick(IB_normal)

pylt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12}) #Global Paramaters for fontsize and font, duh

#Plot spectra lines
pylt.plot(shiftA, IA_normal, label=lableA, linestyle='-', linewidth=2, color='red') # Plots files, also assigns a legend name and line color
pylt.plot(shiftB, IB_normal, label=lableB, linestyle='-', linewidth=2, color='blue')

#Plot peak values
pylt.plot(shiftA[peakA], IA_normal[peakA], "x")
pylt.plot(shiftB[peakB], IB_normal[peakB], "x")

for i in peakA:
    x = shiftA[i]
    y = IA_normal[i]
    pylt.annotate(f"{x:.0f}", (x, y), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=9, color='black')

# Annotate peaks for File 2 (add more as needed)
for i in peakB:
    x = shiftB[i]
    y = IB_normal[i]
    pylt.annotate(f"{x:.0f}", (x, y), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=9, color='black')



pylt.xlabel("Raman shift (cm⁻¹)", fontsize=14)
pylt.ylabel("Intensity (a.u.)", fontsize=14)

pylt.legend(loc='upper right', fontsize=12) #calls the legend and asserts its location
pylt.title("Raman")

pylt.show()
