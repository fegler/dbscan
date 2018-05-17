from my_pack.point import Point

def setups(input_file):
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



