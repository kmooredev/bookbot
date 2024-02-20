def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  char_dict = count_letters(text)
  chars_sorted_list = chars_dict_to_sorted_list(char_dict)

  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} found in the document")
  print()

  for item in chars_sorted_list:
    if not item["char"].isalpha():
      continue
    print(f"The '{item['char']}' character was found {item['num']} times")
  print("--- End report ---")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  return len(text.split())

def count_letters(text):
  dict = {}
  characters = text.lower()
  for char in characters:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1
  return dict

def sort_on(dict):
  return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()