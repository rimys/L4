from functools import reduce

def miles_to_km(miles):
    return miles*1.6

print(miles_to_km(10))

miles_dist = [1.2 , 4 , 55]

km_dist = list(map(miles_to_km, miles_dist))
print(type(km_dist), km_dist)

km_dist = list(map(lambda x: 1.6*x, miles_dist))
print(type(km_dist), km_dist)

l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = list(map(lambda x,y: x*y, l_1, l_2))
print(type(l_3), l_3)

# reduce

list_red = [14, 22, 125, 233, 1, 2222]
max = reduce(lambda a,b: a if a>b else b, list_red)
print(max)

#  filter

list_50 = list(filter(lambda x: x % 10 == 1, list_red))
print(list_50)

# sorted

list_sort = sorted (list_red)
print(list_sort)

list_sort_reverce = sorted(list_red, reverse= True)
print(list_sort_reverce)

# key

list_names = ['Ваня', 'Ренат', 'Серега', 'Оля']
list_names_sort = sorted(list_names)
print(list_names_sort)
list_names_sort_key = sorted(list_names, key= lambda x: x[2])
print(list_names_sort_key)




