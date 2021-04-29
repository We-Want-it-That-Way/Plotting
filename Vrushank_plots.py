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

# In[11]:


a=m['B_Lc']
b=m['pdot']
c=m['po']
d=m['B_s']
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


# In[12]:


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

# In[13]:


from math import *
sinb = (np.sqrt((c*b)/2))
print(sinb)


# ## Tryng for R, using the empirical equation
# ###  $R_{NS} = \frac{\dot{E}^{1/6}}{B_{s}^{1/3}P^{2/3}}$

# In[14]:


R = (((m['Edot'])**(1/6))/((m['B_s'])**(1/3))*((m['po'])**(2/3)))
R


# ### From I , B, P and Pdot
# ### From relation : $R_{ns} = (\frac{IP\dot{P}}{B_{s}^{2}})^{1/6}$

# In[15]:


R2 = ((m['I']*m['pdot']*m['po'])/(m['B_s']**2))**(1/6)
R2


# In[16]:


pop=(m['po']*m['pdot'])
pop


# In[17]:


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


# In[20]:


pop2 = ((m['B_s']**2)*(R**6))/(I)
pop2


# In[21]:


M = (I/(R2**2))
M


# In[19]:


I = ((m['B_s']**(2))*(R**6))/(m['po']*m['pdot'])
I


# In[22]:


matplotlib.rc('xtick', labelsize=12) 
matplotlib.rc('ytick', labelsize=12) 
plt.rcParams.update({'font.size': 15})
f = plt.figure()
f.set_figwidth(7)
f.set_figheight(7)
plt.scatter(np.sort(R2),np.sort(np.log(M)))


# In[23]:


lum = (R**(2))*((4*np.pi**2)*(2898*10**(-6))**(4))
lum


# In[24]:


density = M/(R2**3)
density


# In[25]:


import matplotlib.pyplot as plt
matplotlib.rc('xtick', labelsize=12) 
matplotlib.rc('ytick', labelsize=12) 
plt.rcParams.update({'font.size': 15})
f = plt.figure()
f.set_figwidth(7)
f.set_figheight(7)
plt.scatter(np.log(lum),m['D in Kpc'])


# In[26]:


ang_mom = m['I']*((2*np.pi)/m['po'])
ang_mom


# ### also $L_{ang} = \frac{4\pi}{5} \frac{MR^{2}}{P}$

# ### $M = \frac{5PL_{ang}}{4\pi R^{2}}$

# In[27]:


M_ = (5*m['po']*ang_mom)/(4*(np.pi)*(R**2))
M_/(2*10**30)


# In[28]:


lu = (m['I']*m['pdot'])/(m['po'])**3
lu


# In[29]:


omega = 2*(np.pi)/m['po']
omega


# ### M $\propto R^{3}$
# ### Then the curve shall be like this:

# In[30]:


k = np.arange(0,10**8)
q = np.arange(0,10)

k = q**3
plt.plot(np.log(k),q)


# In[31]:


matplotlib.rc('xtick', labelsize=12) 
matplotlib.rc('ytick', labelsize=12) 
plt.rcParams.update({'font.size': 15})
f = plt.figure()
f.set_figwidth(7)
f.set_figheight(7)
plt.scatter(R,R)
plt.plot(R2,R2)
plt.scatter(R2,R2)


# ### This above graph is to check the 2 radius values obtained using different parameters. R is 2 times the R2 values.
# 
# ### Although R2 values are most likely to be certain.

# ### Luminosity calculation in terms of $L_{\odot}$

# In[32]:


n=print(lu/(3.826*10**33))

# in solar luminosity L_{sun}


# ### interms of Watts

# In[33]:


# in watts

lu/(3.826*10**26)


# ### Plot for P and $\ddot{P}$

# In[34]:


p =[0.065715928,0.002323091,0.005757452,0.033392412,0.063202131,0.135476854,0.069356847,0.136855047,0.004931115,0.051623574,0.016122222,0.237099442,0.245983683,0.064667,0.326571288,3.76373308,0.237099442,1.984597367,1.432704197,1.205374441,8.020392,0.354437595,11.0062624,7.55592,5.540742829,11.7889784,5.198346,6.97907097,3.76373308,8.047]
pdot2 = [1.94E-13
,7.74E-20
,5.73E-20
,4.21E-13
,1.58E-14
,7.53E-13
,1.35E-13
,7.51E-13
,2.06E-20
,7.83E-14
,5.18E-14
,1.10E-14
,1.54E-14
,4.40E-14
,7.11E-12
,5.48E-16
,1.10E-14
,3.17E-15
,2.25E-15
,1.91E-14
,1.88E-11
,7.36E-17
,1.96E-11
,5.49E-10
,2.83E-12
,4.09E-11
,9.20E-11
,4.71E-13
,1.76E-11
,6.50E-11]


