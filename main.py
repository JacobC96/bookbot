def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)

    word_count = count_words(book_text)
    char_count = count_characters(book_text.lower())

    char_list = [{"char": c, "num": count} for c, count in char_count.items()]
    char_list.sort(reverse=True, key=sort_on)

    #print_book_text(book_text)
    print_report(word_count, char_list, book_path)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for c in text:
        if c.isalpha():
            char_count[c] = char_count.get(c, 0) + 1
    return char_count

def sort_on(d):
    return d["num"]

def print_book_text(book_text):
    print(book_text)

def print_report(word_count, char_list, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

main()