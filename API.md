# PIN
## Authorization with PIN
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


## Change PIN
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

## Reset PIN to "0000"
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

# Setup and settings
## Synchronize datetime
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

## Request settings
```
char-write-req 0x2b 0f051000000011ffff
                    | | |   |   | + always ffff
                    | | |   |   + checksum byte starting with length-byte
                    | | |   + always 0000
                    | | + Request settings command, 0x1000
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f

Notification handle = 0x002e value: 0f 0e 10 00 00 c8 64 00 00 00 00 01 00 0e 60 ac ff ff
                                    |  |  |     |  |  |  |  |  |  |  |     |  |  |  + static end sequence of message, 0xffff
                                    |  |  |     |  |  |  |  |  |  |  |     |  |  + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     |  |  |  |  |  |  |  |     |  + Over power low-byte
                                    |  |  |     |  |  |  |  |  |  |  |     + Over power high-byte
                                    |  |  |     |  |  |  |  |  |  |  + LED 1=on / 0=off
                                    |  |  |     |  |  |  |  |  |  + reduced mode end in min lox-byte
                                    |  |  |     |  |  |  |  |  + reduced mode end in min high-byte
                                    |  |  |     |  |  |  |  + reduced mode start in min low-byte
                                    |  |  |     |  |  |  + reduced mode start in min high-byte
                                    |  |  |     |  |  + reduced price / 100.0
                                    |  |  |     |  + normal Price / 100.0
                                    |  |  |     + reduced mode active 1=yes, 0=no
                                    |  |  + Request settings command, 0x1000
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```

## Set LED ring
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

## Set overload power
```
char-write-req 2b 0f0705000e60000074ffff
                  | | |   |   |   | + static end sequence of message, 0xffff
                  | | |   |   |   + checksum byte starting with length-byte, ending w/ byte before
                  | | |   |   + status 0x0000
                  | | |   + overload value, low-byte
                  | | | + overload value, high-byte
                  | | + Set overload command, 0x0500
                  | + Length of payload starting w/ next byte incl. checksum
                  + static start sequence for message, 0x0f

Notification handle = 0x002e value: 0f 04 05 00 00 06 ff ff
                                    |  |  |     |  |  + static end sequence of message, 0xffff
                                    |  |  |     |  + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     + always 0x00
                                    |  |  + Set overload command, 0x0500
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```

## Set prices
```
char-write-req 2b 0f90f00047b2d00000000b2ffff
                  | | |     | | |       | + End sequence 0xffff
                  | | |     | | |       + Checksum
                  | | |     | | + static 0x00000000
                  | | |     | + reduced price * 100
                  | | |     + normal price * 100
                  | | + Setprice command, 0x0f0004
                  | + Length of payload starting w/ next byte incl. checksum
                  + static start sequence for message, 0x0f

Notification handle = 0x2b value: 0f 05 0f 00 04 00 14 ff ff
                                  |  |  |        |  |  + static end sequence of message, 0xffff
                                  |  |  |        |  + checksum byte starting with length-byte, ending w/ byte before
                                  |  |  |        + always 0x00
                                  |  |  + Set price command, 0x0f0004
                                  |  + Length of payload starting w/ next byte incl. checksum
                                  + static start sequence for message, 0x0f
```

## Set reduced period
```
char-write-req 2b 0f090f000101005301288effff
                  | | |     | |   |    | + End sequence 0xffff
                  | | |     | |   |    + Checksum
                  | | |     | |   + 2 bytes for end time in minutes, here 04:56
                  | | |     | + 2 bytes for start time in minutes, here 01:23
                  | | |     + reduced period on / off, 1 = on, 0 = off
                  | | + Set reduced period command, 0x0f0001
                  | + Length of payload starting w/ next byte incl. checksum
                  + static start sequence for message, 0x0f

Notification handle = 0x2b value: 0f 05 0f 00 01 00 11 ff ff
                                  |  |  |        |  |  + static end sequence of message, 0xffff
                                  |  |  |        |  + checksum byte starting with length-byte, ending w/ byte before
                                  |  |  |        + always 0x00
                                  |  |  + Set reduced period command, 0x0f0001
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

# Timer
## Get timer status
```
char-write-req 2b 0f05090000000affff

