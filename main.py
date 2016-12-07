from LUNA_FSM import *
from State import *
from Transition import *
from Character import LunaSrv

##==================== Main ==========================
if __name__=="__main__":
    l = LunaSrv() # Create an instance of the RobotMaid
    for i in range(10):
        startTime = clock()
        timeInterval = 1
        while(startTime+timeInterval > clock()): # MAKES SURE TO WAIT ONE SECOND so that it executes literally every second
            pass
        l.Execute()
