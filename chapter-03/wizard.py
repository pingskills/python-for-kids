wizard_list = [
    'spider legs', 'toe of frog', 'eye of newt', 
    'bat wing', 'slug butter', 'snake dandruff'
]
print(wizard_list)
print(wizard_list[2])

wizard_list[2] = 'snail tongue'
print(wizard_list)
print(wizard_list[2:5])

#append to list
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)

# Delete from list
del wizard_list[5]
print(wizard_list)

numbers = [1, 2, 3, 4]
strings = ['I', 'kicked', 'my', 'toe']
mylist = [numbers, strings]
print(mylist)
print(mylist[0])
print(mylist[0][1])
print(mylist[1][3])

print(numbers + strings)
print(numbers * 5)
