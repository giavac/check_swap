import os
import re
import subprocess

pattern = raw_input('Enter regex for process name (optional):')

total = 0

# for each directory in /proc/...
for filename in os.listdir("/proc/"):
    # if it is numeric...
    if re.match("\d", filename):
        # get the command name for that process
        process_name = subprocess.Popen(["ps", "-p", filename, "--no-headers", "-o", "comm"], stdout=subprocess.PIPE).communicate()[0]

        #pattern = "^.*$"
        if (re.match(pattern, str(process_name))):
            # sudo grep Swap /proc/29164/smaps
            swap = subprocess.Popen(["grep", "Swap", "/proc/" + filename + "/smaps"], stdout=subprocess.PIPE).communicate()[0]
            swap_list = swap.split()
            swap_list[:] = (value for value in swap_list if (value != "Swap:" and value != "kB"))
            partial = sum(int(value) for value in swap_list)
            print process_name.rstrip() + ": " + str(partial) + " kB"
            total += partial
        else:
            # print "Skipped: ", output
            continue

print "Total: " + str(total) + " kB"
