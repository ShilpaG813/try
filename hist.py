import pandas as pd
import matplotlib.pyplot as plt
t=pd.read_csv(r'C:\Users\shilp\Onedrive\Desktop\titan.csv')
a=t[t['Survived']==1]['Age']
d=t[t['Survived']==0]['Age']
plt.hist(a,label='Survived',color='b',alpha=1)
plt.hist(d,label='Not survived',color='g',alpha=0.6)
plt.show()