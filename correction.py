import math


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point: ({self.x}; {self.y})"

    def DistanceCordonee(self, x: float, y: float) -> float:
        Distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        (math.pow(self.x - x, 2)) + math.pow(self.y - y, 2)
        ((self.x - x) * (self.x - x) + (self.y - y) * (self.y - y))
        return Distance


if __name__ == "__main__":
    p1 = Point(3.2, 1)
    print(p1)
    p2 = Point()
    print(p2)


