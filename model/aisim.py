import copy
import aisim_model
from aisim_model import EDGE, CLOUD

ALPHA_TIME = 0
ALPHA_DATA = 0
ALPHA_CHARGE = 1

def optimize():
    model = aisim_model.AISimModel()
    task = [EDGE, EDGE, EDGE, EDGE, EDGE, EDGE, EDGE, EDGE, EDGE]

    loss_min = -1
    iter_max = 2 ** (len(task) - 2)
    for i in range(iter_max):
        for j in range(1, len(task)-1): # Fix EDGE for task1 and task9
            task[j] = CLOUD if i & (1 << (j-1)) else EDGE
        
        # Run Simulation
        print("[Iterate " + str(i) + "]")
        model.simulate(task)

        # Objective Function
        loss = model.time_avg * ALPHA_TIME + model.data_avg * ALPHA_DATA + model.charge * ALPHA_CHARGE
        if((loss_min > loss) or (loss_min == -1)):
            loss_min = loss
            opt_task = copy.copy(task)
            opt_time_avg = model.time_avg
            opt_data_avg = model.data_avg
            opt_charge = model.charge
    
    # Print Result
    print("Result:")
    print(" Task1:" + getResStr(opt_task[0]) + " Task2:" + getResStr(opt_task[1]) + " Task3:" + getResStr(opt_task[2]) + \
          " Task4:" + getResStr(opt_task[3]) + " Task5:" + getResStr(opt_task[4]) + " Task6:" + getResStr(opt_task[5]) + \
          " Task7:" + getResStr(opt_task[6]) + " Task8:" + getResStr(opt_task[7]) + " Task9:" + getResStr(opt_task[8]))
    print(" loss: " + str(loss_min))
    print(" TimeAvg: " + str(opt_time_avg) + " DataAvg: " + str(opt_data_avg))
    print(" Charge: " + str(opt_charge))

def getResStr(value):
    return "CLOUD" if (value == CLOUD) else "EDGE"

if __name__ == '__main__':
    optimize()