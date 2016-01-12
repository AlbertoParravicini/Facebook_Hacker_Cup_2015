filename = "Qualification Round/Boomerang Constellations/boomerang_constellations.txt"

txt = open(filename)
output = open("Qualification Round/Boomerang Constellations/output.txt", "w")

# Class that holds the spatial coordinates of a star;
class Star():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

# Class that holds a couple of stars.
class StarCouple():
    def __init__(self, star_1, star_2):
        self.star_1 = star_1
        self.star_2 = star_2

# Squared euclidean distance between two stars;
def distance(star_1, star_2):
    return (star_1.x - star_2.x)*(star_1.x - star_2.x) + (star_1.y - star_2.y)*(star_1.y - star_2.y)

num_of_nights = int(txt.readline())
nights = []
for i in range(0,num_of_nights):
    num_of_stars = int(txt.readline())
    stars = []
    for i in range(0, num_of_stars):
        star_string = (txt.readline()).split()
        star = Star(int(star_string[0]), int(star_string[1]))
        stars.append(star)
    nights.append(stars)

txt.close()


for night_index, night in enumerate(nights): 
    
    boomerangs_per_night = 0
    for star_index_1, star_1 in enumerate(night):
        # Save in a map the star couples containing "star_1";
        # the key is the distance from "star_1"
        distance_map = {}
        for star_index_2, star_2 in enumerate(night):
            if (star_index_1 != star_index_2):
                dist = distance(star_1, star_2)
                star_couple = StarCouple(star_1, star_2)
                distance_map.setdefault(dist, []).append(star_couple)
       
        for dist in distance_map:
            star_num = len(distance_map[dist])
            if star_num > 1:
                # The number of possible combination is equivalent to the binomial coefficient (n, 2),
                # i.e. n * (n - 1) / 2
                # n is the number of couples containing "star_1", for a given length "dist";
                boomerangs_per_night = boomerangs_per_night + star_num * (star_num - 1)//2
    result_string = "Case #" + str(night_index + 1) + ": " + str(boomerangs_per_night) + "\n" 
    output.write(result_string)
    print(result_string)

output.close()


        
            