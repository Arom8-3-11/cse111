Concepts
Here are the Python programming concepts and topics that you should learn during this lesson:

Lists
A Python program can store many values in a list. Lists are mutable, meaning they can be changed after they are created. Each value in a list is called an element and is stored at a unique index. An index is always an integer and determines where an element is stored in a list. The first index of a Python list is always zero (0). The following diagram shows a list that contains five strings. The diagram shows both the elements and the indexes of the list. Notice that each index is a unique integer, and that the first index is zero.

elements	"yellow"	"red"	"green"	"yellow"	"blue"
indexes	[0]	[1]	[2]	[3]	[4]
← list length is 5 →
In a Python program, we can create a list by using square brackets ([ and ]). We can determine the number of items in a list by calling the built-in len function. We can retrieve an item from a list and replace an item in a list using square brackets ([ and ]) and an index. Example 1 contains a program that creates a list, prints the length of the list, retrieves and prints one item from the list, changes one item in the list, and then prints the entire list.







# Example 1

def main():
    # Create a list that contains five strings.
    colors = ["yellow", "red", "green", "yellow", "blue"]

    # Call the built-in len function
    # and print the length of the list.
    length = len(colors)
    print(f"Number of elements: {length}")

    # Print the element that is stored
    # at index 2 in the colors list.
    print(colors[2])

    # Change the element that is stored at
    # index 3 from "yellow" to "purple".
    colors[3] = "purple"

    # Print the entire colors list.
    print(colors)


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_1.py
Number of elements: 5
green
['yellow', 'red', 'green', 'purple', 'blue']
We can add an item to a list by using the insert and append methods. We can determine if an element is in a list by using the Python membership operator, which is the keyword in. We can find the index of an item within a list by using the index method. We can remove an item from a list by using the pop and remove methods. Example 2 shows how to create a list and add, find, and remove items from a list.



minerals=[word, 555]

len(minerals)







# Example 2

def main():
    # Create an empty list that will hold fabric names.
    fabrics = []

    # Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")

    # Insert an element at the beginning of the fabrics list.
    fabrics.insert(0, "chiffon")
    print(fabrics)

    # Determine if gingham is in the fabrics list.
    if "gingham" in fabrics:
        print("gingham is in the list.")
    else:
        print("gingham is NOT in the list.")

    # Get the index where velvet is stored in the fabrics list.
    i = fabrics.index("velvet")

    # Replace velvet with taffeta.
    fabrics[i] = "taffeta"

    # Remove the last element from the fabrics list.
    fabrics.pop()

    # Remove denim from the fabrics list.
    fabrics.remove("denim")

    # Get the length of the fabrics list and print it.
    n = len(fabrics)
    print(f"The fabrics list contains {n} elements.")
    print(fabrics)


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_2.py
['chiffon', 'velvet', 'denim', 'gingham']
gingham is in the list.
The fabrics list contains 2 elements.
['chiffon', 'taffeta']
The lists in examples 1 and 2 store strings. Of course, it is possible to store numbers in a list, too. In fact, Python allows a program to store any data type in a list, including other lists.

Repetition
A programmer can cause a computer to repeat a group of statements by writing for and while loops.

for loop
A for loop iterates over a sequence, such as a list. This means a for loop causes the computer to repeatedly execute the statements in the body of the for loop, once for each element in the sequence. In example 3, consider the list of colors at line 5 and the for loop at lines 8–9. Notice how the for loop causes the computer to repeat line 9 once for each element in the colors list. Of course, the code in the body of a loop can do much more with each element than simply print it.








# Example 3

def main():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]

    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_3.py
red
orange
yellow
green
blue
Notice in example 3 at lines 8–9 that just like if statements in Python, the body of a loop starts and ends with indentation.

range function
The Python built-in range function creates and returns a sequence of numbers. The range function accepts one, two, or three parameters as shown in example 4 and its output. Many programmers use the range function in a for loop to cause the computer to repeat code once for each number in a range of numbers. Example 4 shows four for loops that iterate over a range of numbers.










# Example 4

def main():
    # Count from zero to nine by one.
    for i in range(10):
        print(i)
    print()

    # Count from five to nine by one.
    for i in range(5, 10):
        print(i)
    print()

    # Count from zero to eight by two.
    for i in range(0, 10, 2):
        print(i)
    print()

    # Count from 100 down to 70 by three.
    for i in range(100, 69, -3):
        print(i)


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_4.py
0
1
2
⋮
8
9

