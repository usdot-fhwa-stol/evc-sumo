import sys
import os
if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

# must be declare after getting SUMO_HOME env var
import traci
from contextlib import contextmanager

class SumoConnector:
    def __init__(self, port, order_num):
        self.port = port
        self.order_num = order_num
        self.traci = traci

    @contextmanager
    def traci_handler(self):
        self.traci.init(int(self.port))
        self.traci.setOrder(self.order_num)
        yield
        self.traci.close()

    def tick(self):
        self.traci.simulationStep()

    def set_traffic_light_status_to_SUMO(self, sumo_tl_id, tl_state_string):
        traci.trafficlight.setRedYellowGreenState(str(sumo_tl_id), tl_state_string)

    def get_detector_status_from_SUMO(self):
        ## TBD
        pass

    