import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u

def RelativeVelocity(phi_r, d_au):
  v_E = 29.8*u.km/u.s # orbital speed of Earth [km/s]
  a_E = 1*u.AU# Astronomical Unit
  return v_E*(np.cos(phi_r) - np.sqrt((a_E/d_au)*(1-(np.power(a_E,2)/np.power(d_au,2))*np.power(np.sin(phi_r),2))))


#print(f'{RelativeVelocity(np.radians(203.74), 3.436*u.AU)}')
#print(f'{RelativeVelocity(np.radians(156.93), 3.042*u.AU)}')

#exit()

#print(f"{(1*u.AU).to(u.m)}")

# fix at 3AU
# sweep angle from 0 to 360

angles = np.linspace(0, 359, 360)
#print(f'{angles}')

v = RelativeVelocity(np.radians(angles), 3.2*u.AU)
print(f'{v}')

fig = plt.figure(figsize=(12,8))
ax = plt.subplot2grid((1,1), (0,0))
#ax.set_yscale("log", nonposy="clip")
#ax.plot(angles, v)
#ax.plot(angles, RelativeVelocity(np.radians(angles), 2.2*u.AU))
ax.plot(angles, RelativeVelocity(np.radians(angles), 4.95*u.AU))
ax.plot(angles, RelativeVelocity(np.radians(angles), 5.46*u.AU))

plt.tight_layout()
plt.show()
