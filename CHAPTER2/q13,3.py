import random
import string

while True:
    random_letter = random.choice(string.ascii_lowercase)
    print(random_letter, end='')
    
    if random_letter == 'k':
        next_letter = random.choice(string.ascii_lowercase)
        print(next_letter, end='')
        
        if next_letter == 'm':
            break

