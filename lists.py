import random
famous_people = ['john', 'jacob', 'jill']

def guest_list(people):
    for i in people:
        print(f"Hi {i}, you are invited to dinner")

guest_list(famous_people)

def change_guest_list(people):
    busy_person = random.choice(people)
    print(f"Oh no! {busy_person} can't make it!")

    people.remove(busy_person)
    guest_list(people)

change_guest_list(famous_people)

more_people = ['jeremy', 'arthur', 'theo']

def more_guests(people, additions):
    print("I found a bigger table")
    people.insert(0, additions.pop())
    people.insert(int(len(people)/2), additions.pop())
    people.append(additions.pop())
    guest_list(people)

more_guests(famous_people, more_people)

def shrinking_guest_list(people):
    i,j=0,0
    while i<2:
        guest = people.pop()
        print(f"Sorry {guest}. I can't invite you to dinner. {people[i].title()}, you are still invited")
        i+=1

    while j<len(people):
        del people[j]

    print(people)



shrinking_guest_list(famous_people)