import numpy as np

import aisim_task as t
import aisim_comm as c
import aisim_model_param as p
import aisim_model_metrics as m

class TrialResult:

  def __init__(self):
    self.time = 0
    self.cloud_time = 0
    self.data = 0
    self.out_data = 0
    self.comm_time = 0
    self.task_time = [0,0,0,0,0,0,0,0,0]

  def exec_task(self, task):
    t = task.get_time()
    self.time += t
    self.task_time[task.idx] += t
    if task.location == p.CLOUD:
      self.cloud_time += t
    
  def exec_comm(self, comm):
      t = comm.get_time()
      self.time += t
      self.comm_time += t
      self.data += comm.get_data_size()
      self.out_data += comm.get_cloud_out_data_size()

class AISimModel:

  ##### シミュレーションパラメータ #####
  ITERATION = 100

  def __init__(self, metrics, seed=None):    
    # Constitute Workflow Model
    self.metrics = metrics
    self.task1 = t.AISimTask(0, p.TASK_AVG_1, p.TASK_VAR_1, False, False)
    self.task2 = t.AISimTask(1, p.TASK_AVG_2, p.TASK_VAR_2, False, True)
    self.task3 = t.AISimTask(2, p.TASK_AVG_3, p.TASK_VAR_3, False, False)
    self.task4 = t.AISimTask(3, p.TASK_AVG_4, p.TASK_VAR_4, False, True)
    self.task5 = t.AISimTask(4, p.TASK_AVG_5, p.TASK_VAR_5, False, True)
    self.task6 = t.AISimTask(5, p.TASK_AVG_6, p.TASK_VAR_6, False, True)
    self.task7 = t.AISimTask(6, p.TASK_AVG_7, p.TASK_VAR_7, True, True)
    self.task8 = t.AISimTask(7, p.TASK_AVG_8, p.TASK_VAR_8, False, True)
    self.task9 = t.AISimTask(8, p.TASK_AVG_9, p.TASK_VAR_9, False, False)

    self.comm12 = c.AISimComm(p.COMM_AVG_1_2, p.COMM_VAR_1_2)
    self.comm23 = c.AISimComm(p.COMM_AVG_2_3, p.COMM_VAR_2_3)
    self.comm34 = c.AISimComm(p.COMM_AVG_3_4, p.COMM_VAR_3_4)
    self.comm45 = c.AISimComm(p.COMM_AVG_4_5, p.COMM_VAR_4_5)
    self.comm56 = c.AISimComm(p.COMM_AVG_5_6, p.COMM_VAR_5_6)
    self.comm67 = c.AISimComm(p.COMM_AVG_6_7, p.COMM_VAR_6_7)
    self.comm78 = c.AISimComm(p.COMM_AVG_7_8, p.COMM_VAR_7_8)
    self.comm89 = c.AISimComm(p.COMM_AVG_8_9, p.COMM_VAR_8_9)
    self.comm58 = c.AISimComm(p.COMM_AVG_5_6, p.COMM_VAR_5_6) # Same as comm56

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

  def simulate(self, task_location):

    self.update_location(task_location)

    for i in range(self.ITERATION):

      result = TrialResult()

      result.exec_task(self.task1)
      
      result.exec_comm(self.comm12)

      result.exec_task(self.task2)

      result.exec_comm(self.comm23)

      result.exec_task(self.task3)

      result.exec_comm(self.comm34)

      result.exec_task(self.task4)

      result.exec_comm(self.comm45)

      result.exec_task(self.task5)

      result.exec_comm(self.comm56)

      result.exec_task(self.task6)

      result.exec_comm(self.comm67)

      result.exec_task(self.task7)

      result.exec_comm(self.comm58)

      result.exec_comm(self.comm78)

      result.exec_task(self.task8)

      result.exec_comm(self.comm89)

      result.exec_task(self.task9)

      self.metrics.add_record(result.time, result.data, result.out_data, result.cloud_time, result.comm_time, result.task_time)
      # print("[Iteration " + str(i) + "] time=" + str(time) + "s, data=" + str(data))

  def calc_static_metrics(self):
    # Calculate Cloud Access Count
    self.metrics.cloud_access_num = 0
    if self.task1.location == p.CLOUD: self.metrics.cloud_access_num += 1
    if (self.task1.location != p.CLOUD and self.task2.location == p.CLOUD): self.metrics.cloud_access_num += 1
    if (self.task2.location != p.CLOUD and self.task3.location == p.CLOUD): self.metrics.cloud_access_num += 1
    if (self.task3.location != p.CLOUD and self.task4.location == p.CLOUD): self.metrics.cloud_access_num += 1
    if (self.task4.location != p.CLOUD and self.task5.location == p.CLOUD): self.metrics.cloud_access_num += 1
    if (self.task5.location != p.CLOUD and self.task6.location == p.CLOUD): self.metrics.cloud_access_num += 1
    if (self.task6.location != p.CLOUD and self.task7.location == p.CLOUD): self.metrics.cloud_access_num += 1
    if (self.task7.location != p.CLOUD and self.task8.location == p.CLOUD): self.metrics.cloud_access_num += 1
    if (self.task8.location != p.CLOUD and self.task9.location == p.CLOUD): self.metrics.cloud_access_num += 1

if __name__ == '__main__':
  task_location = [p.EDGE, p.CLOUD, p.CLOUD, p.CLOUD, p.CLOUD, p.CLOUD, p.CLOUD, p.CLOUD, p.EDGE]
  metrics = m.AISimModelMetrics(len(task_location))
  model = AISimModel(metrics)

  print(str(task_location))
  model.simulate(task_location)
