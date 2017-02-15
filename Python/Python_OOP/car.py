class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()
    def display_all(self):
        print "Price: " + str(self.price) + "\nSpeed: " + self.speed + "\nFuel: " + self.fuel + "\nMileage: " + self.mileage + "\nTax: " + str(self.tax) + "\n"
fee = Car(14000, "40mph", "Full", "27mpg")
fie = Car(8000, "50mph", "Not Full", "23mpg")
foe = Car(100000, "80mph", "Empty", "15mpg")
fum = Car(1000, "0mph", "Empty", "0mpg")
hidey = Car(26500, "45mph", "Full", "34mpg")
ho = Car(35000, "50mph", "Not Full", "25mpg")
