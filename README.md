A program to check swap memory usage of all or some processes

Usage:

$ python check_swap.py

You'll probably need 'sudo'.

At prompt, enter a regex to specify what processes are you interested in.
Empty regex will match all.

e.g.:

$ sudo python check_swap.py
Enter regex for process name (optional):syslo
syslog-ng: 412 kB
syslog-ng: 452 kB
Total:  864 kB
