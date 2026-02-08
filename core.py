import turtle as t
import random
import os

os.chdir("assets")
t.setup(900, 600)
t.hideturtle()
flashlight = 0
enemy1active = 0
enemy1delay = 1000
enemy1attack = 0
globalattack = 0
underblanket = 0
e1apatience = 100
flashlightpressed = 0
gameon = 1
t.bgpic("l0d0.gif")
enemy2delay = 3000
enemy2attack = 0
e2patience = 200

underbedb = 0

jim = 0
if(jim==1):exec('while(True):\n    print("jim")')
t.penup()
t.tracer(0, 0)
def flash():
    global flashlight, flashlightpressed
    t.clear()
    if 1==1:

        if flashlight == 1:
            flashlight = 0

        elif flashlight == 0:
            flashlight = 1


            
        flashlightpressed = 0
    t.goto(-100, -100)
    #t.write(f"flashlight = {flashlight}")

def enemy1():
    #george
    global enemy1active, enemy1delay, enemy1attack, globalattack
    if enemy1delay > 0:
        enemy1delay -= 1
    if enemy1delay <= 0:
        
        if enemy2attack != 1:
            enemy1attack = 1
            globalattack = 1

def bgcalc():
    if underbedb != 1:
        if enemy1attack == 1:
            if flashlight == 1:
                t.bgpic("l1d1.gif")
            elif flashlight == 0:
                t.bgpic("l0d1.gif")
        elif enemy1attack != 1:
            if flashlight == 1:
                t.bgpic("l1d0.gif")
            elif flashlight == 0:
                t.bgpic("l0d0.gif")
    elif underbedb == 1:
        if enemy2attack == 1:
            if flashlight == 1:
                t.bgpic("b1a1.gif")
            elif flashlight == 0:
                t.bgpic("b0a1.gif")
        elif enemy1attack != 1:
            if flashlight == 1:
                t.bgpic("b1.gif")
            elif flashlight == 0:
                t.bgpic("b0.gif")


def e1reset():
    global enemy1attack, enemy1active, enemy1delay, e1apatience, globalattack
    enemy1delay = random.randint(300, 600)
    enemy1attack = 0
    globalattack = 0
    e1apatience = 100
def e1a():
    global e1apatience, enemy1attack, globalattack
    if enemy1attack == 1:
        print("warning")
        if underbedb == 0:
            t.goto(0, 0)

            #t.write("enemy 1 attacking!")
        e1apatience -= 1
        if e1apatience == 0:
            if flashlight == 1:
                e1reset()
                t.clear()
            elif flashlight == 0:
                gameover()
def gameover():
    global gameon
    gameon = 0
    t.clear()
    t.goto(0, 0)
    t.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
    t.update()
    t.ontimer(quit, 2000)




def flashswitch():
    global flashlightpressed
    if flashlightpressed == 0:
        flashlightpressed = 1

def underbed():
    if underbedb == 1:
        t.goto(100, 100)
        #t.write("under bed")
    

def gounder():
    global underbedb
    if underbedb == 1:
        underbedb = 0
    elif underbedb == 0:
        underbedb =1 
    t.clear()
#second guy bob himself :O


def enemy2():
    global enemy2delay, enemy2attack, e2patience
    enemy2delay -= 1
    if enemy2delay == 0:
        enemy2attack = 1

def e2reset():
    global enemy2delay, enemy2attack, e2patience
    enemy2delay = random.randint(2500, 3500)
    enemy2attack = 0
    e2patience = 200
def e2a():
    global enemy2delay, enemy2attack, e2patience
    if enemy2attack == 1:
        print("warning")
        if underbedb == 1:
            t.goto(0, 0)
            
            #t.write("enemy 2 is attacking you")
        e2patience -=1
        if e2patience == 0:
            if flashlight == 1:
                t.clear()
                e2reset()
            else:gameover()





t.onkey(flash, "space")
t.onkey(gounder, "s")
t.listen()
def mainloop():
    if gameon == 1:
        underbed()
        enemy1()
        e1a()

        enemy2()
        e2a()
        bgcalc()
        t.update()
        t.ontimer(mainloop, 30)
    if gameon != 1:
        quit()
        return



mainloop()
t.mainloop()