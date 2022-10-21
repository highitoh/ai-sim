import random
import aisim_model_param

EDGE = 0
CLOUD = 1

class AISimModel:

  ##### シミュレーションパラメータ #####
  ITERATION = 100

  ##### 実行箇所の切り替え #####
  task1 = EDGE
  task2 = EDGE
  task3 = EDGE
  task4 = EDGE
  task5 = CLOUD
  task6 = CLOUD
  task7 = CLOUD
  task8 = EDGE
  task9 = EDGE
  #############################

  time_avg = 0
  data_avg = 0

  def simulate(self, task):

    time_all = 0
    data_all = 0
    time_max = 0
    time_min = 0
    data_max = 0
    data_min = 0

    self.task1 = task[0]
    self.task2 = task[1]
    self.task3 = task[2]
    self.task4 = task[3]
    self.task5 = task[4]
    self.task6 = task[5]
    self.task7 = task[6]
    self.task8 = task[7]
    self.task9 = task[8]

    for i in range(self.ITERATION):
      time = 0
      data = 0

      if self.task1 == EDGE:
        t = random.normalvariate(aisim_model_param.TASK_AVG_1, aisim_model_param.TASK_VAR_1)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.EDGE_CPU_CLOCK)
      elif self.task1 == CLOUD:
        t = random.normalvariate(aisim_model_param.TASK_AVG_2, aisim_model_param.TASK_VAR_2)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.CLOUD_CPU_CLOCK)

      if (self.task1 == EDGE and self.task2 == CLOUD) or (self.task1 == CLOUD and self.task2 == EDGE):
        data += random.normalvariate(aisim_model_param.COMM_AVG_1_2, aisim_model_param.COMM_VAR_1_2)
        t = data / aisim_model_param.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *aisim_model_param.LT_SIGMA_GAIN)

      if self.task2 == EDGE:
        t = random.normalvariate(aisim_model_param.TASK_AVG_2, aisim_model_param.TASK_VAR_2)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.EDGE_CPU_CLOCK)
      elif self.task2 == CLOUD:
        t = random.normalvariate(aisim_model_param.TASK_AVG_2, aisim_model_param.TASK_VAR_2)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.CLOUD_CPU_CLOCK)

      if (self.task2 == EDGE and self.task3 == CLOUD) or (self.task2 == CLOUD and self.task3 == EDGE):
        data += random.normalvariate(aisim_model_param.COMM_AVG_2_3, aisim_model_param.COMM_VAR_2_3)
        t = data / aisim_model_param.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *aisim_model_param.LT_SIGMA_GAIN)

      if self.task3 == EDGE:
        t = random.normalvariate(aisim_model_param.TASK_AVG_3, aisim_model_param.TASK_VAR_3)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.EDGE_CPU_CLOCK)
      elif self.task3 == CLOUD:
        t = random.normalvariate(aisim_model_param.TASK_AVG_3, aisim_model_param.TASK_VAR_3)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.CLOUD_CPU_CLOCK)

      if (self.task3 == EDGE and self.task4 == CLOUD) or (self.task3 == CLOUD and self.task4 == EDGE):
        data += random.normalvariate(aisim_model_param.COMM_AVG_3_4, aisim_model_param.COMM_VAR_3_4)
        t = data / aisim_model_param.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *aisim_model_param.LT_SIGMA_GAIN)

      if self.task4 == EDGE:
        t = random.normalvariate(aisim_model_param.TASK_AVG_4, aisim_model_param.TASK_VAR_4)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.EDGE_CPU_CLOCK)
      elif self.task4 == CLOUD:
        t = random.normalvariate(aisim_model_param.TASK_AVG_4, aisim_model_param.TASK_VAR_4)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.CLOUD_CPU_CLOCK)

      if (self.task4 == EDGE and self.task5 == CLOUD) or (self.task4 == CLOUD and self.task5 == EDGE):
        data += random.normalvariate(aisim_model_param.COMM_AVG_4_5, aisim_model_param.COMM_VAR_4_5)
        t = data / aisim_model_param.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *aisim_model_param.LT_SIGMA_GAIN)

      if self.task5 == EDGE:
        t = random.normalvariate(aisim_model_param.TASK_AVG_5, aisim_model_param.TASK_VAR_5)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.EDGE_CPU_CLOCK)
      elif self.task5 == CLOUD:
        t = random.normalvariate(aisim_model_param.TASK_AVG_5, aisim_model_param.TASK_VAR_5)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.CLOUD_CPU_CLOCK)

      if (self.task5 == EDGE and self.task6 == CLOUD) or (self.task5 == CLOUD and self.task6 == EDGE):
        data += random.normalvariate(aisim_model_param.COMM_AVG_5_6, aisim_model_param.COMM_VAR_5_6)
        t = data / aisim_model_param.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *aisim_model_param.LT_SIGMA_GAIN)

      if self.task6 == EDGE:
        t = random.normalvariate(aisim_model_param.TASK_AVG_6, aisim_model_param.TASK_VAR_6)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.EDGE_CPU_CLOCK)
      elif self.task6 == CLOUD:
        t = random.normalvariate(aisim_model_param.TASK_AVG_6, aisim_model_param.TASK_VAR_6)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.CLOUD_CPU_CLOCK)

      if (self.task6 == EDGE and self.task7 == CLOUD) or (self.task6 == CLOUD and self.task7 == EDGE):
        data += random.normalvariate(aisim_model_param.COMM_AVG_6_7, aisim_model_param.COMM_VAR_6_7)
        t = data / aisim_model_param.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *aisim_model_param.LT_SIGMA_GAIN)

      if self.task7 == EDGE:
        t = random.normalvariate(aisim_model_param.TASK_AVG_7, aisim_model_param.TASK_VAR_7)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.EDGE_CPU_CLOCK)
      elif self.task7 == CLOUD:
        t = random.normalvariate(aisim_model_param.TASK_AVG_7, aisim_model_param.TASK_VAR_7)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.CLOUD_CPU_CLOCK)

      if (self.task7 == EDGE and self.task8 == CLOUD) or (self.task7 == CLOUD and self.task8 == EDGE):
        data += random.normalvariate(aisim_model_param.COMM_AVG_7_8, aisim_model_param.COMM_VAR_7_8)
        t = data / aisim_model_param.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *aisim_model_param.LT_SIGMA_GAIN)

      if self.task8 == EDGE:
        t = random.normalvariate(aisim_model_param.TASK_AVG_8, aisim_model_param.TASK_VAR_8)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.EDGE_CPU_CLOCK)
      elif self.task8 == CLOUD:
        t = random.normalvariate(aisim_model_param.TASK_AVG_8, aisim_model_param.TASK_VAR_8)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.CLOUD_CPU_CLOCK)

      if (self.task8 == EDGE and self.task9 == CLOUD) or (self.task8 == CLOUD and self.task9 == EDGE):
        data += random.normalvariate(aisim_model_param.COMM_AVG_8_9, aisim_model_param.COMM_VAR_8_9)
        t = data / aisim_model_param.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *aisim_model_param.LT_SIGMA_GAIN)

      if self.task9 == EDGE:
        t = random.normalvariate(aisim_model_param.TASK_AVG_9, aisim_model_param.TASK_VAR_9)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.EDGE_CPU_CLOCK)
      elif self.task9 == CLOUD:
        t = random.normalvariate(aisim_model_param.TASK_AVG_9, aisim_model_param.TASK_VAR_9)
        time += t * (aisim_model_param.MY_CPU_CLOCK / aisim_model_param.CLOUD_CPU_CLOCK)

      time_all += time
      data_all += data
      if (time_max < time) or (time_max == 0): # 0は無効値
        time_max = time
      elif (time_min > time) or (time_min == 0): # 0は無効値
        time_min = time
      if (data_max < data) or (data_max == 0): # 0は無効値
        data_max = data
      elif (data_min > data) or (data_min == 0): # 0は無効値
        data_min = data
      # print("[Iteration " + str(i) + "] time=" + str(time) + "s, data=" + str(data))

    self.time_avg = time_all / self.ITERATION
    self.data_avg = data_all / self.ITERATION
    print("time_avg=" + str(self.time_avg) + ", time_max=" + str(time_max) + ", time_min=" + str(time_min))
    print("data_avg=" + str(self.data_avg) + ", data_max=" + str(data_max) + ", data_min=" + str(data_min))