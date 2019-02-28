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
        self.vertical_photos = np.empty([])
        self.horizontal_photos = np.empty([])

    def dump(self):
        print('dumping problem info')

def get_or_create_tag_id(tag, current_dict, current_tag_id):
    if tag in current_dict:
        return current_dict[tag]
    else:
        current_dict[tag] = current_tag_id
        return current_tag_id


def parse_input(filename):
    file = open(filename)

    problem_obj = ProblemInfo()
    num_photos = int(file.readline())

    vertical_count = 0
    horizontal_count = 0
    max_num_tags = 100

    tag_to_label_mapping = dict()
    current_tag_id = 0
    default_tag_id = -1

    for i in range(num_photos):
        info = file.readline().split(' ')
        shape = str(info[0])
        num_tags = int(info[1])
        if shape == 'V':
            problem_obj.vertical_photos[vertical_count] = np.zeros([max_num_tags])
            for j in range(num_tags):
                problem_obj.vertical_photos[vertical_count][j] = \
                    get_or_create_tag_id(j + 2, tag_to_label_mapping, current_tag_id)
            vertical_count += 1
        elif shape == 'H':
            problem_obj.horizontal_photos[horizontal_count] = np.zeros([max_num_tags])
            for j in range(num_tags):
                problem_obj.horizontal_photos[horizontal_count][j] = \
                    get_or_create_tag_id(j + 2, tag_to_label_mapping, current_tag_id)
            horizontal_count += 1
        else:
            raise ValueError

    return problem_obj