Notification handle = 0x2b value: 0f 0e 09 00 01 10 04 10 08 07 13 01 51 45 00 e8 ff ff
                                  |  |  |     |  |  |  |  |  |  |  |           |  + static end sequence of message, 0xffff
                                  |  |  |     |  |  |  |  |  |  |  |           + checksum byte starting with length-byte, ending w/ byte before
                                  |  |  |     |  |  |  |  |  |  |  + Origin runtime in seconds, 3 bytes
                                  |  |  |     |  |  |  |  |  |  + target year
                                  |  |  |     |  |  |  |  |  + target Month
                                  |  |  |     |  |  |  |  + target day on month
                                  |  |  |     |  |  |  + target hour
                                  |  |  |     |  |  + target minute
                                  |  |  |     |  + target second
                                  |  |  |     + Action, 1 = turn on, 2 = turn off
                                  |  |  + Request timer status command, 0x0900
                                  |  + Length of payload starting w/ next byte incl. checksum
                                  + static start sequence for message, 0x0f
```

## Set timer
```
char-write-req 2b 0f0c0800012d1c1607071300008affff
                  | | |   | | | | | | | |   | + static end sequence of message, 0xffff
                  | | |   | | | | | | | |   + checksum byte starting with length-byte, ending w/ byte before
                  | | |   | | | | | | | + Static 0x0000
                  | | |   | | | | | | + Schedule year
                  | | |   | | | | | + Schedule month
                  | | |   | | | | + Schedule day of month
                  | | |   | | | + Schedule hour
                  | | |   | | + Schedule minutes
                  | | |   | + Schedule seconds
                  | | |   + Timer action, 1 = on, 2 = off
                  | | + Set timer command, 0x0800
                  | + Length of payload starting w/ next byte incl. checksum
                  + static start sequence for message, 0x0f

Notification handle = 0x2b value: 0f 04 08 00 00 09 ff ff
                                  |  |  |        |  + static end sequence of message, 0xffff
                                  |  |  |        + checksum byte starting with length-byte, ending w/ byte before
                                  |  |  + Request timer status command, 0x080000
                                  |  + Length of payload starting w/ next byte incl. checksum
                                  + static start sequence for message, 0x0f
```

## Stop timer
```
char-write-req 2b 0f0c080000000000000000000009ffff
                  | | |   | | | | | | | |   | + static end sequence of message, 0xffff
                  | | |   | | | | | | | |   + checksum byte starting with length-byte, ending w/ byte before
                  | | |   | | | | | | | + Static 0x0000
                  | | |   | | | | | | + Schedule year, 0 for reset
                  | | |   | | | | | + Schedule month, 0 for reset
                  | | |   | | | | + Schedule day of month, 0 for reset
                  | | |   | | | + Schedule hour, 0 for reset
                  | | |   | | + Schedule minutes, 0 for reset
                  | | |   | + Schedule seconds, 0 for reset
                  | | |   + Timer action, 0 = reset
                  | | + Set timer command, 0x0800
                  | + Length of payload starting w/ next byte incl. checksum
                  + static start sequence for message, 0x0f

Notification handle = 0x2e value: 0f 04 08 00 00 09 ff ff
                                  |  |  |        |  + static end sequence of message, 0xffff
                                  |  |  |        + checksum byte starting with length-byte, ending w/ byte before
                                  |  |  + Request timer status command, 0x080000
                                  |  + Length of payload starting w/ next byte incl. checksum
                                  + static start sequence for message, 0x0f
