import random
import aisim_model_param as p

class AISimComm:

    location_from = p.EDGE
    location_to = p.EDGE
    time_avg = 0
    time_var = 0
    
    def __init__(self, time_avg, time_var):
        self.time_avg = time_avg
        self.time_var = time_var
        self.data_size = 0

    def get_data_size(self):
        # Just Return DataSize Calculated Before
        return self.data_size

    def get_cloud_out_data_size(self):
        # Just Return DataSize Calculated Before
        return self.get_data_size() if (self.location_from == p.CLOUD and self.location_to == p.EDGE) else 0

    def get_time(self):
        self.data_size = 0
        time = 0
        # Update DataSize and CommTime
        if (self.location_from == p.EDGE and self.location_to == p.CLOUD) or (self.location_from == p.CLOUD and self.location_to == p.EDGE):
            self.data_size = random.normalvariate(self.time_avg, self.time_var)
            time = random.normalvariate(self.data_size / p.CLOUD_EDGE_BPS, self.data_size / p.CLOUD_EDGE_BPS * p.LT_SIGMA_GAIN)        
        return time
