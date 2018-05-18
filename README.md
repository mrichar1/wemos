Wemos D1 Mini
-------------

Some documentation, setup, tools and scripts for the Wemos D1 Mini.

See the wiki for the full docs.

Quick Setup
===========

```
cp udev/99-wemos.rules /etc/udev/rules.d
udevadm control --reload-rules
udevadm trigger

bin/wemos-venv-setup.sh
bin/rshell
```

Layout
======

`bin/` - commands to help set up and control a wemos d1 mini.
'python/` - misc samples and examples for common tasks.
'udev/` - udev rules for creating devices with friendly names and setting permissions.

