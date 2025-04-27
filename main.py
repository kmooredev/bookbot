import sys
from stats import count_words, count_characters_dict, dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def print_report(dict_list, path, word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in dict_list:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    word_count = count_words(text)
    character_count = count_characters_dict(text)
    sorted_list = dict_to_sorted_list(character_count)
    print_report(sorted_list, sys.argv[1], word_count)
main()
