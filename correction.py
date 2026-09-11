import math


class Point:
    def __init__(self, x : int =0, y : int = 0):
        self.x = x
        self.y = y

    def  __str__(self) -> str:
        return f" Point: ({self.--x}; {self.--y})"


    def DistanceCordonee(self,x:float, y:float)-> float :
        Distance= math.sqrt((x-self.x)**2 + (y-self.y)**2)
        (math.pow(self.__x-x,2)) +  math.pow(self.__y-y,2))
        ((self.__x-x)*(self.__x-x)+(self.__y-y)*(self.__y-y))
        return Distance