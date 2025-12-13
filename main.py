from stats import count_words, sort_print
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {count_words()} total words")
    print("--------- Character Count -------")
    sort_print()
    print("============= END ===============")
    



main()
