from day6 import str    

test = 'nppdvjthqldpwncqszvftbrmjlhg'
# while processing:
start = 0
stop = 14
letters_checked = 14
length = len(str)

def check_for_repeat(str):
    has_repeated_chars = len(set(str)) != len(str)
    if has_repeated_chars:
        return True

for i in range(length):
    four_letters = str[start:stop]

    if check_for_repeat(four_letters) != True:
        print(f'Letters Checked: {letters_checked}')
        break
    else:
        start+=1
        stop+=1
        letters_checked+=1
        continue
