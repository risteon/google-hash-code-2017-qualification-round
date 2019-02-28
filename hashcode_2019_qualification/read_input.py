import numpy as np

"""
EXAMPLE
Input file Description
4                       The collection has 4 photos
H 3 cat beach sun       Photo 0 is horizontal and has tags [cat, beach, sun]
V 2 selfie smile        Photo 1 is vertical and has tags [selfie, smile]
V 2 garden selfie       Photo 2 is vertical and has tags [garden, selfie]
H 2 garden cat          Photo 3 is horizontal and has tags [garden, cat]
"""


class ProblemInfo:
    def __init__(self):
        self.vertical_photos = None
        self.horizontal_photos = None

    def dump(self):
        print('dumping problem info')
        print('number of photos: ', self.num_photos)


def parse_input(filename):
    file = open(filename)

    problem_obj = ProblemInfo()
    num_photos = int(file.readline())

    tag_to_label_mapping = dict()
    vertical_count = 0
    horizontal_count = 0

    for i in range(num_photos):
        info = file.readline().split(' ')
        if str(info[0]) == 'V':
            vertical_count += 1
        elif str(info[0]) == 'H':
            horizontal_count += 1
        else:
            raise ValueError

    problem_obj.vertical_photos = np.empty([vertical_count])
    problem_obj.horizontal_photos = np.empty([horizontal_count])

    file = open(filename)
    file.readline()

    for i in range(num_photos):
        pass

    return problem_obj
