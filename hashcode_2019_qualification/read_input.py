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
        self.vertical_tags = None
        self.horizontal_tags = None

        self.vertical_id = None
        self.horizontal_id = None

    def dump(self):
        print('dumping problem info')


def get_or_create_tag_id(tag, current_dict, current_tag_id):
    if tag in current_dict:
        print('{} in dict as {}'.format(tag, current_dict[tag]))
        return current_dict[tag]
    else:
        print('set {} as {}'.format(tag, current_tag_id))
        current_dict[tag] = current_tag_id
        return current_tag_id


def parse_input(filename):
    file = open(filename)

    problem_obj = ProblemInfo()
    num_photos = int(file.readline())

    vertical_count = 0
    horizontal_count = 0

    print('count vertical and horizontal images')
    for i in range(num_photos):
        info = file.readline().split(' ')
        shape = str(info[0])
        if shape == 'V':
            vertical_count += 1
        elif shape == 'H':
            horizontal_count += 1
        else:
            raise ValueError

    # open file again
    file = open(filename)
    num_photos = int(file.readline())

    max_num_tags = 100
    problem_obj.vertical_tags = np.zeros([vertical_count, max_num_tags])
    problem_obj.horizontal_tags = np.zeros([horizontal_count, max_num_tags])

    problem_obj.vertical_id = np.empty(vertical_count)
    problem_obj.horizontal_id = np.empty(horizontal_count)

    tag_to_label_mapping = dict()
    current_tag_id = 1

    vertical_count = 0
    horizontal_count = 0

    for i in range(num_photos):
        info = file.readline().split(' ')
        shape = str(info[0])
        num_tags = int(info[1])
        tags = info[2:]
        print(info)
        if shape == 'V':
            for j in range(num_tags):
                print(tags[j])
                problem_obj.vertical_tags[vertical_count][j] = \
                    get_or_create_tag_id(tags[j].strip(), tag_to_label_mapping, current_tag_id)
                problem_obj.vertical_id[vertical_count] = i
            vertical_count += 1
        elif shape == 'H':
            for j in range(num_tags):
                print(tags[j])
                problem_obj.horizontal_tags[horizontal_count][j] = \
                    get_or_create_tag_id(tags[j].strip(), tag_to_label_mapping, current_tag_id)
                problem_obj.horizontal_id[horizontal_count] = i
            horizontal_count += 1
        else:
            raise ValueError

    return problem_obj
