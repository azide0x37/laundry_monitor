# laundry_monitor

### Install

`brew install terminal-notifier`

Note: if you don't have the Samantha voice installed, either install it in `macos>preferences>accessability>spoken content`, or just remove the '-v' and 'Samantha' args from lines 21 and 29 to use the default voice. 
'''

### Usage
Call on command line with device IP as argument. 

#### To get the device IP
'''
❯ kasa
No host name given, trying discovery..
Discovering devices on 255.255.255.255 for 3 seconds
== Washer  - HS110(US) ==
        Host: xxx.xxx.xxx.xxx
        Device state: ON

        == Generic information ==
        Time:         2022-05-05 15:02:18
        Hardware:     1.0
        Software:     1.2.6 Build 200727 Rel.121701
        MAC (rssi):   50:C7:BF:xx:xx:xx (-64)
        Location:     {'latitude': xx.xxx, 'longitude': xx.xxx}

        == Device specific information ==
        LED state: True
        On since: 2022-04-18 10:34:46

        == Current State ==
        <EmeterStatus power=0.768329 voltage=121.20441 current=0.031014 total=1.098>'''

'''
❯ python main.py 192.168.1.xx
Current power usage is 1.32 watts...
'''