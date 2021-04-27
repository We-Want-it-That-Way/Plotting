#!/usr/bin/env python
# coding: utf-8

# Radio High Energy Pulsars collected by @Ginna Mystica, Catherine,Ashwin

# In[1]:


import pandas as pd
import numpy as np
import math
G={'Name of pulsar':['J0205+6449','J0218+4232','J0437-4715','J0534+2200','J1105-6107','J1124-5916','J1617-5055','J1930+1852','J2124-3358','J2229+6114'],'po':[0.06571592849324,0.00232309053151224,0.005757451936712637,0.0333924123,0.0632021309179,0.13547685441,0.069356847,0.136855046957,0.00493111494309662,0.05162357393],'pdot':[1.93754256e-13,7.73955e-20,5.729215e-20,4.20972e-13,1.584462e-14,7.52566e-13,1.351e-13,7.5057e-13,2.05705e-20,7.827e-14],'D in Kpc':[3.200,3.150,0.157,2.000,2.360, 5.000, 4.743, 7.000, 0.410, 3.000],'Age':[5.37e+03,4.76e+08,1.59e+09,1.26e+03,6.32e+04,2.85e+03, 8.13e+03, 2.89e+03, 3.8e+09, 1.05e+04],'R_L':[0,466.36,13.52,2200.00,0,0,0,0, 2.86, 13.50],'B_s':[3.61e+12,4.29e+08,4.29e+08,3.79e+12,1.01e+12,1.02e+13,3.1e+12,1.03e+13,3.22e+08,2.03e+12],
'Edot':[2.7e+37,2.4e+35,1.2e+34,4.5e+38,2.5e+36,1.2e+37,1.6e+37,1.2e+37,6.8e+33,2.2e+37],
'Edot2':[2.6e+36,2.5e+34,4.8e+35,1.1e+38,4.4e+35,4.8e+35,7.1e+35,2.4e+35,2.4e+35,2.5e+36],
'B_sI':[3.61e+12,4.27e+08,2.85e+08,3.79e+12,0,0,0,0, 1.92e+08,0],
'B_Lc':[1.19e+05,3.21e+05,2.85e+04,9.55e+05,3.76e+04,3.85e+04, 8.70e+04, 3.75e+04, 2.52e+04, 1.39e+05]}
l=pd.DataFrame(G)
l.to_csv('High_energy_pulsar.csv')
l


# Non Radio Pulsars collected by@Anjali Shivani, Ashwin

# In[2]:


import pandas as pd
import numpy as np
import math
A={'Name of pulsar':['J0537-6910','J0633+1746','J0543+2329','J1811-1925','J1846-0258','J0628+0909','J0633+1746','J0636-4549','J1811-4930','J1812-1718'],'po':[0.0161222220245,0.2370994416923,0.245983683333,0.06466700,0.32657128834,3.763733080,0.2370994416923,1.98459736713,1.4327041968,1.20537444137],'pdot':[5.1784338e-14,1.097087e-14,1.541956e-14,4.40e-14,7.107450e-12,0.5479e-15,1.097087e-14,3.1722e-15,2.254e-15,1.9077e-14],'D in Kpc':[49.700,0.190,1.565,5.000,5.800,1.771,0.190,0.383,1.447,3.678],'R_L':[0,0,71.03,0,0,0,0,0,0,0],'Age':[4.93e+03,3.42e+05,2.53e+05,2.33e+04,728,3.59e+07,3.42e+05,9.91e+06,1.01e+07,1e+06],'B_s':[9.25e+11,1.63e+12,1.97e+12,1.71e+12,4.88e+13,8.35e+11,1.63e+12,2.54e+12,1.82e+12,4.85e+12],'Edot':[4.9e+38,3.2e+34,4.1e+34,6.4e+36,8.1e+36,1.1e+31,3.2e+34,1.6e+31,3.0e+31,4.3e+32],'Edot2':[2.0e+35,9.0e+35,1.7e+34,2.6e+35,2.4e+35,3.6e+30,9.0e+35,1.1e+32,1.4e+31,3.2e+31],'B_sI':['NaN',1.63e+12,1.97e+12,'NaN','NaN','NaN',1.63e+12,'NaN','NaN','NaN'],'B_Lc':[2.07e+06,1.15e+03,1.24e+03,5.92e+04,1.31e+04,4.09e+00,1.15e+03,3.05e+00,5.80e+00,2.60e+01]}
p=pd.DataFrame(A)
p.to_csv('Non_Radio_pulsar.csv')
p


# Magnetors collected by@Ram Kumar, Aniket

# In[3]:


