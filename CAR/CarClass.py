#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.9 | CAR |

#Create Car Class
class CAR:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

#define accelerate, brake, speed
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        return self.__speed


#end