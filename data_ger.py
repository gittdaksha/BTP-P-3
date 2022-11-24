import random
import numpy as np
import pandas as pd
n = 10000
h = np.random.normal(136.56, 0.067,n)
hd = np.random.normal(2.03, 0.0067,n)
bd = np.random.normal(74.70, 0.067,n)
pipe = np.random.normal(75.30, 0.067,n)
h1h2 = np.random.normal(230, 0.067,n)
h2h3 = np.random.normal(110, 0.067,n)
res = np.zeros(n)
bd.sort()
h.sort()
pipe.sort()

hd[::-1].sort()
fh = np.zeros(n)
for i in range(len(h)):
  if h[i] >= 136.56 - 0.2 and h[i] <= 136.56 + 0.2:
    fh[i] = 1
    # print(h[i], " ", "InRange")
  else:
    fh[i] = 0

fhd = np.zeros(n)
for i in range(len(hd)):
  if hd[i] >= 2 + 0.01 and hd[i] <= 2 + 0.05:
    fhd[i] = 1
    # print(hd[i], " ", "InRange")
  else:
    fhd[i] = 0

fbd = np.zeros(n)
for i in range(len(bd)):
  if bd[i] >= 75 - 0.5 and bd[i] <= 75 - 0.1:
    fbd[i] = 1 
    # print(bd[i], " ", "InRange")
  else:
    fbd[i] = 0

fpipe = np.zeros(n)
for i in range(len(pipe)):
  if pipe[i] >= 75 + 0.1 and pipe[i] <= 75 + 0.5:
    fpipe[i] = 1
    # print(pipe[i], " ", "InRange")
  else:
    fpipe[i] = 0  

fh1h2=np.zeros(n)
for i in range(len(h1h2)):
  if h1h2[i] >= 230 - 0.2 and h1h2[i] <= 230 + 0.2:
    fh1h2[i] = 1
    # print(h1h2[i], " ", "InRange")
  else:
    fh1h2[i] = 0


fh2h3 = np.zeros(n)
for i in range(len(h2h3)):
  if h2h3[i] >= 110 - 0.2 and h2h3[i] <= 110 + 0.2:
    fh2h3[i] = 1
    # print(h2h3[i], " ", "InRange")
  else:
    fh2h3[i] = 0 
     
for i in range(n):
  if fh[i]==1 and fhd[i] ==1 and fbd[i] ==1 and fpipe[i] == 1 and fh1h2[i]== 1 and fh2h3[i] == 1:
    res[i] = 1
    # print(h[i], " ", hd[i], " ", bd[i], " ", pipe[i], " ", h1h2[i], " ", h2h3[i])
  else:
    res[i] = 0
    # print("ouch")
array = np.array([h,hd,bd, pipe, h1h2, h2h3, res]).T
# array

column_values = ['Hole_distance', 'Hole_dia', 'Big_Hole_dia', 'Pipe_Dia', 'H1H2', 'H2H3','res']  
df = pd.DataFrame(data = array, columns = column_values)

df.to_csv('file1.csv')