import pandas as pd
import numpy as np
import math
R={'Name of pulsar':['J0100-7211','J0525-6607','J1708-4008','J1808-2024','J1809-1943','J1841-0456','J1907+0919','J2301+5852','J1745-2900','J0525-6607'],'po':[8.020392, 0.35443759451370,11.0062624,7.55592,5.540742829,11.7889784, 5.198346,6.9790709703,3.763733080,8.0470],'pdot':[1.88e-11, 7.36052e-17,1.960e-11,5.49e-10,2.8281e-12,4.092e-11,9.2e-11,4.7123e-13,1.756e-11,6.5e-11],'D in Kpc':[59.700, 1.841,3.800,13.000,3.600,9.600,'NaN',3.300,8.300,'NaN'],'R_L':[0, 66.09,0,0,0,0,0,0,0,0],'Age':[6.76e+03,7.63e+07,8.9e+03,218,3.1e+04,4.57e+03,895,2.35e+05,3.4e+03,1.96e+03],'B_s':[3.93e+14,1.63e+11,4.7e+14,2.06e+15,1.27e+14,7.03e+14,7e+14,5.8e+13,2.6e+14,7.32e+14],'Edot':[1.4e+33,6.5e+31,5.8e+32,5.0e+34,6.6e+32,9.9e+32,2.6e+34,5.5e+31,1.3e+34,4.9e+33],'Edot2':[4.0e+29,1.9e+31,4.0e+31,3.0e+32,5.1e+31,1.1e+31,'NaN',5.0e+30,1.9e+32,'NaN'],'B_sI':['NaN', 1.62e+11,'NaN',2.06e+15, 1.27e+14,'NaN','NaN', 5.80e+13,2.60e+14,'NaN'],'B_Lc':[7.14e+00,3.44e+01,3.30e+00,4.48e+01,6.98e+00,4.02e+00,4.67e+01,1.60e+00,4.57e+01,1.32e+01]}
c=pd.DataFrame(R)
c.to_csv('magnetor_pulsar.csv')
c


# Main code(high pulsar + Non Radio + Magnetors)

# In[4]:


o=pd.concat([l,p,c],ignore_index=True)
o.to_csv('Combined_data.csv')
o


# ## $B_{Lc} = B_{s}(\frac{\omega R}{c})^{3} = 9.2 \times (\frac{P}{s})^{\frac{-5}{2}}(\frac{\dot{P}}{10^{-15}})^{\frac{-1}{2}}Gauss$

# In[5]:


a=o['B_Lc']
b=o['pdot']
c=o['po']
d=o['B_s']
import matplotlib.pyplot as plt
import numpy as np
import matplotlib 
matplotlib.rc('xtick', labelsize=12) 
matplotlib.rc('ytick', labelsize=12) 
plt.rcParams.update({'font.size': 15})
f = plt.figure()
f.set_figwidth(7)
f.set_figheight(7)
x= np.log(((c)**(-5))*(b**(-1))) # normalized by squaring both sides of B_Lc and P*Pdot relation
y = np.log(a**2)*(10**(-15/2)) # multiplied by a factor e-15/2 (check actaul equation of relation for ref)

plt.title('$B_{Lc}^{2}$ vs $P^{-5}(\dot{P})^{-1}$')
plt.xlabel('$log(P^{-5}(\dot{P})^{-1})$')
plt.ylabel('$log(B_{Lc}^{2})$')
plt.scatter(x,y)

#plots after sorting the points
plt.scatter(np.sort(x),np.sort(y))
plt.legend(['orginal','sorted'])
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs[0, 0].scatter(np.sort(x),np.sort(y),marker='v',color='magenta')
axs[0, 1].plot(np.sort(x), np.sort(y),marker='*',color='black')
axs[1,1].hist(x,color='r')
axs[1,0].hist(y,color='cyan')
#giving titles for each subplot

axs[0, 0].set_title("Sorted-scatter of $log(B_{Lc}^{2})$ vs $log(P^{-5}(\dot{P})^{-1}$)",pad=20)
axs[0, 1].set_title("Line plot of $log(B_{Lc}^{2})$ vs $log(P^{-5}(\dot{P})^{-1})$ ",pad=20)
axs[1, 0].set_title("$log(P^{-5}(\dot{P})^{-1})$ ")
axs[1, 1].set_title("$log(B_{Lc}^{2})$")

#since the relation between B_Lc can be given to B_s and it is connected to p & pdot


# In[6]:


import matplotlib 
matplotlib.rc('xtick', labelsize=12) 
matplotlib.rc('ytick', labelsize=12) 
plt.rcParams.update({'font.size': 15})
f = plt.figure()
f.set_figwidth(7)
f.set_figheight(7)
plt.title('$B_{Lc}$ vs $B_{s}$')
plt.xlabel('$B_{Lc}$')
plt.ylabel('$B_{s}$')
plt.scatter(np.sort(np.log(a)),np.sort(np.log(d)),marker='*')
plt.plot(np.sort(np.log(a)),np.sort(np.log(d)))


# ### checking the relation : $\sin{\beta} = \sqrt{\frac{P\dot{P}}{2}}$

