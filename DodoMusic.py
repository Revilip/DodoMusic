import wave
import math
import struct
f=wave.open("wave.wav","w")
f.setframerate(8000)
f.setnchannels(1)
f.setsampwidth(2)

def writewav(file,t=0,fre=0,vol=0.5,sr=8000):
    tt=0
    dt=1.0/sr
    while tt<=t:
        s=math.sin(tt*math.pi*2*fre)*vol*32768
        s=int(s)
        file.writeframes(struct.pack("h",s))
        tt+=dt

fres=[262,277,294,311,330,349,370,392,415,440,466,494]

with open("music.txt","r") as fn:
    data_origin=fn.read()

data=[]
time=[]

def process():
    flag=False
    count=1
    for i in range(len(data_origin)):
        char=data_origin[i]
        if char=='0':
            data.append(-1)
            time.append(count)
            count=1
        elif char=='1':
            data.append(0)
            time.append(count)
            count=1
        elif char=='2':
            data.append(2)
            time.append(count)
            count=1
        elif char=='3':
            data.append(4)
            time.append(count)
            count=1
        elif char=='4':
            data.append(5)
            time.append(count)
            count=1
        elif char=='5':
            data.append(7)
            time.append(count)
            count=1
        elif char=='6':
            data.append(9)
            time.append(count)
            count=1
        elif char=='7':
            data.append(11)
            time.append(count)
            count=1
        elif char=='#':
            data[len(data)-1]+=1
        elif char=='+':
            data[len(data)-1]+=12
        elif char=='|':
            count+=1
        elif char=='$':
            if(count==1):
                count=4
            else:
                count+=4

process()

print(len(data))
print(data)
print(time)

def freq(q):
    if(q==-1):
        return 0
    return fres[q%12]*(q//12+1)

div=8.0

for i in range(len(data)):
    writewav(f,time[i]/div,freq(data[i]))

f.close()
