import aisim_model_param as p

class AISimModelCharge:

    def __init__(self):
        self.time_avg = 0
        self.data_avg = 0
        self.out_data_avg = 0
        self.cloud_access_num = 0
        self.cloud_time_avg = 0
        self.comm_time_avg = 0

    def calc_charge(self):
        charge = 0
        if p.CLOUD_SERVICE == "EC2":
            charged_out_data = max(p.REQUEST_NUM * self.out_data_avg - p.OUT_DATA_COST_FREE_TIER, 0)
            charge += p.EC2_INSTANCE_NUM * p.EC2_COST_PER_HOUR * 730
            charge += p.EBS_STORAGE_SIZE * p.EBS_COST_PER_GB * p.EC2_INSTANCE_NUM
            charge += p.OUT_DATA_COST_PER_GB * (charged_out_data / 1000000000)
        elif p.CLOUD_SERVICE == "LAMBDA":
            exec_time_s = p.REQUEST_NUM * self.cloud_time_avg
            charged_request_num = max(p.REQUEST_NUM - p.LAMBDA_REQ_FREE_TIER, 0)
            charged_exec_time_s = max(exec_time_s - p.LAMBDA_GBS_FREE_TIER, 0)
            charged_out_data    = max(p.REQUEST_NUM * self.out_data_avg - p.OUT_DATA_COST_FREE_TIER, 0)
            charge += self.cloud_access_num * p.LAMBDA_MEM_SIZE * charged_exec_time_s * p.LAMBDA_COST_PER_MEMS
            charge += self.cloud_access_num * charged_request_num * p.LAMBDA_COST_PER_REQ
            charge += p.OUT_DATA_COST_PER_GB * (charged_out_data / 1000000000)
        return charge

    def print_summary(self):
        print("charge=" + str(self.calc_charge()))