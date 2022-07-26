magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print (magician)

#the above defines a loop. It tells python to associate the variable magician with the first value from the magicians list. Then print the name of the magician. Repeat until we've iterated over the entire list.

# list function converts the output of the range to a list of numbers
# range returns numbers between the start and end - 1.
def list_range(start, end):
    numbers = list(range(start, end))
    print(numbers)

list_range(0, 10)


def list_range_skip_2(start, end):
    numbers = list(range(start, end, 2))
    print(numbers)

list_range_skip_2(0, 10)
# passing the third argument to range, tells python to add 2 to the current number. It does this repeatedly until it reaches or passes the end value. 

# find the square of each integer in range 1 - 10 and place them in a list
def square_range(start, end):
    list = []
    for i in range(1, 11):
        list.append(i**2)
    
    print(list)

def methods_for_lists_of_numbers(list):
    print(max(list), min(list), sum(list))

methods_for_lists_of_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
