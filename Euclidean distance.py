points = [(4, 6), (10, 5), (3, 4), (6, 8)]

def euclideanDistance(points):
    distances = []
    for x in range(0, round(len(points) - 1)):
        euclid = pow((pow((points[x][0] - points[x+1][0]), 2) + pow((points[x][1] - points[x+1][1]), 2)), 0.5)
        distances.append(euclid)

    return distances


euclideanDistance(points)