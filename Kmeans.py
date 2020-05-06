"""K-means"""

from Point3 import Point3
from random import randint


def __AssignToCentroids(points, centroids):
    """
    Assign data to the nearest centroid
    :param points: tuple of data
    :param centroids: list of centroids
    :return: List of indexes of the nearest centroids
    """
    distances = []
    for index, i in enumerate(points):
        distances.append([])
        for j in centroids:
            distances[index].append(i.getDistance(j))

    temp = []
    for i in distances:
        temp.append(i.index(min(i)))
    return temp


def __GetNewCentroids(points, centroids, ass):
    """
    :param points: tuple of data
    :param centroids: list od centroids
    :param ass: List of indexes of the nearest centroids
    :return: new centroids' coordinates
    """
    for i in range(len(centroids)):
        x, y, z, counter = 0, 0, 0, 0
        for j, k in zip(points, ass):
            if k == i:
                x += j.getX()
                y += j.getY()
                z += j.getZ()
                counter += 1
        if counter != 0:
            centroids[i] = Point3(x / counter, y / counter, z / counter)
    return centroids


# =========================================================


def K_means(D, k):
    """
    Main function
    :param D: points [tuple (or list) of Point3 objects]
    :param k: number of centroids
    :return: list of k centroids (list of Point3 objects)
    """
    c = []

    xcoord = [i.getX() for i in D]
    ycoord = [i.getY() for i in D]
    zcoord = [i.getZ() for i in D]

    for _ in range(k):
        c.append(Point3(randint(min(xcoord), max(xcoord)), randint(min(ycoord), max(ycoord)),
                        randint(min(zcoord), max(zcoord))))

    notEqual = True

    while notEqual < 2:
        assigned = __AssignToCentroids(D, c)
        newCentroids = __GetNewCentroids(D, c, assigned)
        if newCentroids == c:
            notEqual += 1
        else:
            notEqual = 0
        c = newCentroids

    return c
