import sys
from stats import get_num_words, get_num_chars, sort_char_counts


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    text = get_book_text(file)
    num_words = get_num_words(text)
    d = get_num_chars(text)
    ds = sort_char_counts(d)
    print("=" * 10, end="")
    print(" BOOKBOT ", end="")
    print("=" * 10)
    print(f"Analyzing book found at {file}...")
    print("-" * 10, end="")
    print(" Word Count ", end="")
    print("-" * 10)
    print(f"Found {num_words} total words")
    print("-" * 10, end="")
    print(" Character Count ", end="")
    print("-" * 10)
    for e in ds:
        if e["char"].isalpha():
            print(f"{e["char"]}: {e["num"]}")
    print("=" * 10, end="")
    print(" END ", end="")
    print("=" * 10)


if __name__ == "__main__":
    main()
