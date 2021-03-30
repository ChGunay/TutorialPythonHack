import subprocess
import time
import optparse#We add the optparse library to the script so that the content of the script can be determined by the user.--Optparse kitaplığını komut dosyasına ekliyoruz, böylece komut dosyasının içeriği kullanıcı tarafından belirlenebilir.

parse_object = optparse.OptionParser()#We create an object using the optparse library and using this object we can get options from the user.--Optparse kütüphanesini kullanarak bir nesne oluşturuyoruz ve bu nesneyi kullanarak kullanıcıdan seçenekler alabiliyoruz.
parse_object.add_option("-i","--interface", dest="interface", help = "interface to change!")#We direct the options we receive from the user to the variables in the script with dest.--Kullanıcıdan aldığımız seçenekleri dest ile betikteki değişkenlere yönlendiriyoruz.


interface = "wlan0"
mac_adress= "10:00:22:44:55:44"

print("Mac Changer Started ")
subprocess.call(["ifconfig",interface,"down"])#First of all, we disable our internet tool.--Öncelikle internet aracımızı devre dışı bırakıyoruz.
subprocess.call(["ifconfig",interface,"hw","ether","00:11:22:33:44:55"]) #By stating that we will make changes in the hardware, we enter our new mac address.--Donanımda değişiklik yapacağımızı belirterek yeni mac adresimize giriyoruz.  
subprocess.call(["ifconfig",interface,"down"])#Finally, we activate our internet tool.--Son olarak internet aracımızı etkinleştiriyoruz.
animation = "|/-\\"
idx = 0
a=0
while a<10:
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)
    a+=1
    
print("Mac Changer Finished ")
    