#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import numpy as np
import math

G={'Name of pulsar':['J0205+6449','J0218+4232','J0437-4715','J0534+2200','J1105-6107','J1124-5916','J1617-5055','J1930+1852','J2124-3358','J2229+6114'],'po':[0.06571592849324,0.00232309053151224,0.005757451936712637,0.0333924123,0.0632021309179,0.13547685441,0.069356847,0.136855046957,0.00493111494309662,0.05162357393],'pdot':[1.93754256e-13,7.73955e-20,5.729215e-20,4.20972e-13,1.584462e-14,7.52566e-13,1.351e-13,7.5057e-13,2.05705e-20,7.827e-14],'D in Kpc':[3.200,3.150,0.157,2.000,2.360, 5.000, 4.743, 7.000, 0.410, 3.000],'Age':[5.37e+03,4.76e+08,1.59e+09,1.26e+03,6.32e+04,2.85e+03, 8.13e+03, 2.89e+03, 3.8e+09, 1.05e+04],'R_L':['NaN',466.36,13.52,2200.00,'NaN','NaN','NaN','NaN', 2.86, 13.50],'B_s':[3.61e+12,4.29e+08,4.29e+08,3.79e+12,1.01e+12,1.02e+13,3.1e+12,1.03e+13,3.22e+08,2.03e+12],
'Edot':[2.7e+37,2.4e+35,1.2e+34,4.5e+38,2.5e+36,1.2e+37,1.6e+37,1.2e+37,6.8e+33,2.2e+37],
'Edot2':[2.6e+36,2.5e+34,4.8e+35,1.1e+38,4.4e+35,4.8e+35,7.1e+35,2.4e+35,2.4e+35,2.5e+36],
'B_sI':[3.61e+12,4.27e+08,2.85e+08,3.79e+12,'NaN','NaN','NaN','NaN', 1.92e+08,'NaN'],
'B_Lc':[1.19e+05,3.21e+05,2.85e+04,9.55e+05,3.76e+04,3.85e+04, 8.70e+04, 3.75e+04, 2.52e+04, 1.39e+05]}
z=pd.DataFrame(G)
z.to_csv('Hig_energy_pulsar.csv')
z


# In[ ]:





# In[43]:


import pandas as pd
import numpy as np
import math
A={'Name of pulsar':['J0537-6910','J0633+1746','J0543+2329','J1811-1925','J1846-0258','J0628+0909','J0633+1746','J0636-4549','J1811-4930','J1812-1718'],'po':[0.0161222220245,0.2370994416923,0.245983683333,0.06466700,0.32657128834,3.763733080,0.2370994416923,1.98459736713,1.4327041968,1.20537444137],'pdot':[5.1784338e-14,1.097087e-14,1.541956e-14,4.40e-14,7.107450e-12,0.5479e-15,1.097087e-14,3.1722e-15,2.254e-15,1.9077e-14],'D in Kpc':[49.700,0.190,1.565,5.000,5.800,1.771,0.190,0.383,1.447,3.678],'R_L':[0,0,71.03,0,0,0,0,0,0,0],'Age':[4.93e+03,3.42e+05,2.53e+05,2.33e+04,728,3.59e+07,3.42e+05,9.91e+06,1.01e+07,1e+06],'B_s':[9.25e+11,1.63e+12,1.97e+12,1.71e+12,4.88e+13,8.35e+11,1.63e+12,2.54e+12,1.82e+12,4.85e+12],'Edot':[4.9e+38,3.2e+34,4.1e+34,6.4e+36,8.1e+36,1.1e+31,3.2e+34,1.6e+31,3.0e+31,4.3e+32],'Edot2':[2.0e+35,9.0e+35,1.7e+34,2.6e+35,2.4e+35,3.6e+30,9.0e+35,1.1e+32,1.4e+31,3.2e+31],'B_sI':['NaN',1.63e+12,1.97e+12,'NaN','NaN','NaN',1.63e+12,'NaN','NaN','NaN'],'B_Lc':[2.07e+06,1.15e+03,1.24e+03,5.92e+04,1.31e+04,4.09e+00,1.15e+03,3.05e+00,5.80e+00,2.60e+01]}
w=pd.DataFrame(A)
w.to_csv('N_Radio_pulsar.csv')
w


# In[44]:


