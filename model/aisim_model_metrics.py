import pandas as pd

class AISimModelMetrics:

    def __init__(self, task_num):
        # 収集するメトリクスのリスト
        self.metrics_list = ["total_time", "total_data", "out_data", "cloud_time", "comm_time"]
        self.metrics_list = self.metrics_list + list(map(lambda i: "Task" + str(i), range(1, task_num+1)))
        self.df = pd.DataFrame(columns=self.metrics_list)
        self.task_num = task_num
        self.cloud_access_num = 0

    def add_record(self, total_time, total_data, out_data, cloud_time, comm_time, task_time):
        self.df.loc[len(self.df)] = [total_time, total_data, out_data, cloud_time, comm_time] + task_time

    def max(self, column_name):
        return self.df.max()[column_name]

    def min(self, column_name):
        return self.df.min()[column_name]

    def average(self, column_name):
        return self.df.mean()[column_name]

    def print_summary(self):
        print("time_avg=" + str(self.average("total_time")) + ", time_max=" + str(self.max("total_time")) + ", time_min=" + str(self.min("total_time")))
        print("data_avg=" + str(self.average("total_data")) + ", data_max=" + str(self.max("total_data")) + ", data_min=" + str(self.min("total_data")))
        print("task_time=" + str(list(map(lambda i: self.average("Task"+str(i)), range(1, self.task_num+1)))))
        print("comm_time_avg=" + str(self.average("comm_time")))
