from random import randint
from time import clock

import logging

##==================== Logging Configuration ==========================
FORMAT = '%(levelname)s:%(filename)s:%(funcName)s:%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

##==================== STATES ==========================

class State(object):
    def __init__(self, FSM):
        self.FSM = FSM
        self.timer = 0
        self.startTime = 0
    """
    Three functions instead of just one (execute for main and transition)
    Need Enter and Exit of each state.
    """

    def Enter(self):
        """

        :return:
        """
        self.timer = randint(0, 5)
        self.startTime = int(clock())

    def Execute(self):
        """

        :return:
        """
        pass

    def Exit(self):
        """

        :return:
        """
        pass

##==================== ACTUAL STATES ==========================
class SystemOff(State):
    def __init__(self, FSM):
        """
        Going to as a FSM to be passed into the state constructor so that we can make adjustments and grab data
        from it.

        :param FSM:
        """
        super(SystemOff, self).__init__(FSM)

    def Enter(self):
        logging.info("enter")


    def Execute(self):
        logging.info("System is Off")


    def Exit(self):
        logging.info("exit")



class SystemStartup(State):
    def __init__(self, FSM):
        """
        2.1 System Startup

        From:
        1) Systemoff (U) / turn_on_clicked()
        2) Stopped (U) / restart_clicked()
        To:
        1) Initialize Reagents (S) / system_Startup_finished()
        2) Stopped (S) / error()
        3) Shutting Down (S) / power_loss() or (U) / shutdown_clicked()
        """
        super(SystemStartup, self).__init__(FSM)

    def Enter(self):
        logging.info("SystemStartup enter")
        super(SystemStartup, self).Enter()

    def Execute(self):
        """
        Have a condition in order to check if we need to transition into another state.
        Randomly choose if the robot is going to to Vacuum or go to sleep.
        :return:
        """
        logging.info("System is in SystemStart State")
        if self.startTime + self.timer <= clock():
            rand_num = randint(0,1)
            if (rand_num) == 0:
                # system_startup_finished() / S
                self.FSM.ToTransition("toInitializedReagents")
            elif (rand_num == 1):
                # error() / S
                self.FSM.ToTransition("toStopped")
            # elif (rand_num == 2):
            #     # power_loss() / S
            #     pass
            # elif (rand_num == 3):
            #     # user_click_shutdown
            #     pass

    def Exit(self):
        logging.info("System Startup exit")


class InitializeReagent(State):
    """
    2.2 Initialize Reagent State

    From:
    1) System Startup (S) / system_startup_finalized()
    2) Running (S) / run_finished()
    To:
    1) Ready (S) / reagents_checked()
    2) Stopped (S) / error()
    3) Shutting Down (S) / power_loss() or (U) / shutdown_clicked()
    """
    def __init__(self, FSM):
        """
        Going to as a FSM to be passed into the state constructor so that we can make adjustments and grab data
        from it.

        :param FSM:
        """
        super(InitializeReagent, self).__init__(FSM)

    def Enter(self):
        logging.info("enter")

    def Execute(self):
        logging.info("System is Initialize Reagent")
        if self.startTime + self.timer <= clock():
            rand_num = randint(0,1)
            if (rand_num) == 0:
                # system_startup_finished() / S
                self.FSM.ToTransition("toSystemStartup")
            elif (rand_num == 1):
                # error() / S
                self.FSM.ToTransition("toStopped")

    def Exit(self):
        logging.info("exit")


class Ready(State):
    """
    2.3 Ready State

    From:
    1) Initialize Reagents (S) / reagents_checked()
    To:
    1) Running (U) / start_run_clicked()
    2) Stopped (S) / error() or (U) stop_run_clicked()
    3) Shutting Down (S) / power_loss() or (U) / shutdown_clicked()
    """

    def __init__(self, FSM):
        """
        Going to as a FSM to be passed into the state constructor so that we can make adjustments and grab data
        from it.

        :param FSM:
        """
        super(Ready, self).__init__(FSM)

    def enter(self):
        logging.info("enter")

    def execute(self):
        logging.info("System is Ready")

    def exit(self):
        logging.info("exit")

class Running(State):
    """
    2.4 Running

    From:
    1) Ready (S) / start_run()
    To:
    1) Initialize Reagents (S) / run_complete()
    2) Stopped (S) / error() or (U) stop_run_clicked()
    3) Shutting Down (S) / power_loss()                 (or (U) / shutdown_clicked())
    """

    def __init__(self, FSM):
        """
        Going to as a FSM to be passed into the state constructor so that we can make adjustments and grab data
        from it.

        :param FSM:
        """
        super(Running, self).__init__(FSM)

    def enter(self):
        logging.info("enter")

    def execute(self):
        logging.info("System is Ready")

    def exit(self):
        logging.info("exit")

class Stopped(State):
    """
    2.5 Stopped

    From:

    To:

    """

    def __init__(self, FSM):
        """
        Going to as a FSM to be passed into the state constructor so that we can make adjustments and grab data
        from it.

        :param FSM:
        """
        super(Stopped, self).__init__(FSM)

    def Enter(self):
        logging.info("Stopped State enter")
        super(Stopped, self).Enter()

    def Execute(self):
        """
        Have a condition in order to check if we need to transition into another state.
        Randomly choose if the robot is going to to Vacuum or go to sleep.
        :return:
        """
        logging.info("System is Stopped")
        if self.startTime + self.timer <= clock():
            rand_num = randint(0,1)
            if (rand_num) == 0:
                # system_startup_finished() / S
                self.FSM.ToTransition("toInitializedReagents")
            elif (rand_num == 1):
                # error() / S
                self.FSM.ToTransition("toSystemStartup")
            # elif (rand_num == 2):
            #     # power_loss() / S
            #     pass
            # elif (rand_num == 3):
            #     # user_click_shutdown
            #     pass

    def Exit(self):
        logging.info("Stopped exit")


class ShuttingDown(State):
    """
    2.6 Shutting Down

    From:

    To:

    """

    def __init__(self, FSM):
        """
        Going to as a FSM to be passed into the state constructor so that we can make adjustments and grab data
        from it.

        :param FSM:
        """
        super(ShuttingDown, self).__init__(FSM)

    def enter(self):
        logging.info("enter")

    def execute(self):
        logging.info("System is Shutting Down")

    def exit(self):
        logging.info("exit")

