import random

print()
def main():
    numbers = [16.2, 75.1, 52.3]
    print(f'numbers {numbers}')

    append_random_numbers(numbers)
    print(f'numbers {numbers}')
    
    
    append_random_numbers(numbers, 3)
    print(f'numbers {numbers}')
    





    words=[]

    append_random_words(words)
    print(f'words {words}')

    append_random_words(words, 5)
    print(f'words {words}')









def append_random_numbers(numbers_list, quantity=1):
    for x in range(quantity):
        quantity=round(random.uniform(0, 100), 1)
        numbers_list.append(quantity)




        

def append_random_words(words_list, quantity=1):
    # words=['baseball', 'football', 'tennis']
    words = ["baseball", "soccer", "tennis", "football", "rugby", "hockey", "volleyball"]

    for x in range(quantity):
        word=random.choice(words)
        words_list.append(word)

    



if __name__ == "__main__":
    main()

print()