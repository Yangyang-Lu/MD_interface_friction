def write_top_file(title, top_data):
    with open("C:/Users/dell001/Pictures/计算软件与理论/lammps/石墨烯摩擦/0/atom_top.dump", "a", encoding='utf-8') as f:
        title_inf = ''
        for i in range(0, len(title)):
            title_inf = str(title_inf) + str(str(title[i]).replace("['", "").replace("']", ""))
            title_inf = title_inf + "\n"
        xyz_inf = ''
        for i in range(0, len(top_data)):

            for j in range(0, len(top_data[0])):
                xyz_inf = str(xyz_inf)+ " " + str(top_data[i][j])
            xyz_inf = xyz_inf + "\n"
        inf = str(title_inf)+str(xyz_inf)
        f.write(str(inf))
        f.close()


def write_bottom_file(title, bottom_data):
    with open("C:/Users/dell001/Pictures/计算软件与理论/lammps/石墨烯摩擦/0/atom_bottom.dump", "a", encoding='utf-8') as f:
        title_inf = ''
        for i in range(0, len(title)):
            title_inf = str(title_inf) + str(str(title[i]).replace("['", "").replace("']", ""))
            title_inf = title_inf + "\n"
        xyz_inf = ''
        for i in range(0, len(bottom_data)):

            for j in range(0, len(bottom_data[0])):
                xyz_inf = str(xyz_inf)+ " " + str(bottom_data[i][j])
            xyz_inf = xyz_inf + "\n"
        inf = str(title_inf)+str(xyz_inf)
        f.write(str(inf))
        f.close()


def write_total_file(title, top_data, bottom_data):
    with open("C:/Users/dell001/Pictures/计算软件与理论/lammps/石墨烯摩擦/0/atom_total.dump", "a", encoding='utf-8') as f:
        title_inf = ''
        for i in range(0, len(title)):
            title_inf = str(title_inf) + str(str(title[i]).replace("['", "").replace("']", ""))
            title_inf = title_inf + "\n"
        xyz1_inf = ''
        for i in range(0, len(top_data)):

            for j in range(0, len(top_data[0])):
                xyz1_inf = str(xyz1_inf)+ " " + str(top_data[i][j])
            xyz1_inf = xyz1_inf + "\n"
        xyz2_inf = ''
        for i in range(0, len(bottom_data)):

            for j in range(0, len(bottom_data[0])):
                xyz2_inf = str(xyz2_inf) + " " + str(bottom_data[i][j])
            xyz2_inf = xyz2_inf + "\n"
        inf = str(title_inf)+str(xyz1_inf)+str(xyz2_inf)
        f.write(str(inf))
        f.close()

def write_group_top_file(total_top_force):
    with open("C:/Users/dell001/Pictures/计算软件与理论/lammps/石墨烯摩擦/0/group_top.dump", "a", encoding='utf-8') as f:
        xyz_inf = ''
        for i in range(0, len(total_top_force)):

            for j in range(0, len(total_top_force[0])):
                xyz_inf = str(xyz_inf)+ " " + str(total_top_force[i][j])
            xyz_inf = xyz_inf + "\n"

        inf = str(xyz_inf)
        f.write(str(inf))
        f.close()


def write_group_bottom_file(total_bottom_force):
    with open("C:/Users/dell001/Pictures/计算软件与理论/lammps/石墨烯摩擦/0/group_bottom.dump", "a", encoding='utf-8') as f:
        xyz_inf = ''
        for i in range(0, len(total_bottom_force)):

            for j in range(0, len(total_bottom_force[0])):
                xyz_inf = str(xyz_inf) + " " + str(total_bottom_force[i][j])
            xyz_inf = xyz_inf + "\n"

        inf = str(xyz_inf)
        f.write(str(inf))
        f.close()