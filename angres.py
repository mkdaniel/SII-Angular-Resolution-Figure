"""
Broken axis example, where x-axis is compressed
"""
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import matplotlib
matplotlib.rcParams.update({'font.size':20})

xmin = 100
xmax = 1e9
ymin = 0.01
ymax = 1e6

#plt.figure(figsize=(12,6))
#plt.subplots_adjust(left=0.11, right=0.97, top=0.96, bottom=0.11, wspace=0.04, hspace=0.2)
f, (ax, ax2) = plt.subplots(1, 2, sharey=True, figsize=(16,9))
#f.set_figheight(9)
#f.set_figwidth(16)
f.subplots_adjust(left=0.075, right=0.97, top=0.96, bottom=0.085, wspace=0.04, hspace=0.2)
ax.set_xscale("log", nonposx='clip')
ax2.set_xlabel(r"Wavelength $\lambda$  [nm]")
ax.set_yscale("log", nonposy='clip')
ax.set_ylabel(r"Angular Scale $\theta$ [mas]")
ax.axis([xmin, xmax, ymin, ymax])
ax2.set_xscale("log", nonposx='clip')
ax2.set_yscale("log", nonposy='clip')
ax2.axis([xmin, xmax, ymin, ymax])
#f.grid(which='both')

lo=420
hi=500
#pltNSII = ax.plot([lo,hi], [0.535, 0.803], marker='^', color='black', label='NSII')
pltNSII = ax.fill_between(range(lo, hi), [(3600*1000*180/np.pi)*1.22*x*1e-9/10 for x in range(lo, hi)], [(3600*1000*180/np.pi)*1.22*x*1e-9/188 for x in range(lo, hi)], interpolate=True, facecolor='grey', alpha=0.3, label='NSII')
ax.text(450, 6, 'NSII', rotation=90, va='center', ha='left', fontsize=18)

pltVTS = ax.plot(450, 0.15*1000*3600, marker='h', color='black') # pixel PSF
ax.text(470., 0.13*1000*3600, "IACT PSF", fontsize=18)
ax.plot(450, 0.66, marker='.', color='black', markersize=12) # T14
ax.plot(450, 0.9, marker='.', color='black', markersize=12) # T13
ax.plot(450, 1.02, marker='.', color='black', markersize=12) # T23
ax.plot(450, 1.12, marker='.', color='black', markersize=12) # T24
ax.plot(450, 1.14, marker='.', color='black', markersize=12) # T12
ax.plot(450, 1.39, marker='.', color='black', markersize=12) # T34
VTS_logo = mpimg.imread('VERITAS_logo.png')
imagebox = OffsetImage(VTS_logo, zoom=0.1)
imagebox.image.axes = ax
ab = AnnotationBbox(offsetbox=imagebox, xy=(450, 0.5*(0.66+1.39)), frameon=False)
ax.add_artist(ab)

# asteroid occultations
plImprinetta = ax.errorbar(470, 0.125, xerr=60, yerr=[[0.021], [0.022]], fmt='*', color='black', markersize=12, label='Imprinetta')
plPenelope = ax.errorbar(450, 0.094, xerr=70, yerr=[[0.01], [0.009]], fmt='*', color='black', markersize=12)
ax.text(x=540, y=0.1, s='asteroid occultations')

# lunar occultations
lo=370
hi=800
ax.fill_between(range(lo, hi), [0.5 for x in range(lo, hi)], [1 for x in range(lo, hi)], interpolate=True, color="darkgrey", hatch='x', edgecolor='darkgrey', alpha=0.6, label='Lunar')
ax.text(x=800, y=0.5, s='lunar occultation\nlimit', va='center')

pltCTAS = ax.fill_between(range(400, 600), [(3600*1000*180/np.pi)*1.22*x*1e-9/68 for x in range(400, 600)], [(3600*1000*180/np.pi)*1.22*x*1e-9/2503.8 for x in range(400, 600)], interpolate=True, facecolor='blue', alpha=0.3, label='CTA-S')
ax.text(400, 0.065, 'CTA-S', rotation=10, fontsize=18)
pltCTAN = ax.fill_between(range(400, 600), [(3600*1000*180/np.pi)*1.22*x*1e-9/71.56 for x in range(400, 600)], [(3600*1000*180/np.pi)*1.22*x*1e-9/854.7 for x in range(400, 600)], interpolate=True, facecolor='b', alpha=0.3, label='CTA-N')
ax.text(410, 0.2, 'CTA-N', rotation=10, fontsize=18)
CTA_logo = mpimg.imread('CTA_Logo.png')
imagebox = OffsetImage(CTA_logo, zoom=0.1)
imagebox.image.axes = ax
ab = AnnotationBbox(offsetbox=imagebox, xy=(300, 0.35), frameon=False)
ax.add_artist(ab)

