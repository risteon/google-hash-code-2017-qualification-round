from .read_input import parse_input, ProblemInfo
import numpy as np


def combine_vertical_images_random(stuff: ProblemInfo):

    image_slice_indices = stuff.vertical_id
    if stuff.vertical_id.size % 2 != 0:
        image_slice_indices = image_slice_indices[:-1]

    image_slice_index_pairs = np.reshape(image_slice_indices,[-1,2])

    return image_slice_index_pairs

def combine_vertical_images(stuff: ProblemInfo):

    image_is_used = np.zeros(shape=len(stuff.vertical_id),dtype=np.bool)

    num_max_matches = round(stuff.vertical_id.shape[0]/2)

    best_matches = np.zeros(shape=[round(stuff.vertical_id.shape[0]/2), 2], dtype=stuff.vertical_id.dtype)

    for counter, img in enumerate(stuff.vertical_tags):
        if counter < num_max_matches:
            num_matches = 0
            for pair_counter, pair_candidate in enumerate(stuff.vertical_tags):

                # candidate_image has already been used
                if image_is_used[pair_counter] or image_is_used[counter]:
                    continue

                # compute num matching tags
                else:
                    matching_tags = np.setdiff1d(img, pair_candidate)
                    if len(matching_tags) > num_matches:
                        best_matches[counter, :] = np.array([counter, pair_counter])
                        image_is_used[counter] = True

        print(str(counter) + " out of " + str(len(stuff.vertical_tags)) + " done.")

    image_slide_indices_pairs = best_matches

    slide_tag_list = list()
    for matched_pair in best_matches:
        slide_tag_list.append(np.union1d(stuff.vertical_tags[matched_pair[0]],
                                           stuff.vertical_tags[matched_pair[1]]))

    len_list = len(slide_tag_list)
    max_length= max([len(x) for x in slide_tag_list])

    slide_tag_matrix = np.zeros((len_list, max_length),dtype=np.int32)

    for row_idx, tag_list in enumerate(slide_tag_list):
        for col_idx, tag in enumerate(tag_list):
            slide_tag_matrix[row_idx,col_idx] = tag

    return image_slide_indices_pairs, slide_tag_matrix