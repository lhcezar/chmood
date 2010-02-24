#!/usr/bin/python

try:
	import Skype4Py as skp
	skype = skp.Skype()

except ImportError, e:
	sys.exit(1)

import commands
import time

INTERVAL = 300

class ChangeMood:
	""" @todo build a new service to handle daemon
	"""
	def __init__(self):
		skype.Attach()

	def run(self):
		while True:
			time.sleep(INTERVAL)
			self.getQuote()
			self.setMood(self.fortune)

	""" @todo class to fortune a python's list 
	"""
	def getQuote(self):
		self.fortune = commands.getoutput('fortune  50% fortunes_big 50% startrek')
	def setMood(self,quote):
		skype.CurrentUserProfile.MoodText = quote

if __name__ == "__main__":
	c = ChangeMood()
	c.run()
