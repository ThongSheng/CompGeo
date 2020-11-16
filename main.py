from Methods.closest_pair_of_points import *
from Methods.convex_hull import *
from Methods.largest_empty_circle import *
from Methods.line_segment_intersection import *
from classes.Point import *
import math

testing  = [Point(2, 3), Point(12, 3),
     Point(40, 50), Point(5, 1),
     Point(12, 10), Point(3, 5),
     Point(11, 11), Point(9, 12),
     Point(12, 15), Point(0, -1)]

close = closest(testing, len(testing))
hull = convex_hull(testing)

print("closest pair of points in test data: ")
for point_ in close:
     print(point_.x, point_.y)
print("member of convex hull in test data: ")
for point_ in hull:
     print(point_.x, point_.y)

