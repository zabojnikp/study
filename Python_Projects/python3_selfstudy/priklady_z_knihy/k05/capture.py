#!/usr/bin/env python3

import io
import sys

sys.stdout = io.StringIO()

print("Chybová zpráva", file=sys.stdout)
sys.stdout.write("Další chybová zpráva\n")
print("Do konzole se nic nevypsalo", file=sys.stdout)

error_strings = sys.stdout.getvalue()
sys.stdout = sys.__stdout__
print(error_strings)