```

# Scheduler
## Request scheduler

No schedulers set
```
char-write-req 2b 0f06140000000015ffff
                  | | |   |     | + static end sequence of message, 0xffff
                  | | |   |     + checksum byte starting with length-byte, ending w/ byte before
                  | | |   + Page if more than 4 schedulers, 0 = 1st page , 1 = 2nd page
                  | | + Set timer command, 0x1400
                  | + Length of payload starting w/ next byte incl. checksum
                  + static start sequence for message, 0x0f

No schedulers:
Notification handle = 0x2e value: 0f 04 14 00 00 15 ff ff
                                  |  |  |     + Number of active schedulers, here no slots set
                                  |  |  + Request schedulers command, 0x1400
                                  |  + Length of payload starting w/ next byte incl. checksum
                                  + static start sequence for message, 0x0f
```

If only 1 scheduler is set then there is a single notification.
```
Notification handle = 0x2e value: 0f 10 14 00 01 0c 01 01 00 13 08 09 0a 0b 00 00 4f ac ff ff
                                  |  |  |     |  |  |  |  |  |  |  |  |  |  |     + some kind of checksum for specific scheduler
                                  |  |  |     |  |  |  |  |  |  |  |  |  |  + static, 0x0000
                                  |  |  |     |  |  |  |  |  |  |  |  |  + Minute
                                  |  |  |     |  |  |  |  |  |  |  |  + Hour
                                  |  |  |     |  |  |  |  |  |  |  + day in month
                                  |  |  |     |  |  |  |  |  |  + Month
                                  |  |  |     |  |  |  |  |  + Year (2 digts)
                                  |  |  |     |  |  |  |  + Weekday mask, 0 if once
                                  |  |  |     |  |  |  + Action, 1 = turn on, 0 = turn off
                                  |  |  |     |  |  + Active, 0 = inactive, 1 = active
                                  |  |  |     |  + Slot ID
                                  |  |  |     + Number of active schedulers, here 1 
                                  |  |  + Request scheduler status command, 0x1400
                                  |  + Length of payload starting w/ next byte incl. checksum
                                  + static start sequence for message, 0x0f
```

If there are more than 1 schedulers set then there are multiple notifications. 
```
# notification #1
Notification handle = 0x2e value: 0f 28 14 00 03 0a 01 01 01 13 07 0d 0b 2c 00 00 75 0b 01 00
                                  |  |  |     |  |  |  |  |  |  |  |  |  |  |     + Checksum of scheduler?
                                  |  |  |     |  |  |  |  |  |  |  |  |  |  + static, 0x0000
                                  |  |  |     |  |  |  |  |  |  |  |  |  + Minute
                                  |  |  |     |  |  |  |  |  |  |  |  + Hour
                                  |  |  |     |  |  |  |  |  |  |  + day in month
                                  |  |  |     |  |  |  |  |  |  + Month
                                  |  |  |     |  |  |  |  |  + Year (2 digts)
                                  |  |  |     |  |  |  |  + Weekday mask, 0 if once, 1 = Sunday, 2 = Monday, 4 = Tuesday, etc.
                                  |  |  |     |  |  |  + Action, 1 = turn on, 0 = turn off
                                  |  |  |     |  |  + Active, 0 = inactive, 1 = active
                                  |  |  |     |  + Slot ID, starting with 10, 0x0a=0, 0x0b=1, 0x0c=2
                                  |  |  |     + Number of active schedulers, here 3
                                  |  |  + Request scheduler status command, 0x1400
                                  |  + Length of payload starting w/ next byte incl. checksum
                                  + static start sequence for message, 0x0f

# notification #2
Notification handle = 0x2e value: 7f 13 07 0d 0e 0f 00 00 e4 0c 00 01 00 13 08 09 0a 0b 00 00

# notification #3
Notification handle = 0x2e value: 5b 4c ff ff
``` 

Request 2nd page
```
char-write-req 2b 0f06140001000016ffff
                          + Page if more than 4 schedulers, 0 = 1st page , 1 = 2nd page