pltCHARA = ax.fill_between(range(551, 2200), [(3600*1000*180/np.pi)*1.22*x*1e-9/34.07 for x in range(551, 2200)], [(3600*1000*180/np.pi)*1.22*x*1e-9/330.66 for x in range(551, 2200)], interpolate=True, facecolor='green', alpha=0.3, label='CHARA')
ax.text(700., 2.5, "CHARA", va='baseline', ha='left', rotation=10, fontsize=18)
lmin = 1220
lmax=2190
pltVLTI = ax.fill_between(range(lmin, lmax), [(3600*1000*180/np.pi)*1.22*x*1e-9/47 for x in range(lmin, lmax)], [(3600*1000*180/np.pi)*1.22*x*1e-9/130 for x in range(lmin, lmax)], interpolate=True, facecolor='yellow', alpha=0.3, label='VLTI')
#ax.text(1220., 2.2, "VLTI", rotation=30)
ax.text(1500., 4.5, "VLTI", rotation=10, fontsize=18)

pltHubble = ax.plot(500, 1000*0.05, marker='o', color='g', markersize=6, label='Hubble')
ax.text(520., 45., "Hubble Space Telescope", fontsize=12)

#SMA = http://sma1.sma.hawaii.edu/specs.html
#GHz = np.array([230, 345, 400])
#wave = 3e8/GHz
# baselines 3-509m
#pltSMA = ax2.fill_between(wave, 1.22*wave/8, 1.22*wave/509, interpolate=True, facecolor='darkcyan', alpha=0.2, label='SMA')
#ax2.text(x=3e8/345, y=1000*0.3, s="SMA", rotation=90)

large = int(0.0003448276/1e-9)
small = int(0.03/1e-9)
GHz = np.array([100,150,183,230,345,460,650,870])
AR = np.array([12.5, 8.4, 6.8, 5.4, 3.6, 2.7, 1.9, 1.4])
MRS = np.array([66.7, 44.5, 36.1, 29, 19.3, 14.5, 10.3,7.7])
pltALMA7m = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2, label='ALMA')
AR = np.array([3.4, 2.3, 1.8, 1.5, 1.0, 0.74, 0.52, 0.39])
MRS = np.array([28.5, 19.0, 15.4, 12.4, 8.3, 6.2, 4.4, 3.3])
pltALMAC431 = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2)
AR = np.array([2.3,1.5,1.2,1.0,0.67,0.5,0.35,0.26])
MRS = np.array([22.6,15.0,12.2,9.8,6.5,4.9,3.5,2.6])
pltALMAC432 = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2)
AR = np.array([1.4,0.94,0.77,0.62,0.41,0.31,0.22,0.16])
MRS = np.array([16.2,10.8,8.7,7.0,4.7,3.5,2.5,1.9])
pltALMAC433 = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2)
AR = np.array([0.92,0.61,0.50,0.40,0.27,0.20,0.14,0.11])
MRS = np.array([11.2,7.5,6.1,4.9,3.3,2.4,1.7,1.3])
pltALMAC434 = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2)
AR = np.array([0.54,0.36,0.30,0.24,0.16,0.12,0.084,0.063])
MRS = np.array([6.7,4.5,3.6,2.9,1.9,1.5,1.0,0.77])
pltALMAC435 = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2)
AR = np.array([0.31,0.20,0.16,0.13,0.089,0.067,0.047,0.035])
MRS = np.array([4.1,2.7,2.2,1.8,1.2,0.89,0.63,0.47])
pltALMAC436 = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2)
AR = np.array([0.21,0.14,0.11,0.092,0.061,0.046,0.033,0.024])
MRS = np.array([2.6,1.7,1.4,1.1,0.75,0.56,0.40,0.30])
pltALMAC437 = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2)
GHz = np.array([100,150,183,230,345])
AR = np.array([0.096,0.064,0.052,0.042,0.028])
MRS = np.array([1.4,0.95,0.77,0.62,0.41])
pltALMAC438 = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2)
GHz = np.array([100,150,183,230])
AR = np.array([0.057,0.038,0.031,0.025])
MRS = np.array([0.81,0.54,0.44,0.35])
pltALMAC439 = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2)
AR = np.array([0.042,0.028,0.023,0.018])
MRS = np.array([0.50,0.33,0.27,0.22])
pltALMAC4310 = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='darkcyan', alpha=0.2)
#ax.text(5e5, 1e2, "ALMA", rotation=30)
# why suddenly become offset in y axis?
ax2.text(5e5, 1e3, "ALMA", rotation=30, fontsize=18)

