import random


words = {
    'eat': ['tea', 'ate'],
    'listen': ['silent', 'enlist'],
    'rat': ['tar', 'art'],
    'god': ['dog'],
    'evil':['vile', 'veil'],
    'ten': ['net'],
    'tik': ['kit'],
    
    
}

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

    
def play_game():
    print("Welcome to 'Guess the Anagrams!'")

    original_word = random.choice(list(words.keys()))
    scrambled_word = scramble_word(original_word)

    print(f"Your scrambled word is: {scrambled_word}")

    attempts = 3
    while attempts > 0:
        guess = input("Guess the correct word: ").strip().lower()
        
        if guess == original_word or guess in words[original_word]:
            print(f"Congratulations! '{guess}' is the correct word!")
            break
        
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Game Over! The correct word was: '{original_word}'.")

play_game()