5
6
7
8
9

0
2
4
6
8

100
97
94
 ⋮
73
70
In example 5 at lines 8–9 and lines 15–17, there are two for loops. Both loops print each element from a list named colors. The first loop iterates over the elements in the colors list. The second loop uses the built-in len and range functions to iterate over the indexes of the colors list. Which style of for loop do you prefer to read and write? Most programmers prefer to write a loop like the one at lines 8–9 because it is simpler than the one at lines 15–17.







# Example 5

def main():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]

    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)

    print()

    # Use a different for loop to
    # print each element in the list.
    for i in range(len(colors)):
        # Use the index i to retrieve
        # an element from the list.
        color = colors[i]

        print(color)


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_5.py
red
orange
yellow
green
blue

red
orange
yellow
green
blue
In the previous example, the code in the body of both for loops is very short and simply prints one element from the list each time through the loop. However, you can write as many lines of code as you need in the body of a loop to repeatedly perform all sorts of computations for each element in a list.

break statement
A break statement causes a loop to end early. In example 6 at lines 8–12, there is a for loop that asks the user to input ten numbers one at a time. However, the loop will terminate early if the user enters a zero (0) because of the if statement and break statement at lines 10 and 11.














# Example 6

def main():
    sum = 0

    # Get ten or fewer numbers from the user and
    # add them together.
    for i in range(10):
        number = float(input("Please enter a number: "))
        if number == 0:
            break
        sum += number

    # Print the sum of the numbers for the user to see.
    print(f"sum: {sum}")


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_6.py
Please enter a number: 6
Please enter a number: 4
Please enter a number: -2
Please enter a number: 0
sum: 8.0
while loop
A while loop is more flexible than a for loop and repeats while some condition is true. Imagine that we need a function to compare the contents of two lists? Can we use a loop to compare the contents of two lists? Example 7 contains a while loop at lines 35–46 with an if statement at line 42 that finds the first index where two lists differ.

















# Example 7

def main():
    list1 = ["red", "orange", "yellow", "green", "blue"]
    list2 = ["red", "orange", "green", "green", "blue"]

    index = compare_lists(list1, list2)
    if index == -1:
        print("The contents of list1 and list2 are equal")
    else:
        print(f"list1 and list2 differ at index {index}")


def compare_lists(list1, list2):
    """Compare the contents of two lists. If the contents
    of the two lists are not equal, return the index of
    the first difference. If the contents of the two lists
    are equal, return -1.

    Parameters
        list1: a list
        list2: another list
    Return: an index or -1
    """
    # Get the length of the shortest list.
    length1 = len(list1)
    length2 = len(list2)
    limit = min(length1, length2)

    # Begin at the first index (0) and repeat until the
    # computer finds two elements that are not equal or
    # until the computer reaches the end of the shortest
    # list, whichever comes first.
    i = 0
    while i < limit:
        # Retrieve one element from each list.
        element1 = list1[i]
        element2 = list2[i]

        # If the two elements are not
        # equal, quit the while loop.
        if element1 != element2:
            break

        # Add one to the index variable.
        i += 1

    # If the length of both lists are equal and the
    # computer verified that all elements are equal,
    # set i to -1 to indicate that the contents of
    # the two lists are equal.
    if length1 == length2 == i:
        i = -1

    return i


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_7.py
list1 and list2 differ at index 2
Compound Lists
A compound list is a list that contains other lists. Compound lists are used to store lots of related data. Example 8 shows how to create a compound list, retrieve one inner list from the compound list, and retrieve an individual number from the inner list.
















# Example 8

def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3

    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]

    # Retrieve one inner list from the compound list.
    one_tree = apple_tree_data[2]

    # Retrieve one value from the inner list.
    height = one_tree[HEIGHT_INDEX]

    # Print the tree's height.
    print(f"height: {height}")


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_8.py
height: 2.3
Example 9 shows how to process all elements in a compound list. The for loop at line 24 causes the computer to repeat lines 24–34 once for each inner list that is inside the compound list named apple_tree_data. Line 28 retrieves the fruit amount from one inner list and then line 34 adds one fruit amount to the total fruit amount.

















# Example 9

