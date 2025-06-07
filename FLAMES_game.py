#Add the inputs on a list
def add_list(name):
    name_list = []
    for letters in name:
        name_list.append(letters)
    return name_list

#Convert the list into a set
def list_to_set(list):
    set_name = set()
    for letters in list:
        set_name.add(letters)
    return set_name

#Identify the common letters in the set
def common_letters(set1, set2):
    comletters = set1.intersection(set2)
    return comletters

#Remove the identified common letters in the set in the list of the inputs
def remove_letters(common, list1, list2):
    for letters in common:
        while letters in list1:
            list1.remove(letters)
        while letters in list2:
            list2.remove(letters)
    return list1, list2

#Counts how many letters are in the list that remained after removing the common letters in the list 
def counter(new_list):
    count = 0
    for i in new_list:
        count += 1
    return count


name1 = input('first name: ').strip().lower().replace(' ', '')
name2 = input('second name: ').strip().lower().replace(' ', '')

list1 = add_list(name1)
list2 = add_list(name2)

print(list1)
print(list2)

setlist1 = list_to_set(list1)
setlist2 = list_to_set(list2)

# print(setlist1)
# print(setlist2)

comletters = common_letters(setlist1, setlist2)
# print(comletters)

new_list1, new_list2= remove_letters(comletters, list1, list2)
print(new_list1)
print(new_list2)

counter_new_list1 = counter(new_list1)
counter_new_list2 = counter(new_list2)
letter_count = counter_new_list1 + counter_new_list2

#Main Game
print(f'The list contains: {letter_count} letters')
flames = list("FLAMES")
pos = 0  

#Will circle around the word FLAMES
while letter_count > 0:
    pos = (pos+ 1) % len(flames)
    letter_count -= 1

print(f'The count stopped at {flames[pos]}')
if flames[pos] == 'F':
    print('It means that you are friends')
elif flames[pos] == 'L':
    print('It means that you are lovers')
elif flames[pos] == 'A':
    print('It means that you are aquaintance')
elif flames[pos] == 'M':
    print('Time to marry each other')
elif flames[pos] == 'E':
    print('You are enemies')
else:
    print('Siblings')


        




    
