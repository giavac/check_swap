# check_swap
# Giacomo Vacca

import os
import re
import subprocess

def check_swap(pattern):
    total = 0

    # for each directory in /proc/...
    for dirname in os.listdir("/proc/"):
        # if it is numeric...
        if (dirname.isdigit()):
            # get the command name for that process
            process_name = subprocess.Popen(["ps", "-p", dirname, "--no-headers", "-o", "comm"], stdout=subprocess.PIPE).communicate()[0]

            if (re.match(pattern, str(process_name))):

                swap = subprocess.Popen(["grep", "Swap", "/proc/" + dirname + "/smaps"], stdout=subprocess.PIPE).communicate()[0]
                swap_list = swap.split()
                swap_list[:] = (value for value in swap_list if (value != "Swap:" and value != "kB"))
                partial = sum(int(value) for value in swap_list)
                print process_name.rstrip() + ": " + str(partial) + " kB"
                total += partial
            else:
                # print "Skipped: ", output
                continue

    print "Total: " + str(total) + " kB"


# ====== MAIN =============
pattern = raw_input('Enter regex for process name (optional):')
check_swap(pattern)
# ====== END ==============
