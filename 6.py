import math


class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point: ({self.x}; {self.y})"

    def distanceCoord(self, a: float, b: float) -> float:
        Distance = math.sqrt((a - self.x) ** 2 + (b - self.y) ** 2)
        return Distance

    def distancePoint(self, camarade) -> float:
        Distance = math.sqrt((camarade.x - self.x) ** 2 +
                             (camarade.y - self.y) ** 2)
        return Distance


class Cercle:
    def __init__(self, rayon: float, centre: Point = Point()):
        self.centre = centre
        self.rayon = rayon

    def diametre(self) -> float:
        return 2 * self.rayon

    def perimetre(self) -> float:
        return 2 * math.pi * self.rayon

    def surface(self) -> float:
        return math.pi * self.rayon ** 2

    def intersection(self, cercle) -> bool:
        distance = self.centre.distancePoint(cercle.centre)

        return distance <= self.rayon + cercle.rayon

    def contientPoint(self, point) -> bool:
        distance = self.centre.distancePoint(point)

        return distance <= self.rayon


class Rectangle:
    def __init__(self, basGauche: Point = Point(),
                 longueur: float = 1, hauteur: float = 1,
                 hautDroit: Point = None):

        if hautDroit is None:
            self.basGauche = basGauche
            self.longueur = longueur
            self.hauteur = hauteur
        else:
            self.basGauche = basGauche
            self.longueur = hautDroit.x - basGauche.x
            self.hauteur = hautDroit.y - basGauche.y

    def surface(self) -> float:
        return self.longueur * self.hauteur

    def perimetre(self) -> float:
        return 2 * (self.longueur + self.hauteur)

    def pointBasGauche(self) -> Point:
        return self.basGauche

    def pointBasDroit(self) -> Point:
        return Point(self.basGauche.x + self.longueur,
                     self.basGauche.y)

    def pointHautGauche(self) -> Point:
        return Point(self.basGauche.x,
                     self.basGauche.y + self.hauteur)

    def pointHautDroit(self) -> Point:
        return Point(self.basGauche.x + self.longueur,
                     self.basGauche.y + self.hauteur)

    def contientPoint(self, point) -> bool:
        return (self.basGauche.x <= point.x <= self.basGauche.x + self.longueur
                and
                self.basGauche.y <= point.y <= self.basGauche.y + self.hauteur)


class TriangleRectangle:
    def __init__(self, cote1: float, cote2: float,
                 angleDroit: Point = Point()):

        self.cote1 = cote1
        self.cote2 = cote2
        self.angleDroit = angleDroit

    def hypotenuse(self) -> float:
        return math.sqrt(self.cote1 ** 2 + self.cote2 ** 2)

    def perimetre(self) -> float:
        return self.cote1 + self.cote2 + self.hypotenuse()

    def surface(self) -> float:
        return (self.cote1 * self.cote2) / 2

    def isocèle(self) -> bool:
        return self.cote1 == self.cote2


if __name__ == "__main__":

    # -------------------------
    # TEST DE LA CLASSE POINT
    # -------------------------

    p1 = Point(3.2, 1)
    print(p1)

    p2 = Point()
    print(p2)

    print("Distance avec les coordonnées :",
          p1.distanceCoord(5, 4))

    print("Distance avec un autre Point :",
          p1.distancePoint(p2))


    # -------------------------
    # TEST DE LA CLASSE CERCLE
    # -------------------------

    c1 = Cercle(5)
    c2 = Cercle(3, Point(6, 0))

    print("Diamètre du cercle :", c1.diametre())
    print("Périmètre du cercle :", c1.perimetre())
    print("Surface du cercle :", c1.surface())

    print("Les cercles sont en intersection :",
          c1.intersection(c2))

    p3 = Point(3, 0)
    print("Le point appartient au cercle :",
          c1.contientPoint(p3))


    # -------------------------
    # TEST DE LA CLASSE RECTANGLE
    # -------------------------

    r1 = Rectangle()

    print("Surface du rectangle :", r1.surface())
    print("Périmètre du rectangle :", r1.perimetre())

    print("Bas gauche :", r1.pointBasGauche())
    print("Bas droit :", r1.pointBasDroit())
    print("Haut gauche :", r1.pointHautGauche())
    print("Haut droit :", r1.pointHautDroit())

    p4 = Point(0.5, 0.5)

    print("Le point est dans le rectangle :",
          r1.contientPoint(p4))


    # -------------------------
    # TEST DU TRIANGLE RECTANGLE
    # -------------------------

    t1 = TriangleRectangle(3, 4)

    print("Hypoténuse :", t1.hypotenuse())
    print("Périmètre du triangle :", t1.perimetre())
    print("Surface du triangle :", t1.surface())
    print("Le triangle est isocèle :", t1.isocèle())
