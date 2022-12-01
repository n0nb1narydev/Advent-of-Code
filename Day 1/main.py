with open('input.txt') as f:
    calories = f.readlines()
    calories
    for ind, calorie in enumerate(calories):
        # Removes the \n character
        if calorie.__contains__('\n'):
            size = len(calorie)
            calories[ind] = calorie[:size-1]
    calories = ','.join(calories).split(',,')
    elves_list = [i.split(',') for i in calories]
    for i in range(0, len(elves_list)):
        # elves_list[i] = int(elves_list[i])
        for j in range(0, len(elves_list[i])):
            elves_list[i][j] = int(elves_list[i][j])
        
        elves_list[i] = sum(elves_list[i])   

    top_three = sorted(elves_list, reverse=True)[:3]
    print(sum(top_three))

