import numpy as np
import matplotlib.pyplot as plt

models = np.loadtxt('models.txt')

fig=plt.figure(figsize=(4, 6), dpi=200, facecolor='w', edgecolor='k')

plt.semilogx(models[:,1], models[:,0], label = 'C1', linestyle = '--')
plt.semilogx(models[:,2], models[:,0], label = 'M2', linestyle = '--')
plt.semilogx(models[:,3], models[:,0], label = 'Joint sparse')
plt.semilogx(models[:,4], models[:,0], label = 'Joint smooth')

plt.xlim(1e-4, 1e1);
plt.ylim(0, 2800);
plt.xlabel(r'Conductivity $\sigma$ (S/m)')
plt.ylabel(r'Depth (km)')
plt.gca().invert_yaxis()
plt.legend()    
plt.grid()

plt.tight_layout()
plt.savefig('models.png', dpi=200)
