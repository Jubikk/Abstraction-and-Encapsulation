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
       print(f"The current speed is: {Fore.BLUE}{The_Car.get_speed()}{Fore.RESET}")
    
   for i in range(5):
       The_Car.brake()
       print(f"The current speed is: {Fore.YELLOW}{The_Car.get_speed()}{Fore.RESET}")

if __name__== "__main__" :
    car()

#end

