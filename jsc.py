#!/bin/python3
import os
import time
print ("\033[40;37m\ngive the js file ? ")
a=input().strip()
b=a.replace(".js","")
c="""#include <stdio.h>
void print(char *c){
    printf("%s",c);
}
"""
os.system("rm $1.c 2>/dev/null".replace("$1",b).strip())
os.system("js2c toc $1 $2.c".replace("$1",a).replace("$2",b).strip())
d=c
time.sleep(1)
f1=open("$1.c".replace("$1",b).strip(),"r")
dd=f1.read()
f1.close()
d=d+dd
d=d.replace("static int main"," int main")
f1=open ("$1.c".replace("$1",b),"w")
f1.write(d)
f1.close()
os.system("clang -o $1.elf $1.c".replace("$1",b))