import turtle as t

x = open("settings.eff", "w").read()
t.title(f"{x}")
t.write(f"{x}\npress anything to start")
import os

def startup():
    os.startfile("core.py")
t.onkey(startup, "space")
t.listen()
t.mainloop()