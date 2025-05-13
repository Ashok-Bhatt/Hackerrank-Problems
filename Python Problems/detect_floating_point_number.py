import re

for _ in range(int(input())):
    word = input()
    if (re.match(r"^[+-]?[0-9]*\.[0-9]+$", word)):
        print(True)
    else:
        print(False)
