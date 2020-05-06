"""Point3"""

from math import sqrt


class Point3:
    """Represents a point as (x, y, z)"""

    def __init__(self, x, y, z):
        """Initialize Point
        :param x: x coordinate
        :param y: y coordinate
        :param z: z coordinate
        """
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self):
        return '(' + str(self.__x) + ', ' + str(self.__y) + ', ' + str(self.__z) + ')'

    def getDistance(self, p):
        """Return distance to p as int of float
        :param p: Point3 object
        """
        return sqrt((self.__x - p.getX()) ** 2 + (self.__y - p.getY()) ** 2 + (self.__z - p.getZ()) ** 2)

    def getX(self):
        """Return X coordinate as int of float"""
        return self.__x
    
    def getY(self):
        """Return Y coordinate as int of float"""
        return self.__y
    
    def getZ(self):
        """Return Z coordinate as int of float"""
        return self.__z