import pandas as pd
import numpy as np
import math
R={'Name of pulsar':['J0100-7211','J0525-6607','J1708-4008','J1808-2024','J1809-1943','J1841-0456','J1907+0919','J2301+5852','J1745-2900','J0525-6607'],'po':[8.020392, 0.35443759451370,11.0062624,7.55592,5.540742829,11.7889784, 5.198346,6.9790709703,3.763733080,8.0470],'pdot':[1.88e-11, 7.36052e-17,1.960e-11,5.49e-10,2.8281e-12,4.092e-11,9.2e-11,4.7123e-13,1.756e-11,6.5e-11],'D in Kpc':[59.700, 1.841,3.800,13.000,3.600,9.600,'NaN',3.300,8.300,'NaN'],'R_L':[0, 66.09,0,0,0,0,0,0,0,0],'Age':[6.76e+03,7.63e+07,8.9e+03,218,3.1e+04,4.57e+03,895,2.35e+05,3.4e+03,1.96e+03],'B_s':[3.93e+14,1.63e+11,4.7e+14,2.06e+15,1.27e+14,7.03e+14,7e+14,5.8e+13,2.6e+14,7.32e+14],'Edot':[1.4e+33,6.5e+31,5.8e+32,5.0e+34,6.6e+32,9.9e+32,2.6e+34,5.5e+31,1.3e+34,4.9e+33],'Edot2':[4.0e+29,1.9e+31,4.0e+31,3.0e+32,5.1e+31,1.1e+31,'NaN',5.0e+30,1.9e+32,'NaN'],'B_sI':['NaN', 1.62e+11,'NaN',2.06e+15, 1.27e+14,'NaN','NaN', 5.80e+13,2.60e+14,'NaN'],'B_Lc':[7.14e+00,3.44e+01,3.30e+00,4.48e+01,6.98e+00,4.02e+00,4.67e+01,1.60e+00,4.57e+01,1.32e+01]}
v=pd.DataFrame(R)
v.to_csv('magnetor_pulsar.csv')
v


# In[47]:


u=pd.concat([z,w,v],ignore_index=True)
u.to_csv('Combined_data.csv')
u


# In[102]:


import pandas as pd
import numpy as np
a = z['po']
b = z['pdot']
d = z['Edot']
e = b*a**(-3)
f = np.log(e)
h = np.log(d)
import matplotlib.pyplot as plt
plt.xlabel('p(dot)*p^(-3)')
plt.ylabel('E(dot)')
plt.scatter(f,h,color='magenta')


# In[101]:


import pandas as pd
import numpy as np
a = w['po']
b = w['pdot']
d = w['Edot']
e = b*a**(-3)
f = np.log(e)
h = np.log(d)
import matplotlib.pyplot as plt
plt.xlabel('p(dot)*p^(-3)')
plt.ylabel('E(dot)')
plt.scatter(f,h,color='b')


# In[100]:


import pandas as pd
import numpy as np
a = v['po']
b = v['pdot']
d = v['Edot']
e = b*a**(-3)
f = np.log(e)
h = np.log(d)
import matplotlib.pyplot as plt
plt.xlabel('p(dot)*p^(-3)')
plt.ylabel('E(dot)')
plt.scatter(f,h,color='g')


# In[99]:


#age vs po
import pandas as pd
import numpy as np
g = z['po']
e = z['Age']
i = (g)
j = np.log(e)
import matplotlib.pyplot as plt
plt.xlabel('Age')
plt.ylabel('po')
plt.scatter(i,j,color='magenta')


# In[98]:


#age vs po
import pandas as pd
import numpy as np
g = w['po']
e = w['Age']
i = (g)
j = np.log(e)
import matplotlib.pyplot as plt
plt.xlabel('Age')
plt.ylabel('po')
plt.scatter(i,j,color='b')


# In[96]:


#age vs po
import pandas as pd
import numpy as np
g = v['po']
e = v['Age']
i = (g)
j = np.log(e)
import matplotlib.pyplot as plt
plt.xlabel('Age')
plt.ylabel('po')
plt.scatter(i,j,color='g')


# In[105]:


import pandas as pd
import numpy as np
k = z['B_s']
l = z['po']
m = z['pdot']
n = l*m
q = np.log(k)
p = np.log(n)
import matplotlib.pyplot as plt
plt.xlabel('$B_{s}$')
plt.ylabel('P$\dot{P}$')
plt.scatter(q,p,color='magenta')


# In[94]:


