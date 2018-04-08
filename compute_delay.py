import objects_and_functions as tools
def main():

	#define speed of light
	c = 3e8

	ant1 = tools.receiver('ant1',1,0,0)
	ant2 = tools.receiver('ant2',-1,0,0)
	pulser = tools.emitter('pulser',90,90,10)

	ant1.PrintCoords()
	ant2.PrintCoords()
	pulser.PrintCoords()

	time1 = tools.dist(ant1,pulser)/3e8
	time2 = tools.dist(ant2,pulser)/3e8
	delay = time1 - time2

	print "Time 1",time1
	print "Time2 2",time2
	print "Delay ",delay

main()