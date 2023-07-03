import sys

#filename = sys.argv[1]
filename = "C:\\Users\\dell001\\Documents\\Python Scripts\\lammps\\600-2.txt"
x = [ [0]*1024 for i in range(1024) ]
y = [ [0]*1024 for i in range(1024) ]
z = [ [0]*1024 for i in range(1024) ]

splitChar ='\t'
data = list()
i=0
j=0
f = open(filename, "r")

with open(filename) as f:
        count = 0
        for line in f:
            count += 1
f.close()
with open(filename) as f:
	for line in f.readlines()[0:count]:
		curline = line.strip().split(splitChar)
		if(len(curline) > 1):
			#print(curline)
			data.append(curline)
f.close()
i=0
j=0

for line in range(len(data)):
	#print(data[line])
	x[i][j] = float(data[line][0])
	y[i][j] = float(data[line][1])
	z[i][j] = float(str(data[line][2]))
	i += 1
	if(i==1024):
		i = 0 
		j += 1



fpnew = open("huahen.txt","w")
for i in range(1024):
	for j in range(1024):
		if (z[i][j]<2000):
			fpnew.write("%f\t%f\t%f\n" %(x[i][j], y[i][j], z[i][j]))
fpnew.close()
print(len(data))