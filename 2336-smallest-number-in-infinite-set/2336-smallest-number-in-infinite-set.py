import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.current = 1
        self.added = []
        self.seen = set()

    def popSmallest(self):
        if self.added:
            num = heapq.heappop(self.added)
            self.seen.remove(num)
            return num

        num = self.current
        self.current += 1
        return num

    def addBack(self, num):
        if num < self.current and num not in self.seen:
            heapq.heappush(self.added, num)
            self.seen.add(num)