# In[7]:


from math import *
sinb = (np.sqrt((c*b)/2))
print(sinb)


# ### inverse relation check:

# In[8]:


def PPdot(a):
    a=int(input("Enter angle: "))
    ppdot = 2*(a**2)
    print(ppdot)
    
PPdot(a)


# In[9]:


print(np.sqrt((o['po']*o['pdot'])/2))


# ## Tryng for R

# In[10]:


R = (((o['Edot'])**(1/6))/((o['B_s'])**(1/3))*((o['po'])**(2/3)))
R


# ### From I , B, P and Pdot

# In[17]:


R2 = ((l['I']*o['pdot']*o['po'])/(o['B_s']**2))**(1/6)
R2


# In[12]:


pop=(o['po']*o['pdot'])
pop


# In[13]:


import pandas as pd
import numpy as np
import math
G={'Name of pulsar':['J0205+6449','J0218+4232','J0437-4715','J0534+2200','J1105-6107','J1124-5916','J1617-5055','J1930+1852','J2124-3358','J2229+6114'],'po':[0.06571592849324,0.00232309053151224,0.005757451936712637,0.0333924123,0.0632021309179,0.13547685441,0.069356847,0.136855046957,0.00493111494309662,0.05162357393],'pdot':[1.93754256e-13,7.73955e-20,5.729215e-20,4.20972e-13,1.584462e-14,7.52566e-13,1.351e-13,7.5057e-13,2.05705e-20,7.827e-14],'D in Kpc':[3.200,3.150,0.157,2.000,2.360, 5.000, 4.743, 7.000, 0.410, 3.000],'Age':[5.37e+03,np.nan,1.59e+09,1.26e+03,6.32e+04,2.85e+03, 8.13e+03, 2.89e+03, np.nan, 1.05e+04],'R_L':[np.nan,466.36,13.52,2200.00,'NaN','NaN','NaN','NaN', 2.86, 13.50],'B_s':[3.61e+12,4.29e+08,4.29e+08,3.79e+12,1.01e+12,1.02e+13,3.1e+12,1.03e+13,3.22e+08,2.03e+12],
'Edot':[2.7e+37,2.4e+35,1.2e+34,4.5e+38,2.5e+36,1.2e+37,1.6e+37,1.2e+37,6.8e+33,2.2e+37],
'Edot2':[2.6e+36,2.5e+34,4.8e+35,1.1e+38,4.4e+35,4.8e+35,7.1e+35,2.4e+35,2.4e+35,2.5e+36],
'B_sI':[3.61e+12,4.27e+08,2.85e+08,3.79e+12,np.nan,np.nan,np.nan,np.nan, 1.92e+08,np.nan],
'B_Lc':[1.19e+05,3.21e+05,2.85e+04,9.55e+05,3.76e+04,3.85e+04, 8.70e+04, 3.75e+04, 2.52e+04, 1.39e+05],
'I':[1.002779e+45,9.857678e+44,1.013579e+45,1.009214e+45,1.010029e+45,1.005339e+45,1.001875e+45,1.039090e+45,1.005033e+45,9.805105e+44]}
l=pd.DataFrame(G)
l.to_csv('High_energy_pulsar.csv')
l


# In[15]:


pop2 = ((o['B_s']**2)*(R**6))/(I)
pop2


# In[32]:


M = (I/(R2**2))
M


# In[14]:


I = ((o['B_s']**(2))*(R**6))/(o['po']*o['pdot'])
I


# In[19]:


plt.plot(np.sort(R2),np.sort(M))


# In[20]:


import matplotlib.pyplot as plt
from numpy import *
from astropy import constants as const

L = ((const.h)*(const.c)*(o['po']**2))/(2*(I)*(np.pi)**2)
L


# In[21]:


const.h


# In[22]:


const.c


# In[23]:


lum = (R**(2))*((4*np.pi**2)*(2898*10**(-6))**(4))
lum


# In[24]:


density = M/(R2**3)
density


# In[25]:


plt.scatter(np.log(lum),o['D in Kpc'])


# In[26]:


ang_mom = l['I']*((2*np.pi)/o['po'])
ang_mom


# ### also $L_{ang} = \frac{4\pi}{5} \frac{MR^{2}}{P}$

# ### $M = \frac{5PL_{ang}}{4\pi R^{2}}$

# In[27]:


M_ = (5*o['po']*ang_mom)/(4*(np.pi)*(R**2))
M_


# In[30]:


lu = (l['I']*o['pdot'])/(o['po'])**3
lu


# In[40]:


# Simple Scatterplot with colored points
x = range(50)
y = range(50) + np.random.randint(0,30,50)
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
plt.scatter(x, y, c=y, cmap='Spectral')
plt.colorbar()
plt.title('Simple Scatter plot')
plt.xlabel('X - value')
plt.ylabel('Y - value')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




