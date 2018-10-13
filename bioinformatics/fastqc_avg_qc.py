'''
fastqc 里面的zip 文件里面的txt 文件，统计平均测序深度
'''

import zipfile
import numpy as np
import os
from scipy import stats
#遍历文件夹，得到zip所有文件
path = "../../fastqc/"
files= os.listdir(path)
filelist=[]
for i in files:
    if "zip" in i:
        filelist.append(i)
final_list=[]

for i in filelist:
    z = zipfile.ZipFile("../../fastqc/"+i, "r")
    # txt 文件在倒数第二个
    file=z.read(z.namelist()[-2])
    # 去除b""
    file=str(file)[2:-1].split('\\n')
    list=[]
    # 读取13-51行，统计
    for j in file[13:51]:
        list.append(float(j.split('\\')[1][1:]))
    final_list.append(np.mean(list))
    #print(i)
    print(np.mean(list))
#print(list)
#print(final_list)

interval=stats.norm.interval(0.95,np.mean(final_list[0:15]),np.std(final_list[0:15]))
interval2=stats.norm.interval(0.95,np.mean(final_list[15:]),np.std(final_list[15:]))
#print(final_list[0:15],final_list[15:])
#print(np.mean(final_list[0:15]),interval)
#print(np.mean(final_list[15:]),interval2)

print(np.mean(final_list[0:15]),np.min(final_list[0:15]),max(final_list[0:15]))
print(np.mean(final_list[15:]),min(final_list[15:]),max(final_list[15:]))