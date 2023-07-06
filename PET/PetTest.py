# Joebeck Andrew F. Gusi | BSCPE 1-5 | Assigment No.9 | PET |

#import the PetClass
from PetClass import PET
from colorama import Fore, Style
import time
pet = PET()

#input function for:
#name
name = input("Please enter the name of your pet:")
#age
age = input("Please enter the age of your pet:")
#animal_type
type = input("Please enter the type of animal is your pet:")


#set the inputted values
pet.set_name(name)
pet.set_age(age)
pet.set_animal_type(type)

time.sleep(1)
print("\n================================")
#print/display the details
print("The pet's name is: " + Fore.BLUE + pet.get_name() + Style. RESET_ALL)
print("The pet's age is: " + Fore.RED + pet.get_age() + Style. RESET_ALL)
print("The pet's animal type is: " + Fore.YELLOW + pet.get_animal_type() + Style. RESET_ALL)

#end