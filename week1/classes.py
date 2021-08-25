"""
Write program that asks for names of all classes taking and
put them in a list.
The print the list, one per line.
"""

number_of_classes = int(input('How many classes are you taking? '))
classes = []
for x in range(number_of_classes):
    class_name = input(f'What is the name of class number {x + 1}? ')
    classes.append(class_name)

for y in range(len(classes)):
    print(f'class {y+1} is {classes[y]}')