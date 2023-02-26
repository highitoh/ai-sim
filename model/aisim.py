import copy
import aisim_model
from aisim_model import EDGE, CLOUD
import aisim_model_metrics as m
import aisim_model_charge as c

ALPHA_TIME = 0
ALPHA_DATA = 0
ALPHA_CHARGE = 1

def optimize():
    task = [EDGE, EDGE, EDGE, EDGE, EDGE, EDGE, EDGE, EDGE, EDGE]

    loss_min = -1
    iter_max = 2 ** (len(task) - 2)
    for i in range(iter_max):
        for j in range(1, len(task)-1): # Fix EDGE for task1 and task9
            task[j] = CLOUD if i & (1 << (j-1)) else EDGE

        # Initialize
        metrics = m.AISimModelMetrics(len(task))
        model = aisim_model.AISimModel(metrics)

        # Run Simulation
        print("[Iterate " + str(i) + "]")
        model.simulate(task)

        # Calculate Charge
        charge = c.AISimModelCharge()
        charge.time_avg = metrics.average("total_time")
        charge.data_avg = metrics.average("total_data")
        charge.out_data_avg = metrics.average("out_data")
        charge.cloud_time_avg = metrics.average("cloud_time")
        charge.comm_time_avg = metrics.average("comm_time")

        # Objective Function
        time_avg = metrics.average("total_time")
        data_avg = metrics.average("total_data")
        charge_amount = charge.calc_charge()
        loss = time_avg * ALPHA_TIME + data_avg * ALPHA_DATA + charge_amount * ALPHA_CHARGE
        if((loss_min > loss) or (loss_min == -1)):
            loss_min = loss
            opt_task = copy.copy(task)
            opt_time_avg = time_avg
            opt_data_avg = data_avg
            opt_charge = charge_amount

        # Print Summary
        metrics.print_summary()
        charge.print_summary()
    
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