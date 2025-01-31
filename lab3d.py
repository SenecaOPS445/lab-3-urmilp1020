#!/usr/bin/env python3
'''Lab 3 Inv 2 - Get Free Disk Space'''
# Author ID: [seneca_id]

import subprocess

def free_space():
    # Run the df command to get free space in the root directory
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Return the free space, decoded in utf-8 and stripped of newline characters
    return result.stdout.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())

