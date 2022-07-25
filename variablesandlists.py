x, y, z = ['Sean', 'Vincent', 'Balayan']
print (f"{x} {y} {z}")


friends = ['john', 'jacob', 'jeremy']
def personalize_message(names):
    x = 0
    for i in names:
        print(f"Hey, {i} \n You're {x} in my list")
        x+=1
        # print (f"Hey, {names[i]}! \n You're an ass!")

# personalize_message(friends)


transportation=['motorcycle', 'car', 'airplane', 'bike', 'bus', 'hot air balloon']
cars = ['audi', 'lexus', 'toyota', 'dodge']

def print_statements(transports, vehicles):
    i, j = 0, 0
    while i<len(transports):
        print (f"I would like to own a {vehicles[j]} {transports[i]}")
        i+= 1
        if j == len(vehicles)-1: j = 0
        else: j+=1

print_statements(transportation, cars)
