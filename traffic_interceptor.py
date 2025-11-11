import subprocess
import sys

if len(sys.argv) < 3:
    sys.exit(1)

iface = sys.argv[1]
outfile = sys.argv[2]

print(f"Capturing traffic on {iface}...")

subprocess.run(['tcpdump', '-i', iface, '-w', outfile])
