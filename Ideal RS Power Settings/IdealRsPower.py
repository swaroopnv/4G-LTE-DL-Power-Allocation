#Created by github.com/zulfadlizainal

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Print Information
print('\n###############################################################\n')
print('Ideal LTE RS Power Settings - 3GPP TS 36.213 Section 5.2 Rel 12')
print('\n###############################################################\n')

#Input
df_tx = pd.read_excel('TxPowerPerPort.xlsx', encoding = 'utf-8-sig')
print(df_tx.to_string(index = False))
print('\n')
tx = float(input('Tx Power per Port (dBm) = '))
print('\n')

df_sysbw = pd.read_excel('SystemBandwidth.xlsx', encoding = 'utf-8-sig')
print(df_sysbw.to_string(index = False))
print('\n')
bw = int(input('LTE System Bandwidth (MHz) = '))
print('\n')

#Subcarrier Number
for index, row in df_sysbw.iterrows():
    if df_sysbw['Bandwidth (MHz)'][index] == bw:
        subcarrier = df_sysbw['Subcarrier Number'][index]
        print(f'\nSubcarrier Number = {subcarrier}\n')

#Ideal Pa Pb Combination for 100% Channel Power Distribution
pa = [0, -3, -4.77, -6]
pb = [0, 1, 2, 3]
papb = {'Pa (dB)': pa, 'Pb': pb}
df_rs = pd.DataFrame(papb)

df_rs['RS Power (dBm)'] = tx-(10*math.log(subcarrier,10)) - df_rs['Pa (dB)']
df_rs = df_rs.round({'RS Power (dBm)': 1})

#Ideal RS Power settings for 100% Channel Power Distribution
print('\n')
print(f'Ideal RS Power Settings for BW: {bw} MHz & Tx Power Per Port: {tx} dBm are:')
print('\n')
print(df_rs.to_string())
print('\n')

#Best Options for RS Power in Selecteed System Bandwidth

df_rs_options = pd.DataFrame(papb)

power1 = 40
power2 = 43
power3 = 44.7
power4 = 46

df_rs_options['40'] = power1-(10*math.log(subcarrier,10)) - df_rs_options['Pa (dB)']
df_rs_options['43'] = power2-(10*math.log(subcarrier,10)) - df_rs_options['Pa (dB)']
df_rs_options['44.7'] = power3-(10*math.log(subcarrier,10)) - df_rs_options['Pa (dB)']
df_rs_options['46'] = power4-(10*math.log(subcarrier,10)) - df_rs_options['Pa (dB)']

df_rs_options.drop(columns=['Pa (dB)'], inplace = True)
df_rs_options.drop(columns=['Pb'], inplace = True)

#3D Plotting

#thickness of the bars
dx, dy = .8, .8
# prepare 3d axes
fig = plt.figure()
ax = Axes3D(fig)
#set up positions for the bars
xpos=np.arange(df_rs_options.shape[0])
ypos=np.arange(df_rs_options.shape[1])
#set the ticks in the middle of the bars
ax.set_xticks(xpos + dx/2)
ax.set_yticks(ypos + dy/2)
#create meshgrid
xpos, ypos = np.meshgrid(xpos, ypos)
xpos = xpos.flatten()
ypos = ypos.flatten()
#the bars starts from 0 attitude
zpos=np.zeros(df_rs_options.shape).flatten()
#the bars' heights
dz = df_rs_options.values.ravel()
#plot
colors = plt.cm.jet(dz/dz.max())
ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color = colors)
#put the column / index labels
papb_combination = ['Pa0 Pb0','Pa-3 Pb1','Pa-4.77 Pb2','Pa-6 Pb3']
ax.w_xaxis.set_ticklabels(papb_combination)
ax.w_yaxis.set_ticklabels(df_rs_options.columns)
#name the axes
ax.set_xlabel('Pa Pb Combination', fontsize = 10)
ax.set_ylabel('Tx Power per Port (dBm)', fontsize = 10)
ax.set_zlabel('RS Power (dBm)', fontsize = 10)
plt.title(f'Ideal RS Power (dBm) settings for {bw} MHz Bandwidth', fontsize = 15)

#Line Plotting

fig = plt.figure()

power1 = df_rs_options['40'].values.tolist()
power2 = df_rs_options['43'].values.tolist()
power3 = df_rs_options['44.7'].values.tolist()
power4 = df_rs_options['46'].values.tolist()

plt.plot(power1, label="40 dBm", ls = '--', marker = 'o')
plt.plot(power2, label="43 dBm", ls = '--', marker = 'v')
plt.plot(power3, label="44.7 dBm", ls = '--', marker = 's')
plt.plot(power4, label="46 dBm", ls = '--', marker = 'p')

plt.xticks(np.arange(0, 4, 1))
plt.xlabel('Pa Pb Combination', fontsize = 10)
plt.ylabel('RS Power (dBm)', fontsize = 10)
plt.title(f'Ideal RS Power (dBm) settings for {bw} MHz Bandwidth', fontsize = 15)
plt.legend()
plt.grid()

plt.show()

print(' ')
print('ありがとうございました！！')
print('Download this program: https://github.com/zulfadlizainal')
print('Author: https://www.linkedin.com/in/zulfadlizainal')
print(' ')
