def get_boot_text():
    with open("./books/frankenstein.txt") as f:
        file_content = f.read()

    return file_content

def word_count(text):
    wc = len(text.split())
    return wc

def main():
    content = get_boot_text()
    count = word_count(content)
    print(f"{count} words found in the document")

main()