Notification handle = 0x2e value: 0f 10 14 00 05 0b 01 00 01 13 07 0e 01 01 00 00 40 91 ff ff
```

## Set scheduler
```
char-write-req 2b 0f0f1300010001010113070e0e1a000068ffff
                  | | |   | | | | | | | | | | |   | + Static end sequence of message, 0xffff 
                  | | |   | | | | | | | | | | |   + Checksum byte starting with length-byte, ending w/ byte before
                  | | |   | | | | | | | | | | + Static 0x0000
                  | | |   | | | | | | | | | + Minute
                  | | |   | | | | | | | | + Hour
                  | | |   | | | | | | | + Day of month
                  | | |   | | | | | | + Month, 1 = January
                  | | |   | | | | | + Year, 2 digits, eg. 19 for 2019
                  | | |   | | | | + Weekday mask, 7 bits, 1st bit = Sunday, ... 
                  | | |   | | | + Action, 1 = turn on, 0 = turn off
                  | | |   | | + State , 1 = active, 0 = inactive
                  | | |   | + If edit / remote scheduler then ID of slot else 0x00
                  | | |   + 0 = add new scheduler, 1 = edit existing scheduler, 2 = remove scheduler
                  | | + Set timer command, 0x1300
                  | + Length of payload starting w/ next byte incl. checksum
                  + Static start sequence for message, 0x0f

Notification handle = 0x2b value: 0f 06 13 00 01 00 00 15 ff ff
                                  |  |  |     |  |     |  + Static end sequence of message, 0xff
                                  |  |  |     |  |     + Checksum byte starting with length-byte, ending w/ byte before
                                  |  |  |     |  + Static 0x0000
                                  |  |  |     + 0 = success, 1 = unsuccess
                                  |  |  + Set timer command, 0x1300
                                  |  + Length of payload starting w/ next byte incl. checksum
                                  + Static start sequence for message, 0x0f
```

## Reset scheduler
```
char-write-req 2b 0f0f1300020c0000000000000000000022ffff
                          | + ID of slot
                          + 2 = remove scheduler
```

# Random mode
## Get randommode

```
char-write-req 0x2b 0f051600000017ffff

Notification handle = 0x2b value: 0f 0b 16 00 01 55 02 03 04 05 00 00 7b ff ff
                                  |  |  |     |  |  |  |  |  |        |  + Static end sequence of message, 0xffff 
                                  |  |  |     |  |  |  |  |  |        + Checksum byte starting with length-byte, ending w/ byte before            
                                  |  |  |     |  |  |  |  |  + End minute
                                  |  |  |     |  |  |  |  + End hour
                                  |  |  |     |  |  |  + Start minute
                                  |  |  |     |  |  + Start hour
                                  |  |  |     |  + Weekday mask, bit 1 = Sunday, bit 2 = Monday, etc.
                                  |  |  |     + Randommode status, 1 = on, 0 = off
                                  |  |  + Request scheduler status command, 0x1600
                                  |  + Length of payload starting w/ next byte incl. checksum
                                  + static start sequence for message, 0x0f
```

## Set random mode
```
char-write-req 2b 0f0b1500017f020304050000a4ffff
                  | | |   | | | | | |     | + Static end sequence of message, 0xffff
                  | | |   | | | | | |     + Checksum byte starting with length-byte, ending w/ byte before           
                  | | |   | | | | | + End minute
                  | | |   | | | | + End hour
                  | | |   | | | + Start minute
                  | | |   | | + Start hour
                  | | |   | + Weekday mask, bit 1 = Sunday, bit 2 = Monday, etc.
                  | | |   + Randommode status, 1 = on, 0 = off
                  | | + Set randommode command 0x1500
                  | + Length of payload starting w/ next byte incl. checksum
                  + static start sequence for message, 0x0f

