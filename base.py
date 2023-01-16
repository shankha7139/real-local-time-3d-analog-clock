from vpython import *
import numpy as np
import time



cr=2
ct=cr/50
majortick=cr/7
majortickw=2*np.pi*cr/500
majortickt=ct*1.2


minortick=cr/12
minortickw=2*np.pi*cr/900
minortickt=ct*1.2

hrhandl=cr*0.6
hrhandw=2*np.pi*cr/450
hrhandt=ct*1.4
minhandl=cr*0.8
minhandw=2*np.pi*cr/550
minhandt=ct*1.2
secondhandl=cr*.9
secondhandt=ct*.8

hra=np.pi/2
mina=np.pi/2
seca=np.pi/2

deltamin=0.001
deltasec=deltamin*60
deltahr=deltamin/12

c=cylinder(axis=vector(0,0,1),pos=vector(0,0,-ct/2),radius=cr,length=ct,color=vector(0,1,.85))

hrhand=arrow(pos=vector(0,0,ct*1.5),axis=vector(0,1,0),length=hrhandl,color=color.red,shaftwidth=hrhandt)
minhand=arrow(pos=vector(0,0,ct*2.5),axis=vector(1,0,0),length=minhandl,color=color.orange,shaftwidth=minhandt)
secondhand=arrow(pos=vector(0,0,ct*2),axis=vector(0,1,0),length=secondhandl,color=color.black,shaftwidth=secondhandt)

x=cylinder(axis=vector(0,0,1),pos=vector(0,0,-0),radius=.05,length=ct*4,color=vector(1,0,0))
for i in np.linspace(0,2*np.pi,13):
    tic=box(axis=vector(cr*np.cos(i),cr*np.sin(i),0),color=color.black,length=majortick,width=majortickt,height=majortickw,pos=vector((cr-majortick/2)*np.cos(i),(cr-majortick/2)*np.sin(i),0))

for i in np.linspace(0,2*np.pi,61):
    mintic=box(axis=vector(cr*np.cos(i),cr*np.sin(i),0),color=color.black,length=minortick,width=minortickt,height=minortickw,pos=vector((cr-minortick/2)*np.cos(i),(cr-minortick/2)*np.sin(i),0))

while True:
    rate(5000)
    hr=time.localtime(time.time())[3]
    min=time.localtime(time.time())[4]
    sec=time.localtime(time.time())[5]
    if hr>12:hr=hr-12
    hra=-((hr+min/60)/12)*2*np.pi+np.pi/2
    mina=-((min+sec/60)/60)*2*np.pi+np.pi/2
    seca=-(sec/60)*2*np.pi+np.pi/2
    hrhand.axis=vector(hrhandl*np.cos(hra),hrhandl*np.sin(hra),0)
    minhand.axis=vector(minhandl*np.cos(mina),minhandl*np.sin(mina),0)
    secondhand.axis=vector(secondhandl*np.cos(seca),secondhandl*np.sin(seca),0)