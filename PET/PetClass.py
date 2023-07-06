# Joebeck Andrew F. Gusi | BSCPE 1-5 | Assigment No.9 | PET |

#Create a class pet
class PET:

    #def init
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__animal_type = ""

    #set name, age, animal_type
    #get name, age, animal_type
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age
    def get_age(self):
        return self.__age
    
    def set_animal_type(self, animal_type): 
        self.__animal_type = animal_type
    def get_animal_type(self):
        return self.__animal_type

#end

