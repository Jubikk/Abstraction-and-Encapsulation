#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.9 | CAR |

#import Class
from CarClass import CAR
from colorama import init, Fore

#def "car"
def car():
 
   #The_Car = Car(,)
   The_Car = CAR(2004, "Subaru")

#Use range for both acceleration and brake
   for i in range(5):
       The_Car.accelerate()
       print("The current speed is:", The_Car.get_speed())
    
   for i in range(5):
       The_Car.brake()
       print("The current speed is:", The_Car.get_speed())

if __name__== "__main__" :
    car()

#end

