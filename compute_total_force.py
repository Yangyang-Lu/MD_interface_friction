def compute_total_force (top_data, bottom_data, total_top_force, total_bottom_force,frame):
    list1 =len(top_data[0])
    for i in range(0, len(top_data)):
        total_top_force[frame][1] = float(total_top_force[frame][1]) + float(top_data[i][list1 - 7])
        total_top_force[frame][2] = float(total_top_force[frame][2]) + float(top_data[i][list1 - 6])
        total_top_force[frame][3] = float(total_top_force[frame][3]) + float(top_data[i][list1 - 5])
        total_top_force[frame][4] = float(total_top_force[frame][4]) + float(top_data[i][list1 - 4])
        total_top_force[frame][5] = float(total_top_force[frame][5]) + float(top_data[i][list1 - 3])
        total_top_force[frame][6] = float(total_top_force[frame][6]) + float(top_data[i][list1 - 2])
        total_top_force[frame][7] = float(total_top_force[frame][7]) + float(top_data[i][list1 - 1])


    for i in range(0, len(bottom_data)):
        total_bottom_force[frame][1] = float(total_bottom_force[frame][1]) + float(bottom_data[i][list1 - 7])
        total_bottom_force[frame][2] = float(total_bottom_force[frame][2]) + float(bottom_data[i][list1 - 6])
        total_bottom_force[frame][3] = float(total_bottom_force[frame][3]) + float(bottom_data[i][list1 - 5])
        total_bottom_force[frame][4] = float(total_bottom_force[frame][4]) + float(bottom_data[i][list1 - 4])
        total_bottom_force[frame][5] = float(total_bottom_force[frame][5]) + float(bottom_data[i][list1 - 3])
        total_bottom_force[frame][6] = float(total_bottom_force[frame][6]) + float(bottom_data[i][list1 - 2])
        total_bottom_force[frame][7] = float(total_bottom_force[frame][7]) + float(bottom_data[i][list1 - 1])
    return total_top_force, total_bottom_force