import random
import aisim_model_param as p

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
  charge = 0

  def simulate(self, task):

    time_all = 0
    data_all = 0
    time_max = 0
    time_min = 0
    data_max = 0
    data_min = 0
    cloud_time_all = 0
    cloud_time_avg = 0
    cloud_access_num = 0

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
      cloud_time = 0
      data = 0
      cloud_access_num = 0

      if self.task1 == EDGE:
        t = random.normalvariate(p.TASK_AVG_1, p.TASK_VAR_1)
        time += t * (p.MY_CPU_CLOCK / p.EDGE_CPU_CLOCK)
      elif self.task1 == CLOUD:
        t = random.normalvariate(p.TASK_AVG_2, p.TASK_VAR_2)
        time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        cloud_time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        cloud_access_num += 1

      if (self.task1 == EDGE and self.task2 == CLOUD) or (self.task1 == CLOUD and self.task2 == EDGE):
        data += random.normalvariate(p.COMM_AVG_1_2, p.COMM_VAR_1_2)
        t = data / p.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *p.LT_SIGMA_GAIN)

      if self.task2 == EDGE:
        t = random.normalvariate(p.TASK_AVG_2, p.TASK_VAR_2)
        time += t * (p.MY_CPU_CLOCK / p.EDGE_CPU_CLOCK)
      elif self.task2 == CLOUD:
        t = random.normalvariate(p.TASK_AVG_2, p.TASK_VAR_2)
        time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        cloud_time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        if(self.task1 != CLOUD): cloud_access_num += 1

      if (self.task2 == EDGE and self.task3 == CLOUD) or (self.task2 == CLOUD and self.task3 == EDGE):
        data += random.normalvariate(p.COMM_AVG_2_3, p.COMM_VAR_2_3)
        t = data / p.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *p.LT_SIGMA_GAIN)

      if self.task3 == EDGE:
        t = random.normalvariate(p.TASK_AVG_3, p.TASK_VAR_3)
        time += t * (p.MY_CPU_CLOCK / p.EDGE_CPU_CLOCK)
      elif self.task3 == CLOUD:
        t = random.normalvariate(p.TASK_AVG_3, p.TASK_VAR_3)
        time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        cloud_time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        if(self.task2 != CLOUD): cloud_access_num += 1

      if (self.task3 == EDGE and self.task4 == CLOUD) or (self.task3 == CLOUD and self.task4 == EDGE):
        data += random.normalvariate(p.COMM_AVG_3_4, p.COMM_VAR_3_4)
        t = data / p.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *p.LT_SIGMA_GAIN)

      if self.task4 == EDGE:
        t = random.normalvariate(p.TASK_AVG_4, p.TASK_VAR_4)
        time += t * (p.MY_CPU_CLOCK / p.EDGE_CPU_CLOCK)
      elif self.task4 == CLOUD:
        t = random.normalvariate(p.TASK_AVG_4, p.TASK_VAR_4)
        time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        cloud_time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        if(self.task3 != CLOUD): cloud_access_num += 1

      if (self.task4 == EDGE and self.task5 == CLOUD) or (self.task4 == CLOUD and self.task5 == EDGE):
        data += random.normalvariate(p.COMM_AVG_4_5, p.COMM_VAR_4_5)
        t = data / p.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *p.LT_SIGMA_GAIN)

      if self.task5 == EDGE:
        t = random.normalvariate(p.TASK_AVG_5, p.TASK_VAR_5)
        time += t * (p.MY_CPU_CLOCK / p.EDGE_CPU_CLOCK)
      elif self.task5 == CLOUD:
        t = random.normalvariate(p.TASK_AVG_5, p.TASK_VAR_5)
        time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        cloud_time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        if(self.task4 != CLOUD): cloud_access_num += 1

      if (self.task5 == EDGE and self.task6 == CLOUD) or (self.task5 == CLOUD and self.task6 == EDGE):
        data += random.normalvariate(p.COMM_AVG_5_6, p.COMM_VAR_5_6)
        t = data / p.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *p.LT_SIGMA_GAIN)

      if self.task6 == EDGE:
        t = random.normalvariate(p.TASK_AVG_6, p.TASK_VAR_6)
        time += t * (p.MY_CPU_CLOCK / p.EDGE_CPU_CLOCK)
      elif self.task6 == CLOUD:
        t = random.normalvariate(p.TASK_AVG_6, p.TASK_VAR_6)
        time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        cloud_time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        if(self.task5 != CLOUD): cloud_access_num += 1

      if (self.task6 == EDGE and self.task7 == CLOUD) or (self.task6 == CLOUD and self.task7 == EDGE):
        data += random.normalvariate(p.COMM_AVG_6_7, p.COMM_VAR_6_7)
        t = data / p.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *p.LT_SIGMA_GAIN)

      if self.task7 == EDGE:
        t = random.normalvariate(p.TASK_AVG_7, p.TASK_VAR_7)
        time += t * (p.MY_CPU_CLOCK / p.EDGE_CPU_CLOCK)
      elif self.task7 == CLOUD:
        t = random.normalvariate(p.TASK_AVG_7, p.TASK_VAR_7)
        time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        cloud_time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        if(self.task6 != CLOUD): cloud_access_num += 1

      if (self.task7 == EDGE and self.task8 == CLOUD) or (self.task7 == CLOUD and self.task8 == EDGE):
        data += random.normalvariate(p.COMM_AVG_7_8, p.COMM_VAR_7_8)
        t = data / p.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *p.LT_SIGMA_GAIN)

      if self.task8 == EDGE:
        t = random.normalvariate(p.TASK_AVG_8, p.TASK_VAR_8)
        time += t * (p.MY_CPU_CLOCK / p.EDGE_CPU_CLOCK)
      elif self.task8 == CLOUD:
        t = random.normalvariate(p.TASK_AVG_8, p.TASK_VAR_8)
        time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        cloud_time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        if(self.task7 != CLOUD): cloud_access_num += 1

      if (self.task8 == EDGE and self.task9 == CLOUD) or (self.task8 == CLOUD and self.task9 == EDGE):
        data += random.normalvariate(p.COMM_AVG_8_9, p.COMM_VAR_8_9)
        t = data / p.CLOUD_EDGE_BPS
        time += random.normalvariate(t, t *p.LT_SIGMA_GAIN)

      if self.task9 == EDGE:
        t = random.normalvariate(p.TASK_AVG_9, p.TASK_VAR_9)
        time += t * (p.MY_CPU_CLOCK / p.EDGE_CPU_CLOCK)
      elif self.task9 == CLOUD:
        t = random.normalvariate(p.TASK_AVG_9, p.TASK_VAR_9)
        time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        cloud_time += t * (p.MY_CPU_CLOCK / p.CLOUD_CPU_CLOCK)
        if(self.task8 != CLOUD): cloud_access_num += 1

      time_all += time
      data_all += data
      cloud_time_all += cloud_time
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
    cloud_time_avg = cloud_time_all / self.ITERATION
    self.charge = self.calc_charge(self.time_avg, self.data_avg, cloud_access_num, cloud_time_avg)
    print("time_avg=" + str(self.time_avg) + ", time_max=" + str(time_max) + ", time_min=" + str(time_min))
    print("data_avg=" + str(self.data_avg) + ", data_max=" + str(data_max) + ", data_min=" + str(data_min))
    print("charge=" + str(self.charge))

  def calc_charge(self, time_avg, data_avg, cloud_access_num, cloud_time_avg):
    charge = 0
    if p.CLOUD_SERVICE == "EC2":
      charge += p.EC2_INSTANCE_NUM * p.EC2_COST_PER_HOUR * 730
      charge += p.EBS_STORAGE_SIZE * p.EBS_COST_PER_GB * p.EC2_INSTANCE_NUM
    elif p.CLOUD_SERVICE == "LAMBDA":
      exec_time_s = p.REQUEST_NUM * cloud_time_avg
      charge += cloud_access_num * p.LAMBDA_MEM_SIZE * exec_time_s * p.LAMBDA_COST_PER_MEMS
      charge += cloud_access_num * p.REQUEST_NUM * p.LAMBDA_COST_PER_REQ
    return charge

if __name__ == '__main__':
  model = AISimModel()
  task = [EDGE, EDGE, EDGE, EDGE, CLOUD, CLOUD, CLOUD, EDGE, EDGE]

  print(str(task))
  model.simulate(task)
