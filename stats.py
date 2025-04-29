def get_num_words(text):
    wc = len(text.split())
    return wc

def get_char_count(text):
    dict = {}
    low_text = text.lower()
    for char in low_text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    return dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list = []
    for char, value in dict.items():
        # Create a new dict
        tmp_dict = {"char": char, "num": value }

        # Add the tmp dict to the list
        list.append(tmp_dict)

    list.sort(reverse=True, key=sort_on)
    return list
