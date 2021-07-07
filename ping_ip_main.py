# typo error in import
import subprocess

for ping in range(10,22):
    address = "192.168.0." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print ("ping to this ip", address, "OK")
    elif res == 2:
        print ("no response from", address)
    else:
        print ("ping to", address, "failed!")
