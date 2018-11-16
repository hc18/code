
files=open("text",'r')
list=[]
for i in files.readlines():
    list.append(i.strip())
begain="bcftools merge "
end= " -O z -o 15_A.vcf.gz"
str=""
for i in list[15:]:
    str=str+" "+i
#print(begain+str+end)

#for i,j in enumerate(list):
    #print(i,j)
print(begain +" "+list[5]+" "+list[14]+" "+list[2]+end)