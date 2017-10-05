class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price= price
        self.speed= speed
        self.fuel= fuel
        self.mileage= mileage
        self.price = price
        if price > 10000:       #keep as interger not string
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()  # without this, only the Car1 would be displayed
    def display_all(self):
        print "Price is $ " + str(self.price)
        print "Speed " + str(self.speed) + "mph"
        print "Fuel " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: " + str(self.tax)

Car1 = Car(1100,200,"full",1050)
Car2 = Car(2000,200,"full",1030)
Car3 = Car(90000,200,"full",1070)
Car4 = Car(111000,200,"full",1030)
Car5 = Car(3000,200,"full",1100)
Car6 = Car(2000,200,"full",1030)


Car1.display_all()