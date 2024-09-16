import random
def lower():
    lower = input("Enter the lower bound: ")
    return int(lower)

def upper():
    upper = input ("Enter the upper bound: ")
    return int(upper)



def boundGenerator(lower, upper):
    lower = lower
    upper = upper + 1
    bound = random.randrange(lower, upper)

    return bound


lower = lower()
upper = upper()
bound = boundGenerator(lower, upper)
print(bound)