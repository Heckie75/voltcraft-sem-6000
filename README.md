# voltcraft-sem-6000
_"A full-features shell script in order to manage bluetooth switch, scheduler and smart energy meter Voltcraft SEM 6000 with Linux and Raspberry Pi"_

The Voltcraft SEM-6000 is a remote 230V switch and smart energy meter. It was sold by *Conrad Elektronik* in Germany. 


For details take a look at [Conrad](https://www.conrad.de/de/p/voltcraft-sem6000-energiekosten-messgeraet-bluetooth-schnittstelle-datenexport-datenloggerfunktion-trms-stromtarif-e-1558906.html). The device is also known as _Smart Power Plug EU_ by Revogi, see https://www.revogi.com/smart-power/power-plug-eu/#section0

In comparison to many remote switches which use the 433MHz band the SEM-6000 is based on bluetooth v4.0. The advantage is that there is no need to have additional hardware, e.g. via GPIO connected sender/receiver. 

Voltcraft SEM-6000  has the following features:
* 12 schedulers which can run once or assigned to weekdays
* Countdown mode in order to switch power _on_ or _off_ after a certain period 
* Configurable overload-mode in order to auto-turn-off or alarm in case of power overload
* Energy meter in order to measure volt, ampere and watts in realtime
* Energy meter recorder in order to measure power consumption over long period

For official manual by Voltcraft visit [Conrad](https://produktinfo.conrad.com/datenblaetter/1500000-1599999/001558906-an-01-en-APP_VOLTCRAFT_SEM6000_BLUETOOTH_EKM.pdf)

## Getting started
### 1. Check pre-conditions

Install `expect`:
```
$ sudo apt install expect
```

Check if `gatttool` is available:
```
$ gatttool
Usage:
  gatttool [OPTION...]
...

```

### 2. Discover the MAC address of the smart energy meter

```
$ sudo hcitool lescan
E Scan ...
FC:69:47:06:CB:C6 Voltcraft
```

The devices are called "Voltcraft" by default. Note that device appears with a different name if you have renamed if before.

### 3. Pair bluetooth

There is no need to pair device.


### 4. Aliases
For convenience reasons I recommend to use aliases. Instead of entering the bluetooth mac address each time you want to run the script, you can call the script by using meaningful names.

The script tries to read a file called `.known_sem6` which must be located in your home folder. It is a text file with three columns:

1. MAC address
2. PIN
3. Meaningful name

My `.known_sem6` looks as follows:
```
$ cat ~/.known_sem6
FC:69:47:06:CB:C6 0000 fridge
```

This enables you to call the script like this
```
$ ./sem-6000.exp fridge --sync
```

instead of 
```
$ ./sem-6000.exp FC:69:47:06:CB:C6 0000 --sync
```

**Note**: 
You don't even have to write the whole alias. This works as well:
```
$ ./sem-6000.exp f --sync
```

## Getting help

In order to get an overview of the full feature set enter the following:
```
$ ./sem-6000.exp fr --help
Usage: <mac/alias> <pin> --<command1> <parameters...> --<command2>
                                   <mac>: bluetooth mac address of smart energy meter
                                   <alias>: you can use alias instead of mac address, see ~/.known_sem6
                                   <pin>: pin of smart energy meter if not stored in alias file
                                   <command>: For command and parameters

Basic commands:

 --on                               - turn on smart energy meter
 --off                              - turn off smart energy meter
 --toggle                           - toggle smart energy meter
 --standby <watts>                  - turn off device if consumption is less than given watts
                                      watts - low-water-mark, max. 3680, e.g. 2.6 for 2.6W
Scheduler commands:

 --scheduler <on|off> <hh:mm|+mm> [<smtwtfs>] [<YYYY-MM-DD>]
                                      on|off    - action of new scheduler
                                      hh:mm|+mm - start time or minutes from now
                                      smtwtfs   - (optional) weekdays, use capital letters to set, e.g. sMTWTFs
                                                  use the word "sameday" for same weekdays like today
                                                  if weekdays are missing then scheduler runs only once
                                      YYYY-MM-DD - (optional) Date from when it should run

 --scheduler <n> <set|unset|reset>  - activate, deactivate or reset given scheduler

 --scheduler reset                  - resets all schedulers, i.e. 1 - 12

 --scheduler                        - query status of all schedulers

Countdown commands:

 --countdown <on|off> <YYYY-MM-DD hh:mm:ss|hh:mm|+mm>
                                    - set countdown action and runtime
                                      on|off - action of countdown
                                      YYYY-MM-DD hh:mm:ss - given ETA
                                      hh:mm  - given ETA within next 24h
                                      +mm    - given runtime in minutes

 --countdown <reset>                - reset countdown

 --countdown                        - query status of countdown

Measurement commands:

 --status                           - get status incl. voltage, ampere, watts, power factor and frequency
 --measure header                   - print header line for measurements
 --measure [<s>]                    - take measurements, optional duration in seconds (use 0 for single), otherwise forever

 --data <day|month|year>            - request measured power consumption from enery meter
 --data reset                       - reset measured power consumption
 --data header                      - print header line for measurements or data

Device commands:

 --device                           - read device meta information, i.e. name and serial no.
 --sync                             - synchronize time
 --name <name>                      - give smart meter a new name, max. 18 characters
 --pin <1234|reset>                 - change PIN or reset to default PIN, i.e. 0000

Device settings:

 --settings                         - request settings from device, i.e. overload, led, price
 --led <on|off>                     - turn led ring on / off
 --overload <watts>
                                    - set overload with high-water-mark and actions
                                      watts - high-water-mark, max. 3680, e.g. 3680 for 3680W

 --price <normal price> [<reduced price> <hh:mm> <hh:mm>]
                                    - set price and optionally a reduced price with start and end time
 --reset                            - factory reset

Other commands:

 --print                            - print gathered information
 --json                             - print some gathered information in JSON format 
 --dump                             - request all information from device
 --sleep <n>                        - pause processing for n seconds
 --verbose                          - print information about processing
 --debug                            - print actions in gatttool
 --help [<command>]                 - print general help or help for specific command
```

You get specific help for a command if you ask for it explicitly:
```
$ $ ./sem-6000.exp --help toggle
Usage: <mac/alias> <pin> --<command1> <parameters...> --<command2>
                                   <mac>: bluetooth mac address of smart energy meter
                                   <alias>: you can use alias instead of mac address, see ~/.known_sem6
                                   <pin>: pin of smart energy meter if not stored in alias file
                                   <command>: For command and parameters

 --toggle                           - toggle smart energy meter
```


## PIN

The smart meter is protected by a 4 digit pin. The default pin is 0000. 

You can change the pin by using the pin command:
```
./sem-6000.exp FC:69:47:06:CB:C6 0000 --pin 1234
```

or if you make use of the _.known_sem6_ file
```
./sem-6000.exp f --pin 0000
```

**Note** Don't forget to change PIN in _.known_sem6_ file since this has to be done manually!

if you have forgotten your PIN you can reset it by doing this:

```
./sem-6000.exp FC:69:47:06:CB:C6 2342 --pin reset
```

This resets the pin to factory default, i.e. 0000

**Note** You can use any pin after the bluetooth mac address!


## Basic commands

### Turn switch on and off

You can turn on the socket as follows:
```
$ ./sem-6000.exp fridge --on
```

Note that there isn't any feedback. 

You can turn the device off by entering this:
```
$ ./sem-6000.exp fridge --off
```

If you want to toggle the switch you use the _toggle_ command:
```
$ ./sem-6000.exp fridge --toggle
```

### Queueing commands / sleep command

Since it takes some time to establish the bluetooth connection each time you start the script, I have introduced command queuing. Each command starts with a dash. In this example I queue 7 commands. The _sleep_ command pauses processing before the next command starts. 

```
$ ./sem-6000.exp fridge --on --sleep 1 --toggle --sleep 1 --toggle --sleep 1 --off
```

### Print gathered information

In most cases the script won't print anything. If you want to print some output, e.g. information that has been gathered by previous commands, you must tell the script to do so explicitly. 

```
$ ./sem-6000.exp fridge --status --print
        Status:
          Power:             on
          Voltage:           236 VAC
          Ampere:            0.012 A
          Watts:             0.056 W
          Frequency:         50 Hz
          Power factor:      0.02
          Total consumption: 0.0 kWh
```

In this example we have already made use of the status command.

### See power state of the socket

If you want to see if the socket is turned on and what the current power consumption is, you must ask for status first and print it afterwards:

```
$ ./sem-6000.exp fridge --status --print
        Status:
          Power:             on
          Voltage:           236 VAC
          Ampere:            0.012 A
          Watts:             0.056 W
          Frequency:         50 Hz
          Power factor:      0.02
          Total consumption: 0.0 kWh
```

## Schedulers

The socket has 12 schedulers that can be programmed once or per weekday. 

First let's take a look at the current state of schedulers:
```
$ ./sem-6000.exp fridge --scheduler --print
        Schedulers:          0
```

_Note, that I have queued two commands again, i.e. "-scheduler" and "-print". The first command gathers the information but doesn't output anything. The second command prints the gathered information._

There are no schedulers set yet.

Let's set the first scheduler for weekdays from Monday to Friday. The scheduler should turn my device on at 7:00 a.m. 

```
$ ./sem-6000.exp fridge --scheduler on 07:00 _MTWTF_
```

Now, I want to add a scheduler that is going to run once at a specific date and turn the device off
```
$ ./sem-6000.exp fridge --scheduler off 21:30 2019-09-03
```

Let's take a look at the settings of all schedulers:

```
$ ./sem-6000.exp fridge --scheduler --print
        Schedulers:          2

        Scheduler 1:
          Slot:              11
          Active:            yes
          Action:            turn off
          Date:              2019-09-03
          Time:              21:30
          Weekdays:          _______

        Scheduler 2:
          Slot:              12
          Active:            yes
          Action:            turn on
          Date:              2019-07-20
          Time:              07:00
          Weekdays:          _MTWTF_
```

In order to reset a specific scheduler or all schedulers run:

``` 
$ ./sem-6000.exp fridge --scheduler 1 reset
$ ./sem-6000.exp fridge --scheduler reset
```

### Countdown

The socket has a timer. You can set it with an ease like this:
```
$ ./sem-6000.exp fridge --countdown off +10
```

This activates a countdown timer which runs for 10 minutes and then turns the socket off. You can also specify a _date of arrival (ETA)_ like this:

```
$ ./sem-6000.exp fridge --countdown off 2019-08-30 07:45:30
```

Let's ask for information about the countdown that we have started before:
```
$ ./sem-6000.exp fridge --countdown --print
        Countdown:            on
          Action:             off
          Started at:         2019-07-20 13:47:19
          ETA:                2019-08-30 07:45:30
          Runtime:            40 days, 17:58:11
          Remaining:          40 days, 17:57:49
```

Enter the following in order to stop the running countdown:
```
$ ./sem-6000.exp fridge --countdown reset
```

## Power commands

The smart energy meter monitors power consumption continuously. It can automatically power off in case that power consumption exceeds a certain limit.

## Measurements

### Snapshot

If you want to take and print a single measurement, just call the status command:

```
$ ./sem-6000.exp fridge --status --print
        Status:
          Power:             on
          Voltage:           236 VAC
          Ampere:            0.012 A
          Watts:             0.013 W
          Frequency:         50 Hz
          Power factor:      0.00
          Total consumption: 0.0 kWh
```

### Realtime monitoring

The _measure_ command captures power data. This monitors the power consumption for 5 seconds:
```
$ ./sem-6000.exp fridge --measure header --measure 5
Timestamp       Power   Volt (V)        Ampere (A)      Watt (W)        Frequency (Hz)  Power factor
2019-07-20 15:56:27     1       236     0.012   0.045   50      0.02
2019-07-20 15:56:29     1       236     0.012   0.045   50      0.02
2019-07-20 15:56:29     1       236     0.012   0.0     50      0.00
2019-07-20 15:56:30     1       236     0.012   0.041   50      0.01
2019-07-20 15:56:31     1       236     0.012   0.041   50      0.01
2019-07-20 15:56:31     1       236     0.012   0.0     50      0.00
```

Note that the *measure* command directly prints a csv record. If you have left out the period, here "5" for 5 seconds, it runs forever. You can stop it by pressing CTRL-C

## Request recorded data

### Recorded data

The smart energy meter records power consumption. Data is recorded  in three scopes:
a. Hourly for the last 24 hours
b. Daily for the last 30 days
c. Monthly for the last 12 month

In order to request recorded data, use the _data_ command. 

The following command requests recorded data for last 24 hours and prints it with header line.
```
$ ./sem-6000.exp fridge --data header --data day --print
Timestamp       Watt (Wh)
2019-07-19 15:00        8
2019-07-19 16:00        11
...
2019-07-20 12:00        17
2019-07-20 13:00        19
2019-07-20 14:00        13
```

### Reset recorded data

If you want to reset all recorded data enter the following:
```
$ ./sem-6000.exp fridge --data reset
```

## Settings

## Synchronize time

If you just want to synchronize the time from your PC with the smart meter call:

```
$ ./sem-6000.exp fridge --sync
```

### LED ring
Normally the LED ring indicates that the switch is turned on. You can turn off the LED ring so that it is always off even if the switch is turned on. 

```
$ ./sem-6000.exp fridge --led off
```

### Overload limit

You can configure that the smart energy meter turn off in case that it exceeds a limit in terms of power consumption. In this example the socket turns off immediately in case that power consumption gets higher that 1000 Watts:

```
$ ./sem-6000.exp fridge --overload 1000
```

The default value is 3680W
```
$ ./sem-6000.exp fridge --overload 3680
```

### Prices
The switch can store two different prices, i.e. the normal price and a reduced price. Actually the switch doesn't seem to calculate internally, so that this setting makes only sense if you use the official app.

It goes like this:
```
$ ./sem-6000.exp fridge --price 0.32 0.20 23:00 07:00
```

### Request settings

Run the settings command in order to request current settings:
```
$ ./sem-6000.exp fridge --settings --print
        LED ring:            off
        Overload limit:      3680 W

        Price:               0.32

        Reduced mode:        on
        Reduced price:       0.20
        Reduced start:       23:00
        Reduced end:         07:00
```

## More commands
### Device information

In order to get general device information, you can request it by using the _device_ command:
```
$ ./sem-6000.exp fridge --device --print
        Mac:                 FC:69:47:06:CB:C6
        Device PIN:          0000
        Name:                Voltcraft
        Serial:              ML01D10012000000
        Alias:               fridge
```

### Set name
You can set a name for the device
```
```

### Verbose

If you want to get some information what's going on while the script is running, add the verbose command. 

```
$ ./sem-6000.exp fridge --verbose --on --status
INFO:   Try to connect to FC:69:47:06:CB:C6
INFO:   Connected to FC:69:47:06:CB:C6
INFO:   Auth SEM
INFO:   >>>     char-write-req 2b 0f0c170000000000000000000018ffff
INFO:   OK
INFO:   <<<     Notification handle = 0x2b value: 0f 06 17 00 00 00 00 18 ff ff
INFO:   Response completed in terms of announced length and end sequence
INFO:   SEM authorized successfully with PIN
INFO:   Switch SEM
INFO:   >>>     char-write-req 2b 0f06030001000005ffff
INFO:   OK
INFO:   <<<     Notification handle = 0x2b value: 0f 04 03 00 00 04 ff ff
INFO:   Response completed in terms of announced length and end sequence
INFO:   SEM successfully switched
INFO:   Request measurement
INFO:   >>>     char-write-req 2b 0f050400000005ffff
INFO:   OK
INFO:   <<<     Notification handle = 0x2b value: 0f 11 04 00 01 00 bd a1 eb 00 e1 32 00 00 00 00 00 00 62
INFO:   Response already completed in current notification in terms of announced length. No need to wait for another notification

INFO:   Measurement successfully requested
INFO:   Disconnect from FC:69:47:06:CB:C6
```

### Debug

The script uses _gatttool_ from the _bluez_ bluetooth stack. You can also see the commands sent to gatttool by using the _debug_ command:

```
$ ./sem-6000.exp fridge --debug --on --status
[                 ][LE]> connect FC:69:47:06:CB:C6
Attempting to connect to FC:69:47:06:CB:C6
Connection successful
[FC:69:47:06:CB:C6][LE]> char-write-req 2b 0f0c170000000000000000000018ffff
Characteristic value was written successfully
Notification handle = 0x002e value: 0f 06 17 00 00 00 00 18 ff ff
[FC:69:47:06:CB:C6][LE]> char-write-req 2b 0f06030001000005ffff
Characteristic value was written successfully
Notification handle = 0x002e value: 0f 04 03 00 00 04 ff ff
[FC:69:47:06:CB:C6][LE]> char-write-req 2b 0f050400000005ffff
Characteristic value was written successfully
Notification handle = 0x002e value: 0f 11 04 00 01 00 be 6f eb 00 e2 32 00 00 00 00 00 00 32
[FC:69:47:06:CB:C6][LE]>
```

### Dump

The _dump_ command tries to gather all information from the device.
```
$ ./sem-6000.exp fridge --dump --print
        Mac:                 FC:69:47:06:CB:C6
        Device PIN:          0000
        Name:                Fridge
        Serial:              ML01D10012000000
        Alias:               fridge

        Status:
          Power:             on
          Voltage:           235 VAC
          Ampere:            0.225 A
          Watts:             48.448 W
          Frequency:         50 Hz
          Power factor:      0.92
          Total consumption: 0.0 kWh

        LED ring:            off
        Overload limit:      3680 W

        Price:               0.32

        Reduced mode:        on
        Reduced price:       0.20
        Reduced start:       23:00
        Reduced end:         07:00

        Schedulers:          0

        Countdown:           off
        Randommode:          off
```
