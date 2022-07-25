places_to_vist = ['japan', 'china', 'france', 'italy', 'korea']

def print_list(list):
    print(list)
    print(sorted(list))
    print(list)
    print(sorted(list, reverse=True))
    print(list)
    list.reverse()
    print(list)
    list.reverse()
    print(list)
    list.sort(reverse=False)
    print(list)
    list.sort(reverse=True)

print_list(places_to_vist)