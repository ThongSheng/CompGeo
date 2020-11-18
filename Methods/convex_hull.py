from classes.Line import Line_Segment
from classes.Point import Point

testing = [Point(2, 3), Point(12, 30),
           Point(40, 50), Point(5, 1),
           Point(12, 10), Point(3, 4)]


def sorter(points):
    return points.x


# determines if point is on right or left of the line
def lr(line, point):
    value = ((line.end.x - line.beginning.x) * (point.y - line.beginning.y)) \
            - ((line.end.y - line.beginning.y) * (point.x - line.beginning.x))
    if value > 0:
        return 1
    else:
        return 0


def convex_hull(points):
    pointsCopy = points.copy()
    pointsCopy.sort(key=sorter)
    hull = []
    point_to_add = points[0]
    endpoint = Point(0, 0)

    while endpoint != pointsCopy[0]:
        hull.append(point_to_add)
        endpoint = pointsCopy[0]
        temp_line = Line_Segment(hull[-1], endpoint)
        for a_point in pointsCopy:
            if lr(temp_line, a_point) == 1 or point_to_add == endpoint:
                endpoint = a_point
                temp_line = Line_Segment(hull[-1], endpoint)
        point_to_add = endpoint

    return hull


