import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel("明码送样表20180627.xlsx", header=None, sheetname='Sheet3')
#print(df)
#C_T=df[12]
all_snps=sum(df.iloc[1][5:-1])
rows,cols=df.shape
list=[]
for i in range(1,rows):
    C_T = df.iloc[i][12]
    all_snps=sum(df.iloc[i][5:-1])
    frq=C_T/all_snps
    list.append(frq)

name_list=['yaoming']
FFT=np.average(list[0:3])
QIAGEN=np.average(list[3:6])
QIAGEN_with_UDG=list[6:9]
KIT=list[9:12]
KIT_repair=list[12:]

total_width, n = 0.8, 2
width = total_width / n
x=1
plt.bar(x, FFT, width=2,label='FFT',fc = 'y')
plt.bar(x, QIAGEN, width=2,label='QIAGEN',fc = 'y')
plt.show()
#plt.bar(x,FFT)
