def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    char_dict = {}
    for char in text:
        c = char.lower()
        if c not in char_dict.keys():
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict


def dict_sort_helper(item):
    return item["num"]


def sort_char_counts(count_dict):
    sorted_list = []
    for r in count_dict:
        sorted_list.append({"char": r, "num": count_dict[r]})
    sorted_list.sort(key=dict_sort_helper, reverse=True)
    return sorted_list
