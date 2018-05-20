
NOCLUSTER = None
NOISE = False

def dbscan(n, eps, minpt, points):
    cluster_num = 0
    for i in points:
        if cluster_num == n:
            break
        if i.status == NOCLUSTER:
            is_clu = clustering(i, cluster_num, eps, minpt, points)
            if is_clu:
                cluster_num = cluster_num + 1
    return points

def clustering(point, n, eps, minpt, inputs):
    [is_core, reachable] = point.core_test(eps,minpt,inputs)
    if is_core is False:
        point.status = NOISE
        return False
    else:
        point.status = n
        for i in reachable:
            i.status = n
        while(len(reachable) > 0):
            cur = reachable[0]
            [core, reach] = cur.core_test(eps, minpt, inputs)
            if core:
                for i in reach:
                    if i.status == NOISE or i.status == NOCLUSTER:
                        if i.status == NOCLUSTER:
                            reachable.append(i)
                        i.status = n

            reachable = reachable[1:]
        return True
