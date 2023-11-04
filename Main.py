import numpy as np
from pandas import *
# create an "infinite" path depending on the user input
def create_path(Area,Directions):
    
    for dir in range(len(Directions)):
        # Add one column on the top or bottom of the Area
        if Directions[dir] == "N" or Directions[dir] == "S":
            if Directions[dir] == "N": 
                Area.insert(0, [0] * len(Area[0]))
            else:
                Area.append([0] * len(Area[0]))
                  
        # Add one column to the left or right of the Area
        elif Directions[dir] == "E" or Directions[dir] == "W":
            if Directions[dir] == "E":
                for i in range(len(Area)):
                    Area[i].append(0)     
            else:
                for i in range(len(Area)):
                    Area[i].insert(0, 0)
    # walk area
    walk_path(Area,Directions)

# count the number of pokemons caught by checking the number of non-zero elements in the Area
def count(Area):
    
    count = 0
    
    for i in range(len(Area)):
        for j in range(len(Area[i])):
            
            if Area[i][j] != 0:
                count += 1
                
    return count

def main(Area = [[5,0]]):
    
    Directions = input("Insert N(North),E(East),W(West) ou S(South) so that you can move Ash:")
    Directions = Directions.upper()
    create_path(Area,Directions)
    

def walk_path(Area,Directions,i = 0,j = 0):
    
    # find the starting position of ash
    for k in range(len(Area)):
        for l in range(len(Area[k])):
            if Area[k][l] == 5:
                i = k
                j = l
                break
    # Transform the Area into numbers depending on the direction that ash is going,could also be done in binary,
    # but its easier to understand this way by associating each number to a direction       
    for dir in range(len(Directions)):
           
            if Directions[dir] == "S":
                if Area[i + 1][j ] == 0:
                    Area[i + 1][j] = 1
                i += 1
            if Directions[dir] == "N":
                
                if Area[i - 1][j] == 0:
                    Area[i -1 ][j] = 2
                i -= 1

            if Directions[dir] == "E":
                if Area[i][j + 1] == 0:
                    Area[i][j + 1] = 3
                j += 1
            if Directions[dir] == "W":
                if Area[i][j - 1] == 0:
                    Area[i][j - 1] = 4
                j -= 1
    end(Area)
   
# show end screen with the number of pokemons caught and the Area   
def end(Area):
    
    print(DataFrame(Area))
    print("Pokemons catched: ", count(Area))
    
 
            
  
main()