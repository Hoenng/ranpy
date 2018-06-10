#!/usr/local/bin/python3

import os

directory = os.fsencode(directory_in_str)

for filename in os.listdir(directory):
    print(filename)
