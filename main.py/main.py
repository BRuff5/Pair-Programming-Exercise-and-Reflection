def load_wordlist():
    """Load word list."""
    return [
        "apple", "banana", "orange", "grape", "peach", "pear", "plum",
        "dog", "cat", "fish", "bird", "elephant", "tiger", "lion", "monkey",
        "computer", "keyboard", "mouse", "monitor", "printer", "laptop",
        "tablet", "phone", "sun", "moon", "star", "planet", "galaxy", "nebula",
        "comet", "asteroid", "ocean", "river", "lake", "mountain", "valley",
        "desert", "forest", "island", "car", "bicycle", "motorcycle", "bus",
        "train", "plane", "boat", "ship", "book", "pen", "pencil", "paper",
        "notebook", "eraser", "scissors", "glue", "house", "apartment",
        "school", "hospital", "office", "restaurant", "library", "park",
        "music", "movie", "art", "dance", "theater", "poetry", "novel",
        "painting", "football", "basketball", "soccer", "tennis", "golf",
        "baseball", "swimming", "running", "happy", "sad", "angry", "surprised",
        "excited", "relaxed", "bored", "confused", "red", "blue", "green",
        "yellow", "orange", "purple", "pink", "black", "math", "science",
        "history", "english", "art", "music", "physical education", "computer science"
    ]
    
def is_one_edit_away(word1, word2):
    """
    Check if two words are one edit away 
    """
    len1, len2 = len(word1), len(word2)
    
    #More than 1 edit needed
    if abs(len1 - len2) > 1:
        return False
    
    #Find the differences
    i, j, edits = 0, 0, 0
    while i < len1 and j < len2:
        if word1[i] != word2[j]:
            edits += 1
            if edits > 1:
                return False
            if len1 > len2:  # Deletion in word1
                i += 1
            elif len1 < len2:  # Insertion into word1
                j += 1
            else:  # Replacement
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    
    # Account for leftover characters in either word
    if i < len1 or j < len2:
        edits += 1
    return edits == 1

def suggest_spelling(word, wordlist):
    """
    Suggest a correct spelling for the word
    """
    for w in wordlist:
        if is_one_edit_away(word, w):
            return w
    return None

def main():
    """
    Main program spell checker.
    """
    wordlist = load_wordlist()
    print("Spell Checker. Enter '111' to quit.")
    
    while True:
        user_input = input("Enter a word: ").strip()
        
        if user_input == "111":
            print("Terminatinging the program. Goodbye!")
            break
        
        if user_input in wordlist:
            print("The spelling is correct.")
        else:
            suggestion = suggest_spelling(user_input, wordlist)
            if suggestion:
                print(f"The suggested spelling is: {suggestion}")
            else:
                print("No suggestions found.")

# Entry point for the program
if __name__ == "__main__":
    main()