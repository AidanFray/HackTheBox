import os
import re

s = None
with open("loginText.txt", "r") as f:
    s = f.read()

s = s.replace(" ", "")
chars = re.findall(r".", s)

for index, value in enumerate(chars):
    chars[index] = f"Ook{value}"

output = " ".join(chars)
print(output)