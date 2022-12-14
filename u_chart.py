
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics


np.random.seed(42)


u = {'defects':np.random.randint(1,5,10).tolist(),
    'group_size':np.random.randint(10,15,10).tolist()}


u = pd.DataFrame(u)


u['u'] = u['defects']/u['group_size']


plt.figure(figsize=(15,7.5))
plt.plot(u['u'], linestyle='-', marker='o', color='black')
plt.step(x=range(0, len(u['u'])), y=u['u'].mean()+3*np.sqrt(u['u'].mean()/u['group_size']), color='red', linestyle='dashed')
plt.step(x=range(0, len(u['u'])), y=u['u'].mean()-3*np.sqrt(u['u'].mean()/u['group_size']), color='red', linestyle='dashed')
plt.axhline(statistics.mean(u['u']), color='blue')
plt.ylim(bottom=0)
plt.title('u Chart')
plt.xlabel('Group')
plt.ylabel('Fraction Defective')


i = 0
control = True
for group in u['u']:
    if group > u['u'].mean()+3*np.sqrt(u['u'].mean()/u['group_size'][i]) or group < u['u'].mean()-3*np.sqrt(u['u'].mean()/u['group_size'][i]):
        print('Group', i, 'out of fraction defective cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')
