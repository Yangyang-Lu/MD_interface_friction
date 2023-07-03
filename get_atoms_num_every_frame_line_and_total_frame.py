
def file_information_get(fileName):
    splitChar ='\t'
    dataSet = []
    with open(fileName, encoding='utf-8') as f:
        count =  0
        for line in f:
            count += 1
    f.close()
    with open(fileName, encoding='utf-8') as f:
        for line in f.readlines()[3:4]:
            curline = line.strip().split(splitChar)  # 字符串方法strip():返回去除两侧（不包括）内部空格的字符串；字符串方法spilt:按照制定的字符将字符串分割成序列
            dataSet.append(curline)
    with open(fileName, encoding='utf-8') as f:
        for line in f.readlines()[5:8]:
            curline = line.strip().split(splitChar)  # 字符串方法strip():返回去除两侧（不包括）内部空格的字符串；字符串方法spilt:按照制定的字符将字符串分割成序列
            dataSet.append(curline)
    return dataSet, count

def get_atoms_num_every_frame_line_and_total_frame(fileName):
    [atoms, total_line] = file_information_get(fileName)
    total_atoms = (int(str(atoms[0]).replace("['", "").replace("']", "").replace("[", "").replace("]", "")))
    total_x = (((str(atoms[1]).replace("['", "").replace("']", "").replace("[", "").replace("]", "")).split()))
    total_y = (((str(atoms[2]).replace("['", "").replace("']", "").replace("[", "").replace("]", "")).split()))
    total_z = (((str(atoms[3]).replace("['", "").replace("']", "").replace("[", "").replace("]", "")).split()))
    lattice=[]
    x=[]
    y=[]
    z=[]
    x.append(float(total_x[0]))
    x.append(float(total_x[1]))
    y.append(float(total_y[0]))
    y.append(float(total_y[1]))
    z.append(float(total_z[0]))
    z.append(float(total_z[1]))
    lattice.append(x)
    lattice.append(y)
    lattice.append(z)
    #print(lattice)
    every_frame_line = total_atoms + 9
    total_frames = int(total_line / every_frame_line)
    # for i in K:
    #    KK.append(str(i).replace("['", "").replace("']", ""))

    return total_atoms, lattice,every_frame_line, total_frames
