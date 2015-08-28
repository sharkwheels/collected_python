# still to do:
# make into texting program. Images are MMS based...or, maybe not.
# find way to open files in chrome instead of preview

import os, time, random, sys, webbrowser
from random import choice

cat_sayings = [
"I can haz?",
"I pooped in your shoe.",
"I ate the fish.",
"I want out.",
"Food? What...? Food?",
"When are you coming home? I need to hide the body?",
"Lulz, I am sleeping in your laundry.",
"I didn't do it. Nope.",
"I brought you a present! Its a birdie!",
]



line = "------------------------------"
print line
print "Texts from your cat"
print "Type 'exit' to quit."
print line


class Cat(object):

	def cat_pics(self,path):
		files = os.listdir(path)
		index = random.randrange(0,len(files))
		# returning files as a list
		return files[index]
	

	# see, this was all I needed for a timer. Stupid stack-overflow
	def cat_auto(self,wait,saying):
			
		boom = wait
			
		while boom > 0:
				
			time.sleep(1)
			print(boom)
			boom -=1
			
			if boom == 0:
				print saying

	

while True:

	kitty = Cat()
	sayings = choice(cat_sayings)

	kitty.cat_auto(5,sayings)

	img_path = "docs/cats"

	x = raw_input("> ")
	
	if x != "exit":

		images = kitty.cat_pics("docs/cats/")
		beep =  "file:///Users/nadinelessio/Documents/python_projects/code30projects/proj_06/docs/cats/%s" % images
		print beep
		webbrowser.open(beep)

	

	if x == "exit":
		print "OK BYEEEE!"
		break

