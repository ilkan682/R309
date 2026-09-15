import math


class point:
    def __init__(self, x: float = 0, y: float = 0):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    def __str__(self) -> str:
        return f"point:[{self.__x}; {self.__y}]"

    def distancecoordonnee(self, x: float, y: float) -> float:
        distance = math.sqrt((self.__x - x) ** 2 + (self.__y - y) ** 2)
        return distance

    def distancepoint(self, camarade) -> float:
        distance = math.sqrt((self.__x - camarade.x) ** 2 + (self.__y - camarade.y) ** 2)
        return distance


class cercle:
    def __init__(self, rayon: float, centre: point = point()):
        if rayon < 0:
            raise ValueError("rayon invalide")

        self.__centre = centre
        self.__rayon = rayon

    @property
    def centre(self) -> point:
        return self.__centre

    @property
    def rayon(self) -> float:
        return self.__rayon

    def diametre(self) -> float:
        return 2 * self.__rayon

    def perimetre(self) -> float:
        return 2 * math.pi * self.__rayon

    def surface(self) -> float:
        return math.pi * (self.__rayon ** 2)

    def intersection(self, cercle) -> bool:
        distance = self.__centre.distancepoint(cercle.centre)
        return distance <= (self.__rayon + cercle.rayon)

    def contientpoint(self, pt) -> bool:
        distance = self.__centre.distancepoint(pt)
        return distance <= self.__rayon


class rectangle:
    def __init__(self, basgauche: point = point(), longueur: float = 1, hauteur: float = 1, hautdroit: point = None):
        if hautdroit is None:
            if longueur < 0 or hauteur < 0:
                raise ValueError("dimensions invalides")
            self.__basgauche = basgauche
            self.__longueur = longueur
            self.__hauteur = hauteur
        else:
            self.__basgauche = basgauche
            self.__longueur = hautdroit.x - basgauche.x
            self.__hauteur = hautdroit.y - basgauche.y

    def surface(self) -> float:
        return self.__longueur * self.__hauteur

    def perimetre(self) -> float:
        return 2 * (self.__longueur + self.__hauteur)

    def pointbasgauche(self) -> point:
        return self.__basgauche

    def pointbasdroit(self) -> point:
        return point(self.__basgauche.x + self.__longueur, self.__basgauche.y)

    def pointhautgauche(self) -> point:
        return point(self.__basgauche.x, self.__basgauche.y + self.__hauteur)

    def pointhautdroit(self) -> point:
        return point(self.__basgauche.x + self.__longueur, self.__basgauche.y + self.__hauteur)

    def contientpoint(self, pt) -> bool:
        return (self.__basgauche.x <= pt.x <= self.__basgauche.x + self.__longueur
                and
                self.__basgauche.y <= pt.y <= self.__basgauche.y + self.__hauteur)


class trianglerectangle:
    def __init__(self, cote1: float, cote2: float, angledroit: point = point()):
        if cote1 < 0 or cote2 < 0:
            raise ValueError("cotes invalides")

        self.__cote1 = cote1
        self.__cote2 = cote2
        self.__angledroit = angledroit

    def hypotenuse(self) -> float:
        return math.sqrt(self.__cote1 ** 2 + self.__cote2 ** 2)

    def perimetre(self) -> float:
        return self.__cote1 + self.__cote2 + self.hypotenuse()

    def surface(self) -> float:
        return (self.__cote1 * self.__cote2) / 2

    def isocele(self) -> bool:
        return self.__cote1 == self.__cote2


if __name__ == "__main__":
    try:
        print(" test du point ")
        x = float(input("entrez x pour le point : "))
        y = float(input("entrez y pour le point : "))
        p1 = point(x, y)
        print(p1)

        print("\n test du cercle ")
        r = float(input("entrez le rayon du cercle : "))
        c1 = cercle(r, p1)
        print("surface du cercle :", c1.surface())

        print("\n test du rectangle ")
        long = float(input("entrez la longueur du rectangle : "))
        haut = float(input("entrez la hauteur du rectangle : "))
        r1 = rectangle(p1, long, haut)
        print("perimetre du rectangle :", r1.perimetre())

        print("\n test du triangle ")
        c1 = float(input("entrez le cote 1 du triangle : "))
        c2 = float(input("entrez le cote 2 du triangle : "))
        t1 = trianglerectangle(c1, c2)
        print("hypotenuse :", t1.hypotenuse())

    except:
        print("erreur detectee")
    else:
        print("\nfin du programme")