def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3

    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]

    total_fruit_amount = 0

    # This loop will repeat once for each inner list
    # in the apple_tree_data compound list.
    for inner_list in apple_tree_data:

        # Retrieve the fruit amount from
        # the current inner list.
        fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]

        # Print the fruit amount for the current tree.
        print(fruit_amount)

        # Add the current fruit amount to the total.
        total_fruit_amount += fruit_amount

    # Print the total fruit amount.
    print(f"Total fruit amount: {total_fruit_amount:.1f}")


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_9.py
70.5
81.3
62.7
42.1
Total fruit amount: 256.6
Values and References
In a Python program, the computer assigns values to variables differently based on their data type. Consider the small program in example 10 and the output of that program. The program in example 10 contains two integer variables named x and y. The program in example 10 does the following:

The statement at line 4 stores the value 17 into the variable x.
Line 5 copies the value that is in the variable x into the variable y.
Line 6 prints the values of x and y which are both 17.
Line 7 adds one to the value of x, making its value 18 instead of 17.
Line 8 prints the values of x and y again. The value of x was changed to 18. The value of y remained unchanged.
Why does line 7 (x += 1) change the value of x but not change the value of y ? Because line 5 copies the value that was in x into y. In other words, x and y are two separate variables, each with its own value.
















# Example 10

def main():
    x = 17
    y = x
    print(f"Before changing x: x {x}  y {y}")
    x += 1
    print(f"After changing x:  x {x}  y {y}")

# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_10.py
Before changing x: x 17  y 17
After changing x:  x 18  y 17
Example 11 shows a small Python program that contains two variables named lx and ly that each refer to a list. This program is similar to the previous program, but it has two lists instead of two integers. From the output of example 11, we see there is a big difference between the way a Python program assigns integers and the way it assigns lists. The program in example 11 does the following:

The statement at line 4 creates a list and stores a reference to that list in the variable lx.
Line 5 copies the reference in the variable lx into the variable ly. Line 5 does not create a copy of the list but instead causes both the variables lx and ly to refer to the same list.
Line 6 prints the values of lx and ly. Notice that their values are the same as we expect them to be because of line 5.
Line 7 appends the number 5 onto the list lx.
Line 8 prints the values of lx and ly again. Notice in the output that when lx and ly are printed the second time, it appears that the number 5 was appended to both lists.
Why does it appear that appending the number 5 onto lx also appends the number 5 onto ly ? Because lx and ly refer to the same list. There is really only one list with two references to that list. Because lx and ly refer to the same list, a change to the list through variable lx can be seen through variable ly.















# Example 11

def main():
    lx = [7, -2]
    ly = lx
    print(f"Before changing lx: lx {lx}  ly {ly}")
    lx.append(5)
    print(f"After changing lx:  lx {lx}  ly {ly}")

# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_11.py
Before changing lx: lx [7, -2]  ly [7, -2]
After changing lx:  lx [7, -2, 5]  ly [7, -2, 5]
From examples 10 and 11, we learn that when a computer executes a Python statement to assign the value of a boolean, integer, or float variable to another variable (y = x), the computer copies the value of one variable into the other. However, when a computer executes a Python statement to assign the value of a list variable to another variable (ly = lx), the computer does not copy the value but instead copies the reference so that both variables refer to the same list in memory.

Pass by Value and Pass by Reference
The fact that the computer copies the value of some data types (boolean, integer, float) and copies the reference for other data types (list and other large data types) has important implications for passing arguments into functions. Consider the Python program in example 12 with two functions named main and modify_args. The program in example 12 does the following:

The statement at line 5 assigns the value 5 to a variable named x.
Line 6 assigns a list to a variable named lx.
Line 7 prints the values of x and lx before they are passed to the modify_args function.
Line 11 calls the modify_args function and passes x and lx to that function.
Within the modify_args function, line 28 changes the value of the parameter n by adding one to it, and line 29 changes the value of the parameter alist by appending the number 4 onto it.
Line 13 prints the values of x and lx after they were passed to the modify_args function. Notice in the output below that the value of x was not changed by the modify_args function. However, the value of lx was changed by the modify_args function.




















# Example 12

def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"After calling modify_args():  x {x}  lx {lx}")


def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1
    alist.append(4)

    print(f"   After changing n and alist:  n {n}  alist {alist}")


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_12.py
main()
Before calling modify_args(): x 5  lx [7, -2]
    modify_args(n, alist)
    Before changing n and alist: n 5  alist [7, -2]
    After changing n and alist:  n 6  alist [7, -2, 4]
