# Wordle Project - A 

from pathlib import Path 
# Change 1: something must be initialized here 
import random 

word_file = Path ("words.txt")


def find_Word_file() -> Path:
    if word_file.exists():
        return word_file
    else:
        print("Couldn't find the file :(")
        return Path
        
    

def load_word_bank(filename = "words.txt"):
    with open (filename, "r") as file:
        return [line.strip().lower() for line in file if len (line.strip()) == 5]
    
    word_bank = load_word_bank()
    
def main():
    print("Wrordle Test Project")
    words = load_word_bank(word_file)
    # change 2: needs a way to call a random sample and print it
    sample = random.choice(words)
    print(f"{sample}")
    
if __name__ == "__main__":
    main()
    
