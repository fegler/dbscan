from my_pack.point import Point

def file_input(input_file):
    data_file = open(input_file, "r")
    total_points = []
    while(True):
        line = data_file.readline()
        if not line:
            break
        splited = line.split("\t")
        id, pox, poy = splited
        poy = poy[:len(poy)-1]
        temp = Point(int(id),float(pox),float(poy))
        total_points.append(temp)

    return total_points

def output_file_setup(data_name, cluster_number, points):

    for i in range(0,cluster_number):
        file_name = data_name + '_cluster_' + str(i) + '.txt'
        output_file = open(file_name, "w")
        for j in points:
            if j.status is None or j.status is False:
                continue
            if j.status == i:
                output_file.write(str(j.id) + '\n')






