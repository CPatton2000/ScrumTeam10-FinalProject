def getReservations():
    
    reservationChart = [["O", "O", "O", "O"], #Initializes reservation chart
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"],
                        ["O", "O", "O", "O"]]
                            
        
    f = open("reservations.txt", "r") #Opens file
        
    lines = f.readlines() #Read all lines

    for i in lines: #Loop through each line
        data = i.split(",") #Split each line
        reservationChart[int(data[1])][int(data[2])] = "X" # changes a 'O' to a 'Y' for each seat in the reservation.txt file

    f.close() #Close file
    return reservationChart #Return Chart 

def verifySeat(row, seat, chart):

    if(chart[row-1][seat-1] == "X"): #If the row and seat (-1), equals an X in the list, the function returns false
        return False
    else: #If not it returns true
        return True
        
def getCode(name):
    i = 0
    j = 0
        
    string = "INFOTC4320"
    code = ""
         
    while i < len(name) and j < len(string): #As long as each number is less than the length of the string the loop continues
        code += name[i] + string[j] #Adds each of the three strings together
        i+=1 #adds to the counters
        j+=1
    while i < len(name): #Loop only triggers if name is greater in length than i, and adds the rest of the characters to the code
        code += name[i]
        i += 1
            
    while j < len(string): #Loop only triggers if string is greater in length than j, and adds the rest of the characters to the code
        code += string[j]
        j += 1
            
    return code #Returns the code


def addReservation(row, seat, name, code):
    f = open("reservations.txt", "a") #Opens up file to append to it
    f.write("\n"+name+", " +str(row-1)+ ", " + str(seat-1) + ", " +code) #Write to the file, subtracts one on the seat to make sure it corresponds with list indicies

    f.close #Close the file