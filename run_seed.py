import django
django.setup()

from app.seed import *

if __name__ == '__main__':
	runAbout()
	runSkills()
	runServices()
	runTesti()
	runCont()
	runFiltre()
	runPorto()