import pandas as pd
import numpy as np
k = w['B_s']
l = w['po']
m = w['pdot']
n = l*m
q = np.log(k)
p = np.log(n)
import matplotlib.pyplot as plt
plt.xlabel('B_s')
plt.ylabel('l*m')
plt.scatter(q,p,color='b')


# In[93]:


import pandas as pd
import numpy as np
k = v['B_s']
l = v['po']
m = v['pdot']
n = l*m
q = np.log(k)
p = np.log(n)
import matplotlib.pyplot as plt
plt.xlabel('B_s')
plt.ylabel('l*m')
plt.scatter(q,p,color='g')


# In[8]:


#calculating and verifying inertia values
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
p1 = 0.0628
pdo = 8.560517117*10**(-15)
R = 10**3
I = 10**38
M = 2.8*10**30
c = 3*10**8
G = 6.67408*10**(-11)
pi = 3.14159265359
eo = (3*I*c**3*p1*pdo)/(4*pi**2*G*M**2*R**2)
#u = math.log(r,10)
#v = math.log(s,10)
#z = ((0.035477*10**8)*r*s)
#w = math.log(z,10)
#print(w)
#print(u)
#print(eo)
x = math.log(eo,10)
print(x)
#e1 = 0.04446555*10**(-9)
#loe1 = math.log(e1,10)
#print(loe1)


# In[59]:


#inertia values
import pandas as pd
import numpy as np
k = u['Edot']
l = u['po']
m = u['pdot']
MI = (k*l**3)/(4*((3.14)**2)*m)
print(MI)


# In[39]:


#REGRESSION PLOT
import seaborn as sns
import matplotlib.pyplot as plt
sns.regplot(x=o['po'], y=np.log(o['pdot']))


# In[63]:


#CALCULATING MAGNETIC MOMENT
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
k = MI
l = u['po']
m = u['pdot']
#i = np.sort(l)
#j = np.sort(m)
#q = np.sort(k)
moment = ((3*l*m*k*((3*10**8)**3))**(1/2))/(8**(1/2)*np.pi)
print(moment)
plt.xlabel('p')
plt.ylabel('moment')
plt.scatter(l,moment)


# In[65]:


#MOMENT VS PDOT
import matplotlib.pyplot as plt
plt.xlabel('pdot')
plt.ylabel('moment')
plt.scatter((m),(moment))


# In[79]:


#*pdoubledot and magnetic index values and respective graphs 
import pandas as pd
import numpy as np
import math
pdoubledot = [4.362022e-74,1.435485e-77,1.645689e-78,3.594040e-73,3.765140e-75,3.983752e-74,2.725094e-74,3.599818e-74,8.226702e-79,2.852902e-74,2.014969e-73,1.900034e-76,2.471356e-76,1.021682e-74,6.672220e-74,3.756395e-80,1.915326e-76,7.661261e-79,1.449304e-81,1.315667e-77,2.843571e-76,5.792669e-79,1.571104e-76,9.862808e-75,9.023199e-77,2.863310e-76,3.339180e-75,9.204737e-78,1.206434e-75,9.555010e-76]
magneticindex = [2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0]
pdotdot=pd.DataFrame(pdoubledot)
import matplotlib.pyplot as plt
l = z['po']
m = z['pdot']
#n = o['Age']
#i = np.sort(l)
#j = np.sort(m)
#k = np.sort(magneticindex)
#q = np.sort(pdoubledot)
print (pdoubledot)
print(magneticindex)
bri = 2-((i*q)/j**2)
plt.plot(bri,magneticindex)


# In[15]:


#pdoubledot vs p
import matplotlib.pyplot as plt
plt.xlabel('p')
plt.ylabel('pdoubledot')
plt.scatter(l,pdoubledot)


# In[17]:


#regression graph
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#o=pd.concat([l,p,c],ignore_index=True)
#o.to_csv('Combined_data.csv')
sns.regplot(x=l, y=m)


# In[91]:


#B_s vs po
import pandas as pd
import numpy as np
a = z['po']
b = z['pdot']
d = z['B_s']
#e = b*a**(-3)
f = (a)
h = np.log(d)
import matplotlib.pyplot as plt
plt.xlabel('po')
plt.ylabel('B_s')
plt.scatter(f,h,color='magenta')


# In[90]:


#B_s vs po
import pandas as pd
import numpy as np
a = w['po']
b = w['pdot']
d = w['B_s']
#e = b*a**(-3)
f = (a)
h = np.log(d)
import matplotlib.pyplot as plt
plt.xlabel('po')
plt.ylabel('B_s')
plt.scatter(f,h,color='b')