After calling modify_args():  x 5  lx [7, -2, 4]
From the output of example 12, we see that modifying an integer parameter changes the integer within the called function only. However, modifying a list parameter changes the list within the called function and within the calling function. Why? Because when a computer passes a boolean, integer, or float variable to a function, the computer copies the value of that variable into the parameter of the called function. Copying the value of an argument into a parameter is known as pass by value. However, when a computer passes a list variable to a function, the computer copies the reference so that the original variable and the parameter both refer to the same list in memory. Copying the reference of an argument into a parameter is known as pass by reference.

Rationale for Pass by Reference
Why are booleans and numbers passed to a function by value and lists are passed to a function by reference? To understand the answer to this question, consider the work a computer would have to do if lists were passed by value.

When a computer passes a number (or boolean) variable to a function, the number is passed by value which means the computer copies the value of the number variable into the parameter of the called function. This works well for numbers because each number variable occupies a small amount of the computer’s memory. Making a copy of a number is fast, and the copy uses a small amount of memory.

However, a list may contain millions of elements and therefore occupy a large amount of the computer’s memory. If lists were passed by value to a function, the computer would have to make a copy of a list each time it is passed to a function. If a list is large, copying the list takes a relatively long time and uses a lot of the computer’s memory for the copy. Therefore, to make programs fast and use less memory, lists (and other large data types) are passed to a function by reference.

Tutorials
If the concepts in this preparation content seem confusing to you, reading these tutorials may help you better understand the concepts.

Lists in Python
More on Lists
Python "for" Loops
Python "while" Loops
Summary
During this lesson, you are learning how to store many values in a list. Each element in a list is stored at a unique index. Each index is an integer, and the first index in a Python list is always zero (0). The built-in len function will return the number of elements stored in a list. The index of the last element in a Python list is always one less than the length of the list. To retrieve or store one element in a list, you can use the square brackets ([ and ]) and an index. To process all the elements in a list, you can write a for loop. A compound list is a list that stores smaller lists.

During this lesson, you are also learning the difference between passing arguments into a function by value and by reference. Numbers are passed into a function by value, meaning that the computer copies the number from an argument into a parameter. Lists are passed into a function by reference, meaning the computer does not make a copy of a list argument but instead passes a reference to the list into a called function. Because lists are passed by reference, if a called function changes a list that is a parameter, that function is not changing a copy of the list but instead is changing the original list from the calling function.

Checkpoint
Purpose
Reinforce your understanding that numbers are passed to a function by value and lists are passed to a function by reference.

Problem Statement
Within a Python program, when a number is passed as an argument to a function, the computer copies the number from the argument into the parameter. In other words, the parameter gets a copy of the value that is in the argument. However, when a list is passed as an argument to a function, the computer does not copy the list. Instead, the computer copies a reference to the list into the parameter. This means the argument and parameter refer to the same list. If a called function changes a list that was passed to the function, this will change the list in both the calling and called functions because both the argument and parameter refer to the same list.

Assignment
During this checkpoint, you will examine and run a Python program that passes both a number and a list to function. Do the following:

Download and save the pass_args.py Python file and then open it in VS Code.
Run the pass_args.py program on your computer. Examine the code and the output and answer the following three questions:
In main, there are two local variables named x and lx. At line 14, both of these local variables are passed to the modify_args function. After the call to modify_args finished, which of main’s two local variables did the modify_args function change?
    x
    # lx
    both of them
    neither of them
Why is the modify_args function NOT able to change main’s local variable x?
    # Because x is a number and therefore passed to a function by value
    Because x is a list and therefore passed to a function by reference
Why is the modify_args function able to change main’s local variable lx?
    Because lx is a number and therefore passed to a function by value
    # Because lx is a list and therefore passed to a function by reference
Sample Run
> python pass_args.py
  main()
      Before calling modify_args(): x 5  lx [7, -2]
      modify_args(n, alist)
          Before changing n and alist: n 5  alist [7, -2]
          After changing n and alist:  n 6  alist [7, -2, 4]
      After calling modify_args():  x 5  lx [7, -2, 4]
              











































































Concepts
Here are the Python programming concepts and topics that you should learn during this lesson:

Dictionaries
A Python program can store many items in a dictionary. Each item in a dictionary is a key value pair. Each key within a dictionary must be unique. In other words, no key can appear more than once in a dictionary. Values within a dictionary do not have to be unique. Dictionaries are mutable, meaning they can be changed after they are created. Dictionaries were invented to enable computers to find items quickly.

