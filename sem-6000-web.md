# Simple Webfrontend
_"Simplistic python/flask wrapper for the _sem-6000.exp_ command"_

This little webserver lets you control your known (`.known_sem6`) devices through a browser.

## Getting started
Install flask and yattag python modules.
```
sudo pip3 install flask yattag
```

## Check functionality
Start the service once.
```
$ python3 ./sem-6000-web.py
```
Access via _http://IP:5000_

## Register as Service
Register as SystemD service at bootup.
```
sudo systemctl enable --now "$(pwd)/sem-6000-web.service"
```

Check the status and logs.
```
systemctl status sem-6000-web
journalctl -f -u sem-6000-web
```