#min https://science.nrao.edu/facilities/vla/docs/manuals/oss/performance/resolution
GHz = np.array([0.074, 0.35, 1.5, 3.0, 6.0, 10.0, 15.0, 22.0, 33.0, 45.0])
AR = np.array([24,5.6,1.3,0.65,0.33,0.2,0.13,0.089,0.059,0.043]) #A
MRS = np.array([20000,4150,970,490,240,145,97,66,44,32]) #D
pltVLA = ax2.fill_between(3e8/GHz, 1000*AR, 1000*MRS, interpolate=True, facecolor='red', alpha=0.3, label="VLA")
ax2.text(2e7, 10*100., "VLA", rotation=30, fontsize=18)
#VLA max
#GHz = np.array([0.0745,0.34,1.73,5.0,8.8,15.4,24.0,50.0])
# EVLA
#GHz = np.array([0.074,0.33,1.5,3.0,6.0,10.0,15.0,22.0,33.0,45.0])
#http://ngvla.nrao.edu/page/refdesign
#GHz = np.array([2.4,8,16,27,41,93])
#AR = np.array([26,8,4,2.3,1.5,0.7]) 
#MRS = np.array([24.4,7.3,3.7,2.2,1.4,0.6]) # arcmin 
#pltngVLA = ax2.fill_between(3e8/GHz, AR, 60*1000*MRS, interpolate=True, facecolor='red', alpha=0.3, label="ngVLA")
#https://ngvla.nrao.edu/page/performance
GHz = np.array([2.4,8,16,27,41,93])
GHz = np.array([2.4,8,16,27,41,93])
# fov [arcmin]
fov = np.array([24.3, 7.3, 3.6, 2.2, 1.4, 0.6])
# resolution of max. baseline [mas]
maxres = np.array([2.91, 0.87, 0.44, 0.26, 0.17, 0.07])
pltngVLA = ax2.fill_between(3e8/GHz, 60*1000*fov, maxres, interpolate=True, 
facecolor='red', alpha=0.3, label="ngVLA")
ax2.text(2e7, 5*10., "ngVLA", rotation=30, fontsize=18)

#VLBA max
GHz = np.array([90,50,21,18,13,6,4,2,1,0.7,0.3])
AR = np.array([22,12,5,4.3,3.2,1.4,0.85,0.47,0.32,0.17,0.12])
pltVLBA = plt.plot(1e9*GHz/100, AR, marker='o', color='darkred', label='VLBA')
# VLBI
#http://www.evlbi.org/user_guide/res.html
GHz = np.array([90,18,6,3.6,1.3,0.7])
AR = np.array([19,3,1,0.7,0.25,0.13])
pltVLBI = ax2.plot(1e9*GHz/100, AR, marker='^', color='darkred', label='EVN+VLBA')
#ax2.text(7e6, 0.35, "EVN+VLBA", rotation=30, fontsize=18)
ax2.text(1e8, 1, "EVN+VLBA", rotation=30, fontsize=18)