The following table represents a dictionary that contains five items (five key value pairs) Notice that each of the keys is unique.

items	
keys	values	
42-039-4736	Clint Huish	↑
61-315-0160	Amelia Davis	|
10-450-1203	Ana Soares	5 items
75-421-2310	Abdul Ali	|
07-103-5621	Amelia Davis	↓
We can create a dictionary by using curly braces ({ and }). We can add an item to a dictionary and find an item in a dictionary by using square brackets ([ and ]) and a key. The following code example shows how to create a dictionary, add an item, remove an item, and find an item in a dictionary.


















# Example 1

def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students_dict = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }

    # Add an item to the dictionary.
    students_dict["81-298-9238"] = "Sama Patel"

    # Remove an item from the dictionary.
    students_dict.pop("61-315-0160")

    # Get the number of items in the dictionary.
    length = len(students_dict)
    print(f"length: {length}")

    # Print the entire dictionary.
    print(students_dict)
    print()

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Check if the student ID is in the dictionary.
    if id in students_dict:

        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        name = students_dict[id]

        # Print the student's name.
        print(name)

    else:
        print("No such student")


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_1.py
length: 5
{'42-039-4736': 'Clint Huish', '10-450-1203': 'Ana Soares',
'75-421-2310': 'Abdul Ali', '07-103-5621': 'Amelia Davis',
'81-298-9238': 'Sama Patel'}

Enter a student ID: 10-450-1203
Ana Soares
Line 15 in the previous code example, adds an item to the dictionary. To add an item to an existing dictionary, write code that follows this template:


    dictionary_name[key] = value
Notice that line 15 follows this template.

Line 32 in the previous code example, uses the Python membership operator, which is the keyword in, to check if a key is stored in a dictionary. To check if a key is stored in a dictionary, write code that follows this template:


    if key in dictionary_name:
Notice that line 32 follows this template.

Line 36 in the previous code example, finds a key and retrieves its corresponding value from a dictionary. To find a key and retrieve its corresponding value, write code that follows this template:


    value = dictionary_name[key]
Notice that line 36 follows this template.

Compound Values
A simple value is a value that doesn’t contain parts, such as an integer. A compound value is a value that has parts, such as a list. In example 1 above, the students dictionary has simple keys and values. Each key is a single string, and each value is a single string. It is possible to store compound values in a dictionary. Example 2 shows a students dictionary where each value is a Python list. Because each list contains multiple parts, we say that the dictionary stores compound values.

















# Example 2

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }

Finding One Item
The reason Python dictionaries were developed is to make finding items easy and fast. As explained in example 1, to find an item in a dictionary, a programmer needs to write just one line of code that follows this template:


    value = dictionary_name[key]
That one line of code will cause the computer to search the dictionary until it finds the key. Then the computer will return the value that corresponds to the key. Some programmers forget how easy it is to find items in a dictionary, and when asked to write code to find an item, they write complex code like lines 24–28 in example 3.















# Example 3

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # This is a difficult and slow way to find an item in a
    # dictionary. Don't write code like this to find an item
    # in a dictionary!

    # For each item in the dictionary, check if
    # its key is the same as the variable id.
    student = None
    for key, value in students_dict.items(): # Bad example!
        if key == id:                        # Don't use a loop
            student = value                  # like this to find an
            break                            # item in a dictionary.
Compare the for loop at lines 24–28 in the previous example to this one line of code.


    value = students_dict[id]
Clearly, writing one line of code is easier for a programmer than writing the for loop. Not only is the one line of code easier to write, but the computer will execute it much, much faster than the for loop. Therefore, when you need to write code to find an item in a dictionary, don’t write a loop. Instead, write one line of code that uses the square brackets ([ and ]) and a key to find an item. Example 4 shows the correct way to find an item in a dictionary.














# Example 4

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Check if the student ID is in the dictionary.
    if id in students_dict:

        # Find the student ID in the dictionary and
        # retrieve the corresponding value, which is a list.
        value = students_dict[id]

        # Retrieve the student's given name (first name) and
        # surname (last name or family name) from the list.
        given_name = value[GIVEN_NAME_INDEX]
        surname = value[SURNAME_INDEX]

        # Print the student's name.
        print(f"{given_name} {surname}")

    else:
        print("No such student")


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_4.py
Enter a student ID: 61-315-0160
Amelia Davis

