import os
x = open("settings.eff", "r").read()
print(f"type [start] to launch {x}")
input("$>")
os.system("py core.py")