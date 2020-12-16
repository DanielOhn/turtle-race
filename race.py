from turtle import *
import random
import time

colors = ['red', 'green', 'blue', 'purple', 'orange']
names = ['Roar', 'Brionne', 'Pocket', 'Catsby', 'Shib']

  
def drawRacer(color, num, name):
    # Drawing Racing Turtles

    racer = Turtle()
    racer.color(color)
    racer.shape('turtle')

    racer.penup()
    racer.goto(-160, 40 + 20 * num)
    racer.pendown()

    turtle = {'name': name, 'turtle': racer, 'finish': None}

    return turtle

def drawWinner(winner):
    draw = Turtle()
    draw.penup()

    draw.goto(0, -15)

    draw.write("The winner is {0}!".format(winner), font=("Arial", 12, "normal"))


def drawResults(draw, racer, pos):
    draw.goto(-100, -15 * (1 + pos))

    draw.write("{0} the {1} turtle finished in {2:.2f} seconds.".format(racer['name'], racer['turtle'].color()[0], racer['finish']), font=("Arial", 12, "normal"))


# Timer Function
# Reset Race
# Dict for Racers - CHECK
# Add Speed and Stability Properties
# Results Function - CHECK

def raceStart():
    racers = []
    race = True
    
    for pos in range(5):
        racer = drawRacer(colors[pos], pos, names[pos])
        racers.append(racer)
    
    start = time.time()

    timer = Turtle()
    timer.penup()
    timer.goto(-160, 0)

    draw = Turtle()
    draw.penup()

    count = 0

    while (race):
        for racer in racers:
            counter = time.time()
            timer.write("{0:.2f}".format(counter - start), font=("Arial", 10, "normal"))

            if (racer['turtle'].position()[0] <= 120):
                racer['turtle'].forward(random.randint(5, 10))
            elif (racer['turtle'].position()[0] >= 120 and racer['finish'] == None):
                racer['finish'] = counter - start
                drawResults(draw, racer, count)
                count += 1
                
            if (count == 5):
                race = False

            timer.undo()

    end = time.time()
    amount = end - start
    
    timer.write("{0:.2f}".format(amount), font=("Arial", 10, "normal"))

    resetTime = time.time()

    while (True):
        resetCounter = time.time()
        if (resetCounter - resetTime >= 10):
            for racer in racers:
                racer['turtle'].clear()
                racer['turtle'].hideturtle()

            timer.clear()
            draw.clear()
    
            return False
            
def createTrack():
    track = Turtle()
    track.speed(0)
    track.penup()
    track.goto(-140, 140)
    
    # Starting Numbers
    for i in range(11):
        track.write(i * 5)
        track.forward(25)

    track.right(90)
    track.forward(10)
    track.right(90)
    track.forward(20)

    # Creating the lines
    for line in range(6):
        for dash in range(11):
            track.pendown()
            track.forward(22)
            track.penup()
            track.forward(3)

        if (line % 2 == 0):
            track.right(-90)
            track.forward(20)
            track.right(-90)
        else:
            track.right(90)
            track.forward(20)
            track.right(90)

createTrack()
race = True

while(race):
    raceStart()



