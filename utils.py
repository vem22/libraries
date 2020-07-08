def sort_dict(dictionary, reverse = True):
    sorted_tuples = sorted(dictionary.items(), key=lambda kv: kv[1], reverse = reverse)
    sorted_d = dict()
    for elem in sorted_tuples:
        sorted_d[elem[0]] = elem[1]
    return sorted_d
