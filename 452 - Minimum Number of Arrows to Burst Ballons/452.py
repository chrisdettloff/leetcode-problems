class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        # sort for nlog(n) time instead of n
        points.sort()
        prev = points[0]
        total = 1
        # init start and end and skip first point
        for start, end in points [1:]:
            # if start is larger than previous add to total and update previous
            if start > prev[1]:
                total += 1
                prev = [start, end]
            # update previous to the min of either previous or end
            else:
                prev[1] = min(prev[1], end)
        return total
