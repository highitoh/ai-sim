import pandas as pd

class AISimModelMetrics:

    def __init__(self, task_num):
        # 収集するメトリクスのリスト
        self.metrics_list = ["total_time", "total_data", "out_data", "cloud_time", "comm_time"]
        self.metrics_list = self.metrics_list + list(map(lambda i: "Task" + str(i), range(1, task_num+1)))
        self.df = pd.DataFrame(columns=self.metrics_list)

    def add_record(self, total_time, total_data, out_data, cloud_time, comm_time, task_time):
        self.df.loc[len(self.df)] = [total_time, total_data, out_data, cloud_time, comm_time] + task_time

    def average(self, column_name):
        return self.df.mean()[column_name]