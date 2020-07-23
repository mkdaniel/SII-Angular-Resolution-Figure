import matplotlib.pyplot as plt, matplotlib.lines as mlines
import numpy as np

# from Ridgway
def OpticalBandwidth(dl, D):
  radians = np.sqrt(dl/D)
  return 1000*3600*np.degrees(radians) # mas

def Sampling(v, D, f):
  radians = v/(D*f)
  return 1000*3600*np.degrees(radians) # mas

def Mirror(d, D):
  radians = 2*d/D
  return 1000*3600*np.degrees(radians) # mas

def Fresnel(l, D):
  radians = np.sqrt(l/(8*D))
  return 1000*3600*np.degrees(radians) # mas

def Geometric(l, D):
  radians = np.sqrt(l/D)
  return 1000*3600*np.degrees(radians) # mas

#vts_fre = Fresnel(420e-9, 12)# less than
#vts_geo = Geometric# greater than

wavelength = 420e-9
diameter = 12
sample_rate = 4800/4
#sample_rate=300

ast_dist_ab = np.linspace(2.2, 3.2) # asteroid belt 2.2->3.2
ast_dist_ab_m = 1.5e11*ast_dist_ab

ast_dist_jup = np.linspace(4.95, 5.46) # asteroid belt 2.2->3.2
ast_dist_jup_m = 1.5e11*ast_dist_jup

fig = plt.figure(figsize=(12,8))
ax = plt.subplot2grid((1,2), (0,0)) #rows, columns
ax.set_title("Limits from Ridgway '77 (4 diffraction fringes present)")
ax.set_yscale("log", nonposy="clip")
ax.set_ylabel('Resolution [mas]')
ax.set_xlabel('Distance [AU]')

ast_dist_moon=3.78e8/1.5e11
ax.text(x=ast_dist_moon, y=1, s='Lunar')
dl = 140
#ax.plot(ast_dist_moon, OpticalBandwidth(dl=dl*1e-9,D=1.5e11*ast_dist_moon), 'bo')
#ax.plot(ast_dist_moon, OpticalBandwidth(dl=20e-9,D=1.5e11*ast_dist_moon), 'bo')
ax.vlines(ast_dist_moon, OpticalBandwidth(dl=20e-9,D=1.5e11*ast_dist_moon), OpticalBandwidth(dl=dl*1e-9,D=1.5e11*ast_dist_moon), 'b')
ax.plot(ast_dist_moon, Sampling(v=800, D=1.5e11*ast_dist_moon, f=sample_rate), 'go')
#ax.plot(ast_dist_moon, Sampling(v=800, D=1.5e11*ast_dist_moon, f=300), 'go')
#ax.plot(ast_dist_moon, Mirror(d=12,D=1.5e11*ast_dist_moon), color='grey')
ax.plot(ast_dist_moon, Fresnel(l=wavelength,D=1.5e11*ast_dist_moon), 'r^')
ax.plot(ast_dist_moon, Geometric(l=wavelength,D=1.5e11*ast_dist_moon), 'rv')

#ax.plot(ast_dist_ab, OpticalBandwidth(dl=120e-9,D=ast_dist_ab_m), color='blue')
ax.text(x=2.2, y=0.15, s='Asteroid Belt')
dl = 140
ax.fill_between(ast_dist_ab, OpticalBandwidth(dl=dl*1e-9,D=ast_dist_ab_m), OpticalBandwidth(dl=20e-9,D=ast_dist_ab_m), color='blue', alpha=0.3)
ax.text(x=2.2, y=OpticalBandwidth(dl=120e-9,D=1.5e11*2.2), s=rf'$\Delta\lambda=${dl}nm', ha='right', color='blue')
ax.text(x=2.2, y=OpticalBandwidth(dl=20e-9,D=1.5e11*2.2), s=r'$\Delta\lambda=$20nm', ha='right', va='bottom', color='blue')
#ax.plot(3.7e8/1.5e11, Sampling(v=800, D=3.7e8, f=sample_rate), 'g*') # depends on D...
#ax.plot(ast_dist, Sampling(v=20.*1e3, D=ast_dist_m, f=sample_rate), color='green') # depends on D...
#ax.plot(ast_dist, Sampling(v=50.*1e3, D=ast_dist_m, f=sample_rate), color='green', ls=':') # depends on D...
#ax.fill_between(ast_dist_ab, Sampling(v=0*1e3, D=ast_dist_ab_m, f=sample_rate), Sampling(v=50.*1e3, D=ast_dist_ab_m, f=sample_rate), color='green', alpha=0.3, interpolate=True)
v_lo=1
v_hi=50
ax.fill_between(ast_dist_ab, Sampling(v=v_hi*1e3, D=ast_dist_ab_m, f=sample_rate), Sampling(v=v_lo*1e3, D=ast_dist_ab_m, f=sample_rate), color='green', alpha=0.3, interpolate=True)
ax.text(x=3.2, y=Sampling(v=v_lo*1e3,D=1.5e11*3.2, f=sample_rate), s=f'f={sample_rate} Hz\n (v={v_lo}km/s)', va='bottom', color='green')
ax.text(x=3.2, y=Sampling(v=v_hi*1e3,D=1.5e11*3.2, f=sample_rate), s=f'f={sample_rate} Hz\n (v={v_hi}km/s)', va='top', color='green')
#ax.fill_between(ast_dist_ab, Sampling(v=50*1e3, D=ast_dist_ab_m, f=4800), Sampling(v=5.*1e3, D=ast_dist_ab_m, f=4800), color='green', alpha=0.6, interpolate=True)
#ax.text(x=3.2, y=Sampling(v=5e3,D=1.5e11*3.2, f=4800), s='f=4800 Hz\n (v=5km/s)')
ax.plot(ast_dist_ab, Mirror(d=diameter,D=ast_dist_ab_m), color='grey')
ax.text(x=2.2, y=Mirror(d=diameter,D=2.2*1.5e11), s=f'D={diameter}m', ha='right', va='center', color='grey')
#ax.hlines(y=Fresnel(l=wavelength, D=ast_dist_m), xmin=ast_dist.min(), xmax=ast_dist.max(), linestyles=':', color='red')
#ax.hlines(y=Geometric(l=wavelength, D=ast_dist_m), xmin=ast_dist.min(), xmax=ast_dist.max(), linestyles='--', color='red')
ax.plot(ast_dist_ab, Fresnel(l=wavelength,D=ast_dist_ab_m), 'r:')
ax.plot(ast_dist_ab, Geometric(l=wavelength,D=ast_dist_ab_m), 'r--')

