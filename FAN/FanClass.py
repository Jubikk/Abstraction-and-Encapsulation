#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.9 | FAN |

#Create a Fan Class and assign the speed
class FAN:
    Slow = 1
    Medium= 2
    Fast = 3
    
    #Define init 
    def __init__(self, speed = Slow , radius = 5 , color = 'blue', on = False) :
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
    
    #Getter and Setter Methods
    def get_speed(self) :
        return self.__speed
    def set_speed(self, speed) :
        return self.__speed
    
    def get_radius(self) : 
        return self.__radius
    def set_radius(self, radius) :
        return self.__radius
    
    def get_color(self) :
        return self.__color
    def set_color(self, color) :
        return self.__color
    
    def get_on(self) :
        return self.__on
    def set_on(self, on) :
        self.__on = on
    
#end



    
    