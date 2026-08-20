import sys
from stats import word_count, char_count, char_dict_to_sorted_list

def get_book_text(path: str) -> str:
    with open(path) as file:
        return file.read()

def print_report(path: str, word_count: int, char_count: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    for char, count in char_count:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


def main():

    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    word_count_value = word_count(get_book_text(path))
    char_count_value = char_dict_to_sorted_list(char_count(get_book_text(path)))

    print_report(path, word_count_value, char_count_value)


main()