# In[35]:


matplotlib.rc('xtick', labelsize=12) 
matplotlib.rc('ytick', labelsize=12) 
plt.rcParams.update({'font.size': 15})
f = plt.figure()
f.set_figwidth(7)
f.set_figheight(7)
plt.scatter((np.log(pdot2)),(p)) 
plt.xlabel('$\log{\ddot{P}}$')
plt.ylabel('P')


# In[36]:


pdoubledot = [4.362022e-74,1.435485e-77,1.645689e-78,3.594040e-73,3.765140e-75,3.983752e-74,2.725094e-74,3.599818e-74,8.226702e-79,2.852902e-74,2.014969e-73,1.900034e-76,2.471356e-76,1.021682e-74,6.672220e-74,3.756395e-80,1.915326e-76,7.661261e-79,1.449304e-81,1.315667e-77,2.843571e-76,5.792669e-79,1.571104e-76,9.862808e-75,9.023199e-77,2.863310e-76,3.339180e-75,9.204737e-78,1.206434e-75,9.555010e-76]


# In[37]:


matplotlib.rc('xtick', labelsize=12) 
matplotlib.rc('ytick', labelsize=12) 
plt.rcParams.update({'font.size': 15})
f = plt.figure()
f.set_figwidth(7)
f.set_figheight(7)
plt.scatter(np.sort(np.log(pdoubledot)),np.sort(m['po']))
plt.xlabel('$\log{\ddot{P}}$')
plt.ylabel('P')


# ## All data

# In[38]:


import pandas as pd
import numpy as np
import math
G={'Name of pulsar':['J0205+6449','J0218+4232','J0437-4715','J0534+2200','J1105-6107','J1124-5916','J1617-5055','J1930+1852','J2124-3358','J2229+6114'],'po':[0.06571592849324,0.00232309053151224,0.005757451936712637,0.0333924123,0.0632021309179,0.13547685441,0.069356847,0.136855046957,0.00493111494309662,0.05162357393],'pdot':[1.93754256e-13,7.73955e-20,5.729215e-20,4.20972e-13,1.584462e-14,7.52566e-13,1.351e-13,7.5057e-13,2.05705e-20,7.827e-14],'D in Kpc':[3.200,3.150,0.157,2.000,2.360, 5.000, 4.743, 7.000, 0.410, 3.000],'Age':[5.37e+03,np.nan,1.59e+09,1.26e+03,6.32e+04,2.85e+03, 8.13e+03, 2.89e+03, np.nan, 1.05e+04],'R_L':[np.nan,466.36,13.52,2200.00,'NaN','NaN','NaN','NaN', 2.86, 13.50],'B_s':[3.61e+12,4.29e+08,4.29e+08,3.79e+12,1.01e+12,1.02e+13,3.1e+12,1.03e+13,3.22e+08,2.03e+12],
'Edot':[2.7e+37,2.4e+35,1.2e+34,4.5e+38,2.5e+36,1.2e+37,1.6e+37,1.2e+37,6.8e+33,2.2e+37],
'Edot2':[2.6e+36,2.5e+34,4.8e+35,1.1e+38,4.4e+35,4.8e+35,7.1e+35,2.4e+35,2.4e+35,2.5e+36],
'B_sI':[3.61e+12,4.27e+08,2.85e+08,3.79e+12,np.nan,np.nan,np.nan,np.nan, 1.92e+08,np.nan],
'B_Lc':[1.19e+05,3.21e+05,2.85e+04,9.55e+05,3.76e+04,3.85e+04, 8.70e+04, 3.75e+04, 2.52e+04, 1.39e+05],
'I':[1.002779e+45,9.857678e+44,1.013579e+45,1.009214e+45,1.010029e+45,1.005339e+45,1.001875e+45,1.039090e+45,1.005033e+45,9.805105e+44]}
b=pd.DataFrame(G)


# In[7]:


b


# In[8]:


