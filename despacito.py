from finch import Finch
from time import sleep
import random

finch = Finch()

fp = open("mid.txt", "r")

line = fp.readline()
while line:
	line.strip()
	if line.startswith("#"):
		print("comment")
		line = fp.readline()
		continue

	left = random.uniform(-0.5, 0.5)
	right = random.uniform(-0.5, 0.5)
	print("L:" + str(left), "R:" + str(right))
	finch.wheels(left, right)

	red = random.randint(0, 255)
	green = random.randint(0, 255)
	blue = random.randint(0, 255)
	print(red, green, blue)
	finch.led(red, green, blue)


	line.replace(" ", "")

	things = line.split(",")
	if things[0] == "T" : finch.buzzer_with_delay(int(float(things[2]))/1000, int(float(things[1])))
	if things[0] == "D" : sleep(int(float(things[1]))/1000)

	print(line)
	line=fp.readline()


fp.close()