Notification handle = 0x2b value: 0f 04 15 00 00 16 ff ff
```

# Measure power and consumption
## Capture measurement
```
char-write-req 0x2b 0f050400000005ffff
                    | | |       | + static end sequence of message, 0xffff
                    | | |       + checksum byte starting with length-byte, ending w/ byte before
                    | | + Capture measurement command 0x040000
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f


Notification handle = 0x002e value: 0f 11 04 00 01 00 00 00 eb 00 0c 32 00 00 00 00 00 00 2f
                                    |  |  |     |  |        |  |     |        |           |  + Static end sequence (0xffff) is missing in this notification!
                                    |  |  |     |  |        |  |     |        |           + checksum byte starting with length-byte
                                    |  |  |     |  |        |  |     |        + total consumption, 4 bytes
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

## Reguest measurements for year, month and day
```
char-write-req 2b 0f050b0000000cffff
                  | | | |     | + static end sequence of message, 0xffff
                  | | | |     + checksum byte starting with length-byte, ending w/ byte before
                  | | | + Static 0x000000
                  | | + 0a = last 24h per hour, 0b = last 30 days per day, 0c = last year per month
                  | + Length of payload starting w/ next byte incl. checksum
                  + static start sequence for message, 0x0f

```

After this request there are several notification handles. 

### Year
For requests on year level there are 12 records for each month. Each records has 4 bytes and 3 bytes representing for consumption in Wh. 

```
Notification handle = 0x002e value: 0f 33 0c 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
                                    |  |  |     |           |           |           + Current month - 8, 3 bytes for Wh
                                    |  |  |     |           |           + Current month - 9, 3 bytes for Wh
                                    |  |  |     |           + Current month - 10, 3 bytes for Wh
                                    |  |  |     + Current month - 11, 3 bytes for Wh
                                    |  |  + 0x0c00, Request data for year request
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f

Notification handle = 0x002e value: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
                                    |           |           |           |           + Current month - 3, 3 bytes for Wh
                                    |           |           |           + Current month - 4, 3 bytes for Wh
                                    |           |           + Current month - 5, 3 bytes for Wh
                                    |           + Current month - 6, 3 bytes for Wh
                                    + Current month - 7, 3 bytes for Wh

Notification handle = 0x002e value: 00 00 00 00 00 00 00 00 00 04 e3 00 f4 ff ff
                                    |           |           |           |  + static end sequence of message, 0xffff
                                    |           |           |           + checksum byte starting with length-byte, ending w/ byte before
                                    |           |           + Current month, 3 bytes for Wh
                                    |           + Current month - 1, 3 bytes for Wh
                                    + Current month - 2, 3 bytes for Wh
```

### Month
For requests on month level there are 30 records for each day in month. Each records has 4 bytes and 3 bytes  representing for consumption in Wh. 

```
Notification handle = 0x002e value: 0f 7b 0b 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
                                    |  |  |     |           |           |           + Today - 26, 3 bytes for Wh
                                    |  |  |     |           |           + Today - 27, 3 bytes for Wh
                                    |  |  |     |           + Today - 28, 3 bytes for Wh
                                    |  |  |     + Today - 29, 3 bytes for Wh
                                    |  |  + 0x0c00, Request data for month request
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f

Notification handle = 0x002e value: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Notification handle = 0x002e value: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Notification handle = 0x002e value: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Notification handle = 0x002e value: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Notification handle = 0x002e value: 00 00 00 00 00 00 e3 00 00 01 37 00 00 01 23 00 00 01 37 00
Notification handle = 0x002e value: 00 00 6f 00 f2 ff ff
                                    |           |  + static end sequence of message, 0xffff
                                    |           + checksum byte starting with length-byte, ending w/ byte before
                                    + Today, 3 bytes for Wh
```

### Day
For requests on day level there are 24 records for each hour in day. Each records has 2 bytes representing for consumption in Wh. 

