# Read in the text file DONE
# split all lines into list of 2 items DONE
# go through each list and find the similarity
# add the priority to each pair

new_list = []

# Capitals are these values + 26
priorities = {'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5,'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 
 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

def get_similar(lst):
    for x in lst[0]:
        for y in lst[1]:
            for z in lst[2]:
                if x == y and x == z:
                    return x


def get_priority(value):
    priority = priorities[value.lower()]
    if value.isupper():
        priority += 26
    return priority




with open("day3.txt") as f:
    items = f.readlines()


def divide_into_threes(lst, n):
    final_list = []
    for i in range(0, len(lst), n):
        final_list.append(lst[i:i + n])
    return final_list

for item in items:
    item = item.replace('\n', '')

item_list = divide_into_threes(items, 3)
similar_vals_pri = []
for x in item_list:
    # gets the common value between the two strings
    common_value = get_similar(x)
    #similar_vals_pri.append(common_value)

    # gets the priority number based on the strings value
    priority = get_priority(common_value)
    similar_vals_pri.append(priority)

# part 2 answer
print(sum(similar_vals_pri))

   
    # item_1, item_2 = item[:len(item)//2], item[len(item)//2:]
        
    # # splits the item after removing the \n
    # item_list.append(item_1)
    # item_list.append(item_2)

    # # gets the common value between the two strings
    # common_value = get_similar(item_list)
    # item_list.append(common_value)

    # # gets the priority number based on the strings value
    # priority = get_priority(common_value)
    # item_list.append(priority)

    # # appends this item list into a new list
    # new_list.append(item_list)

    # priority_sum = 0
    # # get sum of priorities
    # for item in new_list:
    #     priority_sum += item[3]

    # part 1 answer
    # print(priority_sum)

