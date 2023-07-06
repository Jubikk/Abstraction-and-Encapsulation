# Joebeck Andrew F. Gusi | BSCPE 1-5 | Assigment No.9 | PET |

#import the PetClass
from PetClass import PET
from colorama import Fore, Style
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

#print/display the details
print("The pet's name is: " + pet.get_name())
print("The pet's age is: " + pet.get_age())
print("The pet's animal type is: " + pet.get_animal_type())


#end