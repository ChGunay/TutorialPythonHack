import subprocess
import time
import optparse#We add the optparse library to the script so that the content of the script can be determined by the user.--Optparse kitaplığını komut dosyasına ekliyoruz, böylece komut dosyasının içeriği kullanıcı tarafından belirlenebilir.

parse_object = optparse.OptionParser()#We create an object using the optparse library and using this object we can get options from the user.--Optparse kütüphanesini kullanarak bir nesne oluşturuyoruz ve bu nesneyi kullanarak kullanıcıdan seçenekler alabiliyoruz.
parse_object.add_option("-i","--interface", dest="interface", help = "interface to change!")#We direct the options we receive from the user to the variables in the script with dest.--Kullanıcıdan aldığımız seçenekleri dest ile betikteki değişkenlere yönlendiriyoruz.
parse_object.add_option("-m","--mac",dest="mac_adress", help= "New mac address")#We direct the options we receive from the user to the variables in the script with dest.--Kullanıcıdan aldığımız seçenekleri dest ile betikteki değişkenlere yönlendiriyoruz.

#print(parse_object.parse_args())#show change which we did--yaptığımız değişiklikleri gösterir.

(user_options,arguments) = parse_object.parse_args()
print(user_options.interface)#show our selected inteface--seçilen interface gösterir

print(user_options.mac_adress)#show our new mac address--yeni mac adresimizi gösterir

interface = user_options.interface
mac_adress= user_options.mac_adress

print("Mac Changer Started ")
subprocess.call(["ifconfig",interface,"down"])#First of all, we disable our internet tool.--Öncelikle internet aracımızı devre dışı bırakıyoruz.
subprocess.call(["ifconfig",interface,"hw","ether",mac_adress]) #By stating that we will make changes in the hardware, we enter our new mac address.--Donanımda değişiklik yapacağımızı belirterek yeni mac adresimize giriyoruz.  
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
    