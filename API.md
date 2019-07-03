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

# Capture measurement
```
char-write-req 0x2b 0f050400000005ffff
                    | | |       | + static end sequence of message, 0xffff
                    | | |       + checksum byte starting with length-byte, ending w/ byte before
                    | | + Capture measurement command 0x040000
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f


Notification handle = 0x002e value: 0f 11 04 00 01 00 00 00 eb 00 0c 32 00 00 00 00 00 00 2f
                                    |  |  |     |  |        |  |     |                    |  + Static end sequence (0xffff) is missing in this notification!
                                    |  |  |     |  |        |  |     |                    + checksum byte starting with length-byte
                                    |  |  |     |  |        |  |     |
                                    |  |  |     |  |        |  |     + frequency (Hz)
                                    |  |  |     |  |        |  + Ampere/1000 (A), 2 bytes
                                    |  |  |     |  |        + Voltage (V)
                                    |  |  |     |  |
                                    |  |  |     |  + Watt/1000, 3 bytes
                                    |  |  |     + Power, 0 = off, 1 = on
                                    |  |  + Capture measurement response 0x0400
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```

Note: Typical 0xffff end sequence is missing in this response. This is probably since there is no room for it.


# Synchronize datetime
```
char-write-req 0x2b 0f0c010029180a160607e3000053ffff
                    | | |   | | | | | | | |   | + always 0xffff
                    | | |   | | | | | | | |   + checksum byte starting with length-byte
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

# request settings
```
char-write-req 0x2b 0f051000000011ffff
                    | | |   |   | + always ffff
                    | | |   |   + checksum byte starting with length-byte
                    | | |   + always 0000
                    | | + Request settings command, 0x1000
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f

NNotification handle = 0x002e value: 0f 0e 10 00 00 c8 64 00 00 00 00 01 00 0e 60 ac ff ff
                                    |  |  |     |  |  |  |  |  |  |  |     |  |  |  + static end sequence of message, 0xffff
                                    |  |  |     |  |  |  |  |  |  |  |     |  |  + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     |  |  |  |  |  |  |  |     |  + Over power low-byte
                                    |  |  |     |  |  |  |  |  |  |  |     + Over power high-byte
                                    |  |  |     |  |  |  |  |  |  |  + LED 1=on / 0=off
                                    |  |  |     |  |  |  |  |  |  + night mode end in min lox-byte
                                    |  |  |     |  |  |  |  |  + night mode end in min high-byte
                                    |  |  |     |  |  |  |  + night mode start in min low-byte
                                    |  |  |     |  |  |  + night mode start in min high-byte
                                    |  |  |     |  |  + night price / 100.0
                                    |  |  |     |  + normal Price / 100.0
                                    |  |  |     + night mode active 1=yes, 0=no
                                    |  |  + Request settings command, 0x1000
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```

# Set LED ring
```
char-write-req 0x2b 0f090f0005010000000016ffff
                    | | |   | | |       | + always 0xffff
                    | | |   | | |       + checksum byte starting with length-byte
                    | | |   | | + always 0x00000000
                    | | |   | + 1 = on, 0 = off
                    | | |   + always 0x05
                    | | + Set LED ring command, 0x0f00
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f

Notification handle = 0x002e value: 0f 05 0f 00 05 00 15 ff ff
                                    |  |  |     |     |  + static end sequence of message, 0xffff
                                    |  |  |     |     + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     + always 0x0500
                                    |  |  + Set LED ring command, 0x0f00
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```

# Set overload power
```
char-write-req 2b 0f0705000e60000074ffff
                    | |   |   |   | + static end sequence of message, 0xffff
                    | |   |   |   + checksum byte starting with length-byte, ending w/ byte before
                    | |   |   + status 0x0000
                    | |   | + overload value, low-byte
                    | |   + overload value, high-byte
                    | + Set overload command, 0x0500
                    + static start sequence for message, 0x0f

Notification handle = 0x002e value: 0f 04 05 00 00 06 ff ff
                                    |  |  |     |  |  + static end sequence of message, 0xffff
                                    |  |  |     |  + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     + always 0x00
                                    |  |  + Set overload command, 0x0500
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```

# Set tarrif
```
15, 9, 15, 0, 4, normal price, night price, 0, 0, 0, 0, sum, 255, 255
15, 9, 15, 0, 1, night mode (1|0), start minutes high-byte, start minutes low-byte, end minutes high-byte, end minutes low-byte, sum, 255, 255
```



# get name

char-read-hnd 25 00
Characteristic value/descriptor: 56 4f 4c 43 46 54 04 00 00 00 00 01 0d 02 00 1e

# set name
char-write-req 0x2b 0f170200000000000000000000000000000000000000000000ffff
                      |   |                                       | + checksum
                      |   +---------------------------------------+ Name in ASCII
                      + set name command


# Get serial
char-write-req 0x2b 0f051100000012ffff

Notification handle = 0x002e value: 0f 15 11 00 4d 4c 30 31 44 31 30 30 31 32 30 30 30 30 30 30
Notification handle = 0x002e value: 00 00 64 ff ff



# reset data
char-write-req 0x2b
15, 5, 16, 0, 0, 0, 17, -1, -1

15, 9, 15, 0, 0, 0, 0, 0, 0, 0, 16, -1, -1
15, 9, 15, 0, 2, 0, 0, 0, 0, 0, 18, -1, -1

# request randommode
```
char-write-req 0x2b 0f051600000017ffff

Notification handle = 0x002e value: 0f 0b 16 00 00 00 00 00 00 00 00 00 17 ff ff
```


# requset / reset date?
15, 9, 15, 0, 5, data, 0,0,0,0, sum 255, 255

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
