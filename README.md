Delcom 807241 USB Led
======================

This is a Python Library with an commandline tool
to access the `Delcom 807241 USB Led`.

Requirements
----------------------

* Python 2.7.x
* Python `pyusb` library

Installation
----------------------

* Clone the Git Repository
* Run `sudo python setup.py install`

Usage
----------------------

If you want to use the commandline tool, you can print
some instructions with the command:

`delcom-usbled -h`

By default only the root user can access the USB device,
if you want to have user or group access to the
`Delcom 807241 USB Led` you can add a udev rule to
`/etc/udev/rules.d/40-delcom-usbled-807241.rules`:

    SUBSYSTEM=="usb", ATTRS{idVendor}=="0fc5", ATTRS{idProduct}=="1223", GROUP="plugdev", MODE="0666"
    
With dis rule all users in the `plugdev` group can access the USB Led.