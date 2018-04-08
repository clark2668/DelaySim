import objects_and_functions as tools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mpl

def main():

	#define speed of light
	c = 3e8

	ant1 = tools.receiver('ant1',15,0,0)
	ant2 = tools.receiver('ant2',-15,0,0)
	ant2_surveyerror = tools.receiver('ant2_surveyerror',-15,0.1,0)
	ant2_cableyerror = tools.receiver('ant2_cableerror',-15,0,0)


	phis = np.arange(0,360,1)
	delays = np.zeros(360)
	delays_surveyerror = np.zeros(360)
	delays_cableyerror = np.zeros(360)

	for phi in np.nditer(phis):

		pulser = tools.emitter('pulser',90,phi,30) #make a pulser
		time1 = tools.dist(ant1,pulser)/c/1e-9
		time2 = tools.dist(ant2,pulser)/c/1e-9
		time2_surveyerror=tools.dist(ant2_surveyerror,pulser)/c/1e-9
		delay = time1-time2
		delay_surveyerror=time1-time2_surveyerror
		delays[phi]=delay
		delays_surveyerror[phi]=delay_surveyerror
		delays_cableyerror[phi]=delay-2


	fig = plt.figure(figsize=(16,8)) #make a figure object
	ax1 = fig.add_subplot(1,2,1)
	ax2 = fig.add_subplot(1,2,2)
	
	ax1.plot(phis,delays,label='Delay Perfect')
	ax1.plot(phis,delays_surveyerror,label='Delay Survey Error')
	ax1.plot(phis,delays_cableyerror,label='Delay Cable Error')
	ax1.set_xlabel('Phi (deg)') #give it a title
	ax1.set_ylabel('Delay (ns)')
	ax1.legend()

	ax2.plot(phis,delays-delays_surveyerror,label='Perfect-Survey Error')
	ax2.plot(phis,delays-delays_cableyerror,label='Perfect-Cable Error')
	ax2.set_xlabel('Phi (deg)') #give it a title
	ax2.set_ylabel('Perfect - Error (ns)')
	ax2.legend()

	fig.savefig('figure.pdf',edgecolor='none',bbox_inches="tight") #save the figure


main()