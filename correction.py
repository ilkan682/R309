import math


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point: ({self.x}; {self.y})"

    def DistanceCordonee(self, x: float, y: float) -> float:
        Distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        return Distance


if __name__ == "__main__":
    x = float(input("Entrez x : "))
    y = float(input("Entrez y : "))

    p1 = Point(x, y)
    print(p1)

    p2 = Point()
    print(p2)

