#!/usr/bin/env python3
import sys
import time
import bluetooth


addr = None

if len(sys.argv) < 2:
    print("No device specified. Searching all nearby bluetooth devices for "
          "the SampleServer service...")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on {}...".format(addr))

# search for the SampleServer service
uuid = "00001101-0000-1000-8000-00805F9B34FB"



while 1:
    print("searching...")
    service_matches = bluetooth.find_service(uuid=uuid, address=addr)
    if len(service_matches) == 0:
        print("Couldn't find the Server service.")
        time.sleep(2)
    else:
        break

print(service_matches)
first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"{}\" on {}".format(name, host))

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

print("Connected. Type something...")
while True:
    data = input()
    if not data:
        break
    sock.send(data)

sock.close()
