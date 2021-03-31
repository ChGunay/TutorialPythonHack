import subprocess
import time
import optparse#We add the optparse library to the script so that the content of the script can be determined by the user.--Optparse kitaplığını komut dosyasına ekliyoruz, böylece komut dosyasının içeriği kullanıcı tarafından belirlenebilir.
import re

def get_user_input():#We have made our code smoother and simpler by using functions.--Fonksiyonları kullanarak kodumuzu daha temiz ve sorunsuz hale getirdik
    
    parse_object = optparse.OptionParser()#We create an object using the optparse library and using this object we can get options from the user.--Optparse kütüphanesini kullanarak bir nesne oluşturuyoruz ve bu nesneyi kullanarak kullanıcıdan seçenekler alabiliyoruz.
    parse_object.add_option("-i","--interface", dest="interface", help = "interface to change!")#We direct the options we receive from the user to the variables in the script with dest.--Kullanıcıdan aldığımız seçenekleri dest ile betikteki değişkenlere yönlendiriyoruz.
    parse_object.add_option("-m","--mac",dest="mac_address", help= "New mac address")#We direct the options we receive from the user to the variables in the script with dest.--Kullanıcıdan aldığımız seçenekleri dest ile betikteki değişkenlere yönlendiriyoruz.
    return parse_object.parse_args()



def change_mac_adress(interface,mac_address):#We have made our code smoother and simpler by using functions.--Fonksiyonları kullanarak kodumuzu daha temiz ve sorunsuz hale getirdik    
    subprocess.call(["ifconfig",interface,"down"])#First of all, we disable our internet tool.--Öncelikle internet aracımızı devre dışı bırakıyoruz.
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address]) #By stating that we will make changes in the hardware, we enter our new mac address.--Donanımda değişiklik yapacağımızı belirterek yeni mac adresimize giriyoruz.  
    subprocess.call(["ifconfig",interface,"down"])#Finally, we activate our internet tool.--Son olarak internet aracımızı etkinleştiriyoruz.

def detect_new_mac_address(interface):#This function will pull our new mac address from the system.--Bu fonksiyon yeni mac adresimizi sistemden çekecektir.
    ifconfig = subprocess.check_output("ifconfig", interface)#According to the interface received from the user, the subprocess will run ifconfig and assign the result to the variable.--Kullanıcıdan alınan arayüze göre, alt işlem ifconfig çalıştıracak ve sonucu değişkene atayacaktır.
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)#The information obtained using the regex library is filtered and only the mac address is obtained.--Düzenli ifade kitaplığı kullanılarak elde edilen bilgiler filtrelenir ve yalnızca mac adresi alınır.
    
    if new_mac:
        return new_mac.froup(0)
    else:
        return None
    


print("Mac Changer Started ")
(user_input,arguments)=get_user_input()
change_mac_adress(user_input.interface, user_input.mac_address)

finalized_mac = detect_new_mac_address(user_input.interface)

def control_new_mac_address(finalized_mac,mac_address):#This function compares the mac address entered by the user with the mac address of the instant system.--Bu işlev, kullanıcı tarafından girilen mac adresini anlık sistemin mac adresi ile karşılaştırır.
    if finalized_mac == mac_address:
        print("Succes!!")
    else:
        print("Error!!")
        
control_new_mac_address(finalized_mac, user_input.mac_address)

animation = "|/-\\"
idx = 0
a=0
while a<10:
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)
    a+=1
    
print("Mac Changer Finished ")
  