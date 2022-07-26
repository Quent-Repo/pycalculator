import random

# Press the green button in the gutter to run the script.
def main():
    n = float(input("package weight "))

    if n <= 2:
        x = 125;

        y = n * 1.50 + 20;

        z = n * 4.5
        print(str(x) + " ground Premium")
        print(str(y) + " ground")
        print(str(z) + " drone")
        if y < z and y < x:
            print("ground")
        elif z < y and z < x:
            print("Drone")
        else:
            print("ground Premium")
    elif n <= 6:
        x = 125;
        y = n * 2 + 20;
        z = n * 9
        print(str(x) + " ground Premium")
        print(str(y) + " ground")
        print(str(z) + " drone")
        if y < z and y < x:
            print("ground")
        elif z < y and z < x:
            print("Drone")
        else:
            print("ground Premium")

    elif n <= 10:
        x = 125;
        y = n * 4 + 20;
        z = n * 12
        print(str(x) + " ground Premium")
        print(str(y) + " ground")
        print(str(z) + " drone")
        if y < z and y < x:
            print("ground")
        elif z < y and z < x:
            print("Drone")
        else:
            print("ground Premium")
    else:
        x = 125;
        y = n * 4.75 + 20;
        z = n * 14.25
        print(str(x) + " ground Premium")
        print(str(y) + " ground")
        print(str(z) + " drone")
        if y < z and y < x:
            print("ground")
        elif z < y and z < x:
            print("Drone")
        else:
            print("ground Premium")

main()

'''
 name = input("whats your naem? ")
    question = input("whats your question? ")
    n = random.randint(1, 2)
    if n == 1:
        print(name +' asked '+ question +': '+ "yes")
    else:
        print(name +' asked '+ question +': '+ "no")

print("I have information for the following planets:\n")

    print("   1. Venus   2. Mars    3. Jupiter")
    print("   4. Saturn  5. Uranus  6. Neptune\n")

    weight = 185
    planet = 3

    # Write an if statement below:
    look = int(input("what is the wright of the planet? "))
    look2 = int(input("your weight "))

    if look == 1:
        print(0.91 * look2)
    elif look == 2:
        print(0.38 * look2)
    else:
        print(1.19 * look2)
    print_hi('PyCharm')

    x == 5

    if x <= 2:
        print("This is printed")
    if x <= 4:
        print("This is also printed")
    if x = 5:
        print("Is this printed?")
    if x <= 8:
        print("This might be printed.")'''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
