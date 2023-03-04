import random
import numpy as np

import aisim_task as t
import aisim_comm as c
import aisim_model_param as p
import aisim_model_metrics as m

# 乱数シードを設定(不要ならコメント)
random.seed(1)

class AISimModel:

  ##### シミュレーションパラメータ #####
  ITERATION = 100

  def __init__(self, metrics):
    self.metrics = metrics
    self.task1 = t.AISimTask(p.TASK_AVG_1, p.TASK_VAR_1, False, False)
    self.task2 = t.AISimTask(p.TASK_AVG_2, p.TASK_VAR_2, False, True)
    self.task3 = t.AISimTask(p.TASK_AVG_3, p.TASK_VAR_3, False, False)
    self.task4 = t.AISimTask(p.TASK_AVG_4, p.TASK_VAR_4, False, True)
    self.task5 = t.AISimTask(p.TASK_AVG_5, p.TASK_VAR_5, False, True)
    self.task6 = t.AISimTask(p.TASK_AVG_6, p.TASK_VAR_6, False, True)
    self.task7 = t.AISimTask(p.TASK_AVG_7, p.TASK_VAR_7, True, True)
    self.task8 = t.AISimTask(p.TASK_AVG_8, p.TASK_VAR_8, False, True)
    self.task9 = t.AISimTask(p.TASK_AVG_9, p.TASK_VAR_9, False, False)

    self.comm12 = c.AISimComm(p.COMM_AVG_1_2, p.COMM_VAR_1_2)
    self.comm23 = c.AISimComm(p.COMM_AVG_2_3, p.COMM_VAR_2_3)
    self.comm34 = c.AISimComm(p.COMM_AVG_3_4, p.COMM_VAR_3_4)
    self.comm45 = c.AISimComm(p.COMM_AVG_4_5, p.COMM_VAR_4_5)
    self.comm56 = c.AISimComm(p.COMM_AVG_5_6, p.COMM_VAR_5_6)
    self.comm67 = c.AISimComm(p.COMM_AVG_6_7, p.COMM_VAR_6_7)
    self.comm78 = c.AISimComm(p.COMM_AVG_7_8, p.COMM_VAR_7_8)
    self.comm89 = c.AISimComm(p.COMM_AVG_8_9, p.COMM_VAR_8_9)
    self.comm58 = c.AISimComm(p.COMM_AVG_5_6, p.COMM_VAR_5_6) # Same as comm56

  def simulate(self, task_location):

    self.update_location(task_location)

    for i in range(self.ITERATION):
      time = 0
      cloud_time = 0
      data = 0
      out_data = 0
      self.metrics.cloud_access_num = 0

      task_time = [0,0,0,0,0,0,0,0,0]
      comm_time = 0

      t = self.task1.get_time()
      time += t
      task_time[0] += t
      if self.task1.location == p.CLOUD:
        cloud_time += t
        self.metrics.cloud_access_num += 1
      
      t = self.comm12.get_time()
      time += t
      comm_time += t
      data += self.comm12.get_data_size()
      out_data += self.comm12.get_cloud_out_data_size()

      t = self.task2.get_time()
      time += t
      task_time[1] += t
      if self.task2.location == p.CLOUD:
        cloud_time += t
        if(self.task1.location != p.CLOUD): self.metrics.cloud_access_num += 1

      t = self.comm23.get_time()
      time += t
      comm_time += t
      data += self.comm23.get_data_size()
      out_data += self.comm23.get_cloud_out_data_size()

      t = self.task3.get_time()
      time += t
      task_time[2] += t
      if self.task3.location == p.CLOUD:
        cloud_time += t
        if(self.task2.location != p.CLOUD): self.metrics.cloud_access_num += 1

      t = self.comm34.get_time()
      time += t
      comm_time += t
      data += self.comm34.get_data_size()
      out_data += self.comm34.get_cloud_out_data_size()

      t = self.task4.get_time()
      time += t
      task_time[3] += t
      if self.task4.location == p.CLOUD:
        cloud_time += t
        if(self.task3.location != p.CLOUD): self.metrics.cloud_access_num += 1

      t = self.comm45.get_time()
      time += t
      comm_time += t
      data += self.comm45.get_data_size()
      out_data += self.comm45.get_cloud_out_data_size()

      t = self.task5.get_time()
      time += t
      task_time[4] += t
      if self.task5.location == p.CLOUD:
        cloud_time += t
        if(self.task4.location != p.CLOUD): self.metrics.cloud_access_num += 1

      t = self.comm56.get_time()
      time += t
      comm_time += t
      data += self.comm56.get_data_size()
      out_data += self.comm56.get_cloud_out_data_size()

      t = self.task6.get_time()
      time += t
      task_time[5] += t
      if self.task6.location == p.CLOUD:
        cloud_time += t
        if(self.task5.location != p.CLOUD): self.metrics.cloud_access_num += 1

      t = self.comm67.get_time()
      time += t
      comm_time += t
      data += self.comm67.get_data_size()
      out_data += self.comm67.get_cloud_out_data_size()

      t = self.task7.get_time()
      time += t
      task_time[6] += t
      if self.task7.location == p.CLOUD:
        cloud_time += t
        if(self.task6.location != p.CLOUD): self.metrics.cloud_access_num += 1

      t = self.comm58.get_time()
      time += t
      comm_time += t
      data += self.comm58.get_data_size()
      out_data += self.comm58.get_cloud_out_data_size()
      t = self.comm78.get_time()
      time += t
      comm_time += t
      data += self.comm78.get_data_size()
      out_data += self.comm78.get_cloud_out_data_size()

      t = self.task8.get_time()
      time += t
      task_time[7] += t
      if self.task8.location == p.CLOUD:
        cloud_time += t
        if(self.task7.location != p.CLOUD): self.metrics.cloud_access_num += 1

      t = self.comm89.get_time()
      time += t
      comm_time += t
      data += self.comm89.get_data_size()
      out_data += self.comm89.get_cloud_out_data_size()

      t = self.task9.get_time()
      time += t
      task_time[8] += t
      if self.task9 == p.CLOUD:
        cloud_time += t
        if(self.task8.location != p.CLOUD): self.metrics.cloud_access_num += 1

      self.metrics.add_record(time, data, out_data, cloud_time, comm_time, task_time)
      # print("[Iteration " + str(i) + "] time=" + str(time) + "s, data=" + str(data))

  def update_location(self, task_location):
    self.task1.location = task_location[0]
    self.task2.location = task_location[1]
    self.task3.location = task_location[2]
    self.task4.location = task_location[3]
    self.task5.location = task_location[4]
    self.task6.location = task_location[5]
    self.task7.location = task_location[6]
    self.task8.location = task_location[7]
    self.task9.location = task_location[8]

    self.comm12.location_from = task_location[0]
    self.comm23.location_from = task_location[1]
    self.comm34.location_from = task_location[2]
    self.comm45.location_from = task_location[3]
    self.comm56.location_from = task_location[4]
    self.comm67.location_from = task_location[5]
    self.comm78.location_from = task_location[6]
    self.comm89.location_from = task_location[7]
    self.comm58.location_from = task_location[4]

    self.comm12.location_to = task_location[1]
    self.comm23.location_to = task_location[2]
    self.comm34.location_to = task_location[3]
    self.comm45.location_to = task_location[4]
    self.comm56.location_to = task_location[5]
    self.comm67.location_to = task_location[6]
    self.comm78.location_to = task_location[7]
    self.comm89.location_to = task_location[8]
    self.comm58.location_to = task_location[7]

if __name__ == '__main__':
  task_location = [p.EDGE, p.CLOUD, p.CLOUD, p.CLOUD, p.CLOUD, p.CLOUD, p.CLOUD, p.CLOUD, p.EDGE]
  metrics = m.AISimModelMetrics(len(task_location))
  model = AISimModel(metrics)

  print(str(task_location))
  model.simulate(task_location)
