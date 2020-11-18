# Two segments (p1,q1) and (p2,q2) intersect if and only if one of the following two conditions is verified
# 1. General Case:
# – (p1, q1, p2) and (p1, q1, q2) have different orientations and
# – (p2, q2, p1) and (p2, q2, q1) have different orientations.
# 2. Special Case
# – (p1, q1, p2), (p1, q1, q2), (p2, q2, p1), and (p2, q2, q1) are all collinear and
# – the x-projections of (p1, q1) and (p2, q2) intersect
# – the y-projections of (p1, q1) and (p2, q2) intersect

def orientation(self, a,b,c):
    # to find the orientation of an ordered triplet (a,b,c) 
    # function returns the following values: 
    # 0 : Colinear points 
    # 1 : Clockwise points 
    # 2 : Counterclockwise 
    
    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/  
    # for details of below formula.
    
    val = (float(b.y - a.y) * (c.x - b.x)) - (float(b.x - a.x) * (c.y - b.y)) 
    if (val > 0): 
        # Clockwise orientation 
        return 1
    elif (val < 0): 
        # Counterclockwise orientation 
        return 2
    else: 
        # Colinear orientation 
        return 0

def onSegment(self,p,q,r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
        return True
    return False

def ifIntersect(self, a1,b1,a2,b2):
    o1 = self.orientation(a1,b1,a2)
    o2 = self.orientation(a1,b1,b2)
    o3 = self.orientation(a2,b2,a1)
    o4 = self.orientation(a2,b2,b1)
    if o1 != o2 and o3 != o4:
        return True
    # a1 , b1 and a2 are colinear and a2 lies on segment p1q1 
    if ((o1 == 0) and self.onSegment(a1, a2, b1)): 
        return True

    # a1 , b1 and b2 are colinear and b2 lies on segment p1q1 
    if ((o2 == 0) and self.onSegment(a1, b2, b1)): 
        return True

    # a2 , b2 and a1 are colinear and a1 lies on segment p2q2 
    if ((o3 == 0) and self.onSegment(a2, a1, b2)): 
        return True

    # a2 , b2 and b1 are colinear and b1 lies on segment p2q2 
    if ((o4 == 0) and self.onSegment(a2, b1, b2)): 
        return True
        
    return False