FC:69:47:06:CB:C6

(bluetooth.src == fc:69:47:06:cb:c6 || bluetooth.dst == fc:69:47:06:cb:c6) && ((btatt.opcode == 0x52))

https://www.revogi.com/smart-power/power-plug-eu/#section0
https://git.geekify.de/sqozz/sem6000/src/commit/3673e31ffcd1ceaed6969dafb0f6dd967c253d11/sem6000.py


# Authorization with PIN
```
char-write-req 0x2b 0f0c170000000000000000000018ffff
                    | | |   | |     | |       | +  static end sequence of message, 0xffff
                    | | |   | |     | |       + checksum byte starting with length-byte, ending w/ byte before
                    | | |   | |     | + always 0x00000000
                    | | |   | + PIN, 4 bytes e.g. 01020304
                    | | |   + 0x00 for authorization request
                    | | + Authorization command 0x1700
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f


Notification handle = 0x002e value: 0f 06 17 00 00 00 00 18 ff ff
                                    |  |  |     |  |     |  + static end sequence of message, 0xffff
                                    |  |  |     |  |     + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     |  + always 0x0000  
                                    |  |  |     + 0 = success, 1 = unsuccess
                                    |  |  + Login command 0x1700
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```


# Change PIN 
```
char-write-req 0x2b 0f0c170001010203040000000018ffff
                    | | |     |       |       | +  static end sequence of message, 0xffff
                    | | |     |       |       + checksum byte starting with length-byte, ending w/ byte before
                    | | |     |       + old PIN, 4 bytes e.g. 01020304
                    | | |     + new PIN, 4 bytes e.g. 01020304
                    | | + Change pin command 0x170001
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f


Notification handle = 0x002e value: 0f 06 17 00 00 01 00 18 ff ff
                                    |  |  |     |        |  + static end sequence of message, 0xffff
                                    |  |  |     |        + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     + 0 = success  
                                    |  |  + Login command 0x170000
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```

# Reset PIN to "0000"
```
char-write-req 0x2b 0f0c170002000000000000000018ffff
                    | | |   | |               | +  static end sequence of message, 0xffff
                    | | |   | |               + checksum byte starting with length-byte, ending w/ byte before
                    | | |   | + static 0x0000000000000000
                    | | |   + 0x02 for reset PIN
                    | | + Authorization command 0x1700
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f


Notification handle = 0x002e value: 0f 06 17 00 00 02 00 18 ff ff
                                    |  |  |     |        |  + static end sequence of message, 0xffff
                                    |  |  |     |        + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     + 0 = success
                                    |  |  + Login command 0x170000
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```

# Switch on / off
```
char-write-req 0x2b 0f06030000000004ffff
                    | | |   | |   | + static end sequence of message, 0xffff
                    | | |   | |   + checksum byte starting with length-byte, ending w/ byte before
                    | | |   | + Static 0x0000
                    | | |   + 0x01 = turn on, 0x00 = turn off
                    | | + Switch command 0x0300
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f


Notification handle = 0x002e value: 0f 04 03 00 00 04 ff ff
                                    |  |  |     |  |  + static end sequence of message, 0xffff
                                    |  |  |     |  + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     + 0 = success
                                    |  |  + Switch command 0x0300
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```


# sync time
```
char-write-req 0x2b 0f0c010029180a160607e3000053ffff
                    | | |   | | | | | | | |   | + always ffff
                    | | |   | | | | | | | |   + checksum 1 - 12 & 255
                    | | |   | | | | | | | + always 0000
                    | | |   | | | | | +-+ year, high-byte, low-byte
                    | | |   | | | | + month
                    | | |   | | | + day of month
                    | | |   | | + hour
                    | | |   | + minute
                    | | |   + Seconds 
                    | | + Set datetime command, 0x0100
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f

Notification handle = 0x002e value: 0f 04 01 00 00 02 ff ff
                                    |  |  |     |  |  |  + static end sequence of message, 0xffff
                                    |  |  |     |  + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     + Success
                                    |  |  + Set datetime command, 0x0100
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```

# request configuration
char-write-req 0x2b 0f051600000017ffff

Notification handle = 0x002e value: 0f 0b 16 00 00 00 00 00 00 00 00 00 17 ff ff


# request status
char-write-req 0x2b 0f051000000011ffff

Notification handle = 0x002e value: 0f 0e 10 00 00 c8 64 00 00 00 00 01 00 0e 60 ac ff ff
                                    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
                                                |  |  |  |  |  |  |  |     |  + Over power low-byte
                                                |  |  |  |  |  |  |  |     + Over power high-byte
                                                |  |  |  |  |  |  |  + LED 1=on / 0=off
                                                |  |  |  |  |  |  + night mode end in min lox-byte
                                                |  |  |  |  |  + night mode end in min high-byte
                                                |  |  |  |  + night mode start in min low-byte
                                                |  |  |  + night mode start in min high-byte
                                                |  |  + night price
                                                |  + normal Price / 100.0
                                                + night mode active 1=yes, 0=no



char-write-req 0x2b 0f050400000005ffff

Notification handle = 0x002e value: 0f 11 04 00 01 00 00 41 ea 00 0c 32 00 00 00 00 00 00 6f

# Set LED on / off
## on
char-write-req 0x2b 0f090f0005010000000016ffff

Notification handle = 0x002e value: 0f 05 0f 00 05 00 15 ff ff


## off
char-write-req 0x2b 0f090f0005000000000015ffff

Notification handle = 0x002e value: 0f 05 0f 00 05 00 15 ff ff

# Get serial 
char-write-req 0x2b 0f051100000012ffff

Notification handle = 0x002e value: 0f 15 11 00 4d 4c 30 31 44 31 30 30 31 32 30 30 30 30 30 30
Notification handle = 0x002e value: 00 00 64 ff ff

# set name
char-write-req 0x2b 0f170200000000000000000000000000000000000000000000ffff
                      |   |                                       | + checksum
                      |   +---------------------------------------+ Name in ASCII
                      + set name command

# reset data
char-write-req 0x2b 

# data ???
15, 9, 15, 0, 5, (byte) var1, 0, 0, 0, 0, 0, -1, -



# get random mode setting
char-write-req 0x2b 0f051600000017ffff

Notification handle = 0x002e value: 0f 0b 16 00 00 00 00 00 00 00 00 00 17 ff ff

com.cei.meter.activity
com.cei.meter.fragment
com.cei.meter.thread.BleThread.class
com.cei.meter.actions.Config




----




 


 



# Name


# Version




# Notifications 

well known notifications
15 x

x
1 -> Password
2 -> Set name
3 -> switch tootle
4 -> current power 
5 -> over power set
8 -> Timer activity (start / stop)
9 -> get timer
15 -> set tarrif successful
16 -> Led status, price information, valley price, overload power?
17 -> serial number
19 skip
21 
22 -> random mode?
23 -> Login status, password data
255

else it is a data notification



## Switch toggled


## status related data
                self.btle_device.voltage = data[8]
                self.btle_device.current = (data[9] << 8 | data[10]) / 1000
                self.btle_device.power = (data[5] << 16 | data[6] << 8 | data[7]) / 1000
                self.btle_device.frequency = data[11]
                self.btle_device.powered = bool(data[4])




