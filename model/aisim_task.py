import random
import aisim_model_param as p

class AISimTask:

    idx = 0
    time_avg = 0
    time_var = 0
    is_multithread = False
    adjustment = True

    location = p.EDGE

    def __init__(self, idx, time_avg, time_var, is_multithread, adjustment):
        self.idx = idx
        self.time_avg = time_avg
        self.time_var = time_var
        self.is_multithread = is_multithread
        self.adjustment = adjustment

    def get_time(self):
        t = random.normalvariate(self.time_avg, self.time_var)
        if self.adjustment:
            my_cpu_benchmark = p.MY_CPU_BENCHMARK if not self.is_multithread else p.MY_CPU_BENCHMARK * p.MY_CPU_CORES
            if self.location == p.EDGE:
                edge_cpu_benchmark = p.EDGE_CPU_BENCHMARK if not self.is_multithread else p.EDGE_CPU_BENCHMARK * p.EDGE_CPU_CORES
                t = t * (my_cpu_benchmark / edge_cpu_benchmark)
            elif self.location == p.CLOUD:
                cloud_cpu_benchmark = p.CLOUD_CPU_BENCHMARK if not self.is_multithread else p.CLOUD_CPU_BENCHMARK * p.CLOUD_CPU_CORES
                t = t * (my_cpu_benchmark / cloud_cpu_benchmark)
        return t
