# Closest pair of points: Given a set of points, find the two with the smallest distance from each other.
import math


# Returns the Euclidean distance between two given points.
# Arguments: point p and point q.
def dist(p, q):
    return math.sqrt((p.x - q.x)**2 + (p.y - q.y)**2)


# Brute Force method that returns the closest pair of points in an array of points.
# Arguments: an array of points P[], and length of array n.
def closest(P, n):
    min_dist = float('inf')
    if(n < 2):
        print("insufficient points")
        return 0

    for i in range(n):
        for j in range(i+1, n):
            if dist(P[i], P[j]) < min_dist:
                min_dist = dist(P[i], P[j])
                closest_pair = (P[i], P[j])

    return closest_pair