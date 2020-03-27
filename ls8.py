#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

# CPU file and file we are running
if len(sys.argv) == 2:
    cpu = CPU()

    cpu.load(sys.argv[1])
    cpu.run()
else:
    print('Error: Need file name')
    sys.exit(1)
