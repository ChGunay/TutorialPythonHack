import subprocess
import time




print("Mac Changer Started ")
subprocess.call(["ifconfig","wlan0","down"])#First of all, we disable our internet tool.--Öncelikle internet aracımızı devre dışı bırakıyoruz.
subprocess.call(["ifconfig","wlan0","eth0","hw","ether","00:11:22:33:44:55"]) #By stating that we will make changes in the hardware, we enter our new mac address.--Donanımda değişiklik yapacağımızı belirterek yeni mac adresimize giriyoruz.  
subprocess.call(["ifconfig","wlan0","down"])#Finally, we activate our internet tool.--Son olarak internet aracımızı etkinleştiriyoruz.
animation = "|/-\\"
idx = 0
a=0
while a<10:
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)
    a+=1
    
print("Mac Changer Finished ")
    