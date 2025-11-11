# ARP Spoofing & DNS MitM with Scapy

## Setup
- Attacker: Kali Linux (192.168.56.104)
- Victim: Ubuntu (192.168.56.105)
- Gateway: Ubuntu (192.168.56.103)

## Task 1: ARP Spoofing
```bash
sudo python3 arp_spoof.py   
```

**Example:**
```bash
sudo python3 arp_spoof.py 192.168.56.105 192.168.56.103 eth0
```


## Task 2: Traffic Interception
```bash
sudo python3 traffic_interceptor.py  
```

**Example:**
```bash
sudo python3 traffic_interceptor.py eth0 capture.pcap
```

## Task 3: DNS Spoofing
**Terminal 1:**
```bash
sudo python3 arp_spoof.py 192.168.56.105 192.168.56.103 eth0
```

**Terminal 2:**
```bash
sudo python3 dns_spoof.py  
```

**Terminal 3:**
```bash
sudo python3 server.py
```

**On Victim:**
```bash
dig uis.no
```

### Open browser: http://uis.no