> python example_4.py
Enter a student ID: 25-143-1202
No such student
Processing All Items
Occasionally, you may need to write a program that processes all the items in a dictionary. Processing all the items in a dictionary is different than finding one item in a dictionary. Processing all the items is done using a for loop and the dict.items() method as shown in example 5 on line 25.


















# Example 5

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    total = 0

    # For each item in the list add the number
    # of credits that the student has earned.
    for item in students_dict.items():
        key = item[0]
        value = item[1]

        # Retrieve the number of credits from the value list.
        credits = value[CREDITS_INDEX]

        # Add the number of credits to the total.
        total += credits

    print(f"Total credits earned by all students: {total}")

# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_5.py
Total credits earned by all students: 47
As with all the example code in CSE 111, example 5 contains working Python code. Even though the code works, we can combine lines 25–27 into a single line of code by using a Python shortcut called unpacking. Instead of writing lines 25–27, like this:


    for item in students_dict.items():
        key = item[0]
        value = item[1]
We can write one line of code that combines the three lines of code and unpacks the item in the for statement like this:


    for key, value in students_dict.items():
Example 6 contains the same code as example 5 except example 6 uses the Python unpacking shortcut at line 25.





















# Example 6

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    total = 0

    # For each item in the list add the number
    # of credits that the student has earned.
    for key, value in students_dict.items():

        # Retrieve the number of credits from the value list.
        credits = value[CREDITS_INDEX]

        # Add the number of credits to the total.
        total += credits

    print(f"Total credits earned by all students: {total}")


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_6.py
Total credits earned by all students: 47
Dictionaries Are Similar to Lists
Dictionaries are similar to lists in a few ways. The following table compares lists to dictionaries and categorizes their traits as same, similar, or different.

Lists	Dictionaries
Similar	A list can store many elements.	A dictionary can store many items.
Different	Each element in a list does not have to be unique.	Each item in a dictionary is a key value pair. Each key must be unique within a dictionary. Each value does not have to be unique.
Lists were designed for efficiently storing elements. Lists use less memory than dictionaries. However, finding an element in a list is relatively slow.	Dictionaries were designed for quickly finding items. Finding an item in a dictionary is fast. However, dictionaries use more memory than lists.
A programmer uses square brackets ([ and ]) to create a list.	A programmer uses curly braces ({ and }) to create a dictionary.

    # Create a list of cities.
    cities_list = ["Delhi", "Lagos", "Dallas"]

    # Create a dictionary of people.
    people_dict = {
        "P203": "Ignacio Torres",
        "P445": "Whitney Nelson",
        "P128": "Yasmin Li"
    }
Same	Lists are mutable, which means a program can add and remove elements after a list is created.	Dictionaries are mutable, which means a program can add and remove items after a dictionary is created.
Different	A programmer calls the insert and append methods to add an element to a list.	A programmer uses square brackets ([ and ]) to add an item to a dictionary.

    # Add two cities to the cities list.
    cities_list.insert(1, "Paris")
    cities_list.append("Tokyo")

    # Add two people to the people dictionary.
    people_dict["P205"] = "Liam Myers"
    people_dict["P317"] = "Davina Patel"
Similar	To cause the computer to check whether an element is in a list, a programmer uses the in keyword.	To cause the computer to check whether a key is in a dictionary, a programmer uses the in keyword.

    if "Paris" in cities_list:
        print("Paris is in the list of cities.")

    if "P203" in people_dict:
        print("P203 is in the dictionary of people.")
Different	A programmer uses the index method to find an element in a list.	A programmer uses square brackets ([ and ]) and a key to find an item in a list.

    # Find Dallas in the cities list.
    index = cities_list.index("Dallas")

    # Find person P128 in the people dictionary.
    person_name = people_dict["P128"]
Similar	A programmer uses square brackets ([ and ]) and an index to retrieve an element from a list.	A programmer uses square brackets ([ and ]) and a key to retrieve a value from a dictionary.

    # Retrieve the element stored at
    # index 2 in the cities list.
    city_name = cities_list[2]

    # Find person P128 in the people dictionary
    # and retrieve the corresponding value.
    person_name = people_dict["P128"]
A programmer uses square brackets ([ and ]) and an index to replace an element in a list.	A programmer uses square brackets ([ and ]) and a key to replace a value in a dictionary.

    # Change the city name at index 2 to London.
    cities_list[2] = "London"

    # Change the name of person P205 to Finn Meyers.
    people_dict["P205"] = "Finn Myers"
