import os

def string_to_pairs(input_string):
    
    nums = [num for num in input_string.strip("{}").replace('⁻', "-").split(',')]

    # Return every two numbers as a tuple by zip()ing it and then decompressing it back into a list of tuples.
    return list(map(lambda x: (int(x[0]), int(x[1])), zip(*[iter(nums)]*2)))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

string_of_pairs = input("Enter numbers in TI-List format (You can get this from CEmu in the variables tab): ")
list_pairs = string_to_pairs(string_of_pairs)

print(list_pairs)

class Options:
    def __init__(self):
        self.negateX = False
        self.negateY = False
        self.addXandY = False
        self.printDrawer = False
        self.colorVar = "B"
        self.loopVar = "A"

# Ask user for which operation to do by picking a number.
# 1 - Print in Line( format.
# 2 - Change Options
# 3 - Change TI-List
# 4 - Just print the resulting list of tuples.

# Create a new Options object and set it's values
options = Options()

while True:
    clear_terminal()
    print("\nChoose an option (1-6):")
    print("\n1. Print in Line format.")
    print("\n2. Change Options.")
    print("\n3. Change TI-List.")
    print("\n4. Just print the resulting list of tuples.")
    print("\n5. Print Drawer Function.")
    print("\n6. Exit")
    
    try:
        choice = int(input("> "))
        if not(1 <= choice <= 6):
            print("Invalid option, please choose a number between 1 and 6.")
    except ValueError:
        print("Invalid input, please enter a number.")

    if choice == 1:
        # Print in Line( format.
        # Line([First X], [First Y], [Second X], [Second Y], [ColorVar(Defined in options)]
        # A value of -1 in first or second x means a new stroke and that Line shouldnt be printed
        # A value of -1 in first x instead means "{value of first x}->B" should be printed.
        # E.g. [(-1, 11), (2, 10), (5,10), (5,20), (-1, 15), (80, 94), (80, 102)] is outputted as:
        ## 11->B
        ## Line(2, 10, 5, 10, B
        ## Line(5, 10, 5, 20, B
        ## 15->B
        ## Line(80, 94, 80, 102, B
        # If add X and Y is enabled, each x value has a X+ appended, and each y value has a Y+ appended.
        # E.g. [(1, 1), (2, 1)] is outputted as:
        ## Line(X+1, Y+1, X+2, Y+1, B
        # If negate X or negate Y is enabled, respectively, each x value has a X- appended, and each y value has a Y- appended.
        # E.g. [(2, 3), (4, 5)] is outputted as (with negate x):
        ## Line(X-2, Y+3, X-4, Y+5, B
        # E.g. [(2, 3), (4, 5)] is outputted as (with negate y):
        ## Line(X+2, Y-3, X+4, Y-5, B
        # E.g. [(2, 3), (4, 5)] is outputted as (with negate x and negate y):
        ## Line(X-2, Y-3, X-4, Y-5, B
        result = []
        XtoPrint = ("X" + ("-" if options.negateX else "+")) if options.addXandY else ""
        YtoPrint = ("Y" + ("-" if options.negateX else "+")) if options.addXandY else ""
        for i in range(0, len(list_pairs) - 1):
            if list_pairs[i][0] == -1:
                result.append(f"{list_pairs[i][1]}->{options.colorVar}")
            elif list_pairs[i+1][0] != -1:
                result.append(f"Line({XtoPrint}{list_pairs[i][0]},{YtoPrint}{list_pairs[i][1]},{XtoPrint}{list_pairs[i+1][0]},{YtoPrint}{list_pairs[i+1][1]},{options.colorVar})")
        print('\n'.join(result))
        input("Press Enter to continue.")
    elif choice == 2:
        while True:
            clear_terminal()
            print("\nChoose an option to change or to exit (1-5):")
            print("\nOptions:")
            print(f"\n1. Negate X: {str(options.negateX)}")
            print(f"\n2. Negate Y: {str(options.negateY)}")
            print(f"\n3. Add X and Y: {str(options.addXandY)}")
            print(f"\n4. ColorVar: {options.colorVar}")
            print(f"\n5. LoopVar: {options.loopVar}")
            print("\n6. Exit")

            try:
                choice = int(input("> "))
                if not(1 <= choice <= 6):
                    print("Invalid option, please choose a number between 1 and 6.")
            except ValueError:
                print("Invalid input, please choose a number.")

            if choice == 1:
                options.negateX = not options.negateX
            elif choice == 2:
                options.negateY = not options.negateY
            elif choice == 3:
                options.addXandY = not options.addXandY
            elif choice == 4:
                options.colorVar = input("Enter the color variable: ")
            elif choice == 5:
                options.loopVar = input("Enter the loop variable: ")
            elif choice == 6:
                break
    elif choice == 3:
        list_pairs = string_to_pairs(input("Enter numbers in TI-List format (You can get this from CEmu in the variables tab): "))
    elif choice == 4:
        # Just print the resulting list of tuples.
        print(list_pairs)
        input("Press enter to continue.")
    elif choice == 5:
        XtoPrint = ("X" + ("-" if options.negateX else "+")) if options.addXandY else ""
        YtoPrint = ("X" + ("-" if options.negateX else "+")) if options.addXandY else ""
        print(f'''For({options.loopVar},1,dim(L2)-2,2)
			If L2({options.loopVar})=~1:L2({options.loopVar}+1)->{options.colorVar}
			If min({{L2({options.loopVar}),L2({options.loopVar}),L2({options.loopVar}+2),L2({options.loopVar}+2)}}!={{0,~1,0,~1}}):Then
				Line({XtoPrint}L2({options.loopVar}),{YtoPrint}L2({options.loopVar}+1),{XtoPrint}L2({options.loopVar}+2),{YtoPrint}L2({options.loopVar}+3),{options.colorVar}
            End
        End''')
        input("Press enter to continue.")
    elif choice == 6:
        break
clear_terminal()