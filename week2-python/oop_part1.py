class Point:
    # default_color = "Red"

    # Instance methods
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Magic methods
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point({self.x}, {self.y})")


# Point.default_color = "yellow"
point = Point(10, 20)

point.__str__
# print(point)
# print(str(point))

other = Point(1, 2)

# print(point == other)
# print(point > other)

# print(point + other)
# point = Point.zero()
# print(point.default_color)
# print(Point.default_color)
# point.draw()

# another = Point(3, 4)
# print(another.default_color)
# another.draw()


class TagCloud:
    def __init__(self):
        # Private
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()

# cloud["python"] = 10
# len(cloud)
# cloud.add("python")
# cloud.add("Python")
# cloud.add("Python")
# cloud.add("python")
# print(cloud["PYTHON"])
# print(cloud.__tags["PYTHON"])
print(cloud.__dict__)
print(cloud._TagCloud__tags)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value

    # price = property(get_price, set_price)


product = Product(10)
product.price = 12
print(product.price)
