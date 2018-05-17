import random
import queue


def cluster(cls_num, eps, minPt, points):
    n = cls_num
    inputs = points
    for i in range(1, n):
        center = random.choice(inputs)  # pick random initial point
        [core, dd_list] = center.core_test(eps, minPt, inputs)
        if core == False:
            continue
        cluster_ele = bfs(center, eps, minPt, inputs, dd_list)
        output_file_name = 'input1_cluster' + str(i) + '.txt'
        output_file = open(output_file_name, "w")
        if cluster_ele is []:
            print("its wrong!!")
        for i in cluster_ele:
            output_file.write(str(i.id) + '\n')
            inputs.remove(i)


def bfs(now, eps, minpt, inputs, dd_list):
    q = queue.Queue()
    cluster_elements = []
    check = set()
    check.add(now)
    cluster_elements.append(now)
    for i in dd_list:
        q.put(i)
        check.add(i)
        cluster_elements.append(i)

    while q.qsize() != 0:
        top = q.get()
        if top in check: continue
        for i in inputs:
            if i in check: continue
            if top.in_eps(i):
                cluster_elements.append(i)
                check.add(i)
                q.put(i)
    return cluster_elements
