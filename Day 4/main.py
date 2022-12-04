cleaned_list = []
overlap_count = 0

# read in the text file
with open('day4.txt') as f:
    pairs = f.readlines()

def check_in_range_one(pair):
    for i in range(int(pair[0][0]), int(pair[0][1])+1):
        # if i not in range(int(pair[1][0]), int(pair[1][1])+1):
        #     return False
    # return True
        if i in range(int(pair[1][0]), int(pair[1][1])+1):
            return True

def check_in_range_two(pair):
    for i in range(int(pair[1][0]), int(pair[1][1])+1):
    #     if i not in range(int(pair[0][0]), int(pair[0][1])+1):
    #         return False
    # return True
        if i in range(int(pair[0][0]), int(pair[0][1])+1):
            return True



# go through each pair and get the min and max
for pair in pairs:
    pair = pair.replace('\n', '').split(',')
    pair = [pair[0].split('-'), pair[1].split('-')]

    # check if either are in range of eachother
    if check_in_range_one(pair) or check_in_range_two(pair):
        overlap_count += 1


print(overlap_count)
# 462 -> correct

