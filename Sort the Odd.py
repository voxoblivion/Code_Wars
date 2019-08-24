# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
def sort_array(source_array):
    # Return a sorted array.
    swap = 0
    changes_occurred = 1
    i_count = 0
    while changes_occurred > 0:
        changes_occurred = 0
        i_count = 0
        for i in source_array:
            i_count += 1
            j_count = 0
            for j in source_array:
                j_count += 1
                if i % 2 == 0 or j % 2 == 0:
                    swap = 0
                    continue
                else:
                    if i < j and (i_count > j_count) and swap == 0:
                        source_array[j_count - 1], source_array[i_count - 1] = source_array[i_count - 1], source_array[j_count - 1]
                        if abs(j_count - i_count) == 1:
                            swap = 1
                        changes_occurred += 1
                    else:
                        swap = 0
    return source_array


print(sort_array([1, 5, 11, 111, 2, 1, 11, 0]))

print(1 % 2)
