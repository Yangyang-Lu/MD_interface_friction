from numpy import *
def compute_force(top_data, bottom_data):
   len(top_data)
   len(top_data[0])
   len(bottom_data)
   len(bottom_data[0])
   list1 = len(top_data[0])
   e = 0.00284
   k = 3.4
   #################
   #for CC
   #          S

   CC_z0 =3.328819
   CC_C0 = 21.847167
   CC_c2 = 12.060173
   CC_C4 = 4.711099
   CC_C = 6.678908e-4
   CC_delta = 0.7718101
   CC_lambda = 3.143921
   CC_A = 12.660270
   CC_s = 1.0
   CC_rcut= 2.0

#







   for i in range(0, len(top_data)):
       for j in range(0, len(bottom_data)):
           dtx = float(top_data[i][2]) - float(bottom_data[j][2])
           dty = float(top_data[i][3]) - float(bottom_data[j][3])
           dtz = float(top_data[i][4]) - float(bottom_data[j][4])
           dt = pow((pow(dtx, 2) + pow(dty, 2) + pow(dtz, 2)), 0.5)
           if dt <= 10:
               f1=6*CC_A*pow((dt/CC_z0), -7)
               f2 =



               f = 4 * e * ((12 * pow(k, 12)) / pow(dt, 13)) - 4 * e * ((6 * pow(k, 6)) / pow(dt, 7))
               top_data[i][list1 - 3] = float(top_data[i][list1 - 3]) - float(f * (dtx / dt))
               bottom_data[j][list1 - 3] = float(bottom_data[j][list1 - 3]) + float(f * (dtx / dt))
               top_data[i][list1 - 2] = float(top_data[i][list1 - 2]) - float(f * (dty / dt))
               bottom_data[j][list1 - 2] = float(bottom_data[j][list1 - 2]) + float(f * (dty / dt))
               top_data[i][list1 - 1] = float(top_data[i][list1 - 1]) - float(f * (dtz / dt))
               bottom_data[j][list1 - 1] = float(bottom_data[j][list1 - 1]) + float(f * (dtz / dt))
   return top_data, bottom_data


