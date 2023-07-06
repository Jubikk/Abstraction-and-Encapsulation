# Joebeck Andrew F. Gusi | BSCPE 1-5 | Assigment No.9 |

#import Fan_Class 
from FanClass import FAN

#First Fan
fan1 = FAN(FAN.Fast, 10, 'yellow', True)

#Second Fan
fan2 = FAN(FAN.Medium, 5, 'blue', False)

#Print or Display the first fan
print("FAN_1:")
print("-SPEED:", fan1.get_speed())
print("-RADIUS:", fan1.get_radius())
print("-COLOR:", fan1.get_color())
print("-ON:", fan1.get_on())

print("\n================================")

#Print or Display the second fan
print("\nFAN_2:")
print("-SPEED:", fan2.get_speed())
print("-RADIUS:", fan2.get_radius())
print("-COLOR:", fan2.get_color())
print("-ON:", fan2.get_on())

#end 

