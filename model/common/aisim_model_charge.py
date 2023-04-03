import aisim_model_charge_const as cc

class AISimModelCharge:

    def __init__(self):
        self.cloud_service = "EC2"
        self.ec2_instance_num = 1
        self.request_num = 0
        self.time_avg = 0
        self.data_avg = 0
        self.out_data_avg = 0
        self.cloud_access_num = 0
        self.cloud_time_avg = 0
        self.comm_time_avg = 0

    def calc_charge(self):
        charge = 0
        if self.cloud_service == "EC2":
            charged_out_data = max(self.request_num * self.out_data_avg - cc.OUT_DATA_COST_FREE_TIER, 0)
            charge += self.ec2_instance_num * cc.EC2_COST_PER_HOUR * 730
            charge += cc.EBS_STORAGE_SIZE * cc.EBS_COST_PER_GB * self.ec2_instance_num
            charge += cc.OUT_DATA_COST_PER_GB * (charged_out_data / 1000000000)
        elif self.cloud_service == "LAMBDA":
            exec_time_s = self.request_num * self.cloud_time_avg
            charged_request_num = max(self.request_num - cc.LAMBDA_REQ_FREE_TIER, 0)
            charged_exec_time_s = max(exec_time_s - cc.LAMBDA_GBS_FREE_TIER, 0)
            charged_out_data    = max(self.request_num * self.out_data_avg - cc.OUT_DATA_COST_FREE_TIER, 0)
            charge += self.cloud_access_num * cc.LAMBDA_MEM_SIZE * charged_exec_time_s * cc.LAMBDA_COST_PER_MEMS
            charge += self.cloud_access_num * charged_request_num * cc.LAMBDA_COST_PER_REQ
            charge += cc.OUT_DATA_COST_PER_GB * (charged_out_data / 1000000000)
        return charge

    def print_summary(self):
        print("charge=" + str(self.calc_charge()))