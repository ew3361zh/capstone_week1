"""
Write program that asks for names of all classes taking and
put them in a list.
The print the list, one per line.
"""
# start by asking user how many classes they are taking, convert input to integer
number_of_classes = int(input('How many classes are you taking? '))
# set up empty list to hold all their class names
classes = []
# set up for loop to run through the number of classes they're taking
for x in range(number_of_classes):
    # for each number class, ask user for class name
    class_name = input(f'What is the name of class number {x + 1}? ')
    # add class name to the list
    classes.append(class_name)
# use for loop to print out each class in the classes list
for y in range(len(classes)):
    print(f'class {y+1} is {classes[y]}')