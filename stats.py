def count_words(text):
    word_count = len(text.split())
    return word_count

def count_characters_dict(text):
    character_dict = {}
    for char in text:
        current_char = char.lower()
        if char.lower() not in character_dict:
            character_dict[current_char] = 1
        else:
            character_dict[current_char] += 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
