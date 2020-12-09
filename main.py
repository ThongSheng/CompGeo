from Methods.closest_pair_of_points import *
from Methods.convex_hull import *
from Methods.largest_empty_circle import *
from Methods.line_segment_intersection import *
from classes.Point import *
import math

testing = [Point(0, 5), Point(5, 5),
           Point(2, 0), Point(2, 10),
           Point(12, 10), Point(3, 5),
           Point(11, 11), Point(9, 12),
           Point(12, 15), Point(0, -1)]

close = closest(testing, len(testing))
hull = convex_hull(testing)
lc = largest_circle(testing)

print("closest pair of points in test data: ")
for point_ in close:
     print(point_.x, point_.y)

print("member of convex hull in test data: ")
for point_ in hull:
     print(point_.x, point_.y)

print("line segment intersection for first 4 points in test data: ")
print(ifIntersect(testing[0], testing[1], testing[2], testing[3]))

print("largest empty circle in testing data: ")
for point_ in lc:
     print(point_.x, point_.y)
