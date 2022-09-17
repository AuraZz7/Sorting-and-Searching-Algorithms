import random
import time


def random_number(num_range):
    return random.randint(-num_range, num_range)


def linear_search(target, dataset):
    found = False
    print("Test")

    for i, item in enumerate(dataset):
        if target == item:
            index = i
            found = True
            break

    print(f"{target} was found at index {index}") if found else print(f"{target} not found")


def main():
    choices = {
        1: "Linear search",
        2: "Binary search",
        3: "Insertion sort",
        4: "Bubble sort",
        5: "Merge sort",
        6: "Selection sort",
        7: "Quick sort",
    }

    print("Program containing multiple search / sort algorithms. " +
          "Allows you to also enter a custom dataset or randomly generate one.\n")

    # Everything nested inside a while True loop to allow multiple choices consecutively
    while True:
        input("Press enter to continue.")
        # Checking for custom dataset or randomly generated
        print("Do you want to enter your own dataset, or use a random one?")
        print("1 - Enter custom dataset (advanced)\n2 - Generate random dataset")
        while True:
            try:
                d_choice = int(input("Enter choice: "))
            except TypeError:
                print("Invalid type, must be a number.")
                continue
            else:
                break

            if d_choice not in (1, 2):
                print("Invalid option. Pick a valid option next time.")
                continue

            else:
                break

        if d_choice == 1:
            while True:
                delim = str(input("Specify a delimiter (used to separate each value, eg ',' or ' '):"))
                if len(delim) > 1:
                    print("Must be exactly 1 character.")
                    continue
                else:
                    break

        if d_choice == 2:
            while True:
                try:
                    num_range = int(input("Enter the maximum number you wish to generate: "))
                    length = int(input("Enter the amount of numbers you want to be generated: "))
                except TypeError:
                    print("Must be a whole number. Try again. ")
                    continue
                else:
                    break

                if length <= 0:
                    print("Must generate at least 1 number. Try again.")
                    continue

                elif length >= 100000000:
                    print("Cannot generate that many numbers. Try again.")
                    continue

                else:
                    break

            dataset = [random_number(num_range) for i in range(length)]
            print(f"Generated the following dataset: {dataset}")

        input("Press enter to continue to selecting the algorithm.")
        # Printing the options available
        for key, value in choices.items():
            print(f"{str(key)} - {value}")

        # Getting the user choice
        c = int(input("Enter choice: "))
        # Checking if the choice is valid
        if c in choices.keys():
            # Checking if the choice is a searching algorithm
            if "search" in choices[c]:
                while True:
                    try:
                        target = int(input("Enter target number: ")) if c in (1, 2) else 0
                    except ValueError:
                        print("Invalid input. Enter a number next time.")
                        continue
                    else:
                        break

                linear_search(target, dataset) if c == 1 else print("Test")

            # Checking if the choice is a sorting algorithm
            elif "sort" in choices[c]:
                print("Sorting alg")

        else:
            print("Invalid choice. Enter a correct option next time.")

        time.sleep(1)


if __name__ == '__main__':
    main()
