from LUNA_FSM import FSM
# from LUNA_FSM import *
from State import *
from Transition import *



Char = type("Character", (object,), {})

class LunaSrv(Char):
    def __init__(self):
        self.FSM = FSM(self)

        ## States
        # self.FSM.AddState("poweroff", SystemStartup(self.FSM))
        #
        self.FSM.AddState("SystemStartup", SystemStartup(self.FSM))
        self.FSM.AddState("Stopped", Stopped(self.FSM))
        #
        self.FSM.AddState("InitializeReagents", InitializeReagent(self.FSM))
        # self.FSM.AddState("Ready", Ready(self.FSM))
        # self.FSM.AddState("Running", Running(self.FSM))
        # self.FSM.AddState("Stopped", Stopped(self.FSM))
        # self.FSM.AddState("ShuttingDown", ShuttingDown(self.FSM))
        # self.FSM.AddState("SystemStartup", SystemStartup(self.FSM))

        ## Transitions
        """
        AddTransition(transName, transition)
        Cleaner way to add objects to dictionaries
        :param transName:
        :param transition:
        :return:
        """
        self.FSM.AddTransition("toSystemStartup", Transition("SystemStartup"))
        self.FSM.AddTransition("toInitializedReagents", Transition("InitializeReagents"))
        self.FSM.AddTransition("toStopped", Transition("Stopped"))

        ## Initalize State
        self.FSM.SetState("SystemStartup")

    def Execute(self):
        """
        Executes the finite state machine
        :return:
        """
        self.FSM.Execute()