# Imprinetta 3.436 AU from sun on 22/2/2018
#ax.plot(3.436, Sampling(v=1000*43.24, D=1.5e11*3.436, f=300), 'k*') # depends on D...
ax.plot(3.436, 0.116, 'k*')
# Penelope 3.042 AU from sun on 22/5/2018
#ax.plot(3.042, Sampling(v=1000*44.36, D=1.5e11*3.042, f=1200), 'k*') # depends on D...
ax.plot(3.042, 0.094, 'k*') # depends on D...

ax.text(x=5.0, y=0.1, s="Jupiter's Moons")
#ax.plot(ast_dist_jup, OpticalBandwidth(dl=120e-9,D=ast_dist_jup_m), color='blue')
ax.fill_between(ast_dist_jup, OpticalBandwidth(dl=120e-9,D=ast_dist_jup_m), OpticalBandwidth(dl=20e-9,D=ast_dist_jup_m), color='blue', alpha=0.3)
#ax.fill_between(ast_dist_jup, Sampling(v=46*1e3, D=ast_dist_jup_m, f=300), Sampling(v=46.*1e3, D=ast_dist_jup_m, f=4800), color='green', alpha=0.3, interpolate=True)
ax.fill_between(ast_dist_jup, Sampling(v=v_lo*1e3, D=ast_dist_jup_m, f=sample_rate), Sampling(v=v_hi*1e3, D=ast_dist_jup_m, f=sample_rate), color='green', alpha=0.3, interpolate=True)
ax.plot(ast_dist_jup, Mirror(d=12,D=ast_dist_jup_m), color='grey')
ax.plot(ast_dist_jup, Fresnel(l=wavelength,D=ast_dist_jup_m), 'r:')
ax.plot(ast_dist_jup, Geometric(l=wavelength,D=ast_dist_jup_m), 'r--')

ax2 = plt.subplot2grid((1,2), (0,1)) #rows, columns
ax2.set_yscale("log", nonposy="clip")

ast_dist_kbo = np.linspace(30, 50) # Kuiper Belt Objects 30(Neptune)->50AU
ast_dist_kbo_m = 1.5e11*ast_dist_kbo

ax2.text(x=40, y=4e-2, s="KBOs")
ax2.fill_between(ast_dist_kbo, OpticalBandwidth(dl=120e-9,D=ast_dist_kbo_m), OpticalBandwidth(dl=20e-9,D=ast_dist_kbo_m), color='blue', alpha=0.3)
#ax2.fill_between(ast_dist_kbo, Sampling(v=46*1e3, D=ast_dist_kbo_m, f=300), Sampling(v=46.*1e3, D=ast_dist_kbo_m, f=4800), color='green', alpha=0.3, interpolate=True)
ax2.fill_between(ast_dist_kbo, Sampling(v=v_lo*1e3, D=ast_dist_kbo_m, f=sample_rate), Sampling(v=v_hi*1e3, D=ast_dist_kbo_m, f=sample_rate), color='green', alpha=0.3, interpolate=True)
ax2.plot(ast_dist_kbo, Mirror(d=12,D=ast_dist_kbo_m), color='grey')
ax2.plot(ast_dist_kbo, Fresnel(l=wavelength,D=ast_dist_kbo_m), 'r:')
ax2.plot(ast_dist_kbo, Geometric(l=wavelength,D=ast_dist_kbo_m), 'r--')

ax.axis([-0.1, 6, 1e-4, 10])
ax2.axis([25, 55, 1e-4, 10])
# zoom in
ax.set_xlim(-0.1,6)
ax2.set_xlim(25,55)
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

FilterMarker = mlines.Line2D([],[], color='blue', marker='o', label='Optical Bandwidth', ls='-')
SamplingMarker = mlines.Line2D([],[], color='green', marker='o', label='Sampling Rate', ls='-')
MirrorMarker = mlines.Line2D([],[], color='grey', marker='o', label='Dish Size', ls='-')
GeometricMarker = mlines.Line2D([],[], color='red', marker='v', label='Geometrical Limit', ls='--')
FresnelMarker = mlines.Line2D([],[], color='red', marker='^', label='Fresnel Limit', ls=':')

ax2.legend(handles=[GeometricMarker, FresnelMarker, FilterMarker, SamplingMarker, MirrorMarker], loc='best')

plt.tight_layout()
plt.show()
