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
	print(line)
	finch.led(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	line.replace(" ", "")

	things = line.split(",")
	if things[0] == "T" : finch.buzzer_with_delay(int(float(things[2]))/1000, int(float(things[1])))
	if things[0] == "D" : sleep(int(float(things[1]))/1000)
	line=fp.readline()


fp.close()