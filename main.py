from stats import get_num_words, get_num_alphabet, alpha_sort
import sys

if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    
    sys.exit(1)
path= "/mnt/c/Users/Varun/bookbot/"+ sys.argv[1]
num_words = get_num_words(path)
num_alpha = get_num_alphabet(path)
alpha = alpha_sort(num_alpha)

print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{alpha}
============= END ==============""")
