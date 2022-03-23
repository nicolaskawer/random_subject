# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = ["Solving linear equations", "Finding roots", "Approximations", "Integration"]
    size_people = int(input("first of all enter how many people are in the project: "))
    id_arr = []
    for i in range(size_people):
        print(f'enter the id of people: {i + 1}')
        helper = []
        for j in range(9):
            num_id = int(input(f'enter digit number{j + 1} in your id: '))
            helper.append(num_id)
        id_arr.append(helper)
    sum1 = 0
    for j in range(size_people):
        for i in range(9):
            sum1 += id_arr[j][i]

    result = sum1 % 4
    print("your subject is:", arr[result])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
