# 
# Takes a number list(order) and desired amount.  Keeps desired amount of numbers and deletes duplicates exceeding the desired amount(num)
# 
def child(order, num):
    ordered = list()
    for n in order:
        if ordered.count(n) < num:
            new.append(n)
    ordered.sort()
    print(ordered)
test1 = [2,2,3,4,5,5,7,1,1,1]
child(test1 , 1)

# 
# Counts the number of specific letters in a string and returns the keys/values of each in string
# 
def letter_counter(string):
    count = dict()
    for letter in string:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    print(count)
test2 = input("Enter text here: ")
letter_counter(test2)

# 
# Create a list of all numbers between a range of two given numbers
# 
def range_finder(a,b):
    nums = list()
    for i in range(a,(b+1)):
        nums.append(i)
    print(nums)

range_finder(2,8)

# 
# Given a list of scores, if your score is greater than the average, return True else False
# 

def avg_scores(scores, your_score):
    avg = sum(scores)/len(scores)
    if your_score > avg:
        print(True)
    else:
        print(False)

test3 = [99,55,34,77,78,89,67,100,44,23,20]
score = int(input("Enter your score: "))
avg_scores(test3, score)