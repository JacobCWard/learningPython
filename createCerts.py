#!/usr/bin/python

names = ["jacob","jacob1","jacob2"]
#["calvin1","calvin2","claude1","claude2","edwin1","edwin2","erin1","erin2","sam1","sam2","nick1","nick2","ethan1","ethan2","lakshmi1","lakshmi2","juan1","juan2","alan1","alan2","jacob1","jacob2"]

for name in names:
    os.system("docker run --volumes-from $OVPN_DATA --rm -it kylemanna/openvpn easyrsa build-client-full "+name+" nopass")
