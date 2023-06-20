
"""Python implementation of code for CMS Energie management"""

import numpy as np
import time
## lets assume a total of 4 loads and 4 threshold values

PV_Gen = 600
Th = [200, 175, 50, 30]

# These are not actual output but just the rated load value
load_rated = [150, 70, 90, 90]

Switch = [0, 0, 0, 0] # the state of each switch, can be imported via Modbus

waiting_time = 3

# Initially no new outputs are turned ON and there is some default consumption

#reading from Janitaza
Jan0 = 300 # this is a modbus input

Excess = 300 # Excess is calculated using Jan0 and another Modbus register - it may or may not be equal to Janitza

#condition
# user defined stabilization time for every output
stabilization_time = 2



print("available excess:", Excess)
for i in Th:
    if Excess > i and Switch[Th.index(i)] == 0:
        # checking the status of the corresponding switch and if it's OFF, turning it ON
        print("switch Load", Th.index(i), "On and waiting for output to stabilize")
        Switch[Th.index(i)] = 1
        Output = load_rated[Th.index(i)] # + np.random.randint(0, 20) # simulating value of Output and  resultant Excess
        Excess = Excess - Output
        time.sleep(0)
        print("Excess available after stabilized output", Excess)
        if Excess <=0:
            print("No excess energy left, waiting for user decision to overturn Switch ", Th.index(i),"(y/n):")
            decision = str(input())
            if decision == "y":
                Switch[Th.index(i)] = 0
                print("Switch ", Th.index(i), "turned OFF")
                Excess = Excess + Output
                print("Excess available after decision:", Excess)
            else:
                print("Switch ", Th.index(i), "left ON, taking power from grid, status of remaining switches wont be checked")
                break
    else:
        print("Excess Energy less than threshold required for Switch", Th.index(i)," to be  turned ON")

print("Switch final status:", Switch)












