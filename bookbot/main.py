from stats import pretty_print
import sys

def main():
    arguments = sys.argv
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = arguments[1]
    pretty_print(path)

if __name__ == '__main__':
    main()