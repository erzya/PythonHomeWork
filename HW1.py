#Task #1

keyList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def generateValues(keys):
    dicWithMultiply = dict()
    for i in keys:
        dicWithMultiply[i] = i * i
    return dicWithMultiply
print(generateValues(keyList))

#Task #2
def autoGenerateList(start, end):
    numericList = list()
    for i in range (start, end):
        numericList.append(i)
    return numericList[0:101:2]
print(autoGenerateList(0,101))
#Task #3
def replace_consonants_char(str):
    consonants_list = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    vowels_list = ["A", "E", "I", "O", "U"]
    vowels_str = str.upper()
    index = 0
    for i in consonants_list:
        vowels_str = vowels_str.replace(i,vowels_list[index])
        if index==len(vowels_list)-1:
            index = 0
        else:
            index += 1
    return vowels_str
print(replace_consonants_char("RWRROOYUwINAEEt"))
#Task #4
arbitraryList = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
#remove duplicates
def remove_duplicates(innerList):
    return list(set(innerList))
print(remove_duplicates(arbitraryList))

#3 max items
    #easy way
    #arbitraryList.sort(reverse=False)
    #print(arbitraryList[-3:])
#hard way
def get_max_lements(innerList):
    maxListElements = list(innerList[:3])
    maxListElements.sort(reverse=True)
    for i in innerList[2:]:
        if maxListElements[2] < i:
            maxListElements.pop(2)
            maxListElements.append(i)
            maxListElements.sort(reverse=True)
    return maxListElements
print(get_max_lements(arbitraryList))

#index of min item
def get_ndex_of_min_element(innerList):
    minIndex = 0
    index = 0
    value = innerList[0]
    for i in innerList:
        index += 1
        if i < value:
            value = innerList[index]
            minIndex = index
    return minIndex
print(get_ndex_of_min_element(arbitraryList))

#reverse list
def reverse_list(innerList):
    return innerList[::-1]
print(reverse_list(arbitraryList))

#Task #5
dict_one = { "a": 1,"b": 2, "c": 3,"d": 4 }
dict_two = { "a": 6,"b": 7, "z": 20,"x": 40 }

def get_intersect_keys(dict_one,dict_two):
    set_keys_one = set(list(dict_one.keys()))
    set_keys_two = set(list(dict_two.keys()))
    return set_keys_one.intersection(set_keys_two)
print(get_intersect_keys(dict_one,dict_two))

#Task #6
data = [ {"name": "Viktor", "city": "Kiev", "age": 30 },
             {"name": "Maksim", "city": "Dnepr", "age": 20},
             {"name": "Vladimir", "city": "Lviv", "age": 32},
             {"name": "Andrey", "city": "Kiev", "age": 34},
             {"name": "Artem", "city": "Dnepr", "age": 50},
             {"name": "Dmitriy", "city": "Lviv", "age": 21}]

def sort_by_age(in_data):
    return sorted(in_data,key = lambda i: (i['age']))
print(sort_by_age(data))

def group_by_city(in_data):
    persons_by_city = dict()
    for i in in_data:
        person = {"name": i["name"], "age": i["age"]}
        print(person)
        city = i["city"]
        if persons_by_city.get(city,"--none--") == "--none--":
            person_list = list()
            person_list.append(person)
            persons_by_city[city] = person_list
        else:
            person_list = persons_by_city[city]
            person_list.append(person)
            persons_by_city[city] = person_list
    return persons_by_city
print(group_by_city(data))
