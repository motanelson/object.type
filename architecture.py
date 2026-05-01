import os
def spt(s):
    r=s.split(" ")
    rr=[]
    for a in range(len(r)):
        
        if r[a].strip()!= "":
            rr.append(r[a])
    return rr
print("give me the .o object file name ? ")
a=input().strip()
os.system("objdump -x "+a+" > out.txt")

f1=open("out.txt","r")
txt=f1.read()
f1.close()
txts=txt.split("\n")
for a in txts:
    aa=spt(a)
    if len(aa)>0:
        if aa[0].strip()=="architecture:":
             print(aa[1])