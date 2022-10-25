import matplotlib.pyplot as plt

plt.title('Collatz Conjecture')
plt.xlabel("Amount of Iterations until 1 is reached")
plt.ylabel("Value of the N")


def collatz(input):
    y = []
    i = 0
    orginalNumber = input
    while input != 1:
        if input % 2 == 0:  # if number is even divide it by 2
            input = input / 2
        else:
            input = (input * 3) + 1 #if number is odd multiply by 3 then + 1
        y.append(input)  # add the number to a list so that it can be plotted
        i += 1
    print(str(orginalNumber) + " fits this pattern")
    # Make a list x and fill it with intergers from 1 to the size of y
    x = []
    for i in range(len(y)): 
        x.append(i+1)
    print(x)
    print(y)
    plt.plot(x, y, label = orginalNumber)

numberBeingSearched = 100000
i=1
while i<=numberBeingSearched: 
    collatz(i)
    i+=1

print("Data Calculated... Now loading graph")

if numberBeingSearched <= 30:   # This is checked because labels other 30 cannot be displayed
    plt.legend()

plt.show()