# EHT
M87 = mpimg.imread('M87.jpg')
imagebox = OffsetImage(M87, zoom=0.2)
imagebox.image.axes = ax2
ab = AnnotationBbox(offsetbox=imagebox, xy=(6.5e5, 0.047), frameon=False)
ab.set_zorder(1)
ax2.add_artist(ab)
# https://eventhorizontelescope.org/technology
# Baseline @230GHz @345GHz
# LMT - SMT 140uas 93uas
a = 3e8/230e9/1e-9
b = 3e8/340e9/1e-9
#print(f'{a} {b}')
ax2.plot(a, 140e-3, marker='d', color='white', markersize=8) # LMT - SMT
ax2.plot(b, 93e-3, marker='d', color='white', markersize=8) # LMT - SMT
# Hawaii - SMT 58uas 39uas
ax2.plot(a, 58e-3, marker='d', color='white', markersize=8) # LMT - SMT
ax2.plot(b, 39e-3, marker='d', color='white', markersize=8) # LMT - SMT
# Hawaii - ALMA 28uas 19uas
ax2.plot(a, 28e-3, marker='d', color='white', markersize=8) # LMT - SMT
ax2.plot(b, 19e-3, marker='d', color='white', markersize=8) # LMT - SMT
# Plateau de Bure - South Pole 23uas 15uas
ax2.plot(a, 23e-3, marker='d', color='white', markersize=8) # LMT - SMT
ax2.plot(b, 15e-3, marker='d', color='white', markersize=8) # LMT - SMT
#ax2.text(9.5e5, 50e-3, "EHT", rotation=90, color='white', fontsize=18)
ax2.text(1e6, 1.1e-2, "EHT", color='white', fontsize=18)

#ax.plot(pts)
#ax2.plot(pts)
# zoom in
ax.set_xlim(xmin, 2500) # outliers only
ax2.set_xlim(2e5, xmax) # most of the data

# hide the spines between ax and ax2
ax.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax.yaxis.tick_left()
ax.tick_params(labeltop=False) # don't put ticks at the top
ax2.yaxis.tick_right()

# for cut out diagonal lines a bit more work is needed
# in axis coordinates (always 0-1) spine endpoints are at (0,0), (0,1), (1,0), (1,1)
# thus we need to put the diagonals in the appropriate corners of each axis, using the right transform and disable clipping
# this way if we vary the distance between plots using the f.subplots_adjust(hspace=...) or plt.subplot_tool() the diagonal lines will move accordingly, staying at the tips of the spines they are breaking
d=0.01 # how big to make the diagonal lines
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((1-d, 1+d), (1-d, 1+d), **kwargs) # top left diagonal
ax.plot((1-d, 1+d), (-d, +d), **kwargs) # top right diagonal

kwargs.update(transform=ax2.transAxes) # switch to bottom axes
ax2.plot((-d, +d), (1-d, 1+d), **kwargs) # bottom left diagonal
ax2.plot((-d, +d), (-d, +d), **kwargs) # top right diagonal

xmin=150
xmax=450
pl1m = ax.hlines(y=113.24, xmin=xmin, xmax=xmax, label='1m', linestyle='-')
pl10m = ax.hlines(y=11.324, xmin=xmin, xmax=xmax, label='10m', linestyle='-.')
pl1100m = ax.hlines(y=1.1324, xmin=xmin, xmax=xmax, label='100m', linestyle='--')
pl1km = ax.hlines(y=0.11, xmin=xmin, xmax=xmax, label='1km', linestyle=':')
ax.text(xmin, 500, r'$\theta \propto \lambda / d$')
ax.text(xmin, 115, "d=1m", fontsize=12)
ax.text(xmin, 12, "d=10m", fontsize=12)
ax.text(xmin, 1.3, "d=100m", fontsize=12)
ax.text(xmin, 0.13, "d=1000m", fontsize=12)

xmin=4e6
xmax=1e7
pl1km = ax2.hlines(y=1010, xmin=xmin, xmax=xmax, label='1km', linestyle='-')
pl10km = ax2.hlines(y=101, xmin=xmin, xmax=xmax, label='10km', linestyle='-.')
pl100km = ax2.hlines(y=10.1, xmin=xmin, xmax=xmax, label='100km', linestyle='--')
pl1000km = ax2.hlines(y=1.01, xmin=xmin, xmax=xmax, label='1000km', linestyle=':')
ax2.text(xmin, 1010, "d=1km", fontsize=12)
ax2.text(xmin, 101, "d=10km", fontsize=12)
ax2.text(xmin, 10.1, "d=100km", fontsize=12)
ax2.text(xmin, 1.01, "d=1000km", fontsize=12)
ax2.text(xmin, 0.101, "d=10000km", fontsize=12)

plt.savefig(fname='CTA-AngResVsWavelength.jpg')
plt.show()
