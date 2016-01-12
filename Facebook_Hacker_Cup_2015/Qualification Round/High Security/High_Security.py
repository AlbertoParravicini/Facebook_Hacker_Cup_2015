filename = "Qualification Round/High Security/high_security (2).txt"

txt = open(filename)
output = open("Qualification Round/High Security/output.txt", "w")

# Class that holds a reference of the two rows of the corridor;
# A wall X is placed at the start and at the end of each row,
# to makes thing easier later on;
class Day:
    def __init__(self, top_row_string, bottom_row_string):
        self.top_row = list(top_row_string)
        self.top_row.insert(0, "X")
        self.top_row.pop()
        self.top_row.append("X")
        self.bottom_row = list(bottom_row_string)
        self.bottom_row.insert(0, "X")
        self.bottom_row.pop()
        self.bottom_row.append("X")

number_of_days = int(txt.readline())
days = []
for i in range(0, number_of_days):
    size = txt.readline()
    days.append(Day(txt.readline(), txt.readline()))

for day_index, day in enumerate(days):
 
    number_of_guards = 0
    
    # From left to right, mark as T the places near a wall, where a guard could stay;
    # Then mark as P the T which are surrounded by two walls: 
    # these guards are potentially superflous, and might be replaced later on;
    for i in range(0, len(day.top_row)-1):
        if day.top_row[i] == "X" and day.top_row[i+1] == ".":
            day.top_row[i+1] = "T"
        if day.bottom_row[i] == "X" and day.bottom_row[i+1] == ".":
            day.bottom_row[i+1] = "T"

        if day.top_row[i] == "X" and day.top_row[i+1] == "T" and day.top_row[i+2] == "X":
            day.top_row[i+1] = "P"
        if day.bottom_row[i] == "X" and day.bottom_row[i+1] == "T" and day.bottom_row[i+2] == "X":
            day.bottom_row[i+1] = "P"


    for i in range(0, len(day.top_row)):
        
        # For each guard marked as P, examine the row in front of it, 
        # going from the current position to the left, until a wall or another guard is found.
        # If another guard is found, put a new guard in front of the first one,
        # then remove the other two.
        # The trick is that the newly created guard will be able to cover 
        # the range of the two removed guards;
        # This new guard is marked as G, and it won't be moved under any circumstance;
        if day.top_row[i] == "P":
            front_c = day.bottom_row[i]
            j = i
            while front_c != "X" and front_c != "G":
        
                if front_c == "P" or front_c == "T":
                    day.top_row[i] = "."
                    day.bottom_row[j] = "."
                    day.bottom_row[i] = "G"
                    number_of_guards += 1              
                    break
                else:
                    front_c = day.bottom_row[j-1]
                    j -= 1    
    
        if day.bottom_row[i] == "P":
            front_c = day.top_row[i]
            j = i
            while front_c != "X":
        
                if front_c == "P" or front_c == "T" or front_c == "G":
                    day.bottom_row[i] = "."
                    if day.top_row[j] != "G": day.top_row[j] = "."
                    day.top_row[i] = "G"  
                    number_of_guards += 1     
                    break
                else:
                    front_c = day.top_row[j-1]
                    j -= 1 
    
    # Mark as G any remaining guard marked as P or T.
    # If the previous loop didn't replace them,
    # it means that moving these guards won't improve the solution;
    for i in range(0, len(day.top_row)):
        if day.top_row[i] == "T" or day.top_row[i] == "P": 
            day.top_row[i] = "G"
            number_of_guards += 1  
        if day.bottom_row[i] == "T" or day.bottom_row[i] == "P":
            day.bottom_row[i] = "G"
            number_of_guards += 1  

    result = "Case #" + str(day_index + 1) + ": " + str(number_of_guards) + "\n"
    output.write(result)
    print(result)

output.close()