import pandas as pd
import numpy as np
import math
A={'Name of pulsar':['J0537-6910','J0633+1746','J0543+2329','J1811-1925','J1846-0258','J0628+0909','J0633+1746','J0636-4549','J1811-4930','J1812-1718'],
   'po':[0.0161222220245,0.2370994416923,0.245983683333,0.06466700,0.32657128834,3.763733080,0.2370994416923,1.98459736713,1.4327041968,1.20537444137],
   'pdot':[5.1784338e-14,1.097087e-14,1.541956e-14,4.40e-14,7.107450e-12,0.5479e-15,1.097087e-14,3.1722e-15,2.254e-15,1.9077e-14],
   'D in Kpc':[49.700,0.190,1.565,5.000,5.800,1.771,0.190,0.383,1.447,3.678],
   'R_L':['NaN','NaN',71.03,'NaN','NaN','NaN','NaN','NaN','NaN','NaN'],
   'Age':[4.93e+03,3.42e+05,2.53e+05,2.33e+04,728,3.59e+07,3.42e+05,9.91e+06,1.01e+07,1e+06],
   'B_s':[9.25e+11,1.63e+12,1.97e+12,1.71e+12,4.88e+13,8.35e+11,1.63e+12,2.54e+12,1.82e+12,4.85e+12],
   'Edot':[4.9e+38,3.2e+34,4.1e+34,6.4e+36,8.1e+36,1.1e+31,3.2e+34,1.6e+31,3.0e+31,4.3e+32],
   'Edot2':[2.0e+35,9.0e+35,1.7e+34,2.6e+35,2.4e+35,3.6e+30,9.0e+35,1.1e+32,1.4e+31,3.2e+31],
   'B_sI':['NaN',1.63e+12,1.97e+12,'NaN','NaN','NaN',1.63e+12,'NaN','NaN','NaN'],
   'B_Lc':[2.07e+06,1.15e+03,1.24e+03,5.92e+04,1.31e+04,4.09e+00,1.15e+03,3.05e+00,5.80e+00,2.60e+01,],
           'I':[1.005433e+45,9.857828e+44,1.003486e+45,9.973697e+44,1.006435e+45,2.714117e+46,9.857828e+44,9.996716e+44,9.924706e+44,1.000933e+45]}
c=pd.DataFrame(A)
c


# In[9]:


import pandas as pd
import numpy as np
import math
R={'Name of pulsar':['J0100-7211','J0525-6607','J1708-4008','J1808-2024','J1809-1943','J1841-0456','J1907+0919','J2301+5852','J1745-2900','J0525-6607'],
   'po':[8.020392, 0.35443759451370,11.0062624,7.55592,5.540742829,11.7889784, 5.198346,6.9790709703,3.763733080,8.0470],
   'pdot':[1.88e-11, 7.36052e-17,1.960e-11,5.49e-10,2.8281e-12,4.092e-11,9.2e-11,4.7123e-13,1.756e-11,6.5e-11],
   'D in Kpc':[59.700, 1.841,3.800,13.000,3.600,9.600,'NaN',3.300,8.300,'NaN'],
   'R_L':['NaN', 66.09,'NaN','NaN','NaN','NaN','NaN','NaN','NaN','NaN'],
   'Age':[6.76e+03,7.63e+07,8.9e+03,218,3.1e+04,4.57e+03,895,2.35e+05,3.4e+03,1.96e+03],
   'B_s':[3.93e+14,1.63e+11,4.7e+14,2.06e+15,1.27e+14,7.03e+14,7e+14,5.8e+13,2.6e+14,7.32e+14],
   'Edot':[1.4e+33,6.5e+31,5.8e+32,5.0e+34,6.6e+32,9.9e+32,2.6e+34,5.5e+31,1.3e+34,4.9e+33],
   'Edot2':[4.0e+29,1.9e+31,4.0e+31,3.0e+32,5.1e+31,1.1e+31,'NaN',5.0e+30,1.9e+32,'NaN'],
   'B_sI':['NaN', 1.62e+11,'NaN',2.06e+15, 1.27e+14,'NaN','NaN', 5.80e+13,2.60e+14,'NaN'],
   'B_Lc':[7.14e+00,3.44e+01,3.30e+00,4.48e+01,6.98e+00,4.02e+00,4.67e+01,1.60e+00,4.57e+01,1.32e+01],
   'I':[9.741766e+44,9.970224e+44,1.000397e+45,9.961860e+44,1.006547e+45,1.005099e+45,0,0,0,0]}
d=pd.DataFrame(R)
d


# In[10]:


m=pd.concat([b,c,d])
m.to_csv('all_included.csv')
m


# In[ ]:




