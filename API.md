FC:69:47:06:CB:C6

(bluetooth.src == fc:69:47:06:cb:c6 || bluetooth.dst == fc:69:47:06:cb:c6) && ((btatt.opcode == 0x52))

https://www.revogi.com/smart-power/power-plug-eu/#section0
https://git.geekify.de/sqozz/sem6000/src/commit/3673e31ffcd1ceaed6969dafb0f6dd967c253d11/sem6000.py


com.cei.meter.activity
com.cei.meter.fragment
com.cei.meter.thread.BleThread.class
com.cei.meter.actions.Config


GetStatus

Handle: 1010 (WRITE_BLE_DATA)
15, 5, 4, 0, 0, 0, 5, 255, 255

    + cmd

Sync Config
Handle: 1010 (WRITE_BLE_DATA)
15, 5, 16, 0, 0, 0, 17, 255, 255
    + cmd

Sync Time
15, 12, 1, 0, <seconds>, <minute>, <hour>, <day of month>, <month, 1=January>, <year, high-byte>, <year, low-byte>, 0, 0, <chechsum 1 - 12 & 255>, 255, 255
    + cmd
 
# Switch on / off
        # 0f 06 03 00 01 00 00 05 ff ff  -> on
        # 0f 06 03 00 00 00 00 04 ff ff  -> off

# Login
        print("Login")
        self.password = password
        cmd = bytearray([0x17])
        payload = bytearray()
        payload.append(0x00)
        payload.append(0x00)
        payload.append(int(self.password[0]))
        payload.append(int(self.password[1]))
        payload.append(int(self.password[2]))
        payload.append(int(self.password[3]))
        payload.append(0x00)
        payload.append(0x00)
        payload.append(0x00)
        payload.append(0x00)
        msg = self.BTLEMessage(self, cmd, payload)
        msg.send()

## change password

15, 12, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1



        payload.append(0x00)
        payload.append(0x01)
        payload.append(int(newPassword[0]))
        payload.append(int(newPassword[1]))
        payload.append(int(newPassword[2]))
        payload.append(int(newPassword[3]))
        payload.append(int(self.password[0]))
        payload.append(int(self.password[1]))
        payload.append(int(self.password[2]))
        payload.append(int(self.password[3]))


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
