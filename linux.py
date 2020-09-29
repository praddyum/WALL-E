#!/usr/bin/python3
import cgi

print("content-type:text/html")
print()

y= cgi.FieldStorage()

z=y.getvalue("x")
print("Command: {}" format(z))
print()print()
print("Output: ", end='')

import subprocess

if "time" in z:
    x=subprocess.getoutput(timedatectl)

elif "date" in z:
    x=subprocess.getoutput(date)

elif (("cal" in z) or ("calander" in z)):
    x=subprocess.getoutput(cal)



print(x)


