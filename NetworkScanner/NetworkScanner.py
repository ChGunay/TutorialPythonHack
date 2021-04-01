import scapy.all as scapy

############################NetworkScanner Step-By-Step############################

#1)arp request
#2)brodcast
#3)responso

###################################################################################


arp_request_packet = scapy.ARP(pdst="192.168.1.1/16")#First, we create arp request packets for our target network.--Öncelikle hedef ağımız için arp istek paketleri oluşturuyoruz
#scapy.ls(scapy.ARP())
arp_brodcast_packet = scapy.Ether(dest = "ff:ff:ff:ff:ff:ff")#We create broadcast packages to make podcasts.--Podcast yapmak için yayın paketleri oluşturuyoruz.
#scapy.ls(scapy.Ether())
combined_packet = arp_brodcast_packet/arp_request_packet