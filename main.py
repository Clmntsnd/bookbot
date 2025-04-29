import sys
from stats import get_num_words, sort_dict
from stats import get_char_count

def get_boot_text(path):
    with open(path) as f:
        file_content = f.read()

    return file_content

def generate_report(path, count, list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def main():
    # path = "books/frankenstein.txt"
    # test = "books/test.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the argument
    path = sys.argv[1]
    content = get_boot_text(path)

    count = get_num_words(content)
    char_count = get_char_count(content)
    sorted_list = sort_dict(char_count)
    generate_report(path, count, sorted_list)

main()
