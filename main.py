def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count(text)
    num_chars = count_chars(text)
    report(book_path, num_words, num_chars)

def report(book_path, num_words, num_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    sorted_list = sorted(num_chars)
    for char in sorted_list:
        if char.isalpha() == True:
            print(f"The '{char}' character was found {num_chars[char]} times")
    print("--- End Report ---")

def count(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}
    words = text.lower().split()
    for word in words:
        for char in word:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def get_book_text(path):
     with open(path) as f:
         return f.read()
     
main()