```
Notification handle = 0x002e value: 0f 33 0a 00 00 0e 00 0e 00 0e 00 0e 00 0c 00 09 00 08 00 0b
                                    |  |  |     |     |     |     |     |     |     |     + Current hour - 16, 2 bytes for Wh
                                    |  |  |     |     |     |     |     |     |     + Current hour - 17, 2 bytes for Wh
                                    |  |  |     |     |     |     |     |     + Current hour - 18, 2 bytes for Wh
                                    |  |  |     |     |     |     |     + Current hour - 19, 2 bytes for Wh
                                    |  |  |     |     |     |     + Current hour - 20, 2 bytes for Wh
                                    |  |  |     |     |     + Current hour - 21, 2 bytes for Wh
                                    |  |  |     |     + Current hout - 22, 3 bytes for Wh
                                    |  |  |     + Current hour - 23, 2 bytes for Wh
                                    |  |  + 0x0c00, Request data for month request
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f

Notification handle = 0x002e value: 00 0e 00 0e 00 11 00 0f 00 10 00 0f 00 0d 00 0e 00 0e 00 0e
Notification handle = 0x002e value: 00 0e 00 0e 00 0e 00 0e 00 0d 00 00 42 ff ff
                                                            |     |     |  + static end sequence of message, 0xffff
                                                            |     |     + checksum byte starting with length-byte, ending w/ byte before
                                                            |     + Current hour, 2 bytes for Wh
                                                            + Current hour - 2 , 2 bytes for Wh
```

## Reset data
```
char-write-req 2b 0f090f0000000000000010ffff
                  | | |   |           | + static end sequence of message, 0xffff
                  | | |   |           + checksum byte starting with length-byte, ending w/ byte before
                  | | |   + 0 = factory reset, 2 = reset stored consumption
                  | | + Reset command 0x0f00
                  | + Length of payload starting w/ next byte incl. checksum
                  + static start sequence for message, 0x0f


Notification handle = 0x002b value: 0f 05 0f 00 00 00 10 ff ff
                                    |  |  |     |     |  + Static end sequence (0xffff) is missing in this notification!
                                    |  |  |     |      + checksum byte starting with length-byte
                                    |  |  |     + 0 = factory reset, 2 = reset stored consumption
                                    |  |  + Reset command, 0x0f00
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```


# Device settings
## Get name
```
char-read-hnd 3
Characteristic value/descriptor: 48 6f 6c 6c 61 64 69 65 77 61 6c 64 66 65 65

Convert values to ascii,e.g.

Holladiewaldfee
```

## Set name
```
char-write-req 0x2b 0f170200000000000000000000000000000000000000000000ffff
                    | | |   |                                 | |   + checksum
                    | | |   |                                 | + static 0x0000
                    | | |   +---------------------------------+ Name in ASCII, max. 18 characters
                    | | + Set name command, 0x0200
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f

Notification handle = 0x002e value: 0f 04 02 00 00 03 ff ff
                                    |  |  |     |  |  + static end sequence of message, 0xffff
                                    |  |  |     |  + checksum byte starting with length-byte, ending w/ byte before
                                    |  |  |     + always 0x00
                                    |  |  + Set name command, 0x0200
                                    |  + Length of payload starting w/ next byte incl. checksum
                                    + static start sequence for message, 0x0f
```

## Get serial
```
char-write-req 0x2b 0f051100000012ffff
                    | | |   |   + checksum
                    | | |   + static 0x0000
                    | | + Get serial command, 0x1100
                    | + Length of payload starting w/ next byte incl. checksum
                    + static start sequence for message, 0x0f


Notification handle = 0x002e value: 0f 15 11 00 4d 4c 30 31 44 31 30 30 31 32 30 30 30 30 30 30
Notification handle = 0x002e value: 00 00 64 ff ff
```

The serial number is ASCII coded between bytes 5 and 20. In this example the serial is "ML01D10012000000"
Note that there are two notifications!
