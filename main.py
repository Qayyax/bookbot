def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_chars_dict(text)
    sorted_char_dict = sort_dict(char_dict)
    print_report(book_path, num_words, sorted_char_dict)


def print_report(book, lenght, dictionary):
    print(f"--- Begin report of {book} ---")
    print(f"{lenght} words found in the document")
    print()
    print()
    for char in dictionary:
        print(f"The '{char}' character was found {dictionary[char]} times")
    print("--- End report ---")




def sort_dict(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_dict)


def get_chars_dict(text):
    chars = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in chars:
                chars[letter] += 1
            else:
                chars[letter] = 1

    return chars


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path, 'r') as file:
        return file.read()


main()
