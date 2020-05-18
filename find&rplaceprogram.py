text = input('Enter a text:')
while True:
    target = input('What world/words do you want to find?:')
    if target == 'no':
        break
    def word_find(text, tagret):
        start_range = text.find(target)
        return start_range
    print('Number of world in the text:', word_find(text, target))
    while True:
        validation=input('Do you want to replace the word?:')
        if validation == 'yes':
            replace_word = input('Enter a replaceable word:')
            final_text = text.replace(target, replace_word)
            print(final_text)
            break
        elif validation == 'no':
            break
        else:
            print('Please enter "yes" or "no" as your answer')
            continue