Similar	A programmer can use a for loop to process all the elements in a list.	A programmer can use a for loop to process all the items in a dictionary.

    # Process all the elements in the cities list.
    for city_name in cities_list:
        print(city_name)

    # Process all the items in the people dictionary.
    for person_key, person_name in people_dict.items():
        print(person_name)
Same	A programmer uses the pop method to remove an element from a list.	A programmer uses the pop method to remove an item from a dictionary.

    # Remove the element at index 3
    # from the cities list.
    cities_list.pop(3)

    # Remove the key "P203" and its
    # value from the people dictionary.
    people_dict.pop("P203")
Lists are passed by reference into a function.	Dictionaries are passed by reference into a function.

    # Call the draw_chart function and pass
    # the citites list to that function.
    draw_chart(cities_list)

    # Call the hire_people function and pass
    # the people dictionary to that function.
    hire_people(people_dict)
Converting between Lists and Dictionaries
It is possible to convert two lists into a dictionary by using the built-in zip and dict functions. The contents of the first list will become the keys in the dictionary, and the contents of the second list will become the values. This implies that the two lists must have the same length, and the elements in the first list must be unique because keys in a dictionary must be unique.

It is also possible to convert a dictionary into two lists by using the keys and values methods and the built-in list function. The following code example starts with two lists, converts them into a dictionary, and then converts the dictionary into two lists.


















# Example 7

def main():
    # Create a list that contains five student numbers.
    numbers_list = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]

    # Create a list that contains five student names.
    names_list = ["Clint Huish", "Amelia Davis",
            "Ana Soares", "Abdul Ali", "Amelia Davis"]

    # Convert the numbers and names lists into a dictionary.
    student_dict = dict(zip(numbers_list, names_list))

    # Print the entire student dictionary.
    print("Dictionary:", student_dict)
    print()

    # Convert the student dictionary into
    # two lists named keys and values.
    keys = list(student_dict.keys())
    values = list(student_dict.values())

    # Print both lists.
    print("Keys:", keys)
    print()
    print("Values:", values)


# Call main to start this program.
if __name__ == "__main__":
    main()
> python example_7.py
Dictionary: {'42-039-4736': 'Clint Huish',
'61-315-0160': 'Amelia Davis', '10-450-1203': 'Ana Soares',
'75-421-2310': 'Abdul Ali', '07-103-5621': 'Amelia Davis'}

Keys: ['42-039-4736', '61-315-0160', '10-450-1203',
'75-421-2310', '07-103-5621']

Values: ['Clint Huish', 'Amelia Davis', 'Ana Soares',
'Abdul Ali', 'Amelia Davis']





















Tutorials
The following tutorials contain more information about dictionaries in Python.

Official Python tutorial about dictionaries
RealPython tutorial titled Dictionaries in Python
Summary
A dictionary in a Python program can store many pieces of data called items. An item is a key value pair. Each key that is stored in a dictionary must be unique. Values do not have to be unique. To create a dictionary, we use curly braces ({ and }). To add an item and find an item in a dictionary, we use the square brackets ([ and ]) and a key. To process all items in a dictionary, we write a for each loop. Dictionaries were invented to enable a computer to find items very quickly. Do not write a for each loop to find an item in a dictionary. To find an item in a dictionary, use square brackets ([ and ]) and a key.

Checkpoint
Purpose
Improve your ability to use dictionaries in a Python program.

Helpful Documentation
The prepare content for the previous lesson explains how to retrieve an element from a list.
The preparation content for this lesson explains how to find items in a dictionary.
Assignment
Write a program that stores information about vehicles in a Python dictionary. Your program must ask a user to enter a vehicle identification number (VIN), then find that VIN in the dictionary, and print the manufacturer, model, and color of the vehicle. Do the following:

Download and save the vehicles.py Python file and then open it in VS Code.
Using VS Code, read the comments in the program. Then replace all three occurrences of the keyword pass with code that does what the comments describe.
Run your program and verify that it works correctly.
Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Run your program and enter the inputs shown below. Ensure that your program’s output matches the output below.
> python vehicles.py
  Please enter a VIN: QT71603
  QT71603 is not in the dictionary.
  
  > python vehicles.py
  Please enter a VIN: 5TDZA23CXTU102983
  Toyota Sienna gold