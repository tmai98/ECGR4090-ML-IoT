#!/usr/bin/env python
from person import *
import numpy
import matplotlib.pyplot as plt

def printFunc():
    print(f"The average age is {avgAge}")

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]
new_list = []


for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))

new_list = [len(name) for name in list_of_names]
print(new_list)

print(list_of_names)

person1 = x.new_person()
person2 = y.__repr__()


list_of_names.append(person1)
list_of_names.append(person2)

print(person2)
print(person1)
print(list_of_names)

people = {i : list_of_names[i] for i in range(0, len(list_of_names))}
print(people)

#age = np.list_of_ages()
age = numpy.array(list_of_ages)
print(age)

height = numpy.array(list_of_heights_cm)
print(height)

avgAge = numpy.mean(age)
printFunc()

x_axis = age
y_axis = height
plt.scatter(x_axis, y_axis)
plt.title('Scatter Plot')
plt.xlabel('Ages')
plt.ylabel('Height')
plt.grid()
plt.show()


# fig=plt.figure()
# ax=fig.add_axes([0,0,1,1])
# ax.scatter(age, height)
# ax.set_xlabel('Ages')
# ax.set_ylabel('Height')
# ax.set_title('scatter plot')
# plt.show()
