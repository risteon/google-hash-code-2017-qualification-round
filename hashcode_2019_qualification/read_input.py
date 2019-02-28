class ProblemInfo:
    def __init__(self):
        self.num_photos = None  # integer
        self.shapes = list()  # list
        self.tags = list()  # list

    def dump(self):
        print('dumping problem info')
        print('number of photos: ', self.num_photos)
        print('shapes: ', self.shapes)

"""
EXAMPLE
Input file Description
4
H 3 cat beach sun
V 2 selfie smile
V 2 garden selfie
H 2 garden cat
The collection has 4 photos
Photo 0 is horizontal and has tags [cat, beach, sun]
Photo 1 is vertical and has tags [selfie, smile]
Photo 2 is vertical and has tags [garden, selfie]
Photo 3 is horizontal and has tags [garden, cat]
"""


def parse_input(filename):
    file = open(filename)

    problem_obj = ProblemInfo()
    problem_obj.num_photos = int(file.readline())

    for i in range(problem_obj.num_photos):
        info = file.readline().split(' ')
        problem_obj.shapes.append(info[0])
        for j in range(int(info[1])):
            problem_obj.shapes.extend(str(j))

    return problem_obj