# In[89]:


#B_s vs po
import pandas as pd
import numpy as np
a = v['po']
b = v['pdot']
d = v['B_s']
#e = b*a**(-3)
f = (a)
h = np.log(d)
import matplotlib.pyplot as plt
plt.xlabel('po')
plt.ylabel('B_s')
plt.scatter(f,h,color='g')


# In[88]:


#B_s vs pdot
import pandas as pd
import numpy as np
g = z['pdot']
e = z['B_s']
i = np.log(g)
j = np.log(e)
import matplotlib.pyplot as plt
plt.xlabel('pdot')
plt.ylabel('B_s')
plt.scatter(i,j,color='magenta')


# In[87]:


#B_s vs pdot
import pandas as pd
import numpy as np
g = w['pdot']
e = w['B_s']
i = np.log(g)
j = np.log(e)
import matplotlib.pyplot as plt
plt.xlabel('pdot')
plt.ylabel('B_s')
plt.scatter(i,j,color='b')


# In[86]:


#B_s vs pdot
import pandas as pd
import numpy as np
g = v['pdot']
e = v['B_s']
i = np.log(g)
j = np.log(e)
import matplotlib.pyplot as plt
plt.xlabel('pdot')
plt.ylabel('B_s')
plt.scatter(i,j,color='g')


# In[85]:


import pandas as pd
import numpy as np
k = z['B_s']
l = z['po']
m = z['pdot']
n = l*m
q = np.log(k)
p = np.log(n)
import matplotlib.pyplot as plt
plt.xlabel('B_s')
plt.ylabel('l*m')
plt.scatter(q,p,color='magenta')


# In[84]:


import pandas as pd
import numpy as np
k = w['B_s']
l = w['po']
m = w['pdot']
n = l*m
q = np.log(k)
p = np.log(n)
import matplotlib.pyplot as plt
plt.xlabel('B_s')
plt.ylabel('l*m')
plt.scatter(q,p,color='b')


# In[83]:


import pandas as pd
import numpy as np
k = v['B_s']
l = v['po']
m = v['pdot']
n = l*m
q = np.log(k)
p = np.log(n)
import matplotlib.pyplot as plt
plt.xlabel('B_s')
plt.ylabel('l*m')
plt.scatter(q,p,color='g')


# In[77]:


#energy density values
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
energydensity = [5.197004e+23,7.329435e+15,1.344718e+16,5.730662e+23,4.070692e+22,4.158539e+24,3.816843e+23,4.189682e+24,4.140784e+15,1.647759e+23,3.404310e+22,1.063169e+23,1.544215e+23,1.159887e+23,9.465151e+25,8.407745e+22,1.063169e+23,2.564554e+23,1.314073e+23,9.385028e+23,6.146583e+27,1.063405e+21,8.793794e+27,1.690987e+29,6.391975e+26,1.965530e+28,1.949545e+28,1.339982e+26,2.700298e+27,2.132199e+28]
g = u['po']
k = u['B_s']
se = np.log(energydensity)
q = np.log(g)
p = np.log(k)
plt.xlabel('energy density')
plt.ylabel('B_s')
plt.scatter(se,p)


# In[82]:


#energy density vs po
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.xlabel('energy density')
plt.ylabel('po')
plt.scatter(se,q,color='r')


# In[111]:


plt.scatter(np.log(bri),np.log(z['B_s']))
plt.title('Braking Index Vs Magnetic Field')
plt.xlabel('Braking Indes')
plt.ylabel('$B_{s}$')


# In[115]:


u['moment']=[3.61919e+27,4.26409e+23,5.85652e+23,3.81496e+27,1.01864e+27,1.02544e+28,3.10332e+27,1.04641e+28,3.23395e+23,2.01602e+27,9.27974e+26,1.6219e+27,1.97603e+27,1.70625e+27,4.89538e+28,7.57743e+27,1.6219e+27,2.54093e+27,1.81327e+27,4.85922e+27,3.88189e+29,1.63352e+26,4.70524e+29,2.05896e+30,1.27203e+29,7.05274e+29,7.02757e+29,5.82592e+28,2.60494e+29,7.31062e+29]
u


# In[120]:


sns.regplot(np.log(u['pdot']),np.log(u['moment']))


# In[ ]:





# In[ ]:




