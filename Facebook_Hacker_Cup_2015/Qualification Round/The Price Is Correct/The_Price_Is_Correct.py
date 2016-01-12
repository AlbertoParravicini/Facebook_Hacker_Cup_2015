filename = "Qualification Round/The Price Is Correct/the_price_is_correct.txt"

txt = open(filename)
output = open("Qualification Round/The Price Is Correct/output.txt", "w")

# Class that holds a reference to the maximum price reachable in a game, 
# and the price of each pack;
class Game:
    def __init__(self, max_price, packs_string):
        self.max_price = max_price  
        self.packs = [int(i) for i in packs_string.split(" ")]
        

num_of_game = int(txt.readline())
games = []
for i in range(0, num_of_game):
    max_price = int(((txt.readline()).split(" "))[1])
    packs_string = txt.readline()
    games.append(Game(max_price, packs_string))   
    
# Scan the packs sequence using a moving window that will be extended as much as possible.
# If it can no longer be extended, try to shorten it from the left to add more packs on the right;
for game_index, game in enumerate(games):
    max_price = game.max_price
    packs = game.packs
    combinations = 0
    solution = 0
    pack_index = 0
    current_price = 0
    overlap = 0
    sequence_start = 0

    while pack_index < len(packs):
        # If it is possible to increase the size of the sequence, increase it;
        if current_price + packs[pack_index] <= max_price:
            current_price += packs[pack_index]
            combinations += 1
            pack_index += 1
                   
        else:
            # If the sequence lenght can't be improved, 
            # calculate the number of combinations in the current sequence.
            # From this number one has to remove the combinations found previously, 
            # which are computed from the "overlap" variable;
            if combinations > 0:   
                solution += combinations * (combinations + 1) // 2 - overlap * (overlap + 1) // 2               
                overlap = 0
                combinations = 0
            
            # Skip useless packs
            while pack_index < len(packs) and packs[pack_index] > max_price:
                pack_index += 1 
                sequence_start = pack_index  
                current_price = 0       
            if pack_index >= len(packs): 
                break
            
            # It is possible to add more packs to the current sequence by removing packs at the beginning?
            # Try to shorten the current sequence so that a new pack can be added.
            # Then the sequence might be extended even more to the right, through the first loop;
            while current_price > max_price - packs[pack_index] and sequence_start < pack_index:               
                current_price -= packs[sequence_start]    
                sequence_start += 1
            if pack_index - sequence_start > 0: 
                combinations = pack_index - sequence_start 
                overlap = combinations           
            
    # If the scanning reaches the end with an ongoing sequence, 
    # add the remaining combinations to the solution;
    if combinations != 0:      
        solution += combinations * (combinations + 1) // 2 - overlap * (overlap + 1) // 2        
    
    result_string = "Case #" + str(game_index+1) + ": " + str(solution) + "\n"
    print(result_string)
    output.write(result_string)

output.close()

