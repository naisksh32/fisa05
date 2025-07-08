class Car:
    name = '빈차'

    def instance_name(self):
        self.name = '모닝'

    @classmethod
    def class_name(cls):
        cls.name = '현대기아'

A = Car()

print(Car.name)
Car.class_name()
print(Car.name)

print(A.name)
A.instance_name()
print(A.name)

B = Car()
print(B.name)
